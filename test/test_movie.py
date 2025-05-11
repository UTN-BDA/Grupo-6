import unittest
from flask import current_app
from app.models import Movie
from app import create_app, db
from app.services import MovieService

movie_service = MovieService()

class MovieTestCase(unittest.TestCase):
    def setUp(self):
        self.NAME_PRUEBA = 'Kimi No Nawa'
        self.DIRECTOR_PRUEBA = 'Makoto Shinkai'
        self.YEAR_PRUEBA = '2016'
        self.START_DATE_PRUEBA = '2024/05/24'
        self.FINAL_DATE_PRUEBA = '2024/06/28'
        self.DURATION_PRUEBA = '107'
        self.DESCRIPTION_PRUEBA = 'Intercambio de cuerpos y viaje en el tiempo + amor'
        self.GENRE_PRUEBA = 'Drama, Fantasía, Romance'
        self.CLASSIFICATION_PRUEBA = '+3 años'
        self.CAST_PRUEBA = 'Ryūnosuke Kamiki, Masami Nagasawa'
        self.LANGUAGE_PRUEBA = 'Japonés subtitulada'

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_movie(self):
        
        movie = self.__get_movie()

        self.assertTrue(movie.name, self.NAME_PRUEBA)
        self.assertTrue(movie.director, self.DIRECTOR_PRUEBA)
        self.assertTrue(movie.year, self.YEAR_PRUEBA)
        self.assertTrue(movie.start_date, self.START_DATE_PRUEBA)
        self.assertTrue(movie.final_date, self.FINAL_DATE_PRUEBA)
        self.assertTrue(movie.duration, self.DURATION_PRUEBA)
        self.assertTrue(movie.description, self.DESCRIPTION_PRUEBA)
        self.assertTrue(movie.genre, self.GENRE_PRUEBA)
        self.assertTrue(movie.classification, self.CLASSIFICATION_PRUEBA)
        self.assertTrue(movie.cast, self.CAST_PRUEBA)
        self.assertTrue(movie.language, self.LANGUAGE_PRUEBA)


    def test_movie_save(self):

        movie = self.__get_movie()

        movie_service.save(movie)

        self.assertGreaterEqual(movie.id, 1)
        self.assertTrue(movie.name, self.NAME_PRUEBA)
        self.assertTrue(movie.director, self.DIRECTOR_PRUEBA)
        self.assertTrue(movie.year, self.YEAR_PRUEBA)
        self.assertTrue(movie.start_date, self.START_DATE_PRUEBA)
        self.assertTrue(movie.final_date, self.FINAL_DATE_PRUEBA)
        self.assertTrue(movie.duration, self.DURATION_PRUEBA)
        self.assertTrue(movie.description, self.DESCRIPTION_PRUEBA)
        self.assertTrue(movie.genre, self.GENRE_PRUEBA)
        self.assertTrue(movie.classification, self.CLASSIFICATION_PRUEBA)
        self.assertTrue(movie.cast, self.CAST_PRUEBA)
        self.assertTrue(movie.language, self.LANGUAGE_PRUEBA)

    def test_movie_delete(self):
        
        movie = self.__get_movie()

        movie_service.save(movie)

        movie_service.delete(movie.id)
        self.assertIsNone(movie_service.find(movie))

    def test_movie_all(self):
        
        movie = self.__get_movie()
        movie_service.save(movie)

        movies = movie_service.all()
        self.assertGreaterEqual(len(movies), 1)

    def test_movie_find(self):
        
        movie = self.__get_movie()
        movie_service.save(movie)

        movie_find = movie_service.find(1)
        self.assertIsNotNone(movie_find)
        self.assertEqual(movie_find.id, movie.id)
        self.assertEqual(movie_find.name, movie.name)

    def __get_movie(self):
        
        movie = Movie()
        movie.name = self.NAME_PRUEBA
        movie.director = self.DIRECTOR_PRUEBA
        movie.year = self.YEAR_PRUEBA
        movie.start_date = self.START_DATE_PRUEBA
        movie.final_date = self.FINAL_DATE_PRUEBA
        movie.duration = self.DURATION_PRUEBA
        movie.description = self.DESCRIPTION_PRUEBA
        movie.genre = self.GENRE_PRUEBA
        movie.classification = self.CLASSIFICATION_PRUEBA
        movie.cast = self.CAST_PRUEBA
        movie.language = self.LANGUAGE_PRUEBA

        return movie

if __name__ == '__main__':
    unittest.main()