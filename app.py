#STEP 1 - import required modules
from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

#STEP 2 - creating the flask app
app = Flask(__name__)

#STEP 3 - setting up MongoDB connection
client = MongoClient('localhost', 27017)  # default port
db = client.flask_database  # This is a MongoDB database
todos = db.todos  # This is a todos collection

#STEP 4 - define routes and views
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.post("/<id>/delete/")
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})  # Proper conversion
    return redirect(url_for('index'))

#STEP 5 - running the flask app
if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
