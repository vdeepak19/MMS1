# Generated by Django 3.1.4 on 2020-12-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20181112_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('In - Sem 1', 'In - Sem 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Quiz', 'Quiz'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('In - Sem 1', 'In - Sem 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Quiz', 'Quiz'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
