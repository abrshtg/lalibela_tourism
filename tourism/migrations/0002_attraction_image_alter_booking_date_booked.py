# Generated by Django 5.0.3 on 2024-03-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='image',
            field=models.ImageField(blank=True, default='tourism/static/tourism/1.jpeg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_booked',
            field=models.DateTimeField(),
        ),
    ]