from flask import Flask, request, jsonify
import base64
import numpy as np
import cv2

app = Flask(__name__)

# Dummy function to compare signatures
def compare_signatures(image_bytes):
    # Convert image bytes to NumPy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    
    # Dummy logic (Replace with actual model)
    return True if np.mean(img) > 100 else False

@app.route('/verify_signature', methods=['POST'])
def verify_signature():
    try:
        data = request.json
        encoded_image = data.get('signature')
        
        if not encoded_image:
            return jsonify({"error": "No signature data"}), 400

        # Decode Base64 image
        image_bytes = base64.b64decode(encoded_image)

        # Compare signatures
        is_match = compare_signatures(image_bytes)

        return jsonify({"match": is_match})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
