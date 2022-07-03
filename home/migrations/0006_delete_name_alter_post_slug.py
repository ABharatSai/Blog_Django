# Generated by Django 4.0.4 on 2022-07-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_post_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='date'),
        ),
    ]
