# Generated by Django 4.2.5 on 2023-12-10 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_information_user_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='Category_Exercise',
            new_name='categoryExercise',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='Exercise_Image',
            new_name='exerciseImage',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='Category_Food',
            new_name='categoryFood',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='Food_Image',
            new_name='foodImage',
        ),
    ]
