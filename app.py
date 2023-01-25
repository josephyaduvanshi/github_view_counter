import json

from flask import Flask, request, jsonify

from src.helpers.normal_card import normal_card_gen
from src.helpers.view_counter import view_url

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# app.config['CACHE_TYPE'] = 'null'


@app.route("/", methods=["GET"])
def index():
    return "Hello World!, UI is under development"


@app.route("/views-counts", methods=["GET"])
def views():
    """
    View function for root route management. Increase the number of views, generate the URL for the SVG picture,
    and return the SVG image in the response.

    :return: the SVG image of the view counter
The arguments are: label, message, labelColor, backgroundColor, logoSpacing, logo, style, hasLabel
In JSOn FORMAt:  {"label":"","message":"","labelColor":"","backgroundColor":"", logoSpacing":null,"logo":"","style":"", "hasLabel":null}
    """
    arguments = jsonify(request.args).json
    return view_url(arguments)


@app.route("/generate-card", methods=["GET"])
def generate_card():
    arguments = jsonify(request.args).json
    return normal_card_gen(arguments=arguments)


@app.route("/admin/view-all-users", methods=["GET"])
def view_all_users():
    """
    Views all the users in the database.
    currently, it is a JSON file.
    it does not have any authentication because it is a not needed for now.
    :return:
    """
    with open("views.json", "r") as file:
        contents = json.loads(file.read())
        file.close()
    return jsonify(contents)


if __name__ == "__main__":
    app.run()
