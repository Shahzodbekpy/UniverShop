# Generated by Django 4.1.7 on 2023-04-29 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='name',
            field=models.CharField(choices=[('Telefon', 'telefon'), ('Soat', 'soat'), ('Notebook', 'notebook'), ('Oyoq kiyim', 'oyoq kiyim'), ('Erkaklar kiyimi', 'erkaklar kiyimi'), ('Ayollar kiyimi', 'ayollar kiyimi'), ('Bolalar uchun', 'bolalar uchun'), ('Oshxona uchun', 'oshxona uchun'), ('Qurilish uchun', 'qurilish'), ('Parfumeriya', 'parfumeriya'), ('Musiqa', 'musiqa uchun'), ('Avto jihozlar', 'avto')], max_length=200),
        ),
    ]