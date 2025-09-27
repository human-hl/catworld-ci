from flask import Flask
from controllers.cat_controller import cat_blueprint
from controllers.food_controller import food_blueprint
from flask import Flask, send_file
from flask import Flask, send_from_directory
app = Flask(__name__)

app.register_blueprint(cat_blueprint, url_prefix='/api')
app.register_blueprint(food_blueprint, url_prefix='/api')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)