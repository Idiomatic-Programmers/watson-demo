from watson import search
from django.utils.html import strip_tags


class PostAdapter(search.SearchAdapter):
    def get_title(self, obj):
        return obj.title
    

    def get_description(self, obj):
        return strip_tags(obj.body)
