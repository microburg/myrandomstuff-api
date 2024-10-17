from flask import Flask
from routes.myrandomstuff_routes import myrandomstuff_bp
from middleware.example_middleware import log_request_middleware

app = Flask(__name__)

# Register middleware
log_request_middleware(app)

# Register blueprint for routes
app.register_blueprint(myrandomstuff_bp)

if __name__ == '__main__':
    app.run(debug=True)
