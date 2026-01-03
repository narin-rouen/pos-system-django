from django.core.management.base import BaseCommand
from core.models import User


class Command(BaseCommand):
    help = 'Create initial admin user'

    def handle(self, *args, **options):
        if not User.objects.filter(u_name='admin').exists():
            User.objects.create_superuser(
                u_name='admin',
                email='admin@pos.com',
                password='admin123',
                f_name='Admin',
                l_name='User'
            )
            self.stdout.write(self.style.SUCCESS('✓ Admin user created successfully!'))
            self.stdout.write(self.style.SUCCESS('  Username: admin'))
            self.stdout.write(self.style.SUCCESS('  Password: admin123'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists!'))
