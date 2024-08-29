from datetime import timedelta

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from NewsPortal import settings
from .models import Post, Subscription


@shared_task
def every_monday_8am():
    last_week = timezone.now() - timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('category__id', flat=True))
    subscribers = set(Subscription.objects.filter(category__id__in=categories).values_list('user__email', flat=True))

    html_content = render_to_string(
        'weekly_posts.html',
        {
            'link': f'http://127.0.0.1:8000/',
            'posts': posts
        }
    )

    msg = EmailMultiAlternatives(
        subject='Посты за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def notify_about_new_post(pk):
    post = Post.objects.get(id=pk)
    categories = post.category.all()

    emails = User.objects.filter(
        subscriptions__category__in=categories
    ).values_list('email', flat=True)

    subject = f'Новый пост в категории {categories}'

    text_content = (
        f'{post.title}\n'
        f'{post.main_text}\n\n'
        f'Ссылка на пост: http://127.0.0.1:8000{post.get_absolute_url()}'
    )
    html_content = (
        f'{post.title}<br>'
        f'{post.main_text}'
        f'<a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )

    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
