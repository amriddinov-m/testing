from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from main.models import Department


class HomeView(TemplateView):
    template_name = 'index.html'


@csrf_exempt
def get_all_departments(request):
    result = []
    departments = Department.objects.filter(parent__isnull=True)
    for department in departments:
        result.append({
            'type': 'parent',
            'text': department.name,
            'state': {'opened': 'true', 'selected': 'true'},
            'children': [
                {
                    'text': children.name,
                    'type': 'child',
                    'state': {'opened': 'true'},
                    'children': [
                        {
                            'text': sub_children.name,
                            'type': 'child',
                            'state': {'opened': 'true'},
                            'children': [
                                {
                                    'text': employee.full_name,
                                    'type': 'sub_child',
                                    'state': {'opened': 'true'}
                                } for employee in sub_children.employee_set.all()
                            ]
                        } for sub_children in children.get_children()
                    ]
                } for children in department.get_children()
            ]
        })
    return JsonResponse(result, safe=False)
