# Django QuerySet
# A QuerySet is a collection of data from a database.
# A QuerySet is built up as a list of objects.
# QuerySets makes it easier to get the data you actually need,
# by allowing you to filter and order the data at an early stage.

# Querying Data
# In views.py:
# Step 1
# use the .all() method to get all the records and fields of the
# Member model:
# from django.http import HttpResponse
# from django.template import loader
# from .models import Member
# def testing(request):
#   mydata = Member.objects.all()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# The object is placed in a variable called mydata,
# and is sent tothe template via the context object as mymembers.

# Step 2
# In the template use the mymembers object to generate content
# Template
# <table border='1'>
#   <tr>
#     <th>ID</th>
#     <th>Firstname</th>
#     <th>Lastname</th>
#   </tr>
#   {% for x in mymembers %}
#     <tr>
#       <td>{{ x.id }}</td>
#         <td>{{ x.firstname }}</td>
#       <td>{{ x.lastname }}</td>
#     </tr>
#   {% endfor %}
# </table>

# Get Data
# There are different methods to get data from a model into a
# QuerySet.
# The values() Method
# The values() method allows you to return each object as a
# Python dictionary, with the names and values as key/value pairs:
# In views.py:
# def testing(request):
#   mydata = Member.objects.all().values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# Return Specific Columns
# The values_list() method allows you to return only the
# columns that you specify.
# Return only the firstname columns:
# In views.py:
# def testing(request):
#   mydata = Member.objects.values_list('firstname')
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# Return Specific Rows
# You can filter the search to only return specific rows/records,
# by using the filter() method.
# Return only the records where firstname is 'James':
# In views.py
# def testing(request):
#   mydata = Member.objects.filter(firstname='James').values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# QuerySet Filter
# The filter() method is used to filter your search, and
# allows you to return only the rows that matches the search term.

# Return only the records where the firstname is 'James':
# mydata = Member.objects.filter(firstname='James').values()

# In SQL, the above statement would be written like this:
# SELECT * FROM members WHERE firstname = 'Emil';

# AND
# The filter() method takes the arguments as
# **kwargs (keyword arguments), so you can filter on more than
# one field by separating them by a comma.

# Return records where lastname is "Refsnes" and id is 2:
# mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

# In SQL, the above statement would be written like this:
# SELECT * FROM members WHERE lastname = 'Refsnes' AND id = 2;

# OR
# To return records where firstname is Emil or firstname is Tobias
# (meaning: returning records that matches either query,
# not necessarily both)

# Return records where firstname is either "Emil" or Tobias":
# mydata = Member.objects.filter(firstname='Emil').values()
#          | Member.objects.filter(firstname='Tobias').values()

# Another common method is to import and use Q expressions:
# In views.py
# Return records where firstname is either "Emil" or Tobias":
# from django.http import HttpResponse
# from django.template import loader
# from .models import Member
# from django.db.models import Q
# def testing(request):
#   mydata = Member.objects.filter(Q(firstname='Emil') 
#            | Q(firstname='Tobias')).values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# In SQL, the above statement would be written like this:

#SELECT * FROM members WHERE firstname ='Emil' OR firstname ='Tobias';

# Field Lookups
# Django has its own way of specifying SQL statements and WHERE clauses.
# To make specific where clauses in Django, use "Field lookups".
# Field lookups are keywords that represents specific SQL keywords.

# Use the __startswith keyword:
# .filter(firstname__startswith='L');

# Is the same as the SQL statement:
# WHERE firstname LIKE 'L%'
# The above statement will return records 
# where firstname starts with 'L'.

# Field Lookups - contains
# The contains lookup is used to get records that 
# contains a specified value.
# Get all records that have the value "bias" in the firstname column:
# mydata = Member.objects.filter(firstname__contains='bias').values()

# The SQL equivalent to the example above will be:
# WHERE firstname LIKE '%bias%';

# Field Lookups - icontains
# Do a case insensitive search for all records that have the value
# "ref" in the lastname column:
# mydata = Member.objects.filter(lastname__icontains='ref').values()

# The SQL equivalent to the example above will be:
# WHERE lastname LIKE '%ref%';

# Field Lookups - endswith
# The endswith lookup is used to get records that ends 
# with a specified value.
# Get all records where firstname ends with the letter "s":
# mydata = Member.objects.filter(firstname__endswith='s').values()

# For a case insensitive search, use the iendswith lookup.

# The SQL equivalent to the example above will be:
# WHERE firstname LIKE '%s';

# Field Lookups - exact
# The exact lookup is used to get records with a specified value.
# Get all records where firstname is exactly "Emil":
# mydata = Member.objects.filter(firstname__exact='Emil').values()

# For a case insensitive search, use the iexact lookup.

# The SQL equivalent to the example above will be:
# WHERE firstname = 'Emil';

# Field Lookups - in
# The in lookup is used to get records where the value is one of
# the values in an iterable (list, tuple, string, queryset).
# Get all records where firstname is one of the values in the list:
# mydata = Member.objects.filter(
#          firstname__in=['Tobias', 'Linus', 'John']).values()

# The in lookup is case sensitive.

# The SQL equivalent to the example above will be:
# WHERE firstname IN ('Tobias', 'Linus', 'John');

# Field Lookups - gt (greater than)
# The gt lookup is used to get records that are larger 
# than a specified value.
# Get all records where id is larger than 3:
# mydata = Member.objects.filter(id__gt=3).values()

# For a greater than or equal to search, use the gte lookup.

# The SQL equivalent to the example above will be:
# WHERE id > 3;

# Field Lookups - lt (less than)
# The lt lookup is used to get records that are less than a 
# specified value.
# Get all records where id is less than 3:
# mydata = Member.objects.filter(id__lt=3).values()

# For a less than or equal to search, use the lte lookup.

# The SQL equivalent to the example above will be:
# WHERE id < 3;

# Field Lookups - range
# The range lookup is used to get records that are between two values.
# Get all records where id is between 2 and 4:
# mydata = Member.objects.filter(id__range=(2, 4)).values()

# The field can be of any type, numeric string or dates.
# Get all records where firstname is alphanumeric between 'G' and 'M':
# mydata = Member.objects.filter(
# firstname__range=('G', 'M')).values()
# remember that 'G' has a lower alphanumeric value than 'g'.

# The SQL equivalent to the two example above will be:
# WHERE id BETWEEN 2 AND 4;
# WHERE id BETWEEN 'G' AND 'M';

# Field Lookups - startswith
# The startswith lookup is used to get records that starts
# with a specified value.
# Get all records where firstname starts with the letter "S":
# mydata = Member.objects.filter(firstname__startswith='S').values()

# For a case insensitive search, use the istartswith lookup.

# The SQL equivalent to the example above will be:
# WHERE firstname LIKE 'S%';

# Django QuerySet - Order By
# Order By
# To sort QuerySets, Django uses the order_by() method:
# Order the result alphabetically by firstname:
# mydata = Member.objects.all().order_by('firstname').values()

# In SQL, the above statement would be written like this:
# SELECT * FROM members ORDER BY firstname;

# Descending Order
# By default, the result is sorted ascending (the lowest value first),
# to change the direction to descending (the highest value first),
# use the minus sign (NOT), - in front of the field name:
# Order the result firstname descending:
# mydata = Member.objects.all().order_by('-firstname').values()

# In SQL, the above statement would be written like this:
# SELECT * FROM members ORDER BY firstname DESC;

# Multiple Order Bys
# To order by more than one field, separate the fieldnames with
# a comma in the order_by() method:
# Order the result first by lastname ascending, then descending 
# on id:
# mydata = Member.objects.all().order_by('lastname', '-id').values()

# In SQL, the above statement would be written like this:
# SELECT * FROM members ORDER BY lastname ASC, id DESC;