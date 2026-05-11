from flask import Flask

app = Flask(__name__) # inicio o flask

@app.route('/decorator') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'


def ola_mundo():
    return 'Um decorator em Python é uma funcionalidade poderosa e elegante que permite modificar ou estender o comportamento de funções ou classes sem alterar o seu código original.'
     
    # Isso é o que será retornado quando a rota '/' for acessada


if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento

