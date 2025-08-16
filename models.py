from flask_sqlalchemy import SQLAlchemy # pyright: ignore[reportMissingImports]

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)