from flask import Flask
from flaskext.mysql import MySQL
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
app= Flask(__name__)

mysql = MySQL()
app.config['MySQL_DATABASE_HOST'] = 'localhost'
app.config['MySQL_DATABASE_USER'] = 'root'
app.config['MySQL_DATABASE_PASSWORD'] = ''
app.config['MySQL_DATABASE_BD'] = 'prueba'
mysql.init_app(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    sql = ''' SELECT * FROM prueba.jugadores
        '''
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    jugadores = cursor.fetchall()

    return render_template('jugadores/index.html', jugadores=jugadores )

@app.route('/create', methods=['POST'])
def create():   
    _name = request.form['Name']
    _lastname = request.form['Lastname']
    _age = request.form['Age']

    sql= ''' INSERT INTO prueba.jugadores
         ( Nombre,
         Apellido,
         Edad)
         VALUES
         (%s,
          %s,
          %s);
        '''
    data = (_name, _lastname, _age)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,data)
    conn.commit()
    flash('contacto agregado correctamente')
    return redirect (url_for('index'))

@app.route('/edit/<id>')
def edit(id):
    sql = '''SELECT * FROM prueba.jugadores WHERE id=%s '''
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    jugador= cursor.fetchone()

    return render_template('jugadores/edit.html',jugador = jugador)

@app.route('/update/<id>', methods = ['POST'] )
def update(id):
    _name = request.form['Name']
    _lastname = request.form['Lastname']
    _age = request.form['Age']
    sql = ''' 
        UPDATE prueba.jugadores
        SET 
        `Nombre`= %s,
        `Apellido`= %s,
        `Edad`= %s 
        WHERE `id` = %s;
        '''
    data = (_name, _lastname, _age,id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    flash('contacto actualizado')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    sql = 'DELETE FROM prueba.jugadores WHERE id = %s'
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    conn.commit()
    flash('contact removed succesfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)