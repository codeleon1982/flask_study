from flask import render_template, redirect, url_for
from twittor.forms import LoginForm

def index():
  title = {'title':"Welcome Flask"}
  name = {'username':'root'}
  posts = [
    {
      'author':{'username':'root'},
      'body':"hi I'm root!"
    },
    {
      'author':{'username':'CodeLeon'},
      'body':"hi I'm CodeLeon!"
    },
    {
      'author':{'username':'WenJiang1982'},
      'body':"hi I'm WenJiang1982!"
    }
  ]
  return render_template('index.html', title=title, name=name, posts=posts)

def login():
  # form = LoginForm(csrf_enabled=False)
  form = LoginForm()
  if form.validate_on_submit():
    msg = "username={}, password={}, remember_me={}".format(
      form.username.data,
      form.password.data,
      form.remember_me.data
    )
    print(msg)
    return redirect(url_for('index'))
  return render_template('login.html', title="Sign In", form=form)