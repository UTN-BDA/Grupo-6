#https://flask.palletsprojects.com/es/main/blueprints/

class RouteApp:

    API_PREFIX = '/api/v1'

    def init_app(self, app):
        from app.resources import home, user, movie, room, ticket, feature
        app.register_blueprint(home, url_prefix=self.API_PREFIX)
        app.register_blueprint(user, url_prefix=self.API_PREFIX)
        app.register_blueprint(movie, url_prefix=self.API_PREFIX)
        app.register_blueprint(room, url_prefix=self.API_PREFIX)
        app.register_blueprint(ticket, url_prefix=self.API_PREFIX)
        app.register_blueprint(feature, url_prefix=self.API_PREFIX)