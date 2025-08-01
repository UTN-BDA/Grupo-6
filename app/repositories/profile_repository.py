from typing import List
from app.models import Profile
from app import db
from sqlalchemy.exc import NoResultFound

class ProfileRepository:
    
    def save(self, profile: Profile) -> Profile:
        db.session.add(profile) 
        db.session.commit()
        return profile
    
    def update(self, profile: Profile, id: int) -> Profile:
        entity = self.find(id)
        entity.name = profile.name
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, profile: Profile) -> None:
        db.session.delete(profile)
        db.session.commit()
    
    def all(self) -> List[Profile]:
        users = db.session.query(Profile).all()
        return users
    
    def find(self, id: int) -> Profile:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Profile).filter(Profile.id == id).one()
        except NoResultFound:
            return None
        