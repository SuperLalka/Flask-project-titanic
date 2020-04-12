from flask import Flask, render_template
from post_functions import post_info, info_search

app = Flask(__name__)

@app.route('/')                                             
def content_page() -> 'html':
    info = post_info()
    return render_template('post.html',
                           the_info = info)

                               
@app.route('/post/<name>')
def post(name) -> 'html':
    info = info_search('%s' %name, post_info())
    return render_template('page.html',
                           navbar = "Вернуться к содержанию",
                           the_info = info)


if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

