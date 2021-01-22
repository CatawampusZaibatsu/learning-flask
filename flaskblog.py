from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import secrets
app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token

posts = [
    {
        'author': 'Liquid Origami',
        'title': 'Blog Post 1',
        'content': 'First posts content...',
        'date_posted': 'January 20, 2021'
    },
    {
        'author': 'Digital Compost',
        'title': 'Blog Post 2',
        'content': 'Second posts content...',
        'date_posted': 'January 20, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
