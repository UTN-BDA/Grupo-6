from typing import List
from app.models import Feature
from app import db

class FeatureRepository:
    def save(self, feature: Feature) -> Feature:
        db.session.add(feature)
        db.session.commit()
        return feature
    
    def update(self, feature: Feature, id: int) -> Feature:
        entity = self.find(id)
        entity.date_from = feature.date_from
        entity.date_to = feature.date_to
        # AGREGAR MAS FILTRADOS
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, feature: Feature) -> None:
        db.session.delete(feature)
        db.session.commit()
        
    def all(self) -> List[Feature]:
        features = db.session.query(Feature).all()
        return features

    def find(self, id: int) -> Feature:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Feature).filter(Feature.id == id).one()
        except:
            return None
        
    def find_by_name(self, name: str):
        return db.session.query(Feature).filter(Feature.name == name).one_or_none()
    