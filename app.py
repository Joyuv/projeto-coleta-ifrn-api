from flask import Flask, request, jsonify
from sqlalchemy import select
from models.modelos import Base, db, engine, Veiculo, Frota

app = Flask(__name__)

Base.metadata.create_all(engine)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return jsonify({"message": "API de pe e funcionando"})
    else:
        return "Tudo funcional!"


@app.route("/veiculo/list", methods=["GET"])
def veiculos():
    if request.method == "POST":
        list = []
        for veiculo in db.scalars(select(Veiculo)):
            list.append(veiculo)
        return jsonify({"message": "Requisicao autorizada", "list": list})


@app.route("/veiculo/add", methods=["POST"])
def adicionar_veiculo():
    form = request.json()
    if form.get("placa") is not None and form.get("frota_id") is not None:
        data = {"placa": form.get("placa"), "frota_id": form.get("frota_id")}
        veiculo = Veiculo(placa=str(data["placa"], frota_id=int(data["frota_id"])))
        db.add(veiculo)
        db.commit()
        return jsonify({"message": "Veiculo adicionado com sucesso!"})
    else:
        return jsonify({"message": "Erro, falta informacoes"}, 417)


@app.route("/veiculo/update", methods=["POST"])
def atualizar_veiculo():
    pass
