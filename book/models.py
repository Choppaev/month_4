from django.db import models


class BookProgrammlang(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
