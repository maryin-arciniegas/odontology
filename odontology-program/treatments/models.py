from django.db import models
import uuid


class Treatment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # clients = models.ManyToManyField(clients.Clients , through='ClientControl')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"Tratamiento: {self.name}, Precio: {self.price}"

# Create your models here.
