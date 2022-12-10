# Generated by Django 4.1.1 on 2022-12-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_contact_options_alter_contact_kind_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='título')),
                ('start', models.TimeField(verbose_name='começo')),
                ('description', models.TextField(verbose_name='descrição')),
                ('speakers', models.ManyToManyField(to='core.speaker', verbose_name='palestrante')),
            ],
        ),
    ]
