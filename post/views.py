from django.views.generic import ListView
from .models import Post



class ViewPosts(ListView):
    model = Post
    template_name = 'home.html'
    
    # def get_queryset(self):
    #     return Post.objects.order_by('id')


# Create your views here.
