# Generated by Django 4.1.1 on 2022-12-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('website', models.URLField()),
                ('photo', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]