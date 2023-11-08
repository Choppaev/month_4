# Generated by Django 4.2.4 on 2023-09-05 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя заказчика')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер тел:')),
            ],
            options={
                'verbose_name': 'заказчика',
                'verbose_name_plural': 'Заказчики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Добавьте фото продукта')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tag', models.CharField(max_length=100, verbose_name='Укажите хэштег')),
            ],
            options={
                'verbose_name': 'хэштег',
                'verbose_name_plural': 'Хэштеги',
            },
        ),
        migrations.CreateModel(
            name='StatusOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Ожидание', 'Ожидание'), ('Выехал', 'Выехал'), ('Доставлено', 'Доставлено')], max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloth.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloth.product')),
            ],
            options={
                'verbose_name': 'статус',
                'verbose_name_plural': 'Статус',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='cloth.tag'),
        ),
    ]
