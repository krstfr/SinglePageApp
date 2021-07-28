from flask import Flask, render_template, request
import requests

app = Flask(__name__)
#name space of file. this passes the file into the flask application

registered_users = {
    'kevinb@codingtemple.com': {'name':'Kevin', 'password': 'abc123'},
    'johnl@codingtemple.com': {'name':'John', 'password': 'Colt45'},
    'joel@codingtemple.com': {'name':'Joel', 'password': 'MorphinTime'}
}
@app.route('/', methods=['GET'])
def index():
#this index function will be passed through the route function
    return render_template('index.html.j2')

@app.route('/students', methods=['GET'])
def students(): 
    the_students = ["Thu", "Leo", "Sydney", "Josh", "Chris", "Fernando", "Benny", "Vicky", "Bradley"]
    return render_template('students.html.j2', students=the_students)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        #Do Login Stuff
        email = request.form.get('email') 
        password = request.form.get('password')
        if email in registered_users.keys() and\
            password == registered_users.get(email).get('password'):
            #Login Success
                return f"Login Successful Welcome {registered_users.get(email).get('name')}" 
        error_string = "Incorrect Email/Password Combo"
        return render_template("login.html.j2", error = error_string)
    return render_template('login.html.j2')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        name = request.form.get('name')
        url = f"https://pokeapi.co/api/v2/pokemon/{name}" 
        response = requests.get(url)
        if response.ok:
            try:
                data = response.json()
            except:
                error_string =f'There is no pokemon named {name}'
                return render_template("pokemon.html.j2", error= error_string)
                
            pokemon_data = []
            for data in data:
                pokemon_data_dict={
                    "Name" : data['forms'][0]['name'],
                    "Ability": data['abilities'][0]['ability']['name'],
                    "Base experience" : data['base_experience'],
                    "Sprite URL" : data['sprites']['front_shiny']
                }
                pokemon_data.append(pokemon_data_dict)
            return render_template("pokemon.html.j2", data =pokemon_data)
        else: 
            error_string ="Something is Wrong"
            render_template("pokemon.html.j2", error = error_string)
    return render_template("pokemon.html.j2")

    