# Generated by Django 3.1.8 on 2024-01-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_alter_prodcutdb_proprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdb',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prodcutdb',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]