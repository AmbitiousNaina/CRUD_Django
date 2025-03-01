from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Increased max_length for flexibility
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title
