from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)

class Dbdata(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    department=db.Column(db.String(20), nullable=False)

    def __repr__(self)-> str:
        return f"{self.id} is {self.name}"
    

@app.route("/")
def homepage():
    show = Dbdata.query.all()
    return render_template('index.html',show=show) 

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_item = Dbdata(name=title, department="science")
    db.session.add(new_item)
    db.session.commit()
    return redirect("/")


@app.route("/products")
def products():
    
    return "This is product page"

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
