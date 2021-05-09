from django.core.management.base import BaseCommand
from PasswordManager.models import Post, Tag

class Command(BaseCommand):
    def handle(self, *args, **options):
        Tag.objects.all().delete()
        Post.objects.all().delete()