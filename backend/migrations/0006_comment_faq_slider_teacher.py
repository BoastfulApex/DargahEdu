# Generated by Django 4.1.4 on 2022-12-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_cource_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_lat', models.TextField(blank=True, max_length=10000, null=True)),
                ('customer_kril', models.TextField(blank=True, max_length=10000, null=True)),
                ('comment_lat', models.TextField(blank=True, max_length=10000, null=True)),
                ('comment_kril', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_lat', models.TextField(blank=True, max_length=10000, null=True)),
                ('question_kril', models.TextField(blank=True, max_length=10000, null=True)),
                ('answer_lat', models.TextField(blank=True, max_length=10000, null=True)),
                ('answer_kril', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lat', models.CharField(blank=True, max_length=500, null=True)),
                ('name_kril', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('video', models.FileField(null=True, upload_to='')),
                ('description_lat', models.TextField(blank=True, max_length=10000, null=True)),
                ('description_kril', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lat', models.CharField(blank=True, max_length=500, null=True)),
                ('name_kril', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description_lat', models.TextField(blank=True, max_length=10000, null=True)),
                ('description_kril', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]