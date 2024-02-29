# Template Variables
# In Django templates, you can render variables by 
# putting them inside {{ }} brackets:
# <h1>Hello {{ firstname }}, how are you?</h1>
# Create Variable in View
# The variable firstname in the example was sent to the template via a view:
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Linus',
#   }
#   return HttpResponse(template.render(context, request))
# we create an object named context and fill it with data, and
# send it as the first parameter in the template.render() function.

# Create Variables in Template
# You can also create variables directly in the template, 
# by using the {% with %} template tag.
# The variable is available until the {% endwith %} tag appears:
# {% with firstname="Tobias" %}
# <h1>Hello {{ firstname }}, how are you?</h1>
# {% endwith %}

# Data From a Model
# To get data from the Member model, we will have to import it in 
# the views.py file, and extract data from it in the view:
# from .models import Member
# def testing(request):
#   mymembers = Member.objects.all().values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))

# Now we can use the data in the template:
# <ul>
#   {% for x in mymembers %}
#     <li>{{ x.firstname }}</li>
#   {% endfor %}
# </ul>

# Template Tags
# In Django templates, you can perform programming logic like
# executing if statements and for loops.
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% else %}
#   <h1>Bye</h1>
# {% endif %}

# Django Code
# The template tags are a way of telling Django that here comes
# something else than plain HTML.

# The template tags allows us to to do some programming on the server
# before sending HTML to the client.

# <ul>
#   {% for x in mymembers %}
#     <li>{{ x.firstname }}</li>
#   {% endfor %}
# </ul>

# A list of all template tags:

# autoescape Specifies if autoescape mode is on or off
# block	Specifies a block section
# comment Specifies a comment section
# csrf_token Protects forms from Cross Site Request Forgeries
# cycle	Specifies content to use in each cycle of a loop
# debug	Specifies debugging information
# extends Specifies a parent template
# filter Filters content before returning it
# firstof Returns the first not empty variable
# for Specifies a for loop
# if Specifies a if statement
# ifchanged	Used in for loops. Outputs a block only if a value
#  has changed since the last iteration
# include Specifies included content/template
# load Loads template tags from another library
# lorem	Outputs random text
# now Outputs the current date/time
# regroup Sorts an object by a group
# resetcycle Used in cycles. Resets the cycle
# spaceless	Removes whitespace between HTML tags
# templatetag Outputs a specified template tag
# url Returns the absolute URL part of a URL
# verbatim Specifies contents that should not be rendered by the template engine
# widthratio Calculates a width value based on the ratio between a given value and a max value
# with	Specifies a variable to use in the block

# Django If Statement
# if
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% endif %}

# elif
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% elif greeting == 2 %}
#   <h1>Welcome</h1>
# {% endif %}

# else
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% elif greeting == 2 %}
#   <h1>Welcome</h1>
# {% else %}
#   <h1>Goodbye</h1>
# {% endif %} 

# Operators
# Is equal to.
# {% if greeting == 2 %}
#   <h1>Hello</h1>
# {% endif %}

# Is not equal to.
# {% if greeting != 1 %}
#   <h1>Hello</h1>
# {% endif %}

# Is less than.
# {% if greeting < 3 %}
#   <h1>Hello</h1>
# {% endif %}

# Is greater than.
# {% if greeting > 1 %}
#   <h1>Hello</h1>
# {% endif %} 

# Is less than, or equal to.
# {% if greeting <= 3 %}
#   <h1>Hello</h1>
# {% endif %}

# Is greater than, or equal to.
# {% if greeting >= 1 %}
#   <h1>Hello</h1>
# {% endif %}

# and
# To check if more than one condition is true.
# {% if greeting == 1 and day == "Friday" %}
#   <h1>Hello Weekend!</h1>
# {% endif %}

#or
# To check if one of the conditions is true.
# {% if greeting == 1 or greeting == 5 %}
#   <h1>Hello</h1>
# {% endif %}

# and/or
# Combine and and or.
# {% if greeting == 1 and day == "Friday" or greeting == 5 %}
#   <h1>Hello Weekend!</h1>
# {% endif %}

# in
# To check if a certain item is present in an object.
# {% if 'Banana' in fruits %}
#   <h1>Hello</h1>
# {% else %}
#   <h1>Goodbye</h1>
# {% endif %} 

# not in
# To check if a certain item is not present in an object.
# {% if 'Banana' not in fruits %}
#   <h1>Hello</h1>
# {% else %}
#   <h1>Goodbye</h1>
# {% endif %}

# is
# Check if two objects are the same.

# views.py:
# In the view we have two objects, x and y, with the same values:
# from django.http import HttpResponse
# from django.template import loader

# The two objects have the same value, but is it the same object?
# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'x': ['Apple', 'Banana', 'Cherry'], 
#     'y': ['Apple', 'Banana', 'Cherry'], 
#   }
#   return HttpResponse(template.render(context, request))

# Html
# {% if x is y %}
#   <h1>YES</h1>
# {% else %}
#   <h1>NO</h1>
# {% endif %}

# try the same example with the == operator instead:
# {% if x == y %}
#   <h1>YES</h1>
# {% else %}
#   <h1>NO</h1>
# {% endif %} 

# with
# {% with var1=x var2=x %}
#   {% if var1 is var2 %}
#     <h1>YES</h1>
#   {% else %}
#     <h1>NO</h1>
#   {% endif %}
# {% endwith %}

# is not
# To check if two objects are not the same.
# {% if x is not y %}
#   <h1>YES</h1>
# {% else %}
#   <h1>NO</h1>
# {% endif %}

# For Loops
# Loop through the items of a list
# {% for x in fruits %}
#   <h1>{{ x }}</h1>
# {% endfor %}

# Loop through a list of dictionaries:
# {% for x in cars %}
#   <h1>{{ x.brand }}</h1>
#   <p>{{ x.model }}</p>
#   <p>{{ x.year }}</p>
# {% endfor %}

# Django has some variables that are available for you inside a loop:
# forloop.counter
# forloop.counter0
# forloop.first
# forloop.last
# forloop.parentloop
# forloop.revcounter
# forloop.revcounter0

# The current iteration, starting at 1.
# <ul>
#   {% for x in fruits %}
#     <li>{{ forloop.counter }}</li>
#   {% endfor %}
# </ul>

# The current iteration, starting at 0.
# <ul>
#   {% for x in fruits %}
#     <li>{{ forloop.counter0 }}</li>
#   {% endfor %}
# </ul>

# Allows you to test if the loop is on its first iteration.
# <ul>
#   {% for x in fruits %}
#     <li
#       {% if forloop.first %}
#         style='background-color:lightblue;'
#       {% endif %}
#     >{{ x }}</li>
#   {% endfor %}
# </ul>

# Allows you to test if the loop is on its last iteration.
# <ul>
#   {% for x in fruits %}
#     <li
#       {% if forloop.last %}
#         style='background-color:lightblue;'
#       {% endif %}
#     >{{ x }}</li>
#   {% endfor %}
# </ul>

# The current iteration if you start at the end and count backwards, ending up at 1.
# <ul>
#   {% for x in fruits %}
#     <li>{{ forloop.revcounter }}</li>
#   {% endfor %}
# </ul>

# The current iteration if you start at the end and count backwards, 
# ending up at 0.
# <ul>
#   {% for x in fruits %}
#     <li>{{ forloop.revcounter0 }}</li>
#   {% endfor %}
# </ul>

# Comments
# Comments allows you to have sections of code that should be ignored.
# {% comment %}
#   <h1>Welcome ladies and gentlemen</h1>
# {% endcomment %}

# Comment Description
# {% comment "this was the original welcome message" %}
#     <h1>Welcome ladies and gentlemen</h1>
# {% endcomment %}

# Smaller Comments
# <h1>Welcome{# Everyone#}</h1>

# Include
# The include tag allows you to include a template inside 
# the current template.
# templates/footer.html:
# {% include 'footer.html' %}

# Variables in Include
# templates/mymenu.html:
# <div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div> 
# Then in templates/template.html
# <body>
# {% include "mymenu.html" with me="TOBIAS" sponsor="W3SCHOOLS" %}
# </body>    