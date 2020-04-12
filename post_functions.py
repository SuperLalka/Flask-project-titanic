def post_iteration():
    import os
    posts = []
    for post in os.listdir(path="templates/post"):
        posts.append(post)
    return posts

def post_info(file):
    address = file
    post = []
    with open("templates/post/%s" %file, "r") as file:
        for line in file:
            if "<title>" in line:
                title = line.strip(" ")
                a = title.index(">")
                b = title.rindex("<")
                post.append(title[a+1:b])
            if "description" in line:
                description = line.strip(" ")
                post.append(description.split('"')[3])
    post.append(address.split(".")[0])
    return post
