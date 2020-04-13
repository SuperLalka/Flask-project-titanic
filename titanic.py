from flask import Flask, render_template
from post_functions import post_info, get_post

app = Flask(__name__)

@app.route('/')                                             
def content_page() -> 'html':
    info = post_info()
    return render_template('root_page.html',
                           the_info = info)

                               
@app.route('/post/<name>')
def post(name) -> 'html':
    info = get_post(name, post_info())
    return render_template('post.html',
                           navbar = "Вернуться к содержанию",
                           the_info = info)


if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

