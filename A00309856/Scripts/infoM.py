from mBase import db
from mBase import Modelo
from checkCommands import cMemoria, cDisco, cCpu, eServicio

db.create_all()

info = Modelo(cCpu()[2],cMemoria()[0],cDisco()[1],eServicio()[0] )

db.session.add(info)
db.session.commit()

var=Modelo.query.all()
print(var)
