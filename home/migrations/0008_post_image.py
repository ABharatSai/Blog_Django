# Generated by Django 4.0.4 on 2022-07-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/temp.jpg', upload_to='images/'),
        ),
    ]
