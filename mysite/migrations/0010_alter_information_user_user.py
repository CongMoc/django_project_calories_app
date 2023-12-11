# Generated by Django 4.2.5 on 2023-12-03 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0009_remove_information_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_user',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Information_User', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]