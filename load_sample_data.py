# Optional helper to create a sample superuser and a sample post.
# Usage: Activate venv and run `python load_sample_data.py`
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog_project.settings')
import django
django.setup()
from django.contrib.auth.models import User
from blog.models import Post
u, created = User.objects.get_or_create(username='admin')
if created:
    u.set_password('adminpass')
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print('Created admin user with password "adminpass"')
else:
    print('Admin user exists (username=admin)')
if not Post.objects.exists():
    Post.objects.create(title='Welcome', slug='welcome', author=u, body='This is a sample post. Edit or delete it.', published=True)
    print('Created sample post.')
