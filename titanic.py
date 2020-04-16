from flask import Flask, render_template
from post_functions import get_content, get_posts_by_tags, get_tags_for_post, list_pages, page_distribution, post_info, post_pictures

app = Flask(__name__)

@app.route('/')
@app.route('/<int:page>')
def content_page(page=0) -> 'html':
    pages = list_pages(len(post_info()))
    posts = page_distribution(post_info(), page)
    return render_template('root_page.html',
                           the_pages = pages,
                           the_posts = posts)

                               
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
def tag_page(tag="RMS Titanic") -> 'html':
    tag_posts = get_posts_by_tags(tag)
    pages = list_pages(len(tag_posts))
    return render_template('tag_page.html',
                           the_tag_posts = tag_posts,
                           the_tag = tag,
                           the_pages = pages)
    
if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

