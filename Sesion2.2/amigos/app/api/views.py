from . import api
from ..models import Amigo
from flask import request, abort, jsonify
from .. import db

@api.route("/amigo/<int:id>")
def get_amigo(id):
    """
    Retorna JSON con la información de un amigo,
    o un error 404 si no existe.
    """

    amigo = Amigo.query.get_or_404(id)

    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "lati": amigo.lati,
        "longi": amigo.longi
    }

    return jsonify(amigodict)

@api.route("/amigo/byName/<name>")
def get_amigo_by_name(name):

    amigo = Amigo.query.filter_by(name=name).first_or_404()

    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "lati": amigo.lati,
        "longi": amigo.longi
    }

    return jsonify(amigodict)

@api.route("/amigos")
def list_amigos():

    amigos = Amigo.query.all()

    resultado = []

    for amigo in amigos:
        amigodict = {
            "id": amigo.id,
            "name": amigo.name,
            "lati": amigo.lati,
            "longi": amigo.longi
        }
        resultado.append(amigodict)

    return jsonify(resultado)

@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):

    # Buscamos al amigo por su identificador
    amigo = Amigo.query.get_or_404(id)

    # Comprobamos que se haya recibido JSON
    if not request.json:
        abort(422, "No se ha enviado JSON")

    # Extraemos los datos recibidos
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")

    # Actualizamos únicamente los campos recibidos
    if name:
        amigo.name = name

    if lati:
        amigo.lati = lati

    if longi:
        amigo.longi = longi

    # Guardamos los cambios
    if name or lati or longi:
        db.session.commit()

    # Devolvemos los datos actualizados
    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "lati": amigo.lati,
        "longi": amigo.longi
    }

    return jsonify(amigodict)

@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    """
    Elimina un amigo cuyo identificador recibe
    como parámetro.
    """

    amigo = Amigo.query.get_or_404(id)

    db.session.delete(amigo)
    db.session.commit()

    return ('', 204)

@api.route("/amigos", methods=["POST"])
def new_amigo():

    # Comprobamos que hemos recibido JSON
    if not request.json:
        abort(422, "No se ha enviado JSON")

    # Obtenemos el nombre
    name = request.json.get("name")

    # El nombre es obligatorio
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")

    # Comprobamos que no exista otro amigo con ese nombre
    amigo = Amigo.query.filter_by(name=name).first()

    if amigo:
        abort(422, "Ya existe un amigo con ese nombre")

    # Obtenemos las coordenadas, con valor por defecto "0"
    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")

    # Creamos y guardamos el amigo
    amigo = Amigo(name=name, lati=lati, longi=longi)

    db.session.add(amigo)
    db.session.commit()

    # Devolvemos sus datos, incluido el ID generado
    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "lati": amigo.lati,
        "longi": amigo.longi
    }

    return jsonify(amigodict)