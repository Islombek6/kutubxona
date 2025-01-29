from django.db import models


class Student(models.Model):
    KURSLAR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    ism = models.CharField(max_length=100)
    gurux = models.CharField(max_length=10)
    kurs = models.CharField(max_length=5, choices=KURSLAR)
    kitoblar_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Studentlar'

    objects = models.Manager()


class KUtubxonachi(models.Model):
    ish_vaqti = (
        ('08:00 - 13:00', '08:00 - 13:00'),
        ('13:00 - 18:00', '13:00 - 18:00'),
        ('18:00 - 23:00', '18:00 - 23:00'),
    )
    ism = models.CharField(max_length=110)
    ish_vaqt = models.CharField(max_length=30, choices=ish_vaqti)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Kutubxonachilar'

    objects = models.Manager()


class Muallif(models.Model):
    jins_choices = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )
    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=10, choices=jins_choices)
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Mualliflar'

    objects = models.Manager()


class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    Janr = models.CharField(max_length=100)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Kitoblar'

    objects = models.Manager()


class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(KUtubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateTimeField()
    qaytargan_sana = models.DateTimeField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.ism} - {self.kitob.nom}" # noqa

    class Meta:
        verbose_name_plural = 'Recordlar'

    objects = models.Manager()