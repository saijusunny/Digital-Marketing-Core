# Generated by Django 4.0.2 on 2023-04-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0011_work_sub_des_work_sub_file_work_sub_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='smo_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('email', models.CharField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
            ],
        ),
    ]
