from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
