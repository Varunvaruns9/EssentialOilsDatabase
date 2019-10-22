from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Metabolite(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class EssentialOil(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=10)
    scientific_name = models.CharField(max_length=200)
    family = models.CharField(max_length=100)
    graph = models.ImageField(null=True, blank=True)
    metabolites = models.ManyToManyField(Metabolite, through='Through')

    def __str__(self):
        return self.name


class Through(models.Model):
    metabolite = models.ForeignKey(Metabolite, on_delete=models.CASCADE)
    oil = models.ForeignKey(EssentialOil, on_delete=models.CASCADE)
    identity = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100), ])
    mzratio = models.FloatField()
    time = models.FloatField(validators=[MinValueValidator(0), ])
    relative_abundance1 = models.FloatField()
    relative_abundance2 = models.FloatField()
    relative_abundance3 = models.FloatField()
    relative_abundance4 = models.FloatField()

    def __str__(self):
        return self.oil.name + ' - ' + self.metabolite.name
