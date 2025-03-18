from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            middle_name='Developer',
            last_name='SkyPro',
            position='admin',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
