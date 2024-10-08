# import logging
#
# from datetime import timedelta
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.triggers.cron import CronTrigger
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.core.management.base import BaseCommand
# from django.template.loader import render_to_string
# from django.utils import timezone
# from django_apscheduler import util
# from django_apscheduler.jobstores import DjangoJobStore
# from django_apscheduler.models import DjangoJobExecution
#
# from news.models import Post, Subscription
#
# logger = logging.getLogger(__name__)
#
#
# def weekly_newsletter():
#     last_week = timezone.now() - timedelta(days=7)
#     posts = Post.objects.filter(time_in__gte=last_week)
#     categories = set(posts.values_list('category__id', flat=True))
#     subscribers = set(Subscription.objects.filter(category__id__in=categories).values_list('user__email', flat=True))
#
#     html_content = render_to_string(
#         'weekly_posts.html',
#         {
#             'link': f'http://127.0.0.1:8000/',
#             'posts': posts
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject='Посты за неделю',
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
#
# @util.close_old_connections
# def delete_old_job_executions(max_age=604_800):
#     """
#     This job deletes APScheduler job execution entries older than `max_age`
#     from the database.
#     It helps to prevent the database from filling up with old historical
#     records that are no longer useful.
#
#     :param max_age: The maximum length of time to retain historical
#                     job execution records. Defaults to 7 days.
#     """
#     DjangoJobExecution.objects.delete_old_job_executions(max_age)
#
#
# class Command(BaseCommand):
#     help = "Runs APScheduler."
#
#     def handle(self, *args, **options):
#         scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
#         scheduler.add_jobstore(DjangoJobStore(), "default")
#
#         scheduler.add_job(
#             weekly_newsletter,
#             trigger=CronTrigger(
#                 # second="*/3",
#                 day_of_week="fri",
#                 hour="18",
#                 minute="00"
#             ),  # Every Friday in 18:00
#             id="weekly_newsletter",  # The `id` assigned to each job MUST be unique
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info("Added job 'weekly_newsletter'.")
#
#         scheduler.add_job(
#             delete_old_job_executions,
#             trigger=CronTrigger(
#                 day_of_week="fri", hour="18", minute="00"
#             ),
#             id="delete_old_job_executions",
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info("Added weekly job: 'delete_old_job_executions'.")
#
#         try:
#             logger.info("Starting scheduler...")
#             scheduler.start()
#         except KeyboardInterrupt:
#             logger.info("Stopping scheduler...")
#             scheduler.shutdown()
#             logger.info("Scheduler shut down successfully!")
