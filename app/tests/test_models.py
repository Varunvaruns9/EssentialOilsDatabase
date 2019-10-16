from django.test import TestCase
from app.models import Plant, EssentialOil, Through


class TestDB(TestCase):
    @classmethod
    def setUpTestData(cls):
        plant1 = Plant.objects.create(name='Beewort')
        plant2 = Plant.objects.create(name='Gladdon')
        plant3 = Plant.objects.create(name='Celery')
        oil1 = EssentialOil.objects.create(name='Calamus Oil', abbr='COL', sname='Acorus calamus', family='Acoraceae')
        oil2 = EssentialOil.objects.create(name='Celeray Seed Oil', abbr='CSO', sname='Apium graveolens', family='Apiaceae')
        Through.objects.create(plant=plant1, oil=oil1)
        Through.objects.create(plant=plant2, oil=oil1)
        Through.objects.create(plant=plant3, oil=oil2)

    def test_plant_rep(self):
        plant = Plant.objects.get(id=1)
        self.assertEquals(plant.name, str(plant))

    def test_essentialoil_rep(self):
        oil = EssentialOil.objects.get(id=1)
        self.assertEquals(oil.name, str(oil))

    def test_through_rep(self):
        through = Through.objects.get(id=1)
        expected_name = "{} - {}".format(through.plant.name, through.oil.name)
        self.assertEquals(expected_name, str(through))
