from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/check_user/p2/baseDatos.db'
db = SQLAlchemy(app)


class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cCpu = db.Column(db.String(80), nullable=False)
    cRam = db.Column(db.String(120), nullable=False)
    cDisco = db.Column(db.String(120), nullable=False)
    eServicio = db.Column(db.String(120), nullable=False)


    def __init__(self,cCpu,cRam, cDisco, eServicio):
        self.cCpu = cCpu
        self.cRam = cRam
        self.cDisco = cDisco
        self.eServicio = eServicio

    def __repr__(self):
	informacion = self.cCpu +" " + self.cRam + " " + self.cDisco+ " " + self.eServicio

        return '<informacion %r>' % informacion
