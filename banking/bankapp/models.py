from django.db import models


# Create your models here.
class Banking(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    mobile = models.IntegerField()
    address = models.TextField()
    district = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    service_required = models.CharField(max_length=250)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
