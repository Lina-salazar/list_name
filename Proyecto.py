from flask import Flask, jsonify

Proyecto = Flask(__name__)  # __name__ debe ser entre dos guiones bajos

@Proyecto.route('/personas', methods=['GET'])
def obtener_personas():
    # Lista de nombres de personas
    lista_personas = ["Gaby", "Sara", "Naibeth", "Laura", "Andrea"]
    # Convertir la lista a JSON y devolverla
    return jsonify(lista_personas)

if __name__ == '__main__':  # __name__ y __main__ deben estar entre guiones bajos
    Proyecto.run(debug=True)
