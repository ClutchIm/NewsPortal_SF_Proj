from django import template

register = template.Library()


@register.filter()
def length(value):
    return f'Всего постов: {len(value)}'


@register.filter()
def description_time_in(value):
    if value.genre == 'AR':
        genre = 'статьи'
    else:
        genre = 'новости'
    return f'Дата публикации {genre}: {value.time_in.strftime('%d %b %Y')}'

