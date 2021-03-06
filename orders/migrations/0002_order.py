# Generated by Django 2.0.1 on 2018-01-27 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('delivery_date', models.DateField(blank=True)),
                ('payment_option', models.CharField(max_length=50)),
                ('order_status', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.Product')),
            ],
        ),
    ]
