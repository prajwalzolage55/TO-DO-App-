from app import create_app, db
from app.models import Task
import os

app=create_app()

# Ensure instance directory exists
os.makedirs('instance', exist_ok=True)

with app.app_context():
    db.create_all()
    print("Database initialized!")

if __name__=='__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(host=host, port=port, debug=debug)
