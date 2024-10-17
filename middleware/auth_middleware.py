from flask import request, jsonify

def log_request_middleware(app):
    @app.before_request
    def log_request_info():
        print(f"Request method: {request.method}, URL: {request.url}")
