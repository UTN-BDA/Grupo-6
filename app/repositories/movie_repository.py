from typing import List
from app.models import Movie
from app import db

class MovieRepository:
    def save(self, movie: Movie) -> Movie:
        db.session.add(movie)
        db.session.commit()
        return movie
    
    def update(self, movie: Movie, id: int) -> Movie:
        entity = self.find(id)
        entity.name = movie.name
        entity.director = movie.director
        entity.year = movie.year
        entity.start_date = movie.start_date
        entity.final_date = movie.final_date
        entity.duration = movie.duration
        entity.description = movie.description
        entity.genre = movie.genre
        entity.classification = movie.classification
        entity.cast = movie.cast
        entity.language = movie.language
        
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, movie: Movie) -> None:
        db.session.delete(movie)
        db.session.commit()
        
    def all(self) -> List[Movie]:
        movies = db.session.query(Movie).all()
        return movies

    def find(self, id: int) -> Movie:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Movie).filter(Movie.id == id).one()
        except:
            return None
        
    def find_by_name(self, name: str):
        return db.session.query(Movie).filter(Movie.name == name).one_or_none()
    