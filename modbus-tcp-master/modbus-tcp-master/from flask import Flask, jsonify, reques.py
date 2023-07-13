from flask import Flask, jsonify, request

app = Flask(__name__)

# Store the current tag value
tag_value = False

@app.route('/api/tag', methods=['GET'])
def get_tag_value():
    return jsonify({'tag_value': tag_value})

@app.route('/api/tag', methods=['POST'])
def set_tag_value():
    global tag_value
    new_value = request.json.get('tag_value')
    if isinstance(new_value, bool):
        tag_value = new_value
        return jsonify({'message': 'Tag value updated successfully'})
    else:
        return jsonify({'error': 'Invalid tag value'}), 400

if __name__ == '__main__':
    app.run()
