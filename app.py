from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'
# migrate = Migrate(app, db)

# db.init_app(app)


@app.route('/')
def index():
    return 'Welcome to the virtual art gallery'








if __name__ == '__main__':
    app.run(port =  4000, debug = True)  # run the app in debug mode on port 500    