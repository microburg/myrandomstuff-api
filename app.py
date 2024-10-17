from flask import Flask
from routes.myrandomstuff_routes import myrandomstuff_bp
from middleware.auth_middleware import auth_middleware
from middleware.example_middleware import log_request_middleware

app = Flask(__name__)

# Register middleware
log_request_middleware(app)
auth_middleware(app)  # Add this line to enable authentication

# Register blueprint for routes
app.register_blueprint(myrandomstuff_bp)

if __name__ == '__main__':
    app.run(debug=True)
