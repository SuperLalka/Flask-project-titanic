def post_titles_creator():
    import os
    title = input("Enter a post title: ")
    description = input("Enter a post description: ")
    url = input("Enter a name of html-file: ")
    post_info = []
    post_info.append(title), post_info.append(description), post_info.append(url)
    os.chdir(path="templates/")
    with open("allposts.log", "a") as file:
        print(post_info, file=file)

post_titles_creator()
