import os
import django
from django.db import models
from django.db.models import Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):

    if search_name is not None and search_email is not None:
        authors = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email)
    elif search_name is not None:
        authors = Author.objects.filter(full_name__icontains=search_name)
    elif search_email is not None:
        authors = Author.objects.filter(email__icontains=search_email)
    else:
        return ""

    if not authors.exists():
        return ""

    result = []
    for author in authors.order_by('-full_name'):
        status = "Banned" if author.is_banned else "Not Banned"
        result.append(f"Author: {author.full_name}, email: {author.email}, status: {status}")

    return '\n'.join(result)


def get_top_publisher():
    our_authors = Author.objects.annotate(total_articles=models.Count('article', distinct=True)).order_by('-total_articles', 'email')

    if not our_authors.exists() or our_authors.first().total_articles == 0:
        return ""

    top_author = our_authors.first()
    number_articles = top_author.total_articles

    return f"Top Author: {top_author.full_name} with {number_articles} published articles."


def get_top_reviewer():
    authors = Author.objects.annotate(total_reviews=models.Count('review', distinct=True)).order_by('-total_reviews', 'email')

    if not authors.exists() or authors.first().total_reviews == 0:
        return ""

    top_author = authors.first()
    number_reviews = top_author.total_reviews

    return f"Top Reviewer: {top_author.full_name} with {number_reviews} published reviews."


def get_latest_article():
    article = Article.objects.order_by('-published_on').first()

    if not article:
        return ""

    authors = article.authors.all()
    list_authors = ', '.join(sorted([author.full_name for author in authors]))
    reviews_count = Review.objects.filter(article=article).count()
    average_reviews_rating = Review.objects.filter(article=article).aggregate(avg_rating=models.Avg('rating'))['avg_rating']

    if average_reviews_rating is not None:
        average_reviews_rating = "{:.2f}".format(average_reviews_rating.avg_rating)

    return f"The latest article is: {article.title}. Authors: {list_authors}. Reviewed: {reviews_count} times. Average Rating: {average_reviews_rating}."


def get_top_rated_article():
    top_article = Article.objects.annotate(avg_rating=models.Avg('review__rating')).order_by('-avg_rating', 'title').first()

    if not top_article or top_article.avg_rating is None:
        return ""

    num_reviews = Review.objects.filter(article=top_article).count()
    avg_rating = "{:.2f}".format(top_article.avg_rating)

    return f"The top-rated article is: {top_article.title}, with an average rating of {avg_rating}, reviewed {num_reviews} times."


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = Author.objects.filter(email=email).first()

    if not author:
        return "No authors banned."

    num_reviews = Review.objects.filter(author=author).count()
    author.is_banned = True
    author.save()
    Review.objects.filter(author=author).delete()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."