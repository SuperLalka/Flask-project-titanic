def post_iteration():
    import os
    posts = []
    for post in os.listdir(path="templates/post"):
        posts.append(post.split(".")[0])
    return posts

def post_info():
    info = []
    file = open("templates/allposts.log", "r")
    for line in file:
        for word in line.split("|")[:-1]:
            info.append(word.split("^"))
    return info
