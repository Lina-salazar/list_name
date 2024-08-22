from flask import Flask, jsonify # el Flask se utilzar para crear la aplicacion, y el jsonify intercambia datos de Python 
# a JSON, es decir para su estructura cambia, en este caso lo que es la lista.
Proyecto = Flask(__name__)  # se crea una instancia de Flask y  __name__ que tiene doble guion bajo, le indica
# a Flask el nombre del módulo actual, para que sepa donde ubicarse. 

@Proyecto.route('/personas', methods=['GET']) #esta linea de codigo difine una ruta, @Proyecto.route contiene un URL que en este 
# caso es '/personas' y methods=['GET'] indica que este endpoint solo responderá a solicitudes HTTP de tipo GET
def obtener_personas(): #esta linea de codigo nos dice que cuanto acceda al endpoint '/personas', se ejecuta obtener_personas
   
    lista_personas = ["Gaby", "Sara", "Naibeth", "Laura", "Andrea"] # aqui esta la lista de nombres de personas.
    return jsonify(lista_personas) # esta linea de codigo convierte la lista_personas a JSON, usando el jsonify.
if __name__ == '__main__':  # esto nos ayuda a que si __name__ == '__main__' y se ejecuta el archivo en Python directamente,
    # __name__ toma el valor '__main__'.
    Proyecto.run(debug=True) # Si se detecta algun tipo de cambio en el codigo Flask lo que hace es actualizarse, y el comando 
    #debug=True ayuda con la depuracion.
