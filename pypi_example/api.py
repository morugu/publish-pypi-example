from .extention import (
    get_next_age
)


def get_message(name):
    return 'Hello {name}!'.format(name=name)


def get_next_age_message(name, age):
    next_age = get_next_age(age)
    return '{name}! your next age is {next_age}'.format(name=name, next_age=next_age)
