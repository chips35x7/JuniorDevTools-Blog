from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from environs import Env

env = Env()
env.read_env()


class Command(BaseCommand):
    help = "Creates a default superuser using environment variables"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = env.str("DJANGO_SUPERUSER_USERNAME")
        email = env.str("DJANGO_SUPERUSER_EMAIL")
        password = env.str("DJANGO_SUPERUSER_PASSWORD")

        if not (username and email and password):
            self.stderr.write("Missing one or more environment variables: DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD")
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created."))
        else:
            self.stdout.write(f"Superuser '{username}' already exists.")
