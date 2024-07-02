from app.extension import db, ma

class Menu(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return f'<Menu {self.name}>'