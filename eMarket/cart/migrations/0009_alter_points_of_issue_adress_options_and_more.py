# Generated by Django 4.0.6 on 2023-03-08 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_order_options_order_adress_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='points_of_issue_adress',
            options={'verbose_name': 'Пункт выдачи', 'verbose_name_plural': 'Пункты выдачи'},
        ),
        migrations.AlterModelOptions(
            name='the_cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины пользователей'},
        ),
    ]
