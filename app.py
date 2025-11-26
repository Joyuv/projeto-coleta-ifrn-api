from flask import Flask, request, jsonify
from sqlalchemy import select
from models.modelos import Base, db, engine, Veiculo

app = Flask(__name__)

Base.metadata.create_all(engine)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return jsonify({"message": "API de pe e funcionando"})
    else:
        return "Tudo funcional!"


@app.route("/veiculo/list", methods=["POST"])
def veiculos():
    if request.method == "POST":
        list = []
        for veiculo in db.scalars(select(Veiculo)):
            list.append(veiculo)
        return jsonify({"message": "Requisicao autorizada", "list": list})
