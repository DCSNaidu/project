# Generated by Django 2.2.5 on 2021-07-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=20)),
                ('esal', models.FloatField()),
                ('eadd', models.CharField(max_length=20)),
            ],
        ),
    ]
