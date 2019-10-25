from django.test import TestCase

from projects.models import Project, Technology


class TechnologyTests(TestCase):
    def setUp(self):
        Technology.objects.create(
            name="test technology",
            description="This is a test description.")

    def test_technology_name(self):
        tech = Technology.objects.get(id=1)
        expected_tech_name = f'{tech.name}'
        self.assertEquals(expected_tech_name, 'test technology')