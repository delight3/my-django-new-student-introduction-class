# Create Static Folder.
# When building web applications, you probably want to add
# some static files like images or css files.
# Start by creating a folder named static in your project,
# the same place where you created the templates folder:

# Add a CSS file in the static folder
# step 1
# static/style.css:
# body {
#   background-color: lightblue;
#   font-family: verdana;
# }

# step 2
# Modify the Template
# Open the HTML file and add the following:
# {% load static %}
# And:
# <link rel="stylesheet" href="{% static 'myfirst.css' %}">

# Example:
# {% load static %}
# <!DOCTYPE html>
# <html>
# <link rel="stylesheet" href="{% static 'myfirst.css' %}">
# <body>
# {% for x in fruits %}
#   <h1>{{ x }}</h1>
# {% endfor %}
# </body>
# </html>
# Didn't Work?
# You will have install a third-party library in order to handle
# static files.
# use a Python library called WhiteNoise

# Django - Installing WhiteNoise
# WhiteNoise
# Django does not have a built-in solution for serving static files,
# at least not in production when DEBUG has to be False.

# Install WhiteNoise
# To install WhiteNoise in your virtual environment, 
# type the command below:
# pip install whitenoise

# Modify Settings
# To make Django aware of you wanting to run WhitNoise,
# you have to specify it in the MIDDLEWARE list in settings.py file:
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ].

# Django - Collect Static Files
# Handle Static Files
# Static files in your project, like stylesheets, JavaScripts, and
# images, are not handled automatically by Django when DEBUG = False.

# When DEBUG = True, this worked fine, all we had to do was to put 
# them in the static folder of the application.

# When DEBUG = False, static files have to be collected and 
# put in a specified folder before we can use it.

# Collect Static Files
# To collect all necessary static files for your project, 
# start by specifying a STATIC_ROOT property in the settings.py file.
# This specifies a folder where you want to collect your static files.
# call it productionfiles
# In settings.py add:
# STATIC_ROOT = BASE_DIR / 'productionfiles'

# You could manually create this folder and collect and
# put all static files of your project into this folder, 
# but Django has a command that do this for you:

# py manage.py collectstatic
# Which will produce this result:
# 131 static files copied to 'C:\Users\folder_name\productionfiles'.

# Django - Global Static Files
# Add a Global CSS File
# We have learned how to add a static file in the application's
# static folder, and how to use it in the application.
# But what if other applications in your project wants to use the
# file?
# Then we have to create a folder on the root directory and
# put the file(s) there.

# Create a folder on the project's root level, this folder can be
# called whatever you like, I will call it mystaticfiles.

# Add a CSS file in the mystaticfiles folder, 
# the name is your choice, we will call it myglobal.css 

# Modify Settings
#Add this in your settings.py file:
# STATICFILES_DIRS = [
#     BASE_DIR / 'mystaticfiles'
# ]

# In the STATICFILES_DIRS list, you can list all the directories
# where Django should look for static files.

# The BASE_DIR keyword represents the root directory of the project,
# and together with the / "mystaticfiles", it means the 
# mystaticfiles folder in the root directory.

# Modify the Template
# {% load static %}
# And refer to the file like this:
# <link rel="stylesheet" href="{% static 'myglobal.css' %}">

# Example:
# {% load static %}
# <!DOCTYPE html>
# <html>
# <link rel="stylesheet" href="{% static 'myglobal.css' %}">
# <body>
# {% for x in fruits %}
#   <h1>{{ x }}</h1>
# {% endfor %}
# </body>
# </html>

# Collect Static Files
# Run the collectstatic command to collect the new static file:
# py manage.py collectstatic

# Which will produce this result:
# You have requested to collect static files at the destination
# location as specified in your settings:

#   C:\Users\Your Name\myworld\project_folder\productionfiles

# This will overwrite existing files!
# Are you sure you want to do this?

# Type 'yes' to continue, or 'no' to cancel:
# Type yes:

# Which will produce this result:

# 1 static file copied to 'C:\Users\Your Name\productionfiles', 131 unmodified.