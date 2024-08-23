from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    category_list = 'Id/category:'
    for category in Category.objects.all():
        if category.id == 1:
            category_list += f' {str(category.id)}:{str(category.category)}'
        else:
            category_list += f', {str(category.id)}:{str(category.category)}'

    help = f'Delete all posts of selected category. | deleteposts [id category] | {category_list}'
    missing_args_message = 'Enter id of category. Command for list of category: deleteposts --help'

    def add_arguments(self, parser):
        parser.add_argument('category_id', nargs='+', type=int)

    def handle(self, *args, **options):
        id = options['category_id'][0]

        if len(options['category_id']) != 1:
            self.stdout.write(self.style.ERROR('Need only 1 arg'))
        elif id < 1 or id > Category.objects.values('id').order_by('-id').first()['id']:
            self.stdout.write(self.style.ERROR('Out of range'))
        else:
            self.stdout.write(
                f'Do you really would delete all post with category: '
                f'{Category.objects.filter(id=id).values('category')}? y/n'
            )
            answer = input()

            if answer == 'y':
                Post.objects.filter(category__id=id).delete()
                self.stdout.write(self.style.SUCCESS('Successfully wiped posts!'))
                return

            self.stdout.write(self.style.ERROR('Access denied'))




