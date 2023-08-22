from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.contrib.auth.models import User

# Create your views here.
class IndexView(ListView):
    model = Author
    template_name = 'index.html'
    context_object_name = 'author_list'
    # queryset = Author.objects.all()
    
    # This works like the queryset but more flexible, which is why this is preferred
    def get_queryset(self):
        return Author.objects.filter(name__icontains='an')
    
    # This works more with static objects that are not directly related to the model or queryset
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "pussy"
        context['counts'] = Author.objects.count()
        return context
