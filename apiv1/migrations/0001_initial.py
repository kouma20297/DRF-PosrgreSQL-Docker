# Generated by Django 4.0.3 on 2024-01-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testname', models.CharField(max_length=100)),
                ('testvalue', models.IntegerField()),
            ],
        ),
    ]
