# Flask forms

This project adds a tiny bit more complexity and organisation. The form is placed into its own forms.py file, and we have three templates: 
- One to render the base html that all pages include (head with meta info, body etc).
- One index template for the "home" page - this is where we render the clubs form we defined in forms.py.
- One template for displaying the clubs we created with the form (no database yet, so they are only stored while you are running the app).

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


<img width="467" alt="Screenshot 2022-05-11 at 14 45 11" src="https://user-images.githubusercontent.com/20923607/167864797-5504870c-49c9-4211-ba27-ca511b191db1.png">


======================================================

<img width="399" alt="Screenshot 2022-05-11 at 14 44 58" src="https://user-images.githubusercontent.com/20923607/167864832-6da6f2a1-bdec-4195-8a46-c44fb1b7061e.png">





