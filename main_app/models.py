from django.db import models
from django.urls import reverse

class Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('countries_detail', kwargs={'pk': self.id})

class Wine(models.Model):

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'wine_id': self.id})

SWEETNESS = (
        ('B', "Bitter"),
        ('D', 'Dry'),
        ('S', 'Sweet'),
        ('VS', 'Very Sweet')
)

class Drinking(models.Model):
    date = models.DateField('Date Drank')
    sweetness = models.CharField(
        max_length=2,
        choices=SWEETNESS,
        default=SWEETNESS[0][0]
    )
    review = models.CharField(max_length=250)

    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_day_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
