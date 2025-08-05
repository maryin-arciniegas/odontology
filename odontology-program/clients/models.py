import uuid
from datetime import date

from django.db import models
# from treatments.models import Treatment


class Clients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    cellphone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    balance = models.FloatField(default=0.00)
    is_active = models.BooleanField(default=True)

    def calculate_age(self):
        today = date.today()
        return today.year - self.birthday.year - (
                (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )

    def __str__(self):
        return f"Paciente: {self.name}, Cédula: {self.cedula}, Edad: {self.calculate_age()}, Teléfono: {self.cellphone}, Dirección: {self.address}, Saldo: {self.balance}"


# class ClientControl(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     client = models.ForeignKey(Clients, on_delete=models.CASCADE)
#     treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Cliente: {self.client.name}, Tratamiento: {self.treatment.name}"