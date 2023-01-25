import requests
from flask import make_response, jsonify
from src.utils.normal_svg_url import get_normal_svg_url
from src.models.args_model import args_model_from_dict


def normal_card_gen(arguments: dict = None):
    """
    View function for root route management. Increase the number of views, generate the URL for the SVG picture,
    and return the SVG image in the response.

    :return: the SVG image of the view counter
    """
    arguments = args_model_from_dict(arguments)
    """
    {
  "label": "",
  "message": "",
  "labelColor":"",
  "backgroundColor": "",
  "logoSpacing": null,
  "logo": "",
  "style": "",
  "hasLabel": null
  }
    """

    # handle the error if the data file is not found
    if arguments.message is None or arguments.message == "":
        return jsonify({"error": {
            "Message": "The message is required",
            "Payload": "INVALID_MESSAGE",
            "code": 400,
        }}), 400
    response = make_response("")
    response.headers["Content-type"] = "image/svg+xml"
    try:
        response.data = requests.get(get_normal_svg_url(label_color=arguments.label_color,
                                                        color=arguments.background_color,
                                                        logo_width=arguments.logo_spacing,
                                                        style=arguments.style, logo=arguments.logo,
                                                        label=arguments.label if not None else "",
                                                        message=arguments.message,
                                                        logo_color=arguments.logo_color)).text
    except requests.exceptions.RequestException as e:
        # handle the error if the request to the SVG image URL fails
        return str(e), 500
    return response
