# Flask forms

### App structure

This project builds on [hello-templates](https://github.com/ChristinaVoss/flask-templates), and adds a tiny bit more complexity and organisation. We define a form in a forms.py file, and we have three templates: 
- One to render the base html that all pages include (head with meta info, body etc).
- One index template for the "home" page - this is where we render the clubs form we defined in forms.py.
- One template for displaying the clubs we created with the form (no database yet, so they are only stored while you are running the app).

<img width="611" alt="Screenshot 2022-05-12 at 09 40 54" src="https://user-images.githubusercontent.com/20923607/168029589-e89fede6-c9d4-40b8-85ba-582093f0820f.png">

**Key parts**

In forms.py:

Import the installed WTForms libraries (include the types of fields you will use in your form, and any validators you will need):

```
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length
```

Then you define your form as a class which inherits from FlaskForm, and state the type of field, the label name, and then any optional additional arguments (such as validators):
```
class ClubForm(FlaskForm):
    name = StringField('Club name', validators=[InputRequired(), Length(min=10, max=100)])
    ...
```

In app.py:

Import your newly created form from forms.py:

`from froms import ClubForm`

Configure a secret key (WTForms needs this - though hardcoding it like this is not the best for production....):

`app.config['SECRET_KEY'] = 'your secret key'`

Then, in a controller for a route where you want to use the form, create it:

- `form = ClubForm()`
- Pass it to a template to be rendered when users visit the page:

  `return render_template('index.html', form=form)`
- And finally, extract the data from the form if the form submitted without problems:
  ```
  if form.validate_on_submit():
        clubs_list.append({'name': form.name.data, ...})
  ```

In index.html:

Here we have defined a simple html form, and use our fields as defined in forms.py. When you use WTForms, you include the form.csrf_token at the beginning of your form (unless you have gone out fo your way to switch this off, but that shouldn't be necessary (or wise) in most cases), and then output the field label and the actual field:

```
<form method="POST" action="/">
      {# Cross-Site Request Forgery prevention token: #}
      {{ form.csrf_token }}
          
      {{ form.name.label }}
      {{ form.name }}
      {{ validate_field(form.name) }}
      ...
</form>
```

The final line, `validate_field(...)` is linked to an optional macro defined above the form (can also be put in a helper file) so that you can see your errors based on your defined validations in forms.py output to the browser (instead of just bouncing with no message):

```
{# user defined macro to validate forms: #}
  {% macro validate_field(field) %}
    {% if field.errors %}
      <div class=errors>
      {% for error in field.errors %}
        <p>{{ error }}</p>
      {% endfor %}
    </div>
    {% endif %}
  {% endmacro %}
```


### Setup

If you have not installed Python3, [please do](https://www.python.org/downloads/).

First create and activate some form of environment to store your dependencies. I like [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html):

```
$ conda create -n myenv python=3.7

$ conda activate myenv
```

**Or** just use Pythons built in environments:

```
$ python3 -m venv venv

$ . venv/bin/activate
```

Then install Flask and WTForms

`$ pip install Flask Flask-WTF`

### Run the app

`$ flask run`

You should now be able to see the output in your browser window (at http://127.0.0.1:5000) 

### Resulting pages

**index.html**

<img width="520" alt="Screenshot 2022-05-12 at 18 07 55" src="https://user-images.githubusercontent.com/20923607/168130750-94775158-6d2b-4515-9fa2-d68be751bbe1.png">

**clubs.html (after adding a club in the form above - data does not persist in this app!)**

<img width="517" alt="Screenshot 2022-05-12 at 18 08 59" src="https://user-images.githubusercontent.com/20923607/168130767-c0f760ff-7f27-4a18-b6e4-663b355199f9.png">

