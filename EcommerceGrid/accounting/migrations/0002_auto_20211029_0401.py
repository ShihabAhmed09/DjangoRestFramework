# Generated by Django 3.2.7 on 2021-10-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertransactiontrigger',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='debit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
