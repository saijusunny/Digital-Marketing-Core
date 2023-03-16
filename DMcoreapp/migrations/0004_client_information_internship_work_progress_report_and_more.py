# Generated by Django 4.0.2 on 2023-03-16 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0003_remove_user_registration_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('client_address', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('client_mail', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('bs_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('bs_website', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('bs_location', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('client_files', models.ImageField(blank=True, null=True, upload_to='images/client/')),
                ('seo', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('seo_txt', models.TextField(blank=True, default='', null=True)),
                ('seo_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('smm', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('smm_txt', models.TextField(blank=True, default='', null=True)),
                ('smm_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('sem', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('sem_txt', models.TextField(blank=True, default='', null=True)),
                ('sem_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('em', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('em_txt', models.TextField(blank=True, default='', null=True)),
                ('em_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('cm', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cm_txt', models.TextField(blank=True, default='', null=True)),
                ('cm_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('am', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('am_txt', models.TextField(blank=True, default='', null=True)),
                ('am_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('mm', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('mm_txt', models.TextField(blank=True, default='', null=True)),
                ('mm_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('vm', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('vm_txt', models.TextField(blank=True, default='', null=True)),
                ('vm_file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DMcoreapp.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField(blank=True, null=True)),
                ('fullname', models.CharField(max_length=200)),
                ('collegename', models.CharField(max_length=200)),
                ('reg_no', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('alternative_no', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/internship/')),
                ('qr', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('file_attached', models.FileField(blank=True, default='', null=True, upload_to='images/pdf/')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_works', to='DMcoreapp.client_information')),
                ('exe_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exe_works', to='DMcoreapp.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='progress_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_rprt', models.FileField(blank=True, default='', null=True, upload_to='images/pdf/')),
                ('graph', models.FileField(blank=True, default='', null=True, upload_to='images/graph/')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('Work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.work')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DMcoreapp.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='daily_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('workdone', models.TextField(blank=True, default='', null=True)),
                ('daily_file', models.FileField(blank=True, default='', null=True, upload_to='images/pdf/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DMcoreapp.user_registration')),
                ('work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.work')),
            ],
        ),
        migrations.CreateModel(
            name='addi_client_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labels', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('discription', models.TextField(blank=True, default='', null=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to='images/requirement/')),
                ('section', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DMcoreapp.client_information')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DMcoreapp.user_registration')),
            ],
        ),
    ]
