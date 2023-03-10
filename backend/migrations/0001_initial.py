# Generated by Django 4.1.4 on 2022-12-23 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('lang', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField(default=0)),
                ('description_uz', models.TextField(blank=True, max_length=10000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=10000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('lang', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('cource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.cource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]
