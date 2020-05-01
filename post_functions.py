import csv

POSTS_PER_PAGE = 10
COMMENTS_PER_PAGE = 7


def add_comment(comm_post, comm_time, comm_author, comm_text):
    """Добавляет комментарии в csv-файл"""
    if comm_text:
        comment = [comm_post, comm_time, comm_author, comm_text]
        with open("comments.csv", "a", encoding='utf_8', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter='|')
            writer.writerow(comment)


def get_comments(name):
    """Возвращает список комментариев к посту"""
    with open("comments.csv", encoding='utf_8', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter='|')
        found = []
        for row in reader:
            for items in row:
                if name in items:
                    found.append(row)
    return found


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
    return None

        
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
    with open('post_list.csv', encoding='utf_8') as f:
        reader = csv.reader(f, delimiter='|')
        posts = []
        for row in reader:
            posts.append(row)
    return posts[1:]


def post_pictures(key):
    """Извлекает и привязывает изображения к постам"""
    with open("post_pictures.csv", encoding='utf_8', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == key:
                return row[1:]


def post_search(name):
    """Осуществляет поиск по введённому значению по всему содержанию списков постов"""
    found = []
    for items in post_info():
        for item in items:
            if name in item and items not in found:
                found.append(items)
    return found


def transliterate(name):
    """Транслитерация значения name"""
    slovar = {
        'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
        'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
        'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
        'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
        'ю':'u','я':'ja', 'А':'a','Б':'b','В':'v','Г':'g','Д':'d','Е':'e','Ё':'e',
        'Ж':'zh','З':'z','И':'i','Й':'i','К':'k','Л':'l','М':'m','Н':'n',
        'О':'o','П':'p','Р':'r','С':'s','Т':'t','У':'u','Ф':'f','х':'h',
        'Ц':'c','Ч':'cz','Ш':'sh','Щ':'scz','Ъ':'','Ы':'y','Ь':'','Э':'e',
        'Ю':'u','Я':'ja',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
        '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
        ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
        '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
        'Є':'e'
    }
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name.lower()
