from flask import Flask, render_template, request
from post_functions import get_content, get_posts_by_tags, get_tags_for_post, list_pages, page_distribution, post_info, post_pictures, post_search

app = Flask(__name__)

@app.route('/')
@app.route('/<int:page>')
def content_page(page=0) -> 'html':
    pages = list_pages(len(post_info()))
    posts = page_distribution(post_info(), page)
    return render_template('root_page.html',
                           the_pages = pages,
                           the_posts = posts,
                           the_title = "RMS Titanic")

@app.route('/post/<name>')
def post(name) -> 'html':
    info = get_content(name, post_info())
    pictures = post_pictures(name)
    tags = get_tags_for_post(info)
    return render_template('post.html',
                           navbar = "Вернуться к содержанию",
                           the_info = info,
                           the_pictures = pictures,
                           the_tags = tags,
                           the_title = "%s" %get_content(name, post_info())[0])

@app.route('/tags/<tag>')
@app.route('/tags/<tag>/<int:page>')
def tag_page(tag="RMS Titanic", page=0) -> 'html':
    posts = page_distribution(get_posts_by_tags(tag), page)
    pages = list_pages(len(get_posts_by_tags(tag)))
    return render_template('tag_page.html',
                           the_posts = posts,
                           the_pages = pages,
                           the_tag = tag,
                           the_title = "Поиск по тегу %s" %tag)

@app.route('/search')
@app.route('/search<req><int:page>')
def search_page(req="", page=0) -> 'html':
    req = request.args["search_word"]
    posts = page_distribution(post_search(req), page)
    pages = list_pages(len(post_search(req)))
    return render_template('search_page.html',
                           the_posts = posts,
                           the_pages = pages,
                           the_req = req,
                           the_title = "Поиск по значению %s" %req)

if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

