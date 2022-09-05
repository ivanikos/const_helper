from django.db import models

# Модель стыка - Таблица стыков в базе данных
class joint(models.Model):
    title = models.CharField(max_length=30, verbose_name='Титул')
    line = models.CharField(max_length=30, verbose_name='Линия')
    doctitle = models.CharField(max_length=60, verbose_name='Номер чертежа')
    isometric = models.CharField(max_length=60, verbose_name='Изометрия')
    category = models.CharField(max_length=20)
    control = models.CharField(max_length=20)
    materialsteel = models.CharField(max_length=30)
    spoolnumber = models.CharField(max_length=30)
    locationweld = models.CharField(max_length=10, verbose_name='Место сварки')
    numberjoint = models.CharField(max_length=10, verbose_name='Номер стыка')
    typeweld = models.CharField(max_length=10)
    dinch = models.FloatField()
    wayweld = models.CharField(max_length=30)
    dateweld = models.DateTimeField(verbose_name='Дата сварки')
    stamproot1 = models.CharField(max_length=10)
    stamproot2 = models.CharField(max_length=10, null=True, blank=True)
    stampfilling1 = models.CharField(max_length=10)
    stampfilling2 = models.CharField(max_length=10, null=True, blank=True)
    diameter1 = models.FloatField()
    thickness1 = models.FloatField()
    diameter2 = models.FloatField()
    thickness2 = models.FloatField()
    element1 = models.CharField(max_length=60)
    element2 = models.CharField(max_length=60)
    material1 = models.CharField(max_length=60)
    material2 = models.CharField(max_length=60)
    conclusion_vik_date = models.DateTimeField(null=True, blank=True)
    conclusion_vik_result = models.CharField(max_length=2, null=True, blank=True)
    conclusion_vik_number = models.CharField(max_length=80, null=True, blank=True)
    conclusion_vik_file = models.FileField(upload_to='conclusion_vik/', null=True, blank=True)

    # def __str__(self):
    #     return f'{self.line} - {self.isometric} - {self.locationweld}{self.numberjoint}'

    class Meta:
        verbose_name = 'Сварные стыки'
        verbose_name_plural = 'Сварочный журнал'
        ordering = ['-dateweld']

class Work(models.Model):
    id_work = models.CharField(max_length=36, verbose_name='Идентификатор работы')
    type_work = models.CharField(max_length=256, verbose_name='Вид работы')
    unit_measure = models.CharField(max_length=15, verbose_name='Единица измерения')


class Test(models.Model):
    work = models.CharField(max_length=50, verbose_name='Работа')
    type_w = models.CharField(max_length=256, blank=True)

class Test1(models.Model):
    unit_meas = models.CharField(max_length=100)
    all_vol = models.FloatField()
    t_work = models.ForeignKey(Test, on_delete=models.CASCADE)