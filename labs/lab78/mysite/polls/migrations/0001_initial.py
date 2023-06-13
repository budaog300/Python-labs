# Generated by Django 3.2 on 2023-05-21 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.cashier')),
                ('date_time', models.DateTimeField()),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=999999)),                
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('check_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.check')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.item')),
            ],
        ),
        migrations.AddField(
            model_name='check',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.store'),
        ),
    ]
