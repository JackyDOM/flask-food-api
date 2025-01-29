from flask import Flask, jsonify
from flask_cors import CORS
from banner import get_banner_food


app = Flask(__name__)
CORS(app)

# Banner
@app.route('/api/banner', methods=['GET'])
def get_all_banners():  # Renamed function to avoid conflict
    return get_banner_food()


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=35174)
