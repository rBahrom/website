from django.db import models
from django.contrib.auth.models import User
from .helpers import SaveMedia

# Create your models here.

class Auther(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.first_name}  "
                f"{self.last_name}")

    def get_full_info(self):
        return (f"{self.first_name}  "
                f"{self.last_name}")

class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMedia.save_image_path, null=True)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    count = models.PositiveIntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.title}"
                f"{self.description}"
                f"{self.auther}"
                f"{self.price}"
                f"{self.count}")

class Commit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Books)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.user}"
                f"{self.text}"
                f"{self.book}")

# class City(models.Model):
#     pass
#
# class Country(models.Model):
#     pass
#
# class Address(models.Model):
#     pass
#
