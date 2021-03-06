#TELEVIS PROJECT - Inginerie Software

### Project theme
> A smart TV system for user-profiling and automated recommendations

### Programming language
>We are using the **python** language with the django & django-rest-framework

### Content
We are working on a platform that uses multiple APIs:
> 1. movieAPI for movie recommandations with IMDB
> 2. musicAPI for music recommandations with Spotify
> 3. TVMaze for TV Schedule
> 4. Indian Tv Schedule for Indian TV Schedule

And we have the following utilities:
> 1. Recommandations for movies
> 2. Recommandations for music
> 3. Recommandations for watch slots for TV Schedule
> 4. Creation of personalised feed for user
> 5. Ability to register and login to preserve watch history and other utilities

### Useful commands
1. Create a new project **django-admin startproject projectName**
2. Make a new app (component) **python manage.py startapp appName**
> A new component must be added in the source folder, in settings at **INSTALLED_APPS**
>
> Also, you must import all urls from an app to source urls by using **import('appName.urls')** 
3. To save the required libraries for the project, use **pip freeze > requirements.txt**
3. Everytime you make a view, make sure it is added in the urls.py file
4. If you update a model, make sure you execute **python manage.py makemigrations** and **python manage.py migrate**
> For evey model made, you need to create a serializer
> If you want to see the models in the admin interface do the following steps:
>> 1. **from django.contrib import admin**
>
>> 2. **from .models import YourModel**
> 
>> 3. **admin.site.register(YourModel)** 
5. To make a super user for the admin interface use **python manage.py createsuperuser**
6. To run the project use **python manage.py runserver** and it will be visible on port 8000

### Unit Tests commands
1. **Create a superadmin user with username "test"**
2. Run unit tests **python -m pytest -v**
3. Run coverage **coverage run -m pytest -v**
4. Run coverage report **coverage report -m**
5. Create HTML for coverage **coverage html**