# app.py
from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    app.register_blueprint(bp, url_prefix='/api')
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 'Recurso no encontrado'
        }), 404
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)