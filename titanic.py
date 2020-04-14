from flask import Flask, render_template
from post_functions import post_info, get_post, list_pages

app = Flask(__name__)

@app.route('/')
@app.route('/<int:page>')
def content_page() -> 'html':
    info = post_info()
    pages = list_pages(len(info))
    return render_template('root_page.html',
                           the_info = info,
                           the_pages = pages)

                               
@app.route('/post/<name>')
def post(name) -> 'html':
    info = get_post(name, post_info())
    return render_template('post.html',
                           navbar = "Вернуться к содержанию",
                           the_info = info)


if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

