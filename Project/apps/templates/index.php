<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      	<a class="navbar-brand" href="/">GameDevX</a>
      	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar1" aria-controls="navbar1" aria-expanded="false" aria-label="Toggle navigation">
        	<span class="navbar-toggler-icon"></span>
      	</button>

      	<div class="collapse navbar-collapse" id="navbar1">
        	<ul class="navbar-nav mr-auto">
          		<li class="nav-item active">
            		<a class="nav-link" href="contact/">Контакты<span class="sr-only">(current)</span></a>
          		</li>
    		    <li class="nav-item">
    		    	<a class="nav-link" href="/news/">Новости</a>
    		    </li>
            {% if user.is_authenticated %}
             <li>User: {{ user.get_username }}</li>
             <li><a class="btn btn-primary" href="{% url 'logout'%}?next={{request.path}}">Logout</a></li>
           {% else %}
             <li><a class="btn btn-primary" href="{% url 'login'%}?next={{request.path}}">Login</a></li>
           {% endif %}
          		
        	</ul>
        	<form class="form-inline my-2 my-lg-0">
          		<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          		<button class="btn btn-outline-info my-2 my-sm-0" type="submit">Search</button>
        	</form>
      	</div>
    </nav>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->

    {%block content%}
    {%endblock%}
    <footer>
      <p>&copy; Company 2017</p>
    </footer>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
