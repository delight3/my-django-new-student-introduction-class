# Django is a Python framework that makes it easier to create web 
# sites using Python.
# Django takes care of the difficult stuff so that you can 
# concentrate on building your web applications.

# How does Django Work?
# Django follows the MVT design pattern (Model View Template).

# Model - The data you want to present, usually data from a database.
# View - A request handler that returns the relevant template and 
# content - based on the request from the user.
# Template - A text file (like an HTML file) containing the layout
# of the web page, with logic on how to display the data.

# Django Getting Started

# step 1 
# To install Django, you must have Python installed, 
# and a package manager like PIP.
# To check if your system has Python installed, 
# run this command in the command prompt:
# py --version

# step 2
# set up a virtual environment
# The name of the virtual environment is your choice.
# py -m venv myworld
# Then you have to activate the environment, by typing this command:
# venv\Scripts\activate

# step 3
# Install Django
# Now, that we have created a virtual environment, 
# we are ready to install Django.
# Django is installed using pip, with this command:
# >py -m pip install Django
# ou can check if Django is installed
# django-admin --version

# step 4
# Django Create Project
# to start project type this in command:
# django-admin startproject projectname

# Navigate to the /projectname folder and 
# execute this command in the command prompt:
# cd projectname
# execute with
# py manage.py runserver

# step 5
# Django Create App
# An app is a web application that has a specific meaning 
# in your project, like a home page, a contact form, 
# or a members database.
# To create app type:
# py manage.py startapp foldername

# install the folder in setting.py file in INSTALLED_APPS[]
# Then run this command:
# py manage.py migrate

# Views
# Django views are Python functions that takes http requests 
# and returns http response, like HTML documents.
# in views.py type
# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello world!")

# link it to urls file
# URLs
# Create a file named urls.py in the same folder as the views.py
# file, and type this code in it:

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]

# in ulrs file inside projectname type
# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('', include('members.urls')),
#     path('admin/', admin.site.urls),
# ]

# Django Model
# A Django model is a table in your database.
# To create a model, navigate to the models.py file in the /appname/ folder.
# 

# when we have described a Model in the models.py file, 
# we must run a command to actually create the table in the database.

# run py manage.py makemigrations app  foldername.
# Django creates a file describing the changes and stores the file in the /migrations/ folder.
#  Django inserts an id field for your tables, which is an auto increment number

# The table is not created yet, you will have to run one more command,
# then Django will create and execute an SQL statement, 
# based on the content of the new file in the /migrations/ folder.

# Run the migrate command:
# py manage.py migrate

# you can view the SQL statement that were executed from the migration.
# run this command, with the migration number:
# py manage.py sqlmigrate members 0001


# To open a Python shell, type this command:
# Run py manage.py shell
# >>> from appfolder.models import tablename
# Tablename.objects.all() to querry all
# A QuerySet is a collection of data from a database.

# Add Records
# Add a record to the table, by executing these two lines:
# >>> member = Tablename(firstname='Emil', lastname='Refsnes')
# >>> member.save()
# Execute this command to see if the Member table got a member:
# >>> Member.objects.all().values()

# Add Multiple Records
# >>> member1 = Member(firstname='Tobias', lastname='Refsnes')
# >>> member2 = Member(firstname='Linus', lastname='Refsnes')
# >>> member3 = Member(firstname='Lene', lastname='Refsnes')
# >>> member4 = Member(firstname='Stale', lastname='Refsnes')
# >>> member5 = Member(firstname='Jane', lastname='Doe')
# >>> members_list = [member1, member2, member3, member4, member5]
# >>> for x in members_list:
# >>>   x.save()

# Update Records
# To update records that are already in the database, 
# we first have to get the record we want to update:
# >>> from members.models import Member
# >>> x = Member.objects.all()[3]
# let us see if that is correct:
# >>> x.firstname

# To change the values of this record:
# >>> x.firstname = "newname"
# >>> x.save()
# Execute this command to see if the Member table got updated:
# >>> Member.objects.all().values()

# Delete Records
# To delete a record in a table, 
# start by getting the record you want to delete:
# >>> x = Member.objects.all()[2]
# see if that is correct:
# >>> x.firstname
# Then delete the record:
# >>> x.delete()
# The result will be:
# (1, {'members.Member': 1})
# Which tells us how many items were deleted, and from which Model.

# Add Fields in the Model
# To add a field to a table after it is created, 
# open the models.py file, and make your changes:
# class Member(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   phone = models.IntegerField()
#   joined_date = models.DateField()

# Make a migration to tell Django that it has to update the database:
# py manage.py makemigrations appfoldername
# If Django ask if I want to provide the fields with a specific value,
# or if I want to stop the migration and fix it in the model:

# I will select option 2, and open the models.py file again and 
# allow NULL values for the two new fields:

# And make the migration once again:
# py manage.py makemigrations members
# Then Run the migrate command:
# py manage.py migrate

# Insert Data
# We can insert data to the two new fields with the same approach 
# as we did in the Update Data chapter:

# First we enter the Python Shell:
# py manage.py shell
# import the table and insert the date
# >>> from members.models import Member
# >>> x = Member.objects.all()[0]
# >>> x.phone = 5551234
# >>> x.joined_date = '2022-01-05'
# >>> x.save()

# Create Template
# After creating Models, with the fields and data we want in them,
# it is time to display the data in a web page.
# step 1
# Start by creating an HTML file.
# step 2
# Modify View
# we need to make the model data available in the template. 
# This is done in the view.
# In the view we have to import the db tabel model, and 
# send it to the template like this:

# from django.http import HttpResponse
# from django.template import loader
# from .models import Member

# def members(request):
#   mymembers = Member.objects.all().values()
#   template = loader.get_template('all_members.html')
# Creates an object containing the mymembers object.

#   context = {
#     'mymembers': mymembers,
#   }
# Sends the object to the template.
#   return HttpResponse(template.render(context, request))

# Then go to the html file you created and 
# <ul>
#   {% for x in mymembers %}
#     <li>{{ x.firstname }} {{ x.lastname }}</li>
#   {% endfor %}
# </ul>


# Details Template
# we can list more details about a specific member.
# step 1
# start by creating a new template called details.html:
# add link to it
# <body>
#   <h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>
#   <p>Phone: {{ mymember.phone }}</p>
#   <p>Member since: {{ mymember.joined_date }}</p>
#   <p>Back to <a href="/members">Members</a></p>
# </body>
# step 2
# add link to all_member.html:
# <ul>
#   {% for x in mymembers %}
#     <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
#   {% endfor %}
# </ul>
# step 3
# Create new view
# def details(request, id):
#   mymember = Member.objects.get(id=id)
#   template = loader.get_template('details.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))
# step 4
# Add urls
# urlpatterns = [
#     path('members/', views.members, name='members'),
#     path('members/details/<int:id>', views.details, name='details'),
# ]

# Add Master Template
# The extends Tag
# Django provides a way of making a "parent template" that you can include in all 
# pages to do the stuff that is the same in all pages.
# Start by creating a template called master.html, with all the necessary HTML elements:
# <!DOCTYPE html>
# <html>
# <head>
#   <title>{% block title %}{% endblock %}</title>
# </head>
# <body>
# {% block content %}
# {% endblock %}
# </body>
# </html>

# Modify Templates
# {% extends "master.html" %}

# {% block title %}
#   My Tennis Club - List of all members
# {% endblock %}

# {% block content %}
#   <h1>Members</h1>
  
#   <ul>
#     {% for x in mymembers %}
#       <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
#     {% endfor %}
#   </ul>
# {% endblock %}

# Add Main Index Page
# project needs a main page.
# Defaul page
# The main page will be the landing page when someone visits
#  the root folder of the project.
# step 1
# create main.html
# {% extends "master.html" %}

# {% block title %}
#   My Tennis Club
# {% endblock %}

# {% block content %}
#   <h1>My Tennis Club</h1>
#   <h3>Members</h3>
#   <p>Check out all our <a href="members/">members</a></p>
  
# {% endblock %}
# step 2
# Create new View
# def main(request):
#   template = loader.get_template('main.html')
#   return HttpResponse(template.render())
# step 3
# Add url
# urlpatterns = [
#     path('', views.main, name='main'),
#     path('members/', views.members, name='members'),
#     path('members/details/<int:id>', views.details, name='details'),
# ]
# step 4
# Then in setting.py Change DEBUG = True


# 404 (page not found)

# if you get:
# page not found (404)
# requst method GET
# request URL:http://127.0.0.1:8000/filename
# step 1
# then DEBUG is set to True in your settings, 
# and you must set it to False to get directed to the 404 template.

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
# ALLOWED_HOSTS = ['*'] 
# '*', which means any address are allowed to host this site.
# then you will get
# not found
# The requested resource was not found on this server
# step 2
# Customize the 404 Template
# Django will look for a file named 404.html in the templates folder,
# and display it when there is a 404 error.
# To customize this message, all you have to do is to create a file 
# in the templates folder and name it 404.html, and fill it with
#  whatever you want:
# <title>Wrong address</title>
# <body>
# <h1>Ooops!</h1>
# <h2>I cannot find the file you requested!</h2>
# </body>

# In the browser window, type 127.0.0.1:8000 in the address
# bar, and you will get the customized 404 template:

# Add Test View
# When testing different aspects of Django, it can be a good idea
# to have somewhere to test code without destroying the main project.
# It is optional

# step 1
# Add View
# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))

# step 2
# Add URLs
# urlpatterns = [
#     path('', views.main, name='main'),
#     path('members/', views.members, name='members'),
#     path('members/details/<int:id>', views.details, name='details'),
#     path('testing/', views.testing, name='testing'),    
# ]

# step 3
# Create template.html file in template folder
# get the fruit from testing in veiws.py
# {% for x in fruits %}
#   <h1>{{ x }}</h1>
# {% endfor %}

# To see the output
# In the browser window, type 127.0.0.1:8000/testing/ in the address bar.
