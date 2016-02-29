<!DOCTYPE html>
<html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <head>
        <title>Motifs.io - Search Results</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
        <link rel="stylesheet" href="/static/css/base.css" />
        <link rel="stylesheet" href="/static/css/home.css" />
    </head>
    <body>
        <%include file="navbar.mako" />

        <div class="container" role="main">
            <div class="row">
                <div class="col-md-8">
                    <div class="midi-stream">
                        <h2>MIDI Stream</h2>
                        <div class="row">
                            <div class="col-md-10">
                                <div class="midi-track">
                                    <h4>MIDI Title</h4>
                                    <p class="author">Mr. Foo Bar</p>
                                    <p class="release-date">10 minutes ago</p>
                                    <span class="clearfix"></span>
                                    <div class="track-viz">Placeholder for MIDI visualization</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-2.2.0.min.js" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>
    </body>
</html>