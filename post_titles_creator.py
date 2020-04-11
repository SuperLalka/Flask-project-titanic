def post_titles_creator():
    import os
    title = input("Enter a post title: ")
    description = input("Enter a post description: ")
    url = input("Enter a name of html-file: ")
    os.chdir(path="templates/")
    with open("allposts.log", "a") as file:
        print(title, description, url, sep="^", end="|", file=file)

post_titles_creator()
