from flask import Flask, render_template
from post_functions import post_info, get_post, list_pages, page_distribution

app = Flask(__name__)

@app.route('/')
@app.route('/<int:page>')
def content_page(page=0) -> 'html':
    info = post_info()
    pages = list_pages(len(info))
    posts = page_distribution(info, page)
    return render_template('root_page.html',
                           the_pages = pages,
                           the_posts = posts)

                               
@app.route('/post/<name>')
def post(name) -> 'html':
    info = get_post(name, post_info())
    return render_template('post.html',
                           navbar = "Вернуться к содержанию",
                           the_info = info)


if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

