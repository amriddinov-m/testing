from django.contrib import admin
from django.contrib.auth.models import User, Group
from django_mptt_admin.admin import DjangoMpttAdmin
from main.models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(DjangoMpttAdmin):
    list_display = 'name', 'parent'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = 'full_name', 'position', 'employment_date', 'salary', 'department'
    list_filter = 'position',
    list_per_page = 15


admin.site.unregister(User)
admin.site.unregister(Group)
