from flask import Flask, render_template, redirect, url_for
from forms import ClubForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config["TEMPLATES_AUTO_RELOAD"] = True

clubs_list = []

@app.route("/", methods=('GET', 'POST'))
def home():
    form = ClubForm()

    if form.validate_on_submit():
        clubs_list.append({'name': form.name.data,
                           'description': form.description.data,
                           'spaces_available': form.spaces_available.data,
                           'time_of_day': form.time_of_day.data,
                           'is_free': form.is_free.data
                           })
        return redirect(url_for('clubs'))
    return render_template('index.html', form=form)

@app.route('/clubs')
def clubs():
    return render_template('clubs.html', clubs_list=clubs_list)
