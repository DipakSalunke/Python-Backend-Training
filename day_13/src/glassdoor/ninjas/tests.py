from django.test import TestCase
from django.urls import reverse
from .models import Developer, Skill
from .views import level
# Create your tests here.
class IndexListTests(TestCase):
    def test_get_devs_success(self):
        response = self.client.get(reverse('ninjas:index'))
        self.assertEqual(response.status_code, 200)

class DetailsListTests(TestCase):
    def test_get_dev_success(self):
        dev = Developer(name='Joe', experience=5, country='IND')
        dev.save()
        response = self.client.get(reverse('ninjas:details',args=(dev.id,)))
        self.assertEqual(response.status_code, 200)

class DevelopersListTests(TestCase):
    def test_get_ninja_success(self):

        response = self.client.get(reverse('ninjas:developers',kwargs=({"skill":"python"})))
        self.assertEqual(response.status_code, 200)

class SkillModelTests(TestCase):

    def test_create_skill(self):
        dev = Developer(name='Dipak', experience=5.6, country='Japan')
        dev.save()
        skill = dev.skill_set.create(name='java', level=3)
        assert skill.name == 'java'

    def test_skill_of_dev(self):
        dev = Developer(name='Dipak', experience=2.4, country='India')
        dev.save()
        dev.skill_set.create(name='java', level=1)
        dev.skill_set.create(name='python', level=1)
        dev_skill_list = dev.skill_set.all()
        assert len(dev_skill_list) == 2

    def test_level_up(self):
        dev = Developer(name='Dipak', experience=5.4, country='India')
        dev.save()
        dev.skill_set.create(name='java', level=1)
        dev.skill_set.create(name='python', level=3)
        select = dev.skill_set.get(pk=2)
        select.level += 1
        select.save()
        skill = dev.skill_set.all() 
        assert skill[1].level == 4
        
  