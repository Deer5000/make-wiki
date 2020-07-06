from django.contrib.auth.models import User
from django.test import TestCase

from wiki.models import Article


class ArticleListViewTests(TestCase):
    def test_multiple_articles(self):
        # Make some test data to be displayed on the article.
        user = User.objects.create()

        Article.objects.create(title="My Test Article", content="test", author=user)
        Article.objects.create(title="Another Test Article", content="test", author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of articles passed to the template
        # matches the number of articles we have in the database.
        response_articles = response.context['articles']
        self.assertEqual(len(response_articles), 2)

        # Check that the response HTML contains the text of the articles.
        self.assertContains(response, 'My Test Article')
        self.assertContains(response, 'Another Test Article')


class ArticleDetailViewTests(TestCase):
    def test_single_article(self):
        # TODO: Make some test data (one User and one Article)
        user = User.objects.create()

        Article.objects.create(title="Test Article 1", content="test", author=user)

        # TODO: Make a GET request for the detail page
        response = self.client.get('/w/test-article-1/')

        # TODO: Verify (using assertContains) that the article's title and contents
        # appear on the page
        self.assertContains(response, 'Test Article 1')