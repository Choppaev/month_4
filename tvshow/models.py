from django.db import models


class TvShow(models.Model):
    TYPE_TVSHOW = (
        ('Боевик', 'Боевик'),
        ('Комедия', 'Комедия'),
        ('Мультфильмы', 'Мультфильмы'),
        ('Фантастические', 'Фантастические'),
    )
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tvshow/', null=True)
    country = models.CharField(max_length=100)
    director = models.TextField()
    genre = models.CharField(max_length=100)
    time = models.TimeField()
    cycle = models.CharField(max_length=100)
    starring = models.TextField()
    description = models.TextField()
    url_film = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type_tvshow = models.CharField(max_length=100, choices=TYPE_TVSHOW)

    def __str__(self):
        return self.title


class Rating(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    Stars = models.ForeignKey(TvShow, on_delete=models.CASCADE,
                              related_name='comment_object')
    Text = models.CharField(max_length=100, choices=RATING, null=True)
    Created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Text


class Reviews(models.Model):
    stars = ((i, '*' * i) for i in range(1, 6))
    comment = models.CharField('Комментарий', max_length=500, null=True)
    choice_film = models.ForeignKey(TvShow, on_delete=models.CASCADE, related_name='reviews', null=True)
    rate = models.IntegerField('Оценка', choices=stars, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment
