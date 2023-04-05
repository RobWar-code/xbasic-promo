from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import FeaturePage


# Create your views here.
class Feature(View):
    def get(self, request, slug=None, *args, **kwargs):
        if slug is None:
            slug = "xbasic-intro"

        queryset = FeaturePage.objects.all()
        feature_page = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            'index.html',
            {
                'feature_page': feature_page
            }
        )
