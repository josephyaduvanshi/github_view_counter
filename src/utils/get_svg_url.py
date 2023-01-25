from urllib.parse import urlencode

from src.constants.constants import Constants
from src.controller.view_controller import ViewsCounter
from src.helpers.validators.has_label_checker import has_label_check
from src.utils.random_colors import random_color_gen
from src.utils.short_number_converter import short_number


def get_svg_url(
        views_counter: ViewsCounter, message,
        label, color, logo_width, style, label_color,
        logo, has_label, logo_color, cache_buster) -> str:
    """
    Generate the URL for the SVG image of the view counter.

    :return: the SVG image URL
    """
    _random_color = random_color_gen()
    params = {
        "label": has_label_check(has_label, label),
        "message": short_number(views_counter.get_views()) if message is None or message == "" else message,
        "labelColor": _random_color if label_color is None else label_color,
        "color": _random_color if color is None else color,
        "logoWidth": 28 if logo_width is None else logo_width,
        "logo": Constants.custom_icon if logo is None else logo,
        "logoColor": "white" if logo_color is None else logo_color,
        "style": "for-the-badge" if style is None else style,
        "cacheSeconds": 0,
        "maxAge": 0,
        "cache_buster": cache_buster
    }
    return Constants.base_url_svg + urlencode(params)
