from db import db

class usuarios (db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    telefone = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        return f"<{self.name}>"