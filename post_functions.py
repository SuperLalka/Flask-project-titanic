POSTS_PER_PAGE = 10

def list_pages(posts_num):
    if posts_num % POSTS_PER_PAGE == 0:
        pages = range(1, (posts_num // POSTS_PER_PAGE) + 1)
    else:
        pages = range(1, (posts_num // POSTS_PER_PAGE) + 2)
    return list(pages)

def page_distribution(posts, num):
    if num == 0 or num == 1:
        return posts[:POSTS_PER_PAGE]
    else:
        x = (num - 1) * POSTS_PER_PAGE
        return posts[x: POSTS_PER_PAGE + x]

def post_info():
    from post_list import posts
    return posts

def post_pictures(name):
    from post_pictures import pictures
    for key,value in pictures.items():
        if key == name:
            return value

def get_content(key, file):
    post = []
    for line in file:
        if key in line:
            post.append(line)
            break
    return post
