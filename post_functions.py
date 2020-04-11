def post_iteration():
    import os
    posts = []
    for post in os.listdir(path="templates/post"):
        posts.append(post.split(".")[0])
    return posts

def post_info():
    info = []
    with open("templates/allposts.log") as file:
        for post in file:
            info.append(post)
    return info
