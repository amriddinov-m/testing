import random

from django.core.management import BaseCommand
from faker import Faker

from main.models import Department, Employee

fake = Faker()

job_titles = [
    "Директор по продажам",
    "Менеджер по маркетингу",
    "Финансовый аналитик",
    "Программист-разработчик",
    "Дизайнер интерфейсов",
    "Специалист по кадровому делопроизводству",
    "Адвокат",
    "Бухгалтер",
    "Системный администратор",
    "Тестировщик программного обеспечения",
    "Аналитик данных",
    "Менеджер проектов",
    "Продавец-консультант",
    "Инженер-конструктор",
    "Маркетинговый менеджер",
    "Копирайтер",
    "Архитектор",
    "Медицинская сестра",
    "Психолог",
    "HR-специалист",
    "Офис-менеджер",
    "Электромонтажник",
    "Менеджер по закупкам",
    "Специалист по SEO",
    "Технический писатель",
    "Фармацевт",
    "Учитель",
    "Графический дизайнер",
    "Экономист",
    "Консультант по бизнес-анализу",
    "Врач",
    "Фотограф",
    "Монтажник мебели",
    "Электроинженер",
    "Юрист",
    "Телемаркетолог",
    "Инженер по качеству",
    "Арт-директор",
    "Инженер-системотехник",
    "Риелтор",
    "Косметолог",
    "Ассистент руководителя",
    "Физиотерапевт",
    "Журналист",
    "Анестезиолог",
    "Специалист по медицинской статистике",
    "Кинооператор",
    "Инспектор по качеству продукции",
    "Педиатр",
    "Консультант по информационной безопасности"
]

department_titles = [
    {
        'name': 'Отдел продаж',
        'children': [
            'Подразделение по продажам в регионе А',
            'Подразделение по продажам в регионе B',
            'Подразделение по продажам в регионе C',
            'Подразделение по продажам в регионе D',
            'Подразделение по онлайн-продажам'
        ]
    },
    {
        'name': 'Технический отдел',
        'children': [
            'Отдел разработки',
            'Отдел тестирования',
            'Отдел поддержки',
            'Отдел информационной безопасности',
            'Отдел IT-инфраструктуры'
        ]
    },
    {
        'name': 'Отдел маркетинга',
        'children': [
            'Отдел рекламы',
            'Отдел медиапланирования',
            'Отдел маркетинговых исследований',
            'Отдел событий и партнерств',
            'Отдел контент-маркетинга'
        ]
    },
    {
        'name': 'Финансовый отдел',
        'children': [
            'Отдел бухгалтерии',
            'Отдел финансового анализа',
            'Отдел кредитования и финансовых операций',
            'Отдел налогов',
            'Отдел управления бюджетом'
        ]
    },
    {
        'name': 'Отдел разработки',
        'children': [
            'Разработка веб-приложений',
            'Разработка мобильных приложений',
            'Внедрение новых технологий',
            'Разработка API',
            'Управление проектами и продуктами'
        ]
    }
]


def create_departments():
    root_department = Department.objects.create(name='Company')
    for index in range(5):
        department_name = department_titles[index]['name']
        parent = Department.objects.create(name=department_name, parent=root_department)
        for sub_index in range(5):
            department_child_name = department_titles[index]['children'][sub_index]
            Department.objects.create(name=department_child_name, parent=parent)


def create_employee(count):
    departments = Department.objects.all()
    for i in range(count):
        department = random.choice(departments)
        position = random.choice(job_titles)
        Employee.objects.create(
            full_name=fake.name(),
            position=position,
            employment_date=fake.date_between(start_date='-20y', end_date='today'),
            salary=random.randint(30000, 100000),
            department=department
        )


def generic_data():
    create_departments()
    create_employee(count=50000)


class Command(BaseCommand):
    help = 'Генерация данных'

    def handle(self, *args, **options):
        """Генерируем данные"""
        generic_data()
