from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Food

class FoodModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_food = Food.objects.create(
            author = test_user,
            name = 'Shawerma',
            body = 'Fast Food'
        )
        test_food.save()
        
    def test_food_content(self):
        food = Food.objects.get(id=1)
        self.assertEqual(str(food.author), 'tester')
        self.assertEqual(food.name, 'Shawerma')
        self.assertEqual(food.body, 'Fast Food')
        
class APITest(APITestCase):

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_food = Food.objects.create(
            author = test_user,
            name = 'Shawerma',
            body = 'Fast Food'
        )
        test_food.save()

        response = self.client.get(reverse('food_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'name': test_food.name,
            'body': test_food.body,
            'author': test_user.id,
        })


    # def test_create(self):
    #     test_user = get_user_model().objects.create_user(username='tester',password='pass')
    #     test_user.save()

    #     url = reverse('food_list')
    #     data = {
    #         "name":"Testing is Fun!!!",
    #         "body":"when the right tools are available",
    #         "author":test_user.id,
    #     }

    #     response = self.client.post(url, data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

    #     self.assertEqual(Food.objects.count(), 1)
    #     self.assertEqual(Food.objects.get().name, data['name'])

    # def test_update(self):
    #     test_user = get_user_model().objects.create_user(username='tester',password='pass')
    #     test_user.save()

    #     test_food = Food.objects.create(
    #         author = test_user,
    #         name = 'Shawerma',
    #         body = 'Fast Food'
    #     )
    #     test_food.save()

    #     url = reverse('food_detail',args=[test_food.id])
    #     data = {
    #         "name":"Testing is Still Fun!!!",
    #         "author":test_food.author.id,
    #         "body":test_food.body,
    #     }

    #     response = self.client.put(url, data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_200_OK, url)

    #     self.assertEqual(Food.objects.count(), test_food.id)
    #     self.assertEqual(Food.objects.get().name, data['name'])


    # def test_delete(self):
    #     """Test the api can delete a post."""

    #     test_user = get_user_model().objects.create_user(username='tester',password='pass')
    #     test_user.save()

    #     test_food = Food.objects.create(
    #         author = test_user,
    #         name = 'Shawerma',
    #         body = 'Fast Food'
    #     )
    #     test_food.save()

    #     test_food.save()

    #     post = Food.objects.get()

    #     url = reverse('food_detail', kwargs={'pk': post.id})


    #     response = self.client.delete(url)

    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)
