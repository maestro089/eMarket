# Generated by Django 4.0.6 on 2023-01-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='points_of_issue_adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('sity', models.CharField(max_length=255, verbose_name='Sity')),
                ('street', models.CharField(max_length=255, verbose_name='Street')),
                ('num_home', models.CharField(max_length=255, verbose_name='Number home')),
            ],
        ),
        migrations.DeleteModel(
            name='user_adress',
        ),
    ]
