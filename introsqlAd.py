# Django Admin
# Django Admin is a really great tool in Django,
# it is actually a CRUD* user interface of all your models!

# CRUD stands for Create Read Update Delete.

# Create User,
# To be able to log into the admin application, we need to create a user.
# This is done by typing this command in the command view:
# step 1
# py manage.py createsuperuser
# Which will give this prompt:
# Username:
# Here you must enter: username, e-mail address,
# (you can just pick a fake e-mail address), and password

# Include Member in the Admin Interface
# To include the Member model in the admin interface, 
# we have to tell Django that this model should be visible in the
# admin interface.
# This is done in a file called admin.py, and is located in your 
# app's folder, which in our case is the members folder.

# In admin.py type:
# from django.contrib import admin
# from .models import Member

# Register your models here.
# admin.site.register(Member)
# Then go  to the browser and you should get this result
# Make the List Display More Reader-Friendly
# When you display a Model as a list, Django displays each record as
# the string representation of the record object,
# which in our case is "Member object (1)", "Member object(2)" etc.

# To change this to a more reader-friendly format, we have two choices:

# Change the string representation function, __str__() of the Member Model
# Set the list_details property of the Member Model

# To change the string representation, we have to define the
# __str__() function of the Member Model in models.py, like this:
# class Member(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   phone = models.IntegerField(null=True)
#   joined_date = models.DateField(null=True)

#   def __str__(self):
#     return f"{self.firstname} {self.lastname}"

# __str__() function is not a Django feature, 
# it is how to change the string representation of objects in Python.

# Set list_display
# We can control the fields to display by specifying them in in a
# list_display property in the admin.py file.
# First create a MemberAdmin() class and specify 
# the list_display tuple, like this:

# from django.contrib import admin
# from .models import Member
# Register your models here.
# class MemberAdmin(admin.ModelAdmin):
#   list_display = ("firstname", "lastname", "joined_date",)
  
# admin.site.register(Member, MemberAdmin)
# Remember to add the MemberAdmin as an argumet in the 
# admin.site.register(Member, MemberAdmin).

# Update Members
# Now we are able to create, update, and delete members in our
#  database, and we start by giving them all a date for when
#  they became members.
# Click the any member, to open the record for editing, and edit.

# Add Members
# To add a new member, 
# click on the "ADD MEMBERS" button in the top right corner.
# Delete Members
# To delete a new member, you can either select a member and
# choose the action "Delete selected members" 
# Or you can open a member for editing, and 
# click the red DELETE button at the bottom, like this: