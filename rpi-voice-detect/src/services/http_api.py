from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/detect', methods=['POST'])
def detect_voice():
    audio_data = request.files.get('audio')
    if not audio_data:
        return jsonify({'error': 'No audio data provided'}), 400
    
    # Here you would process the audio data and run detection
    # For now, we will just return a placeholder response
    result = {
        'detected': True,
        'confidence': 0.95,
        'message': 'Voice detected successfully'
    }
    
    return jsonify(result), 200

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'running'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)