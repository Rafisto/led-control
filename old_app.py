from flask import Flask, request, jsonify, render_template
from old_control import aliases
from old_control import Control

app = Flask(__name__, static_folder='static', template_folder='templates')
control = Control()

@app.route('/')
def home():
    return render_template('home.html',aliases={x: aliases[x].replace(';',',') for x in aliases})


@app.route('/control', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        query = data.get('query')

        if query is None:
            return jsonify({"error": "Missing 'query' key in JSON body."}), 400

        try:
            if query == "on":
                control.on()
            elif query == "off":
                control.off()
            else:
                control.set_color(query)
            return jsonify({"message": "Successfully set"}), 200
        except Exception as e:
            return jsonify({"error": "Internal server error."}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2137)

