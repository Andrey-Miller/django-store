from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            self.stdout.write(str(user))