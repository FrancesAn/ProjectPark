from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# mysql database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'administrador_db'
mysql = MySQL(app)


app.secret_key='utec123'

@app.route('/mainadmin')
def mainadmin():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('mainadmin.html',usuarios=data)

@app.route('/inicio')
def inicio():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('inicio.html',usuarios=data)

@app.route('/adminevento')
def adminevento():
    cur = mysql.connection.cursor()
    cur.execute('select * from eventos')
    data = cur.fetchall()
    return render_template('adminevento.html',eventos=data)    

@app.route('/edit/<id>')
def edit_user(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios where id = %s',{id})
    data = cur.fetchall()
    print(data[0])
    return render_template('edit.html', usuario=data[0])

@app.route('/editevento/<id>')
def edit_event(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from eventos where id = %s',{id})
    data = cur.fetchall()
    print(data[0])
    return render_template('editevento.html', evento=data[0])    

@app.route('/update/<id>',methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        cod = request.form['codigo']
        nom = request.form['nombre']
        email = request.form['correo']
        perf = request.form['perfil']
        print('UPDATE_USER', id, cod, nom, email, perf)
        cur = mysql.connection.cursor()
        cur.execute("""
            update usuarios
            set codigo = %s,
                nombre = %s,
                correo = %s,
                perfil = %s
            where id = %s
        """,(cod, nom, email, perf, id) )
        mysql.connection.commit()
        # flash('Usuario actualizado correctamente')
        return redirect(url_for('inicio'))

@app.route('/updateevento/<id>',methods=['POST'])
def update_event(id):
    if request.method == 'POST':
        titu = request.form['titulo']
        date = request.form['fecha']
        space = request.form['espacios']
        desc = request.form['descripcion']
        print('UPDATE_EVENT', id, titu, date, space, desc)
        cur = mysql.connection.cursor()
        cur.execute("""
            update eventos
            set titulo = %s,
                fecha = %s,
                espacios = %s,
                descripcion = %s
            where id = %s
        """,(titu, date, space, desc, id) )
        mysql.connection.commit()
        # flash('Evento actualizado correctamente')
        return redirect(url_for('adminevento'))        

@app.route('/add_user',methods=['POST'])
def add_user():
    if request.method == 'POST':
        cod = request.form['codigo']
        nom = request.form['nombre']
        email = request.form['correo']
        perf = request.form['perfil']
        print('INSERT', id, cod, nom, email, perf)
        cur = mysql.connection.cursor()
        cur.execute('insert into usuarios(codigo, nombre, correo, perfil) values(%s,%s,%s,%s)', (cod, nom, email, perf))
        mysql.connection.commit()
        flash('Usuario Insertado correctamente')
        return redirect(url_for('inicio'))

@app.route('/add_event',methods=['POST'])
def add_event():
    if request.method == 'POST':
        titu = request.form['titulo']
        date = request.form['fecha']
        space = request.form['espacios']
        desc = request.form['descripcion']
        print('INSERT', id, titu, date, space, desc)
        cur = mysql.connection.cursor()
        cur.execute('insert into eventos(titulo, fecha, espacios, descripcion) values(%s,%s,%s,%s)', (titu, date, space, desc))
        mysql.connection.commit()
        flash('Evento Insertado correctamente')
        return redirect(url_for('adminevento'))        

@app.route('/delete/<string:id>')
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from usuarios where id = {0}'.format(id))
    mysql.connection.commit()
    flash('Usuario Eliminado correctamente')
    return redirect(url_for('inicio'))

@app.route('/deleteevento/<string:id>')
def deleteevento(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from eventos where id = {0}'.format(id))
    mysql.connection.commit()
    flash('Evento Eliminado correctamente')
    return redirect(url_for('adminevento'))    
    
@app.route('/index.html')
def index():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('index.html',usuarios=data)    

@app.route('/loginutec.html')
def loginutec():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('loginutec.html',usuarios=data)

@app.route('/loginvisita.html')
def loginvisita():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('loginvisita.html',usuarios=data)    

@app.route('/mainutec.html')
def mainutec():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('mainutec.html',usuarios=data) 

@app.route('/mainvisitantes.html')
def mainvisitantes():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('mainvisitantes.html',usuarios=data) 

@app.route('/notificaciones.html')
def notificaciones():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('notificaciones.html',usuarios=data) 

@app.route('/utecespacios1.html')
def utecespacios1():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('utecespacios1.html',usuarios=data) 

@app.route('/utecespacios2.html')
def utecespacios2():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('utecespacios2.html',usuarios=data) 

@app.route('/utecEstadisticas.html')
def utecEstadisticas():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('utecEstadisticas.html',usuarios=data) 

@app.route('/utecEstRap.html')
def utecEstRap():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('utecEstRap.html',usuarios=data) 

@app.route('/visitaespacios1.html')
def visitaespacios1():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('visitaespacios1.html',usuarios=data) 

@app.route('/visitanteEstRap.html')
def visitanteEstRap():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('visitanteEstRap.html',usuarios=data) 

@app.route('/vistaespacios2.html')
def vistaespacios2():
    cur = mysql.connection.cursor()
    cur.execute('select * from usuarios')
    data = cur.fetchall()
    return render_template('vistaespacios2.html',usuarios=data) 

if __name__ == '__main__':
    app.run(debug=True,port=3000)

