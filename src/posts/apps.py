from django.apps import AppConfig
from watson import search
from posts.search import PostAdapter

class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    def ready(self):
        post = self.get_model("Post")
        category = self.get_model("Category")
        author = self.get_model("Author")
        search.register(post, fields=["category__name", "author__name", "title", "body"], store=["category__name", "body"])
        search.register(author)
        search.register(category)
