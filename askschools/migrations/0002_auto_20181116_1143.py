# Generated by Django 2.1.1 on 2018-11-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askschools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schools',
            name='ADVANTAGE',
            field=models.TextField(blank=True, help_text='what do parents tend to benefit  by entrusting their children\n\t  in your school not more than 1000 characters', max_length=1000),
        ),
        migrations.AlterField(
            model_name='schools',
            name='FEES_RANGE',
            field=models.CharField(choices=[('#51,000.00 - #100,000.00', '#51,000.00 - #100,000.00'), ('#101,000.00 - 200,000.00', '#101,000.00 - 200,000.00'), ('#201,000.00  - 300,000.00', '#201,000.00  - 300,000.00'), ('#301,000.00  - 400,000.00', '#301,000.00  - 400,000.00'), ('#401,000.00  - 500,000.00', '#401,000.00  - 500,000.00'), ('#501,000.00  - 600,000.00', '#501,000.00  - 600,000.00'), ('#601,000.00  - 700,000.00', '#601,000.00  - 700,000.00'), ('#701,000.00  - 800,000.00', '#701,000.00  - 800,000.00'), ('#801,000.00  - 900,000.00', '#801,000.00  - 900,000.00'), ('#901,000.00  - 1,000,000.00', '#901,000.00  - 1,000,000.00')], max_length=70),
        ),
        migrations.AlterField(
            model_name='schools',
            name='PHONE',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='schools',
            name='SCHOOL_TYPE',
            field=models.CharField(choices=[('Day', 'Day'), ('Boarding', 'Boarding'), ('Boarding and Day', 'Boarding and Day')], max_length=20),
        ),
    ]