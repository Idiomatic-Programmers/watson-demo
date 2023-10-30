from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from watson import search

from .models import Post
from .serializers import PostSerializer


def search_page(request):
    return render(request, "posts/search.html")


class SearchView(APIView):
    def get(self, request, format=None):
        q = self.request.query_params.get('q', "")
        if q == "":
            search_results = Post.objects.none()
        else:
            search_results = search.filter(Post, q)
        serializer = PostSerializer(search_results, many=True)
        return Response(serializer.data)
