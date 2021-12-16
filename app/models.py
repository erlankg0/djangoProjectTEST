from django.db import models


class SAP(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256, unique=True)
    count = models.PositiveIntegerField(verbose_name='Количество')
    distance = models.PositiveIntegerField(verbose_name='Дистанция')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'SAP'
        verbose_name_plural = "SAP's"

    def __str__(self):
        return self.name
