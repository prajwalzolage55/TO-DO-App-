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
    app.run(debug=True)