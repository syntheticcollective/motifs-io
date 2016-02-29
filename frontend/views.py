import os

import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import View
from djangomako.shortcuts import render_to_response

from api.lib.midas.constants.key import key_to_byte
from api.lib.midas.constants.mode import mode_to_byte
from api.lib.midas.encoder import BinaryEncoder
from api.lib.midas.file import MIDIFile
from api.lib.midas.header import MotifHeader

SOLR_URL = 'http://localhost:8983/solr/motifs/select'
SOLR_UPLOAD_URL = 'http://localhost:8983/solr/motifs/update/extract'
SOLR_ATTRS_TRANSLATION_TABLE = {
    'composer': r'attr_xmpDM\:composer',
    'title': r'title',
    'tags': r'attr_Keywords',
    'bpm': r'attr_xmpDM\:tempo',
    'mode': 'mode',
    'key': 'attr_xmpDM\:key'
}


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('frontend/home.mako', {
            'user': request.user
        })


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'csrftoken': csrf(request)['csrf_token'],
            'user': request.user
        }
        return render_to_response('frontend/login.mako', context)

    def post(self, request, *args, **kwargs):
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()


class SignupView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'csrftoken': csrf(request)['csrf_token'],
            'user': request.user
        }
        return render_to_response('frontend/signup.mako', context)

    def post(self, request, *args, **kwargs):
        user = User.objects.create_user(
            request.POST['user_name'],
            request.POST['email'],
            request.POST['password']
        )
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('login')


def build_solr_query_str(params):
    qs = []
    for p in params:
        if p in SOLR_ATTRS_TRANSLATION_TABLE:
            k = SOLR_ATTRS_TRANSLATION_TABLE[p]
            v = params[p]
            if v:
                qs.append('%s:%s' % (k, v))
    if len(qs) == 0:
        return {'q': '*:*', 'wt': 'json'}
    return {'q': ' && '.join(qs), 'wt': 'json'}


class SearchView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/search.mako', {})

    def post(self, request, *args, **kwargs):
        solr_query = build_solr_query_str(request.POST)
        resp = requests.get(SOLR_URL, data=solr_query)
        return render_to_response('frontend/results.mako', {'docs': resp.json()['response']['docs']})


def write_temp_file(f):
    with open('./tmp.midi', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return './tmp.midi'


def create_header(params):
    title = params.get('title')
    composer = params.get('composer')
    bpm = params.get('bpm')
    key = params.get('key')
    key_byte = key_to_byte(key) if key is not None else None
    mode = params.get('mode')
    mode_byte = mode_to_byte(mode) if key is not None else None
    tags = params.get('tags', '').split(',')
    tags = [str(t.strip()) for t in tags]
    return MotifHeader(BinaryEncoder(), str(title), str(composer), int(bpm), key_byte, mode_byte, tags)


def apply_header_to_file(header, path):
    fh = open(path, 'a+b')
    try:
        midi = MIDIFile(fh)
        midi.write_motif_header(header)
    finally:
        midi.close()


def upload_to_solr(doc_id, path):
    params = {
        'literal.id': doc_id,
        'commit': 'true',
        'stream.contentType': 'application/x-midi'
    }
    files = {'file': open(path, 'rb')}
    try:
        resp = requests.post(SOLR_UPLOAD_URL, params, files=files)
        print resp
    finally:
        files['file'].close()


class UploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/upload.mako', {'msg': ''})

    def post(self, request, *args, **kwargs):
        path = write_temp_file(request.FILES['midi'])
        header = create_header(request.POST)
        apply_header_to_file(header, path)
        upload_to_solr(request.POST['id'], path)
        os.remove(path)
        return render(request, 'frontend/upload.mako', {'msg': 'MIDI file successfully uploaded!'})