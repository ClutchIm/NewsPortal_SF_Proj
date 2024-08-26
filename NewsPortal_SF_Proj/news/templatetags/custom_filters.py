from django import template
from news.resources import censor_list
from django.utils.translation import gettext as _


register = template.Library()


class CharFieldException(Exception):
    pass


@register.filter()
def length(value):
    string = _('Всего постов')
    return f'{string}: {len(value)}'


@register.filter()
def description_time_in(value):
    if value.genre == 'AR':
        genre = 'статьи'
    else:
        genre = 'новости'
    return f'Дата публикации {genre}: {value.time_in.strftime('%d %b %Y')}'


@register.filter()
def censor(value):
    for word in censor_list:
        value = value.replace(word[1:], '*' * len(word[1:]))
    return value


@register.filter()
def censoring(value):
    value = value.split(' ')
    result = ''

    for word in value:
        if len(word) > 2:
            word = word.replace(word[1:-1], '*' * len(word[1:-1]))
        result += word + ' '
    return result

@register.filter()
def trans(value):
    return _(value)



