# Generated by Django 4.2.4 on 2023-08-26 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='tvshow/')),
                ('country', models.CharField(max_length=100)),
                ('director', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('cycle', models.CharField(max_length=100)),
                ('starring', models.TextField()),
                ('description', models.TextField()),
                ('url_film', models.URLField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type_tvshow', models.CharField(choices=[('Боевик', 'Боевик'), ('Комедия', 'Комедия'), ('Мультфильмы', 'Мультфильмы'), ('Фантастические', 'Фантастические')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, null=True, verbose_name='Комментарий')),
                ('rate', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], null=True, verbose_name='Оценка')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('choice_film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tvshow.tvshow')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, null=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Stars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='tvshow.tvshow')),
            ],
        ),
    ]
