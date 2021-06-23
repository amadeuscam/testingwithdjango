from django.test import TestCase
from .models import Post


# Create your tests here.


class ModelTesting(TestCase):

    def setUp(self) -> None:
        self.blog = Post.objects.create(
            title="como mejorar como persona",
            author="lucian cati",
            slug="better-person"
        )

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), "como mejorar como persona")
