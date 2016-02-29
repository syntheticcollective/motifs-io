from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^signup', views.SignupView.as_view(), name='signup'),
    url(r'^logout', views.LogoutView.as_view(), name='logout'),
    url(r'^login', views.LoginView.as_view(), name='login'),
    url(r'^search', views.SearchView.as_view(), name='search'),
    url(r'^upload', views.UploadView.as_view(), name='upload')
]
