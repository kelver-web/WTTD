from django.db import models
from django.shortcuts import resolve_url as r
from core.managers import KindQuerySet, PeriodManager

# Create your models here.


class Speaker(models.Model):
    name = models.CharField('nome', max_length=50)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', self.slug)

class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=100)

    objects = KindQuerySet.as_manager() #Alinhando o API com um manager customizado 
    #objects = KindContactManager()
    # objects = models.Manager()
    # emails = EmailContactManager()
    # phones = PhoneContactManager()

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.value

class Activity(models.Model):
    title = models.CharField('título', max_length=225)
    start = models.TimeField('começo', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManager()

    class Meta:
        abstract = True
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title


class Talk(Activity):
    pass


class Course(Activity):
    slots = models.IntegerField()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
