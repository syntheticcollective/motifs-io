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
        <div id="navbar" class="collapse navbar-collapse pull-left">
            <ul class="nav navbar-nav">
                <li><a href="/fe/upload">Upload</a></li>
                <li><a href="/fe/search">Search</a></li>
                % if user.is_authenticated():
                    <li class="hidden-nav"><a href="/logout">Logout</a></li>
                % else:
                    <li class="hidden-nav"><a href="/login">Login</a></li>
                    <li class="hidden-nav"><a href="/signup">Signup</a></li>
                % endif
            </ul>
        </div><!--/.nav-collapse -->
        <div class="pull-right action-buttons">
            % if user.is_authenticated():
                <span class="greeting">Hello ${user.get_short_name()}!</span>
                 <a href="/logout"><button type="button" class="btn signup-btn btn-primary">Logout</button></a>
            % else:
                <a href="/login"><button type="button" class="btn login-btn btn-primary">Login</button></a>
                <a href="/signup"><button type="button" class="btn signup-btn btn-success">Signup</button></a>
            % endif
        </div>

    </div>
    <div class="header-image">

    </div>
</nav>