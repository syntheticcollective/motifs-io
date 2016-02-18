<!DOCTYPE html>
<html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <head>
        <title>Motifs.io - Search Results</title>
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
                        <li><a href="/fe/upload">Upload</a></li>
                        <li class="active"><a href="/fe/search">Search</a></li>
                    </ul>
                </div><!--/.nav-collapse -->
            </div>
        </nav>
        <div class="container" role="main">
            <div class="row">
                <div class="col-md-8">
                    <div>
                        <h1 class="pull-left">Results</h1>
                        <a href="/fe/search"><span style="margin-top: 20px;" class="pull-right btn btn-primary">Search Again</span></a>
                        <div class="clearfix"></div>
                    </div>

                    % for (i, doc) in enumerate(docs):
                        <div>
                            <h3>${i + 1}. ${doc['id']}</h3>
                            <ul>
                                <li>Title: ${doc.get('title', [''])[0]}</li>
                                <li>Composer: ${doc.get('attr_xmpDM:composer', [''])[0]}</li>
                                <li>BPM: ${doc.get('attr_xmpDM:tempo', [''])[0]}</li>
                                <li>Key: ${doc.get('attr_xmpDM:key', [''])[0]} ${doc.get('mode', [''])[0]}</li>
                                <li>Tags: ${', '.join(doc.get('attr_meta:keyword', ['']))}</li>
                            </ul>
                        </div>
                    % endfor
                </div>
            </div>
        </div>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>
    </body>
</html>