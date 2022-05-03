# Flask forms

This project adds a tiny bit more complexity and organisation. The form is placed into its own forms.py file, and we have three templates: 
- One to render the base html that all pages include (head with meta info, body etc).
- One index template for the "home" page - this is where we render the clubs form we defined in forms.py.
- One template for displaying the clubs we created with the form (no database yet, so they are only stored while you are running the app).

**Setup**

First create and activate some form of environment to store your dependencies. I like Anaconda:

```
$ conda create -n myenv python=3.7

$ conda activate myenv
```

Then install Flask and WTForms

`$ pip install Flask Flask-WTF`

**Run the app**

`$ flask run`

You should now be able to see the output in your browser window (at http://127.0.0.1:5000) 
