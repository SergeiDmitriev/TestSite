from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

MAX_UPLOAD_PHOTO_WIDTH_CART = 600
MAX_UPLOAD_PHOTO_HEIGHT_CART = 600


def image_resolution_check_cart(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width != MAX_UPLOAD_PHOTO_WIDTH_CART or image_height != MAX_UPLOAD_PHOTO_HEIGHT_CART:
        raise ValidationError(
            f'Размер изображения должен быть не более '
            f'{MAX_UPLOAD_PHOTO_WIDTH_CART}'
            f'x'
            f'{MAX_UPLOAD_PHOTO_HEIGHT_CART}'
        )