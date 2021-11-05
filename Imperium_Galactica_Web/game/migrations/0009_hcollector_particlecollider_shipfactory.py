# Generated by Django 3.2.8 on 2021-11-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_alter_steelmills_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='HCollector',
            fields=[
                ('Level', models.AutoField(primary_key=True, serialize=False)),
                ('Steel', models.PositiveIntegerField(default=0)),
                ('Hydrogen', models.PositiveIntegerField(default=0)),
                ('AntiMatter', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ParticleCollider',
            fields=[
                ('Level', models.AutoField(primary_key=True, serialize=False)),
                ('Steel', models.PositiveIntegerField(default=0)),
                ('Hydrogen', models.PositiveIntegerField(default=0)),
                ('AntiMatter', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ShipFactory',
            fields=[
                ('Level', models.AutoField(primary_key=True, serialize=False)),
                ('Steel', models.PositiveIntegerField(default=0)),
                ('Hydrogen', models.PositiveIntegerField(default=0)),
                ('AntiMatter', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
