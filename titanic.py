from flask import Flask, make_response, render_template, request, redirect
from post_functions import add_comment, get_comments, get_content, get_posts_by_tags, get_tags_for_post, list_comments, list_pages, page_comments_distribution, page_distribution, post_info, post_pictures, post_search, transliterate
from post_operations import entered_post, delete_post
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/<int:page>')
def content_page(page=0) -> 'html':
    content = post_info()
    pages = list_pages(len(content))
    posts = page_distribution(content, int(page))
    num_comments = list(map(lambda x: len(get_comments(x)), [post[1] for post in posts]))
    return render_template('root_page.html',
                           the_pages = pages,
                           the_posts = posts,
                           the_num_comments = num_comments,
                           the_title = "RMS Titanic")


@app.route('/post/<name>')
@app.route('/post/<name>/<int:page>')
def post(name, page=0) -> 'html':
    info = get_content(name, post_info())
    pictures = post_pictures(name)
    tags = get_tags_for_post(info)
    comm_content = get_comments(name)
    comment_pages = list_comments(len(comm_content))
    comments = page_comments_distribution(comm_content, page)
    return render_template('post.html',
                           navbar = "Вернуться к содержанию",
                           the_comments = comments,
                           the_comment_pages = comment_pages,
                           the_info = info,
                           the_pictures = pictures,
                           the_tags = tags,
                           the_title = "%s" %get_content(name, post_info())[0])


@app.route('/tags/<tag>')
@app.route('/tags/<tag>/<int:page>')
def tag_page(tag="RMS Titanic", page=0) -> 'html':
    content = get_posts_by_tags(tag)
    posts = page_distribution(content, int(page))
    pages = list_pages(len(content))
    num_comments = list(map(lambda x: len(get_comments(x)), [post[1] for post in posts]))
    return render_template('tag_page.html',
                           the_posts = posts,
                           the_pages = pages,
                           the_tag = tag,
                           the_num_comments = num_comments,
                           the_title = "Поиск по тегу %s" %tag)


@app.route('/search')
def search_page() -> 'html':
    req = request.args.get("search_word", default="RMS Titanic")
    page = request.args.get("page", default=0)
    active = post_search(req)
    posts = page_distribution(active, int(page))
    pages = list_pages(len(active))
    num_comments = list(map(lambda x: len(get_comments(x)), [post[1] for post in posts]))
    return render_template('search_page.html',
                           the_posts = posts,
                           the_pages = pages,
                           the_req = req,
                           the_num_comments = num_comments,
                           the_title = "Поиск по значению %s" %req)


@app.route('/add_post', methods = ["GET", "POST"])
def add_user_post_page() -> 'html':
    if request.method == 'POST':
        post_name = request.values.get("post_name")
        post_description = request.values.get("post_description")
        post_content = request.values.get("post_content")
        post_tags = request.values.get("post_tags", default=None)
        post_pictures = request.values.get("post_pictures", default=None)
        entered_post(post_name, post_description, post_content, post_tags, post_pictures)
        return redirect("/post/%s" %transliterate(post_name), code=302)
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


@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('user', 'admin', max_age=60*5)
    return res


@app.route('/add_сomment', methods = ["GET", "POST"])
def add_user_comment() -> 'html':
    comm_post = request.args.get("post")
    comm_time = datetime.today().strftime("%Y-%m-%d_%H:%M:%S")
    comm_author = (request.values.get("comm_author") if request.values.get("comm_author") else "Anonimus")
    comm_text = request.values.get("comm_text")
    add_comment(comm_post, comm_time, comm_author, comm_text)
    return redirect("/post/%s" %comm_post, code=302)


if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

