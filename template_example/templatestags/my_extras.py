from django import template

register = template.Library()

def cut (value, arg):
    """
    This cuts out all instances of "arg" from the string "value".
    """
    return value.replace(arg, '')


register.filter('cut', cut)