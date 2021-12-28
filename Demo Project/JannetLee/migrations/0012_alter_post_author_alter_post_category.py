# Generated by Django 4.0 on 2021-12-28 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('JannetLee', '0011_alter_post_attack_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, max_length=32, null=True, on_delete=django.db.models.deletion.SET_NULL, to='JannetLee.category'),
        ),
    ]
