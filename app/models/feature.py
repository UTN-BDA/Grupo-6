from dataclasses import dataclass
from datetime import datetime,timedelta

from app import db
from sqlalchemy import Column, DateTime
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin

@dataclass(init=False,repr=True, eq=True)
class Feature(SoftDeleteMixin, AuditMixin,db.Model):
    __tablename__ = 'features'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_from: str = Column(DateTime, nullable=False, default=datetime.now())
    date_to: str = Column(DateTime, nullable=False, default=datetime.now()+timedelta(weeks=2))

    # Relación muchos a 1 con movie
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), nullable=False)
    movie = db.relationship("Movie", back_populates='feature')

    # Relación muchos a 1 con room
    room_id = db.Column('room_id', db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    room = db.relationship("Room", back_populates='feature')

    # Relación 1 a muchos con ticket
    ticket = db.relationship('Ticket', back_populates='feature')
    

    def __init__(self, date_from: str = None, date_to: str = None, movie_id = None, room_id = None):
        self.date_from = date_from
        self.date_to = date_to
        self.movie_id = movie_id
        self.room_id = room_id
