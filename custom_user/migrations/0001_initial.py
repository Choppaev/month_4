# Generated by Django 4.2.4 on 2023-09-02 07:04

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('admin', 'admin'), ('super_admin', 'admin_admin'), ('client', 'client'), ('vipclient', 'vipclient'), ('admin', 'admin')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('phone_number', models.CharField(max_length=13)),
                ('maried', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=7)),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=7)),
                ('children', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=3)),
                ('age', models.PositiveIntegerField(default=18)),
                ('about_me', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('hobby', models.CharField(max_length=20)),
                ('favorite_food', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('height', models.IntegerField(max_length=3)),
                ('weight', models.IntegerField(max_length=3)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
