# Generated by Django 3.2.8 on 2021-11-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20211105_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steelmills',
            name='Level',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
