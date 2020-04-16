POSTS_PER_PAGE = 10

def list_pages(posts_num):
    """Определяет количество страниц"""
    if posts_num % POSTS_PER_PAGE == 0:
        pages = range(1, (posts_num // POSTS_PER_PAGE) + 1)
    else:
        pages = range(1, (posts_num // POSTS_PER_PAGE) + 2)
    return list(pages)

def page_distribution(posts, num):
    """Возвращает срез списка постов в зависимости от номера страницы"""
    if num == 0 or num == 1:
        return posts[:POSTS_PER_PAGE]
    else:
        x = (num - 1) * POSTS_PER_PAGE
        return posts[x: POSTS_PER_PAGE + x]

def post_info():
    """Извлекает информацию из файла со списками постов"""
    from post_list import posts
    return posts

def post_pictures(name):
    """Извлекает и привязывает изображения к постам"""
    from post_pictures import pictures
    for key,value in pictures.items():
        if key == name:
            return value

def get_content(key, file):
    """Получает информацию для страницы поста"""
    post = []
    for line in file:
        if key in line:
            post.append(line)
            break
    return post

def get_posts_by_tags(tag):
    """Возвращает список постов по тегу"""
    found = []
    for items in post_info():
        for item in items:
            if "tags" in item:
                for values in item.values():
                    for value in values:
                        if value == tag:
                            found.append(items)
    return found

def get_tags_for_post(post):
    """Возвращает список тегов поста"""
    for items in post:
        for item in items:
            if "tags" in item:
                return item["tags"]
