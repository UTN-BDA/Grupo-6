from typing import List
from app.models import Feature
from app.repositories import FeatureRepository

repository = FeatureRepository()

class FeatureService:
    
    """ Clase que se encarga de CRUD de Features """
    def save(self, feature: Feature) -> Feature:
        return repository.save(feature)

    def update(self, feature: Feature, id: int) -> Feature:
        return repository.update(feature, id)
    
    def delete(self, id: int) -> None:
        feature = self.find(id)
        repository.delete(feature)

    def all(self) -> List[Feature]:
        return repository.all()
    
    def find(self, id: int) -> Feature:
        return repository.find(id)

