from django.test import TestCase
from django.urls import reverse
from app.models import Metabolite, EssentialOil, Through


class TestIndexView(TestCase):
    """
    Class for testing that right views and templates are being loaded on the home page.
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

    def test_view_url_exists_at_desired_location(self):
        """
        Check if url is accessible.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Check if url is accessible with name.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Check if template is rendered properly.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestManualView(TestCase):
    """
    Class for testing that right views and templates are being loaded on the manual page.
    """
    def test_view_url_exists_at_desired_location(self):
        """
        Check if url is accessible.
        """
        response = self.client.get('/manual/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Check if url is accessible with name.
        """
        response = self.client.get(reverse('manual'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Check if template is rendered properly.
        """
        response = self.client.get(reverse('manual'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manual.html')
