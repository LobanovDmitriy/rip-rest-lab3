# Generated by Django 4.1.2 on 2022-10-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('idservice', models.IntegerField(db_column='idService', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
