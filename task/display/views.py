from django.shortcuts import redirect, render
from .models import User, Group


def user_views(request):
    users = User.objects.all()
    return render(request, "display/users.html", {'users': users})


def add_user_views(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }

    group = Group.objects.first()

    if group is None:
        context['errors'] = 'First you have to create a group'
        return render(request, 'display/add_user.html', context)

    if request.method == 'POST':

        username = request.POST['username']
        group = request.POST['group']
        try:
            user = User.objects.get(username=username)
            context['errors'] = 'A user with this name already exists'
        except User.DoesNotExist:
            user = User.objects.create(username=username, group=Group.objects.get(id=group))
            user.save()

            return redirect('display:users')
    return render(request, 'display/add_user.html', context)


def user_edit_views(request, user_id):
    user = User.objects.get(pk=user_id)
    groups = Group.objects.all()

    context = {
        'user': user,
        'groups': groups
    }

    if request.method == 'POST':
        username = request.POST['username']
        group = request.POST['group']

        user.username = username
        user.group = Group.objects.get(name=group)
        user.save()

        return redirect('display:users')

    return render(request, 'display/user_edit.html', context)


def user_delete_views(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()

    return redirect('display:users')


def group_views(request):
    groups_data = Group.objects.all()
    context = {
        'groups': []
    }
    for group in groups_data:
        group_data = {
            'id': group.pk,
            'name': group.name,
            'description': group.description,
        }

        context['groups'].append(group_data)
    return render(request, 'display/groups.html', context)


def add_group_views(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        if Group.objects.filter(name=name).exists():
            context = {
                'errors': 'A group with this name already exists.'
            }
            return render(request, 'display/add_group.html', context)

        group = Group.objects.create(name=name, description=description)
        group.save()

        return redirect('display:groups')

    return render(request, 'display/add_group.html')


def group_edit_views(request, group_id):
    group = Group.objects.get(pk=group_id)

    context = {
        'group': group,
    }

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        group.name = name
        group.description = description
        group.save()

        return redirect('display:groups')

    return render(request, 'display/group_edit.html', context)


def group_delete_views(request, group_id):
    group = Group.objects.get(pk=group_id)

    if not User.objects.filter(group=group).exists():
        group.delete()
        return redirect('display:groups')
    else:
        return redirect('display:groups')
