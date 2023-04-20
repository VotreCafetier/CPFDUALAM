# Generated by Django 3.2.4 on 2021-08-13 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('product_stock', models.IntegerField(blank=True, null=True)),
                ('product_model', models.CharField(blank=True, max_length=255, null=True)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('product_year_guaranteed', models.SmallIntegerField(blank=True, null=True)),
                ('product_tech_sheet_url', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.color')),
            ],
        ),
    ]
