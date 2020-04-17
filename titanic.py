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
                           the_titles = "RMS Titanic")

@app.route('/post/<name>')
def post(name) -> 'html':
    info = get_content(name, post_info())
    pictures = post_pictures(name)
    tags = get_tags_for_post(info)
    return render_template('post.html',
                           navbar = "Вернуться к содержанию",
                           the_info = info,
                           the_pictures = pictures,
                           the_tags = tags)

@app.route('/tags/<tag>')
@app.route('/tags/<tag>/<int:page>')
def tag_page(tag="RMS Titanic", page=0) -> 'html':
    tag_posts = page_distribution(get_posts_by_tags(tag), page)
    pages = list_pages(len(get_posts_by_tags(tag)))
    return render_template('tag_page.html',
                           the_tag_posts = tag_posts,
                           the_tag = tag,
                           the_pages = pages)

@app.route('/search', methods=["POST"])
def search_page() -> 'html':
    titles = request.form["search_word"]
    posts = post_search(request.form["search_word"])
    pages = list_pages(len(posts))
    return render_template('root_page.html',
                           the_posts = posts,
                           the_pages = pages,
                           the_titles = "Поиск по значению %s" %titles)

if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

