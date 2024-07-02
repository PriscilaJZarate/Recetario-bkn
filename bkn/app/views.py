from flask import jsonify, request
from app.models import Receta


def index():
    return '<h1>Hola mundo con flask 🐍</h1>'


def get_all_recetas():
    recetas = Receta.get_all()
    list_recetas = [receta.serialize() for receta in recetas]
    return jsonify(list_recetas)


def create_receta():
    # recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    new_receta = Receta(
        title=data['title'],
        ingredientes=data['ingredientes'],
        procedimiento=data['procedimiento'],
        banner=data['banner']
    )
    new_receta.save()
    return jsonify({'message': 'Receta creada con exito'}), 201


def update_receta(receta_id):
    receta = Receta.get_by_id(receta_id)
    if not receta:
        return jsonify({'message': 'Receta not found'}), 404
    data = request.json
    receta.title = data['title']
    receta.ingredientes = data['ingredientes']
    receta.procedimiento = data['procedimiento']
    receta.banner = data['banner']
    receta.save()
    return jsonify({'message': 'Receta updated successfully'})


def get_receta(receta_id):
    receta = Receta.get_by_id(receta_id)
    if not receta:
        return jsonify({'message': 'receta not found'}), 404
    return jsonify(receta.serialize())


def delete_receta(receta_id):
    receta = Receta.get_by_id(receta_id)
    if not receta:
        return jsonify({'message': 'receta not found'}), 404
    receta.delete()
    return jsonify({'message': 'receta deleted successfully'})
