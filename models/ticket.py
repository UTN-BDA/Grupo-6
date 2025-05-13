from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Ticket(db.Model):
    __tablename__ = 'tickets'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie: str = db.Column(db.String(80), nullable=False)
    price: int = db.Column(db.Integer, nullable=False)
    date: str = db.Column(db.String(80), nullable=False)
    hour: int = db.Column(db.Integer, nullable=False)
    
    # Relación de N a 1 con feature
    feature_id = db.Column('feature_id', db.Integer, db.ForeignKey('features.id'))
    feature = db.relationship("Feature", back_populates='ticket')

    def __init__ (self, movie: str = None, price: int = None, date: str = None, hour: int = None, feature_id = None):
        self.movie = movie
        self.price = price
        self.date = date
        self.hour = hour
        self.feature_id = feature_id 