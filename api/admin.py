from django.contrib import admin
from api.models import *
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name', 'type')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'position')
    search_fields=('name', 'phone')
    list_filter=('company',)

admin.site.register(Company, CompanyAdmin),
admin.site.register(Employee, EmployeeAdmin)
