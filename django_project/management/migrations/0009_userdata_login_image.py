# Generated by Django 5.1.1 on 2024-09-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_doctorlogin_alter_patientdetails_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='login_image',
            field=models.ImageField(blank=True, null=True, upload_to='Login/'),
        ),
    ]
