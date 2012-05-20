from django import template

register = template.Library()

@register.filter
def isup(value):
    if value == True:
        return "up"
    elif value == False:
        return "down"
    else:
        return "unknown"
