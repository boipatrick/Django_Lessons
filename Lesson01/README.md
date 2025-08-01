Django Path Converters

Slug - matches any slug string consisting of ASCII letters or numbers


# Adding Images

settings.py

Under static add
 MEDIA_URL =
 MEDIA_ROOT =

 ## Challenge

    Add a Users App to our Django project
    Create one template and name it register.html
    

    Solution:
    python manage.py startapp users - create users 
    Settings.py register our app
    cd users
    mkdir templates
    touch register.html


## Protecting Pages in Django

Protect pages from users who are not logged in
