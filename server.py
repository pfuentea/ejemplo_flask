from flask import Flask, render_template,request,redirect
# importar la clase de friend.py
from friend import Friend

app = Flask(__name__)

@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Friend.get_all()
    for f in friends:
        print(f)
    #print(friends)

    return render_template("index.html",all_friends=friends)
            

@app.route('/create_friend', methods=["POST"])
def create_friend():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "d_name": request.form["fname"],
        "d_name" : request.form["lname"],
        "d_occ_1" : request.form["occ"]
    }
    print(data)
    # Pasamos el diccionario de datos al método save de la clase Friend
    id=Friend.save(data)
    print("amigo_id:",str(id))
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/')


    
if __name__ == "__main__":
    app.run(debug=True)
