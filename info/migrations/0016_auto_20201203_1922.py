# Generated by Django 3.1.4 on 2020-12-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_auto_20201203_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
    ]
