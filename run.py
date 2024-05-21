from flask import Flask
from add_app import addition_bp

def create_app():
    app = Flask(__name__)

    #blueprints
    app.register_blueprint(addition_bp)
    

    return app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)
    