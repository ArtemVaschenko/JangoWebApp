# Generated by Django 4.1.2 on 2022-11-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mane', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
