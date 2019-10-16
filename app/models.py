from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class EssentialOil(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=10)
    sname = models.CharField(max_length=200)
    family = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Through(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    oil = models.ForeignKey(EssentialOil, on_delete=models.CASCADE)

    def __str__(self):
        return self.plant.name + ' - ' + self.oil.name
