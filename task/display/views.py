from django.shortcuts import render
from django.contrib.auth.models import User, Group


def user_views(request):
    users_data = User.objects.all()
    context = {
        'users': []
    }

    for user in users_data:
        groups = user.groups.all()
        groups_list = list(groups.values_list('name', flat=True))
        user_data = {
            'id': user.pk,
            'username': user.username,
            'groups': ', '.join(groups_list),
            'date_joined': user.date_joined
        }
        context['users'].append(user_data)

    print('context users: ', context)
    return render(request, "display/users.html", context)


def add_user_views(request):
    return render(request, 'display/add_user.html')


def group_views(request):
    groups_data = Group.objects.all()
    context = {
        'groups': []
    }
    for group in groups_data:
        group_data = {
            'id': group.pk,
            'name': group.name,
            'description': group.group_description,
        }

        context['groups'].append(group_data)
        print(context)
    return render(request, 'display/groups.html', context)


def add_group_views(request):
    return render(request, 'display/add_group.html')
