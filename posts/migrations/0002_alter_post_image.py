# Generated by Django 3.2.4 on 2024-09-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_oszqxy', upload_to='images/'),
        ),
    ]