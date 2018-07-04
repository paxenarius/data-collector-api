from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from model_mommy import mommy

from contribution.models import Data


class TestIndividualContributionList(TestCase):
    def setUp(self, *args, **kwargs):
        self.user_1 = mommy.make(get_user_model(), username='test_user_1')
        self.user_1.set_password('foobar')
        self.user_1.save()

        self.user_2 = mommy.make(get_user_model(), username='test_user_2', password='foobar')
        self.user_2.set_password('foobar')
        self.user_2.save()

        self.user_3 = mommy.make(get_user_model(), username='test_user_3', password='foobar')
        self.user_3.set_password('foobar')
        self.user_3.save()

    def test_get_individual_contributions(self):
        self.client.login(username='test_user_1', password='foobar')
        mommy.make(Data, text="some random text", user=self.user_1, _quantity=5)
        mommy.make(Data, text="some random text", user=self.user_2, _quantity=3)
        mommy.make(Data, text="some random text", user=self.user_3, _quantity=2)

        assert Data.objects.filter(user=self.user_1).count() == 5
        assert Data.objects.filter(user=self.user_2).count() == 3
        assert Data.objects.filter(user=self.user_3).count() == 2

        response = self.client.get(reverse('individual-contribution-list'))
        assert response.status_code == 200
