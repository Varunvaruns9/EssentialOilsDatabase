from django.test import TestCase
from app.models import Metabolite, EssentialOil, Through


class TestDB(TestCase):
    """
    Class for testing if the database is being created properly and values can be accessed.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test database.
        """
        meta1 = Metabolite.objects.create(name='Pentacosane <n->')
        meta2 = Metabolite.objects.create(name='Maaliene <beta->')
        oil1 = EssentialOil.objects.create(name='Lavender Oil', abbr='LEV', scientific_name='Lavandula officinalis', family='Lamiaceae')
        oil2 = EssentialOil.objects.create(name='Juniper Twig Oil', abbr='JTO', scientific_name='Juniperus recurva', family='Cupressaceae')
        Through.objects.create(metabolite=meta1, oil=oil1, identity=72.2, mzratio=57.0, time=22.316, relative_abundance1=9.88036862,
                                relative_abundance2=10.79760986, relative_abundance3=9.625226588, relative_abundance4=9.914526978)
        Through.objects.create(metabolite=meta2, oil=oil1, identity=89.3, mzratio=189.0, time=14.321, relative_abundance1=0.027387527,
                                relative_abundance2=0.027628735, relative_abundance3=0.027549428, relative_abundance4=0.027742598)

    def test_metabolite_rep(self):
        """
        Check values are being stored properly in Metabolite.
        """
        meta = Metabolite.objects.get(name='Pentacosane <n->')
        self.assertEquals(meta.name, str(meta))

    def test_essentialoil_rep(self):
        """
        Check values are being stored properly in EssentialOil.
        """
        oil = EssentialOil.objects.get(name='Lavender Oil')
        self.assertEquals(oil.name, str(oil))

    def test_through_rep(self):
        """
        Check values are being stored properly in Through.
        """
        through = Through.objects.get(id=1)
        expected_name = "{} - {}".format(through.oil.name, through.metabolite.name)
        self.assertEquals(expected_name, str(through))
