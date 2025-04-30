from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .forms import FeedBack

from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, '<p class="lead">Your journey to becoming a pro starts here!</p>')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hello There!')

    def test_homepage_url_resolves_homepage(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    
class AboutPageTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = 'testuser',
            email ='testuser@gmail.com',
            password = 'testpass1234',
        )
        cls.feedback = FeedBack.objects.create(
            user = cls.user,
            message = 'I love the feedback system!'
        )
    
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'pages/about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About')
    
    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'I\'m not on the page.I shouldn\'t be here.')

    def test_aboutpage_url_resolves_aboutpage(self):
        view = resolve('/about')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)

    def test_feedback_form(self):
        self.assertEqual(self.feedback.user, self.user)
        self.assertEqual(self.feedback.message, 'I love the feedback system!')
        self.assertTemplateUsed('pages/about.html')
        