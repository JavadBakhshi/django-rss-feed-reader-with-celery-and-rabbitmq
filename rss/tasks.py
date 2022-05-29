from celery import shared_task
import feedparser

from .models import News


@shared_task
def receiving_information_from_rss():
    url = 'https://www.farsnews.ir/rss'
    feeder = feedparser.parse(url)

    for entry in feeder['entries']:
        News.objects.create(
            title=entry['title'],
            url=entry['link']

        )

