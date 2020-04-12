def post_info():
    from post_list import posts
    post = []
    for line in posts:
        post.append(line)
    return post

def info_search(key, file):
    post = []
    for line in file:
        if key in line:
            post.append(line)
            break
    return post
