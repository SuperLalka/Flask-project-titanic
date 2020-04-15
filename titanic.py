from flask import Flask, render_template
from post_functions import get_content, list_pages, page_distribution, post_info, post_pictures

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
    info = get_content(name, post_info())
    pictures = post_pictures(name)
    return render_template('post.html',
                           navbar = "Вернуться к содержанию",
                           the_info = info,
                           the_pictures = pictures)


if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

