# Generated by Django 5.0 on 2023-12-27 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('about', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('Tfo', 'Tfo'), ('Master', 'Master'), ('Karigar', 'Karigar'), ('Cleaner', 'Cleaner'), ('New', 'New'), ('Expert', 'Expert')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.company')),
            ],
        ),
    ]