import os
import sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.role import Role

# Configuración de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_roles():
    app = create_app()
    with app.app_context():
        try:
            logger.info("Eliminando roles existentes...")
            num_deleted = Role.query.delete()
            db.session.commit()
            logger.info(f"{num_deleted} roles eliminados.")
            
            roles_data = [
                {"name": "admin", "description": "Administrador del sistema"},
                {"name": "user", "description": "Usuario estándar"},
                {"name": "editor", "description": "Editor de contenidos"},
                {"name": "viewer", "description": "Solo lectura"}
            ]

            for role_data in roles_data:
                if not Role.query.filter_by(name=role_data["name"]).first():
                    role = Role(**role_data)
                    db.session.add(role)
                    logger.info(f"Rol '{role.name}' agregado.")
                else:
                    logger.info(f"Rol '{role_data['name']}' ya existe.")
            db.session.commit()
            logger.info("Roles creados exitosamente.")
        except Exception as e:
            logger.exception("Error al crear roles:")
            db.session.rollback()

def run():
    create_roles()

if __name__ == "__main__":
    run()