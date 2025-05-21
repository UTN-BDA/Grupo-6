import os
import sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.profile import Profile

# Configuración de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_profiles():
    app = create_app()
    with app.app_context():
        try:
            logger.info("Eliminando perfiles existentes...")
            num_deleted = Profile.query.delete()
            db.session.commit()
            logger.info(f"{num_deleted} perfiles eliminados.")
            
            profile_names = ['Administrador', 'Gerente', 'Usuario', 'Invitado']
            for name in profile_names:
                if not Profile.query.filter_by(name=name).first():
                    profile = Profile(name=name)
                    db.session.add(profile)
                    logger.info(f"Perfil '{name}' agregado.")
                else:
                    logger.info(f"Perfil '{name}' ya existe.")
            db.session.commit()
            logger.info("Perfiles creados exitosamente.")
        except Exception as e:
            logger.exception("Error al crear perfiles:")
            db.session.rollback()

def run():
    create_profiles()

if __name__ == "__main__":
    run()