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
    # models.CharField are called field types if you want to google others
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # Many to Many, note Toy must be defined before we reference it
    countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        # self.id refers to the cat you just created
        # this redirects the user after they created something
        # or updated the cat.
        return reverse('detail', kwargs={'wine_id': self.id})

DAYS = (
        ('M', "Monday"),
        ('Tu', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
)


class Drinking(models.Model):
    # first argument is optional and it overrides the label tag
    # in the form variable
    date = models.DateField('Drank Date')
    review = models.CharField(
        max_length=2,
        choices=DAYS,  # generate  a select in our form
        # set the default value to 'B'
        default=DAYS[0][0]
    )
    # create a cat_id FK (note the _id is automatically added)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_day_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
