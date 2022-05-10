from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WWW'

    # Importerar allt från template, static o.s.v.
    from .views import views
    from .auth import auth
    ##from .scraper import scraper

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    ## app.register_blueprint(scraper, url_prefix='/')
    ## imageScraper = scraper()
    ## imageScraper.searchPics("Three Hearts","Krönleins","Burk")
   

    return app



