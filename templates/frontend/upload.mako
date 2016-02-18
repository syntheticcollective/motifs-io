<!DOCTYPE html>
<html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <head>
        <title>Motifs.io - Search</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css" integrity="sha384-aUGj/X2zp5rLCbBxumKTCw2Z50WgIr1vs/PFN4praOTvYXWlVyh2UtNUU0KAUhAX" crossorigin="anonymous">
    </head>
    <body>
        <nav class="navbar navbar-inverse">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Motifs.io</a>
                </div>
                <div id="navbar" class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="/fe/upload">Upload</a></li>
                        <li><a href="/fe/search">Search</a></li>
                    </ul>
                </div><!--/.nav-collapse -->
            </div>
        </nav>
        <div class="container" role="main">
            <div class="row">
                {% if msg != '' %}
                    <div class="alert alert-success" role="alert">{{ msg }}</div>
                {% endif %}
                <div class="col-md-8">
                    <h1>Upload New MIDI</h1>
                    <form action="/fe/upload" method="POST" enctype="multipart/form-data">
                        {% csrf_token %}
                        <div class="input-group">
                            <span class="input-group-addon" id="basic-addon1">ID (required)</span>
                            <input type="text" name="id" id="id" class="form-control" placeholder="Title" aria-describedby="basic-addon1">
                        </div>
                        <br />
                        <div class="input-group">
                            <span class="input-group-addon" id="basic-addon1">Title</span>
                            <input type="text" name="title" id="title" class="form-control" placeholder="Title" aria-describedby="basic-addon1">
                        </div>
                        <br />
                        <div class="input-group">
                            <span class="input-group-addon" id="basic-addon1">Composer</span>
                            <input type="text" name="composer" id="composer" class="form-control" placeholder="Composer" aria-describedby="basic-addon1">
                        </div>
                        <br />
                        <div class="row">
                            <div class="col-md-4">
                                <div class="input-group">
                                    <span class="input-group-addon" id="basic-addon1">BPM</span>
                                    <input type="text" name="bpm" id="bpm" class="form-control" placeholder="BPM" aria-describedby="basic-addon1">
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="input-group">
                                    <span class="input-group-addon" id="basic-addon1">Key</span>
                                    <select name="key" id="key" class="form-control">
                                        <option value="" selected> -- select a key -- </option>
                                        <option value="Ab">A♭</option>
                                        <option value="A">A</option>
                                        <option value="A#">A♯</option>
                                        <option value="Bb">B♭</option>
                                        <option value="B">B</option>
                                        <option value="C">C</option>
                                        <option value="C#">C♯</option>
                                        <option value="Db">D♭</option>
                                        <option value="D">D</option>
                                        <option value="D#">D♯</option>
                                        <option value="Eb">E♭</option>
                                        <option value="E">E</option>
                                        <option value="F">F</option>
                                        <option value="F#">F♯</option>
                                        <option value="Gb">G♭</option>
                                        <option value="G">G♭</option>
                                        <option value="G#">G♯</option>
                                    </select>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="input-group">
                                    <span class="input-group-addon" id="basic-addon1">Mode</span>
                                    <select name="mode" id="mode" class="form-control">
                                        <option value="" selected> -- select a mode -- </option>
                                        <option value="major">major</option>
                                        <option value="dorian">dorian</option>
                                        <option value="phrygian">phrygian</option>
                                        <option value="lydian">lydian</option>
                                        <option value="mixolydian">mixolydian</option>
                                        <option value="minor">minor</option>
                                        <option value="locrian">locrian</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <br />
                        <label for="basic-url">In comma separated list form</label>
                        <div class="input-group">
                            <span class="input-group-addon" id="basic-addon3">Tags</span>
                            <input type="text" name="tags" id="tags" class="form-control" id="basic-url" aria-describedby="basic-addon3">
                        </div>
                        <br />
                        <div class="input-group">
                            <span class="input-group-addon" id="basic-addon3">MIDI File</span>
                            <input type="file" name="midi" id="midi" class="form-control" id="basic-url" aria-describedby="basic-addon3">
                        </div>
                        <br />
                        <button type="submit" class="btn btn-primary">Upload</button>
                    </form>
                </div>
            </div>
        </div>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>
    </body>
</html>