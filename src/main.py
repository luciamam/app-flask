from flask import Flask , render_template
from flask_socketio import SocketIO , send


app=Flask(__name__)
app.config['SECRET KEY']='secret'
socketio=SocketIO(app)


#creacion de una ruta 
@app.route('/')    #el nombre de la ruta 
def index():
    return render_template('index.html')  #el archivo html 


#cuando escuches este menaJE
#esta a la eschucha 
@socketio.on('message')
def handleMessage(msg):
    print('Message:'+ msg)


#si el nombre es la ruta principal 
if __name__=='__main__':
    socketio.run(app,debug=True)
    #socketio.run(app,debug=True,port=3000)
    