# Generated by Django 4.0.2 on 2023-05-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0046_addi_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_information',
            name='leeds',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='client_information',
            name='leeds_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/requirement/'),
        ),
        migrations.AddField(
            model_name='client_information',
            name='leeds_target',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='client_information',
            name='leeds_txt',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
