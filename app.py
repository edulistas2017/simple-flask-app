from flask import Flask, request, render_template
app = Flask(__name__,template_folder='templates')

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template("mapa_analise_imoveis_zuckerman.html")

if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0')
    app.run()
