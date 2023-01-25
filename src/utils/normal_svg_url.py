from urllib.parse import urlencode

from src.constants.constants import Constants
from src.utils.random_colors import random_color_gen


def get_normal_svg_url(message,
                       label, color, logo_width, style, label_color,
                       logo, logo_color) -> str:
    """
    Generate the URL for the SVG image of the view counter.

    :return: the SVG image URL
    """
    _random_color = random_color_gen()
    params = {
        "label": "" if label is None or label == "" else label,
        "message": message,
        "labelColor": _random_color if label_color is None else label_color,
        "color": _random_color if color is None else color,
        "logoWidth": 0 if logo_width is None or logo_width == "" else logo_width,
        "logo": "" if logo is None or logo == "" else logo,
        "logoColor": "white" if logo_color is None else logo_color,
        "style": "for-the-badge" if style is None else style
    }
    return Constants.base_url_svg + urlencode(params)
