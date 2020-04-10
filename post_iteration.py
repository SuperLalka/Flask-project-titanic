def post_iteration():
    import os
    posts = []
    for post in os.listdir(path="templates/post"):
        posts.append(post.split(".")[0])
    return posts
