from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Department(MPTTModel):
    name = models.CharField(max_length=255,
                            verbose_name='Название')
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True, blank=True,
                            verbose_name='Родитель',
                            related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, verbose_name='Должность')
    employment_date = models.DateField(verbose_name='Дата приема на работу')
    salary = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Зарплата')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Отдел')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
