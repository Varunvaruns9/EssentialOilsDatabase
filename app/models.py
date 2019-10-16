from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=200)


class EssentialOil(models.Model):
    name = models.CharField(max_length=200)


class Through(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    oil = models.ForeignKey(EssentialOil, on_delete=models.CASCADE)
