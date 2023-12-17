from django.db import models


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        return self.annotate(counter_articles=models.Count('article')).order_by('-counter_articles', 'email')

