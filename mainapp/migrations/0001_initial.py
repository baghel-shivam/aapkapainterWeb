# Generated by Django 4.0.4 on 2022-08-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('phn_num', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=100)),
            ],
        ),
    ]
