from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from io import BytesIO
import qrcode
import hashlib
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# --- Simple Blockchain Implementation ---
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": str(self.timestamp),
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

blockchain = Blockchain()

# --- QR Code generation ---
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    import base64
    return base64.b64encode(img_io.getvalue()).decode('utf-8')

# --- Routes ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', blockchain_chain=blockchain.chain)

# Add a new record
@app.route('/add_record', methods=['POST'])
def add_record():
    species = request.form.get("species")
    collector_id = request.form.get("collector_id")
    location = request.form.get("location")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    timestamp = request.form.get("timestamp")

    if not all([species, collector_id, location, latitude, longitude, timestamp]):
        flash("Please fill in all fields.", "error")
        return redirect(url_for('index'))

    record_data = {
        'species': species,
        'collector_id': collector_id,
        'location': location,
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    }

    new_block = Block(
        index=len(blockchain.chain),
        timestamp=datetime.now(),
        data=record_data,
        previous_hash=blockchain.get_latest_block().hash
    )
    blockchain.add_block(new_block)

    flash("Record added successfully!", "success")
    return redirect(url_for('index'))

# QR code API
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    json_data = request.get_json()
    if not json_data or "data" not in json_data:
        return jsonify({"error": "Missing data"}), 400

    try:
        base64_img = generate_qr_code(json_data["data"])
        return jsonify({'image_data': base64_img})
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return jsonify({"error": "Failed to generate QR code"}), 500

# Nominatim geocoding API
@app.route('/geocode', methods=['POST'])
def geocode():
    import requests
    data = request.get_json()
    location = data.get("location")
    if not location:
        return jsonify({"error": "Missing location"}), 400

    # Nominatim forward geocoding
    response = requests.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": location, "format": "json", "limit": 1},
        headers={"User-Agent": "Flask-App"}
    )
    if response.status_code != 200 or not response.json():
        return jsonify({"error": "Could not geocode location"}), 400

    result = response.json()[0]
    return jsonify({"lat": result["lat"], "lng": result["lon"]})

if __name__ == '__main__':
    app.run(debug=True)
