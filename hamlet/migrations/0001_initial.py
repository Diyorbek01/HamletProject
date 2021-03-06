# Generated by Django 3.1.5 on 2021-02-03 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),

        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamlet.region')),
            ],
        ),
        migrations.CreateModel(
            name='Announcment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('features', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='pictures')),
                ('author', models.CharField(max_length=25)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamlet.district')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamlet.region')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hamlet.status')),
            ],
        ),
    ]
