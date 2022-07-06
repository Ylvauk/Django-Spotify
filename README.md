# Django URLs, Views, and Templates

## Road Map

- Django Learning Path
- Django Philosophy
- Django Request/Response Cycle
- Project setup
- Project Settings Configuration
- Defining Routes
- Defining Views
- Django Templates
- Template Inheritance
- Adding Static Files (css + js)
- Rendering Data in a Template

## Django Learning Path

To learn Django we will be taking one of the biggest applications today built on the framework, Spotify. We will add features, piece-by-piece, to this modern full-stack reference application.

After each major lesson we will be providing lab time for you to repeat what we went over in your own application.

Here is an overview of the high-level topics we will be covering.

- Django Urls, Views and Templates
- Data Models and Migrations
- One to Many Models
- Many to Many Models
- Django User Authentication

## Django Philosophy

### Review The Philosophy of Express

Express was a minimalist framework that didn't provide much functionality out of the box.

It gave us a way to define routes, map controller actions to those routes, and render dynamic views.

Express didn't have many rules, for example, we could name files anything and put them anywhere we wanted.

If we did need additional capability, it usually meant installing and configuring additional middleware.

### The Philosophy of Django

Unlike Express, Django, is a full-featured web framework that provides a lot of built-in functionality.

However, Django has many *conventions*, i.e., it expects us to follow its rules.

You will find that Django has all sorts of *helper* classes, methods, etc.

What Express has to offer can be grasped in a matter of days, whereas Django could take weeks to feel comfortable with what it has to offer.

Luckily for us though, the basics aren't too bad though, as long as you don't try to learn every little detail about each helper, etc.

## The Request/Response Cycle in Django

In Unit 2, we learned that in a full-stack web application:

- Clicking links and submitting forms on the front-end (browser) sends HTTP requests to the web app running on a web server.
- The web server has a routing mechanism that matches HTTP requests to code.
- That code typically performs CRUD, then either:
    - Renders dynamic templates for Read data operations.
    - Redirects the browser in the case of Create, Update or Delete data operations.

Once again, let's review this diagram that shows how a request flows through a Django project:

![https://i.imgur.com/1fFg7lz.png](https://i.imgur.com/1fFg7lz.png)

## Project Setup

Project setup in Django has several steps. Here is an outline of those steps:

1. Create Project Folder
2. Create Python Enviroment for the Project
3. Install Project Dependancies
4. Use Django Start Project to generate settings
5. Use Django Start App to generate template for project functionality

Let's get started.

### 1. Create Project Folder

In terminal:

```bash
mkdir spotify_django && cd spotify_django
```

### 2. Create Python Enviroment for the Project

To house all of the dependencies for our application we must create an enviroment. This is the python version of running npm init and having a node_modules directory.

You must make sure you have python3 installed and available.

In Terminal:

```bash
which python3
```

If your terminal displays a location then you are all set! If you recieve a "not found" then you need to install python3. This process can vary between operating systems. If you are on mac you can use brew for installation.

In Terminal:

```bash
brew install python@3.9
```

Once we have verified that python is installed and available we can create the enviroment using the built in venv package.

In Terminal:

```
python3 -m venv .env

```

You should now see a .env directory within your project folder.

Now comes the tricky part. With Python you must activate the enviroment in order to start using it.

In Terminal:

```
source .env/bin/activate

```

Your terminal should now display that you are inside on an enviroment.

> NOTE: Depending on your configuration it will look different but you should see something like (env) in the prompt.
> 

### 3. Install Project Dependancies

Now that our enviroment is established we can install the dependancies. We will need two dependancies for the project, Dango and Psycopg2.

In Terminal:

```
pip3 install django
pip3 install psycopg2-binary

```

Django doesn't utilize a package.json. Instead, we just use a text file that lists all of our dependencies. The pip freeze command saves the dependencies in our virtualenv to that file. Let's create a requirements.txt file with all of our required modules.

In Terminal:

```
pip3 freeze > requirements.txt

```

Your file should look something like this:

```
asgiref==3.3.4
Django==3.2
psycopg2-binary==2.8.6
pytz==2021.1
sqlparse==0.4.1

```

> NOTE: To install dependancies when you clone down an application the command is pip3 install -r requirements.txt
> 

### 4. Use Django Start Project to generate settings

Django has an incredible super power where it can create all the startup code for our application. To get started we must run the django-admin command.

In Terminal:

```
django-admin startproject spotify_project . # DO NOT FORGET THE 'dot' at the end

```

Take a minute to look at the generated files. Your file structure should look something like this:

```
spotify_django
├── manage.py
├── requirements.txt
└── spotify_project
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

The only file we will need to configure is going to be the [settings.py](http://settings.py/) when we start configuration. As for now we will move on to the next step.

### 5. Use Django Start App to generate template for project functionality

Because of the way Django is structured all functionality is divided into seperate directories referred to as "apps". If you head over to the [settings.py](http://settings.py/) file you can see a list of already installed apps. Our next big step is creating an app of our own.

If we would like to generate the files needed for our project's functionality we will need to use another command called startapp.

In Terminal:

```
django-admin startapp main_app

```

You will see a new directory labeled the app name from above and your directory should look something like this:

```
spotify_django
├── main_app <- this is the app folder to hold functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
└── spotify_project <- this is the project folder to hold settings
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

And with that we have all the files we need to start configuring our application!

## Project Settings Configuration

To configure our settings there are a few steps we will need to do.

1. Install the new app we created.
2. Connect our Database.
3. Test run our server.

### 1. Install the new app we created.

Because Django comes with so many features built in, it goes by an "opt in" approach where you add in the settings what apps should be included on the server.

If you check out the [settings.py](http://settings.py/), we can see a variety of apps installed already. We will be adding our app to the list.

In spotify_project/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app', # our application here.
]

```

### 2. Connect our Database.

Django is extremely versatile and will allow us to connect to a variety of different databases. We will be setting the configuration to connect to postgresql.

In the settings file you will find a DATABASES dictionary. This is where we will be updating the connection.

In spotify_project/settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spotify',
    }
}

```

> NOTE: Django does not create our database for us automatically so we will need to run the create commands for postgresql.
createdb spotify
> 

Now that we have estabished the connection we can apply the intial migrations with the migrate command.

In Terminal:

```
python3 manage.py migrate

```

The output of that command should be a series of OK and look like the below:

```
Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying sessions.0001_initial... OK

```

### 3. Test run our server.

Now that our server is configured we can finally run it!

In Terminal:

```
python3 manage.py runserver

```

Your output should be something like this:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 04, 2021 - 00:20:07
Django version 3.2, using settings 'spotify_project.settings'
Starting development server at <http://127.0.0.1:8000/>
Quit the server with CONTROL-C.

```

With this our server is live and ready! Let's checkout what is available for us at `localhost:8000`.

<img src="[https://i.imgur.com/RozMgJ0.png](https://i.imgur.com/RozMgJ0.png)"/>

If you see the rocketship you all set!

Next we will be jumping into how to set up urls and routes.

## Defining Routes

As you learned with Express, there needs to be a route defined that matches each HTTP request coming from the browser. We also know that the purpose of a route is to map an HTTP request to a view function to generate a response.

Before we start creating our routes let's take a look at the Django flow once more.

<img src="[https://i.imgur.com/1fFg7lz.png](https://i.imgur.com/1fFg7lz.png)">

The way requests are mapped are starting in our project folder and then routed to the corresponding application folder. This allows Django to be extremely flexible and is similar to how we were using controllers in express.

To connect our project urls to our application urls we need to go through a** one time setup**.

### One Time setup to connect project urls to the application urls.

To do this we must do the following steps:

1. Create a [urls.py](http://urls.py/) in our application folder.
2. Point our project urls to the newly created urls file.

### 1. Create a [urls.py](http://urls.py/) in our application folder.

In Terminal:

```
touch main_app/urls.py

```

With our newly created file we will now add the base code to hold url requests.

In main_app/urls.py:

```
from django.urls import path
from . import views

urlpatterns = [

]

```

### 2. Point our project urls to the newly created urls file.

To point our project to our application urls we will need to import include and define a new path.

Each item in the urlpatterns list defines a URL-based route or, as in the case above, mounts the routes contained in other URLconf modules.

Note that similar to how Express appends paths defined in a router module to the path in app.use, the paths defined in 'main_app.urls' will be appended to the path specified in the include function.

In spotify_project/urls.py:

```
from django.contrib import admin
from django.urls import path, include # <- you must add include to the imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')) # <- here is the new line to include the urls of our app
]

```

Now that we have the connection it is time to start creating our views!

## Defining Views

Right now we still see the rocketship because that is the default root route. We will now replace that route by creating a path in our project urls.

But first let's breakdown the syntax of path().

```
path('route string', name of view function, name="string name of route")
# example
path('artists/', views.Artist_List.as_view(), name="artist_list")

```

In the route we will be building we will be using an empty string as the route to signify the root route.

In main_app/urls.py:

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
]

```

> NOTE: This will cause your server to crash because we have not defined the view that this is requiring. Our next step will be to add the view function into our views.py.
> 

Now that we have our route estqablished it is time to build out our view function.

We will be leveraging class base views provided to us by Django. To do this we will be importing the classes at the top of the file.

In main_app/views.py:

```
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(View):

    # Here we are adding a method that will be ran when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Spotify Home")

```

Head back to the root route and browser and see the new response!

### YOU DO

---

Step back through what we just did and create a route for a new url location "about/". This route will respond with a generic response for "Spotify About".

<details>
<summary>Solution</summary>
<br>

In main_app/urls.py:

```

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
]

```

In main_app/views.py:

```

#...
class About(View):

    def get(self, request):
        return HttpResponse("Spotify About")

```

</details>

## Django Templates

Time to crank it up a notch by using templates!

Just like how Express can use different templating engines (Jade, EJS, etc.), so can Django.

Django has two templating engines built-in:

- Its own Django Template Language (DTL)
- Jinja2, a Python template engine, inspired by Django's DTL.

Not surprisingly, a Django project is pre-configured to use DTL, which is very capable, so we'll be using it throughout.

Django is configured to look for a directory labeled templates within each installed application.

To make our templates and use them will require a few steps:

1. Create a templates directory inside our app directory.
2. Create our Html file to be our rendered template.
3. Update our view function to use the template.

### 1. Create a templates directory inside our app directory.

**You only have to do this step once.**

```
mkdir main_app/templates

```

Now that we have a template directory we can start to create our templates.

### 2. Create our Html file to be our rendered template.

Let's create the home template by adding a new html file within the templates directory.

```
touch main_app/templates/home.html

```

Once you have created the template add some base html.

In main_app/templates/home.html:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Spotify</title>
  </head>
  <body>
    <h1>Spotify Home</h1>
  </body>
</html>

```

### 3. Update our view function to use the template.

Now we can adjust our Home Class View to use a template instead of rendering  basic HttpResponse.

To do this we will be importing a new class called TemplateView at the top of our [views.py](http://views.py/)

In main_app/views.py:

```
#...
from django.views.generic.base import TemplateView

```

With our new import we will refactor our Home view class to extend this view instead.

In main_app/views.py:

```
class Home(TemplateView):
    template_name = "home.html"

```

BUT WAIT! What happend to the get method?
When we are using a template view we do not need to define the get method. Django has handled that for us. Thanks Django!

### YOU DO

---

Retrace the steps above and convert the About View into a template view as well.

<details>
<summary>Solution</summary>
<br>

In main_app/templates/about.html:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Spotify</title>
  </head>
  <body>
    <h1>Spotify About</h1>
  </body>
</html>

```

In main_app/views.py:

```
#...
class About(TemplateView):
    template_name = "about.html"

```

</details>

## Template Inheritance

Django has a [template inheritance](https://docs.djangoproject.com/en/3.2/topics/class-based-views/intro/) feature built-in.

Template inheritance is like using partials in EJS with Express, except they're more flexible.

The reason Django calls it template inheritance is because:

- You can declare that a template extends another template.
- Extending another template results in defined blocks overriding (replacing) blocks defined in the template being extended.

<img src="[https://i.imgur.com/ZajRcLx.jpg](https://i.imgur.com/ZajRcLx.jpg)" />

To start using template inheritance we will be doing the follow steps:

1. Create a base.html to extend from.
2. Refactor Home.html to extend base.

### 1. Create a base.html to extend from.

This is the template that will hold all of the boilerplate and markup that belongs on every page, such as the <head>, navigation, even a footer if you wish.

In main_app/templates/base.html:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="<https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css>">
    <script src="<https://code.jquery.com/jquery-3.6.0.min.js>" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <title>Spotify</title>
  </head>
  <body >
        <nav class="navbar is-black" role="navigation" aria-label="main navigation">
          <div class="navbar-brand">
            <a class="navbar-item" href="/">Spotify</a>
            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>
          <div class="navbar-menu navbar-start">
            <a class="navbar-item" href="/about">About</a>
          </div>
          <div class="navbar-menu navbar-end">
            <a class="navbar-item" href="/artists">Artists</a>
          </div>
        </nav>
        <div class="container">

          {% block content %}{% endblock %}

        </div>
      </div>
    </div>
  </body>
</html>

```

> NOTE: We will be using Bulma as our CSS Framework to style our application. You can check out it's documentation. We are also going to be using Jquery to handle some dom manipulation magic later on.
> 

However, the most important part of the boilerplate in regards to template inheritance is:

```
{% block content %}
{% endblock %}

```

Hey, that's our first look at DTL template tags, block & endblock, enclosed within the template tag delimiters {% %}.

Whenever another template extends this base.html, that other template's {% block content %} will replace the same block in base.html.

### 2. Refactor Home.html to extend base.

To see inheritance in action we will refactor Home.html.

In main_app/templates/base.html:

```
{% extends 'base.html' %}
{% block content %}
<h1>Spotify Home</h1>
{% endblock %}

```

Notice the "extends" keyword in our template. This is how the DTL know what to build the template from. Go refresh your page and check it out!

### YOU DO

---

Refactor About.html to extend base.

<details>
<summary>Solution</summary>
<br>

In main_app/templates/about.html:

```
{% extends 'base.html' %} {% block content %}
<h1>About</h1>
{% endblock %}

```

</details>

## Adding Static Files (css + js)

Now that we have our templates would it be nice to be able to style the page and add some js. Well that is our next step!

To serve static files we will be doing the following steps:

1. Create a static directory.
2. Create our CSS and js files.
3. Link the static files to our html.

### 1. Create a static directory.

Just like our templates directory we will need to create a static direcctory for Django to find all static files. This is the same as our public folder in Express.

In Terminal:

```
mkdir main_app/static

```

Once we create the static directory we will also want to created our nested scripts and styles directories to stay organized.

In Terminal:

```
mkdir main_app/static/scripts main_app/static/styles

```

NOw we can move on to making our files.

### 2. Create our CSS and js files.

We need to adjust some styles to make our application look at little more like spotify.

In main_app/static/styles/main.css:

```
body {
  background-color: #121212;
  color: #ffffff;
  min-height: 100vh;
}

h1,
h2,
h3 {
  color: #ffffff;
}

.title {
  color: #ffffff;
}

.gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
}

.gallery .card {
  min-width: 280px;
  max-width: 30%;
  transition: 0.1s linear;
}

.gallery .card:hover {
  transform: scale(1.3);
}

p {
  font-size: 12px;
}

```

Now if you squeeze the page you will notice that Bulma is creating a hamburger menu for us when the screen is to small. If we want to to be able to tap on the icon and animate the menu we will have to use some js! Check out the [bulma documentation on this effect](https://versions.bulma.io/0.7.0/documentation/components/navbar/#navbar-menu).

In main_app/static/scripts/main.js:

```
$(".navbar-burger").click(function () {
  // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
  $(".navbar-burger").toggleClass("is-active");
  $(".navbar-menu").toggleClass("is-active");
});

```

### 3. Link the static files to our html.

To connect our files to our html we will be using a special template tags {% load static %} and {% static 'filename' %}. Checkout info on them [HERE](https://docs.djangoproject.com/en/3.2/howto/static-files/).

In main_app/templates/base.html:

```
<!-- At the top of the file  -->
{% load static %}

```

This line is going to tell Django to look into the static folder and make any files within available to the templates.

To link the new files to our html we will be adding the following lines:

In main_app/templates/base.html:

```
<!-- in our html head tag add the following  -->
<link rel="stylesheet" href="{% static 'styles/main.css' %}" />
<script src="{% static 'scripts/main.js' %}" defer></script>

```

Notice the src and hrefs of our connected files. This is the Django way of refrencing the static folder and its contents.

Refresh your page and check out the awesome new styles and menu functionality!

## Rendering Data in a Template

Now we have the start to a great application! But it would be great to start start displaying data on our html. For this we will be adding an artist list route and using templating to generate a collection of artists on the page.

For this we will be going through the following steps:

1. Add a new url "artists/" and point to a view class ArtistList
2. Create some fake database data
3. Create a class view called ArtistList
4. Create a template view to display the Artists

### 1. Add a new url "artists/" and point to a view class ArtistList

In main_app/urls.py:

```
 urlpatterns = [
    # ...
    path('artists/', views.ArtistList.as_view(), name="artist_list")
]

```

### 2. Create some fake database data

To replicate what we would get back from our database we will be creating a class that is an artist. This class will recieve a name, image, and Bio.

In main_app/views.py:

```
 #adds artist class for mock database data
class Artist:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

artists = [
    Artist("Gorillaz", "<https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29>",
           "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
    Artist("Panic! At The Disco",
           "<https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080>", "Welcome 👋 The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
    Artist("Joji", "<https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df>",
           "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
    Artist("Metallica",
           "<https://i.scdn.co/image/ab67706c0000da84eb6bb372a485d26fd32d1922>", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents.")
]

```

### 3. Create a class view called ArtistList

To handle passing information into our templates we will be using a method built into all template classes called [get_context_data](https://docs.djangoproject.com/en/3.2/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data).

This is similar to how we would create context to pass into our ejs files.

In main_app/views.py:

```
class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artists"] = artists # this is where we add the key into our context object for the view to use
        return context

```

### 4. Create a template view to display the Artists

There are two control flow template tag constructs you'll use quite a bit:

- The {% for %} / {% endfor %} block used to perform looping
- The {% if %} / {% elif %} / {% else %} / {% endif %} block used for conditional logic.

**Important:** Django template tags are designed to mimic very closely their Python counterparts, however, they are not embedding Python the way EJS embedded JavaScript.

For example, Python does not have endfor or endif as part of the language.

In main_app/templates/artist_list.html:

```
{% extends 'base.html' %}

{% block content %}

<h1 class="title">Trending Artists</h1>
<div class="gallery">
  {% for artist in artists %}
  <a href="">
    <div class="card">
      <div class="card-image">
        <figure class="image is-square">
          <img src="{{artist.image}}" alt="{{artist.name}}" />
        </figure>
      </div>
      <div class="card-header">
        <p class="card-header-title">{{artist.name}}</p>
      </div>
    </div>
  </a>
  {% endfor %}
</div>

{% endblock %}

```

Next notice how double curly brace syntax {{}} is used to print the values of variables and object properties.

> NOTE: If the property on an object is a method, it is automatically invoked by the template engine without any arguments and we do not put parens after the method name. For example, assuming a person object has a getFullName method, it would be used like this {{ person.getFullName }} in the template. This is another example of how DTL is its own language and not Python.
> 

Head on over to the new route and checkout our beautiful new artists!

### YOU DO

---

Spend some time practicing by building a route to "songs/" and displaying a collection of songs.

## References

<a href="[https://docs.djangoproject.com/en/3.2/topics/templates/](https://docs.djangoproject.com/en/3.2/topics/templates/)">Django Templates</a>

<a href="[https://docs.djangoproject.com/en/3.2/howto/static-files/](https://docs.djangoproject.com/en/3.2/howto/static-files/)">Django Static Files</a>

<a href="[https://docs.djangoproject.com/en/3.2/topics/class-based-views/](https://docs.djangoproject.com/en/3.2/topics/class-based-views/)">Django Class Based Views</a>
