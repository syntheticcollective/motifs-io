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
            <div class="row centered-form">
                <div class="col-xs-12 col-sm-8 col-md-8 col-sm-offset-2 col-md-offset-2">

                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">Login</h3>
                        </div>
                        <div class="panel-body">
                            <form id="login-form" action="/login" method="post" role="form" style="display: block;">
                                <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}" />
                                <div class="form-group">
                                    <input type="text" name="user_name" id="user_name" tabindex="1" class="form-control" placeholder="Username" value="">
                                </div>
                                <div class="form-group">
                                    <input type="password" name="password" id="password" tabindex="2" class="form-control" placeholder="Password">
                                </div>
                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-sm-6 col-sm-offset-3">
                                            <input type="submit" name="login-submit" id="login-submit" tabindex="4" class="form-control btn btn-login" value="Log In">
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
	    		    </div>
    		    </div>
    	    </div>
        </div>
        <script src="https://code.jquery.com/jquery-2.2.0.min.js" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>
    </body>
</html>