# recipe24

### Description
Recipe24 is a simple recipe app build with Django

#### Recipe data contains:
- title
- photo
- rating
- prep time
- cooking time
- servings
- ingredients
- cooking instructions

#### With this in mind, the admin has the following functionality:
- Listing our collection of recipes.
- Adding new recipes to our collection. 
- Viewing the details on a recipe.

#### Instructions
You will need to have installed [Django](https://docs.djangoproject.com/en/2.0/topics/install/) and [Python](https://www.python.org/downloads/)

After cloning change into the outer **mysite** directory. 
If you haven’t already, and run the following commands:
`python manage.py runserver`

You’ll see the following output on the command line:

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

March 13, 2018 - 15:50:53
Django version 2.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now that the server’s running, visit http://127.0.0.1:8000/ with your Web browser. You’ll see a “Welcome to Recipe24!” page.