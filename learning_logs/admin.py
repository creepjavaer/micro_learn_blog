from django.contrib import admin

# Register your models here.
# "begin my webapp"
#for register

from learning_logs.models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)