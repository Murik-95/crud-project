from django.db import models

class Person(models.Model):
    name = models.CharField('Имя ', max_length=50)
    age = models.IntegerField('Возраст ',)
    date = models.DateField('Дата рождения ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'
