from django.contrib.auth.models import Group
from django.db import models


Group.add_to_class('group_description', models.TextField(max_length=250, null=True, blank=True))
