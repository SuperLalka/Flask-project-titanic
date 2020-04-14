def list_pages(posts_num):
    if posts_num % 10 == 0:
        pages = range(1, (posts_num // 10) + 1)
    else:
        pages = range(1, (posts_num // 10) + 2)
    return list(pages)

def post_info():
    from post_list import posts
    return posts

def get_post(key, file):
    post = []
    for line in file:
        if key in line:
            post.append(line)
            break
    return post
