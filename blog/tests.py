from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='munira',
            email='m@gmail.com',
            password='munira'
        )

        self.post=Post.objects.create(
            title='yangi mavzu',
            body='post matni',
            author=self.user
        )

    def test_string_representation(self):
        post=Post(title='post mavzusi')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'yangi mavzu')
        self.assertEqual(f'{self.post.author}', 'munira')
        self.assertEqual(f'{self.post.body}', 'post matni')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'post matni')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'yangi mavzu')
        self.assertTemplateUsed(response, 'post_detail.html')




