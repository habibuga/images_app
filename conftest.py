import os

from django.core.files.uploadedfile import SimpleUploadedFile

from config.settings import BASE_DIR
from images.models import Image


@pytest.fixture
def user(db, django_user_model):
    return django_user_model.objects.create_user(
        username='testuser',
        password='testPass123'
    )


@pytest.fixture
def image_handler(db):
    image = Image.objects.create(
        author=user,
        url=SimpleUploadedFile('test_file', content=open(os.path.join('tests', 'test_image.jpg'), 'rb').read())
    )

    yield image
    os.remove(os.path.join(BASE_DIR, 'media', 'images', 'test_file.jpg'))
