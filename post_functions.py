def list_pages(posts_num):
    if posts_num % 10 == 0:
        pages = range(1, (posts_num // 10) + 1)
    else:
        pages = range(1, (posts_num // 10) + 2)
    return list(pages)

def page_distribution(posts, num):
    if num == 0 or num == 1:
        return posts[:10]
    else:
        x = (num - 1) * 10
        return posts[x: 10 + x]

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
