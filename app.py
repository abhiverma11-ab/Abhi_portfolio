import os
from flask import Flask, render_template
from config import Config
from database import db
from routes.main_routes import main_bp
from routes.admin_routes import admin_bp
from routes.api_routes import api_bp
from seed_data import seed_database
from portfolio_config import PERSONAL_INFO, sync_local_assets

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Global context processor for personal information
    @app.context_processor
    def inject_personal_info():
        return {
            'personal_info': PERSONAL_INFO,
            'current_year': 2026
        }

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(api_bp)

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    # Sync local PC assets
    sync_local_assets(os.path.abspath(os.path.dirname(__file__)))

    # Ensure tables exist and database is seeded
    with app.app_context():
        db.create_all()
        # Auto-seed if database is empty
        from models import Project
        if Project.query.count() == 0:
            seed_database()

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Abhi Verma Portfolio on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
