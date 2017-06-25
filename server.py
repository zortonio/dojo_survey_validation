from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "ThisIsASecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def new_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    # Validation
    if len(name) < 1:
        flash("Name cannot be blank!")

    if len(comment) < 1:
        flash("Comment cannot be blank!")
    elif len(comment) > 120:
        flash("Comment cannot be more than 120 characters.")

    if '_flashes' in session:
        return redirect('/')
    else:
        return render_template('user.html', name=name, location=location, language=language, comment=comment)

@app.route('/home')
def goBack():
    return redirect('/')

app.run(debug=True)
