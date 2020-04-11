from flask import Flask, render_template, escape
from post_functions import post_iteration, post_info

app = Flask(__name__)

@app.route('/')                                             
def content_page() -> 'html':
    contents = post_iteration()
    info = post_info()
    return render_template('post.html',
                           the_title='Конструкция Титаника',
                           the_contents = contents,
                           the_info = info)

                               
@app.route('/post/<name>')
def post(name) -> 'html':
    return render_template('post/{}.html' .format(name),
                           the_title='{}' .format(name))


if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

