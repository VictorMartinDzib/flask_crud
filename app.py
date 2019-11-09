from flask import Flask, render_template , request, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# gestor, usuario, contrasenia, host, db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/animalitos'

db = SQLAlchemy(app)

class Animal(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(40), unique=True)
      species = db.Column(db.String(60), unique=True)

      def __init__(self, name, species):
            self.name = name
            self.species = species

@app.route('/')
def index():
      animales = Animal.query.all()
      return render_template('index.html', animales = animales)

@app.route('/show/<int:id>')
def show(id):
      pass

@app.route('/create', methods=['POST'])
def create():
      if request.method == 'POST':
            name = request.form['nameA']
            specie = request.form['specie']
            animal = Animal(name, specie)
            db.session.add(animal)
            db.session.commit()
      return redirect('/')

@app.route('/update', methods=['POST'])
def update():
      pass

@app.route('/destroy/<int:id>')
def destroy(id):
      pass

if __name__ == '__main__':
      app.run(debug=True)

