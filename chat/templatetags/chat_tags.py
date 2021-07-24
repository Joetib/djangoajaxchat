from django import template

register = template.Library()

@register.filter(name="getunreadmessages")
def my_tag(other_user, current_user):
    return current_user.count_all_unread_messages(other_user)