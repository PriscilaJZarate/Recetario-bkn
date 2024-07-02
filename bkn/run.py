from flask import Flask
from flask_cors import CORS
from app.views import index
from app.views import get_all_recetas
from app.views import get_receta
from app.views import create_receta
from app.views import update_receta
from app.views import delete_receta
from app.database import init_app

# inicializacion del proyecto Flask
app = Flask(__name__)

init_app(app)
CORS(app)

app.route('/', methods=['GET'])(index)
app.route('/api/recetas/', methods=['GET'])(get_all_recetas)
app.route('/api/recetas/<int:receta_id>', methods=['GET'])(get_receta)
app.route('/api/recetas/', methods=['POST'])(create_receta)
app.route('/api/recetas/<int:receta_id>', methods=['PUT'])(update_receta)
app.route('/api/recetas/<int:receta_id>', methods=['DELETE'])(delete_receta)

if __name__ == '__main__':
    app.run(debug=True)
