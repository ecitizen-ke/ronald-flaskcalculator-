from flask import Flask
from add_app import addition_bp
from divide_app import divide_bp
from multiply_app import multiply_bp
from subtract_app import subtract_bp
def create_app():
    app = Flask(__name__)

    #blueprints
    app.register_blueprint(addition_bp)
    app.register_blueprint(divide_bp)
    app.register_blueprint(multiply_bp)
    app.register_blueprint(subtract_bp)
    

    return app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)
    