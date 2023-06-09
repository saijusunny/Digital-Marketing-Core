# Generated by Django 4.0.2 on 2023-04-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0010_daily_off_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='sub_des',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='sub_file',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/pdf/'),
        ),
        migrations.AddField(
            model_name='work',
            name='sub_task',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
