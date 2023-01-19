import pytest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from config import settings
from images.validators import validate_file_type


def test_valid_images(image):
    assert not validate_file_type(image)


def test_not_valid_image_with_correct_extension():
    image = SimpleUploadedFile('test_image.jpg', content=b'test not valid type')

    with pytest.raises(ValidationError) as excinfo:
        validate_file_type(image)

    assert excinfo.value.args[0] == f'File type not supported. Use: *.{", *.".join(settings.IMAGES_TYPES)}.'
