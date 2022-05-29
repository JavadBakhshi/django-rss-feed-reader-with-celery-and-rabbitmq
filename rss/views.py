from django.shortcuts import render
from .models import News
from rest_framework import viewsets
from .serializers import NewsSerializer


# Create your views here.


def home(request):
    all_data = News.objects.all()
    context = {
        'all_data': all_data,
    }

    return render(request, 'rss/home.html', context)


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

