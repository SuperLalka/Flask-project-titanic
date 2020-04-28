from flask import Flask, render_template, request, redirect
from post_functions import get_content, get_posts_by_tags, get_tags_for_post, list_pages, page_distribution, post_info, post_pictures, post_search
from post_operations import entered_post, delete_post

app = Flask(__name__)

@app.route('/')
@app.route('/<int:page>')
def content_page(page=0) -> 'html':
    pages = list_pages(len(post_info()))
    posts = page_distribution(post_info(), int(page))
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
    posts = page_distribution(get_posts_by_tags(tag), int(page))
    pages = list_pages(len(get_posts_by_tags(tag)))
    return render_template('tag_page.html',
                           the_posts = posts,
                           the_pages = pages,
                           the_tag = tag,
                           the_title = "Поиск по тегу %s" %tag)

@app.route('/search')
def search_page() -> 'html':
    req = request.args["search_word"]
    page = (request.args.get("page") if request.args.get("page") else 0)
    posts = page_distribution(post_search(req), int(page))
    pages = list_pages(len(post_search(req)))
    return render_template('search_page.html',
                           the_posts = posts,
                           the_pages = pages,
                           the_req = req,
                           the_title = "Поиск по значению %s" %req)

@app.route('/add_post', methods = ["GET", "POST"])
def add_user_post_page() -> 'html':
    if request.method == 'POST':
        post_name = request.values.get("post_name")
        post_description = request.values.get("post_description")
        post_content = request.values.get("post_content")
        post_tags = (request.values.get("post_tags") if request.values.get("post_tags") else None)
        post_pictures = ([request.values.get("post_pictures")] if request.values.get("post_pictures") else None)
        entered_post(post_name, post_description, post_content, post_tags, post_pictures)
        return redirect("/post/%s" %post_name, code=302)
    return render_template('add_post.html',
                           the_title = "Добавление поста")

@app.route('/edit_post', methods = ["GET", "POST"])
def edit_user_post_page() -> 'html':
    name = request.args["post"]
    info = get_content(name, post_info())
    pictures = post_pictures(name)
    return render_template('edit_page.html',
                           the_info = info,
                           the_pictures = pictures,
                           the_title = "Редактирование поста")

@app.route('/del_post')
def delete_post_page() -> 'html':
    req = request.args["post"]
    delete_post(req)
    return redirect("/", code=302)

if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

