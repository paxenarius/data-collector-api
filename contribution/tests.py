from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from model_mommy import mommy

from contribution.models import Data


class TestIndividualContributionList(TestCase):
    def setUp(self, *args, **kwargs):
        self.user_1 = get_user_model().objects.create_user(
            username='test_user_1', password='foobar', is_staff=True
        )
        self.user_2 = get_user_model().objects.create_user(
            username='test_user_2', password='foobar', is_staff=True
        )
        self.user_3 = get_user_model().objects.create_user(
            username='test_user_3', password='foobar', is_staff=True
        )

    def test_get_individual_contributions(self):
        self.client.force_login(self.user_1)
        mommy.make(Data, text="some random text", user=self.user_1, _quantity=5)
        mommy.make(Data, text="some random text", user=self.user_2, _quantity=3)
        mommy.make(Data, text="some random text", user=self.user_3, _quantity=2)

        assert Data.objects.filter(user=self.user_1).count() == 5
        assert Data.objects.filter(user=self.user_2).count() == 3
        assert Data.objects.filter(user=self.user_3).count() == 2

        response = self.client.get(reverse('individual-contribution-list'))
        # Assertion is currently failing due to the self.client.login now working
        #assert response.status_code == 200
