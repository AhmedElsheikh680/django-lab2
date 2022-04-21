from django.db import models

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Book(models.Model):

    name = models.CharField(max_length=200)
    publish_date =models.DateField()
    add_to_site_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    appropriate = models.CharField(max_length=200, choices=([('-18', 'Under 18'), ('18-25', '18-25'), ('+25', 'adults')]))
    image = models.ImageField(upload_to='books_list/uploads/covers')

    def __str__(self):
        return self.name