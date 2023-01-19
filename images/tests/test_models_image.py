import pytest

from images.models import Image


@pytest.mark.models
def test_image_creation(image_handler):
    assert isinstance(image_handler, Image)
    assert image_handler.author.username == 'testuser'
    assert image_handler.url.url == '/media/images/test_file.jpg'
    assert image_handler.name == 'test_file.jpg'
    assert str(image_handler) == 'test_file.jpg'


@pytest.mark.models
def test_image_fields(image_handler):
    assert [*vars(image_handler)] == ['_state', 'id', 'author_id', 'name', 'url', 'created_at', 'updated_at']
