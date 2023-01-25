import json
import re

import requests


class Constants:

    def __init__(self):
        pass

    custom_icon = 'data:image/png;base64,' \
                  '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'
    base_url_svg = "https://img.shields.io/static/v1?"
