# Generated by Django 2.1.1 on 2018-09-13 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SeniorManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=25)),
                ('reporting', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='reporting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app85.SeniorManager'),
        ),
        migrations.AddField(
            model_name='employee',
            name='reporting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app85.Manager'),
        ),
    ]
