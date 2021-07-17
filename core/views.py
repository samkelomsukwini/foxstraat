from django.contrib import messages
from django.shortcuts import redirect, render

from utils.helpers import object_id_generator, ref_from_url
from core.models import Feedback, News


def add_feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        if not len(feedback) <= 0 and not feedback == None:
            object_id = object_id_generator(11, Feedback)
            Feedback.objects.create(object_id=object_id, body=feedback)

            messages.success(request, 'Thank you for the feedback. We will review it soon')
            return redirect('about')

        else:
            messages.error(request, 'Something went wrong. We couldn\'t send your feedback')
            return redirect('about')

def index(request):
    ref_from_url(request)
    if request.user.is_authenticated:
        return redirect('accounts:user-dashboard')
    else:
        return render(request, 'views/index.html')

def news(request):
    news_ = News.objects.all().order_by('-datetime_created')
    context = {
        'news': news_
    }
    return render(request, 'views/blog/news.html', context)

def about(request):
    add_feedback(request)
    return render(request, 'views/index.html')
