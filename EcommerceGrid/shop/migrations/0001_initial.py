# Generated by Django 3.2.7 on 2021-10-27 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStockLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.CharField(max_length=255)),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.album')),
            ],
        ),
        migrations.CreateModel(
            name='ShopBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.album')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'verbose_name_plural': 'Shop Branches',
                'unique_together': {('shop', 'name')},
            },
        ),
        migrations.CreateModel(
            name='StockAlertGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StockAlerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('stock_below', models.IntegerField()),
                ('stock_above', models.IntegerField()),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopbranch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'verbose_name_plural': 'Stock Alerts',
            },
        ),
        migrations.CreateModel(
            name='StockAlertTrigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('current_stock', models.IntegerField()),
                ('stock_alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.stockalerts')),
            ],
        ),
        migrations.CreateModel(
            name='StockAlertSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.stockalerts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockAlertGroupSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_alert_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.stockalertgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stockalertgroup',
            name='stock_alert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.stockalerts'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopbranch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'unique_together': {('shop', 'branch', 'product')},
            },
        ),
        migrations.CreateModel(
            name='ShopRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('SO', 'Shop Owner'), ('C', 'Customer'), ('DA', 'Delivery Agent')], max_length=200, null=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('shop', 'user', 'role')},
            },
        ),
        migrations.CreateModel(
            name='ShopBranchProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopbranch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'unique_together': {('shop', 'branch', 'product')},
            },
        ),
    ]
