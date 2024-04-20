from flask import Blueprint, render_template, request, jsonify
from app.serial.led_controller import LedController
from app.api.color_converter import ColorConverter

api_blueprint = Blueprint('api', __name__)

try:
    controller = LedController('/dev/ttyACM0', 9600)
except ConnectionError as e:
    api_blueprint.logger.info(f"Unable to connect to the desired device: {e}")

@api_blueprint.route('/')
def home():
    return render_template('home.html')


@api_blueprint.route('/control', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        query = data.get('query')

        if query is None:
            return jsonify({"error": "Missing 'query' key in JSON body."}), 400

        try:
            if query == "on":
                controller.on()
            elif query == "off":
                controller.off()
            else:
                controller.set_color(ColorConverter.hex_to_rgb_str_semicolon(query))
            return jsonify({"message": "Successfully set"}), 200
        except Exception as e:
            return jsonify({"error": f"Internal server error. Message: {e}" }), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
