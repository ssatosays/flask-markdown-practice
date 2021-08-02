from flask import Flask, render_template, Markup
from markdown import markdown
import codecs
app = Flask(__name__, static_url_path='/static')


def markdown_reader():
    target = codecs.open('./markdowns/index.md', 'r', 'utf-8')
    res = target.read()
    target.close()
    return Markup(markdown(res))


@app.route('/')
def index():
    return render_template('index.html', md=markdown_reader())


if __name__ == '__main__':
    app.run(debug=True)
