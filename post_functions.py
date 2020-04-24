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
    import csv
    with open('post_list.csv', encoding='utf_8') as f:
        reader = csv.reader(f, delimiter='|')
        posts = []
        for row in reader:
            posts.append(row)
    return posts

def post_pictures(name):
    """Извлекает и привязывает изображения к постам"""
    from post_pictures import pictures
    for key,value in pictures.items():
        if key == name:
            return value

def get_content(key, file):
    """Получает информацию для страницы поста"""
    for line in file:
        if key in line:
            return line

def get_posts_by_tags(tag):
    """Возвращает список постов по тегу"""
    found = []
    for items in post_info():
        for item in items:
            if "tags" in item:
                if tag in item:
                    found.append(items)
    return found

def get_tags_for_post(post):
    """Возвращает список тегов поста"""
    for item in post:
        if "tags" in item:
            return item.split(";")[1:]

def post_search(name):
    """Осуществляет поиск по введённому значению по всему содержанию списков постов"""
    found = []
    for items in post_info():
        for item in items:
            if name in item and items not in found:
                found.append(items)
    return found
