# Generated by Django 5.0.2 on 2024-03-27 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Texture', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='kurta',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='users.color'),
        ),
        migrations.AlterField(
            model_name='kurta',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design', to='users.design'),
        ),
        migrations.AlterField(
            model_name='kurta',
            name='fabric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.fabric'),
        ),
    ]