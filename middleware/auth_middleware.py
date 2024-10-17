from flask import request, jsonify

VALID_TOKEN = "guesswhat"

def auth_middleware(app):
    @app.before_request
    def authenticate():
        if request.endpoint not in ['myrandomstuff_bp.get_items', 'myrandomstuff_bp.get_item']:
            token = request.headers.get('Authorization')
            if not token or token != f"Bearer {VALID_TOKEN}":
                return jsonify({'error': 'Unauthorized'}), 401
