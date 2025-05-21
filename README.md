
# Cine

## Descripción del proyecto
Proyecto de software sobre cartelera y boleteria de un cine. Permite admnistrar los usuarios, boletos, cartelera y salas por parte del dueño del cine.

### Tecnologías a usar
Lenguaje: python
Framework: flask
ORM: sqlalchemy
Virtualización: docker

### Instrucciones para correr la aplicación
1. Clonar el repositorio
2. (Opcional) Crear un entorno virtual y activarlo con:
```
python -m ven ven
venv/Scripts/activate
```
3. Instalar las dependencias necesarias
```
pip install -r requirements.txt
```
4. Crear un archivo .env usando el arhcivo env-example como ejemplo. Modificar el puerto inclusive de ser necesario.

#### Para los contenedores
5. Construir y crear los servicios
```
docker-compose up --build
```
6. Ejecutar los contenedores de fondo
```
docker-compose up -d
```

#### Para realizar las migraciones
7. Inicializar las migraciones en la raíz del proyecto:
```
alembic init migrations
```
8. En alembic.ini, si aparece la siguiente linea, comentarla:
```
sqlalchemy.url = sqlite:///example.db
```
9. Modificar el archivo migrations/env.py en base al archivo env-migrations-example
10. Crear una migración y aplicarla 
```
alembic revision --autogenerate -m "Primeras tablas”
alembic upgrade head
```
#### Si todos los pasos fueron ejecutados exitosamente, la aplicación debería estar lista para ingresar datos en la db y funcionar.

#### (Opcional) Para ingresar registros falsos a la db

11. Poner el entorno en modo producción:
```
$Env:FLASK_CONTEXT = "production"
```
13. Ejecutar el script load_all() desde la raíz del repositorio:
```
python scripts/load_all.py
```

## Integrantes
- [@ItsCaaam](https://www.github.com/itscaaam) Barrera Camila
- [@ivanjcs](https://www.github.com/ivanjcs) Castro Ivan
- [@solparejas](https://www.github.com/solparejas) Parejas Sol
