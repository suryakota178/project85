from django.contrib import admin
from  app85.models import Manager,SeniorManager,Employee




admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(SeniorManager)