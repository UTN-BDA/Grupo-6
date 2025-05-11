import unittest
from flask import current_app
from app.models import Feature
from app import create_app, db
from app.services import FeatureService

feature_service = FeatureService()

class FeatureTestCase(unittest.TestCase):
    def setUp(self):
        self.FECHA_INICIO_PRUEBA = '2024/05/28'
        self.FECHA_FINAL_PRUEBA = '2024/06/28'
        
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
    
    def test_feature(self):
        
        feature = self.__get_feature()
        
        self.assertTrue(feature.date_from, self.FECHA_INICIO_PRUEBA)
        self.assertTrue(feature.date_to, self.FECHA_FINAL_PRUEBA)

        
    def test_feature_save(self):
        
        feature = self.__get_feature()
        
        self.assertTrue(feature.date_from, self.FECHA_INICIO_PRUEBA)
        self.assertTrue(feature.date_to, self.FECHA_FINAL_PRUEBA)
        
    
    def test_movie_delete(self):
        
        feature = self.__get_feature()

        feature_service.save(feature)

        feature_service.delete(feature)
        self.assertIsNone(feature_service.find(feature))

    def test_movie_all(self):
        
        feature = self.__get_feature()
        feature_service.save(feature)

        features = feature_service.all()
        self.assertGreaterEqual(len(features), 1)

    def test_feature_finde(self):
        
        feature = self.__get_feature()
        feature_service.save(feature)

        feature_finde = feature_service.find(1)
        self.assertIsNotNone(feature_finde)
        self.assertEqual(feature_finde.id, feature.id)
        
    def __get_feature(self):
        
        feature = Feature()
        feature.date_from = self.FECHA_INICIO_PRUEBA
        feature.date_to = self.FECHA_FINAL_PRUEBA
        
        return feature

if __name__ == '__main__':
    unittest.main()