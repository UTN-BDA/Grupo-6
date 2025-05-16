from dataclasses import dataclass
from app import db
from app.models.relations import users_roles
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin
from datetime import datetime,timedelta
from sqlalchemy import Column, DateTime

@dataclass(init=False, repr=True, eq=True)
class Movie(SoftDeleteMixin, AuditMixin,db.Model):
    __tablename__ = 'movies'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    director: str = db.Column(db.String(80), nullable=False)
    year: int = db.Column(db.Integer, nullable=False)
    start_date: str = Column(DateTime, nullable=False, default=datetime.now())
    final_date: str = Column(DateTime, nullable=False, default=datetime.now()+timedelta(weeks=2))
    duration: int = db.Column(db.Integer, nullable=False)
    description: str = db.Column(db.String(200), nullable=False)
    genre: str = db.Column(db.String(80), nullable=False)
    classification: str = db.Column(db.String(80), nullable=False)
    cast: str = db.Column(db.String(80), nullable=False)
    language: str = db.Column(db.String(80), nullable=False)
    
    # Relación 1 a muchos con feature
    feature = db.relationship('Feature', back_populates='movie')
    
    def __init__(self, name: str = None, director: str = None, year: int = None, start_date: str = None, final_date: str = None, duration: int = None, description: str = None, genre: str = None, classification: str = None, cast: str = None, language: str = None):
        self.name = name
        self.director = director
        self.year = year
        self.start_date = start_date
        self.final_date = final_date
        self.duration = duration
        self.description = description
        self.genre = genre
        self.classification = classification
        self.cast = cast
        self.language = language
    