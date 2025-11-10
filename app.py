from flask import Flask, render_template, request, redirect, url_for
from utils.db import workouts_collection
from utils.analysis import generate_summary_and_chart

app = Flask(__name__)

# Home Page — Show All Workouts
@app.route('/')
def index():
    data = list(workouts_collection.find())
    return render_template('index.html', data=data)

# Add Workout Entry Page
@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        date = request.form['date']
        workout_type = request.form['workout_type']
        calories = float(request.form['calories'])
        duration = float(request.form['duration'])
        workouts_collection.insert_one({
            "date": date,
            "workout_type": workout_type,
            "calories": calories,
            "duration": duration
        })
        return redirect(url_for('index'))
    return render_template('add_entry.html')

# Dashboard Page — Show Summary & Graph
@app.route('/dashboard')
def dashboard():
    data = list(workouts_collection.find())
    summary, chart_path = generate_summary_and_chart(data)
    return render_template('dashboard.html', summary=summary, chart_path=chart_path)

if __name__ == "__main__":
    app.run(debug=True)
