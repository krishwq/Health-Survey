from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask("__main__")
app = Flask(__name__, template_folder='templates')

# Configure SQLAlchemy to use SQLite database in memory 
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///health.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
db=SQLAlchemy(app)

# Define the Health model with necessary fields
class Health(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80),nullable=False)    
    last_name = db.Column(db.String(80),nullable=False) 
    dob = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String( 80), nullable=False)    
    height = db.Column(db.Float, nullable=False) 
    weight = db.Column(db.Float, nullable=False)
    b_groups =db.Column(db.String(5), nullable=  False)
    blood_pressure = db.Column(db.String(10), nullable=False) 
    heart_beat = db.Column(db.Integer, nullable=False) 
    diabates=db.Column(db.String(10), nullable=False)
    more=db.Column(db.String(100), nullable= True) 


    def __repr__(self)->str:
        return f'{self.id}' 

# Create the tables defined by your models in the database
# with app.app_context():
#     db.create_all()  # Creates the tables defined by your models

# route for home page
@app.route('/',methods=['GET','POST'])   
def home():
    if(request.method == 'POST'):
        health = Health(
        first_name=request.form['inputfname'],
        last_name=request.form['inputlname'],
        dob=request.form['inputdob'],
        gender=request.form['inputgender'],
        city=request.form['inputcity'],
        height=request.form['inputheight'],  
        weight=request.form['inputWeight'],   
        b_groups=request.form['inputgroup'], 
        blood_pressure=request.form['inputpressure'],  
        heart_beat=request.form['inputbit'],  
        diabates=request.form['inputdiabetis'] , 
        more=request.form['more']  
        )
        db.session.add(health)  
        db.session.commit() 

    health_data = Health.query.all()
    return render_template('index.html', health_data=health_data)

# route for update page
@app.route('/update/<int:id>',methods=['GET','POST'])
def edit_health(id): 
    if(request.method == 'POST'):
        health = Health.query.filter_by(id=id).first()
        health.first_name = request.form['first_name']
        health.last_name = request.form['last_name']
        health.dob = request.form['dob']
        health.gender = request.form['gender']
        health.city = request.form['city']
        db.session.add(health)
        db.session.commit()
        return redirect('/')      
    health_data = Health.query.all()
    health_edit = Health.query.filter_by(id=id).first()
    return render_template('updates.html', health_data=health_data, health_edit=health_edit)

# route for delete data
@app.route('/delete/<int:id>')
def delete_health(id):
    health = Health.query.filter_by(id=id).first()
    db.session.delete(health)
    db.session.commit()
    return redirect('/')

# Run the application
if __name__ == "__main__":
    app.run(debug=True, port=8000)
