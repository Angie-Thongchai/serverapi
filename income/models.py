from django.db import models
from authentication.models import User

class Income(models.Model):

    SOURCE_OPTION = [
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE-HUSTLE', 'SIDE-HUSTLE'),
        ('OTHERS', 'OTHERS'),
    ]

    source = models.CharField(choices=SOURCE_OPTION, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering : ['-updated_at']

    def __str__(self):
        return str(self.owner)+'s income'
    


