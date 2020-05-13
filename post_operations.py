import csv


def add_favor(post, cookie):
   """Функция записывает пост в куки со списком избранных постов"""
   return cookie + "/" + post


def del_favor(post, cookie):
   """Функция удаляет пост из куки со списком избранных постов"""
   new_cookie = []
   for item in cookie.split("/"):
      if item != post:
         new_cookie.append(item)
   return "/".join(new_cookie)
      

def entered_post(post_id, post_name, post_description, post_content, post_tags, post_pictures):
   """Функция компилирует введёные пользователем данные и записывает их в список постов и изображений"""
   page_info = []
   page_info.append(post_id)
   page_info.append(post_name)
   page_info.append(post_description)
   page_info.append(post_content)

   if post_tags:
      if "tags" not in post_tags.split(";"):
         post_tags = "tags;" + post_tags
   else:
      post_tags = None
   page_info.append(post_tags)
   
   with open("post_list.csv", "a", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      writer.writerow(page_info)
      
   if post_pictures:
      img_list = []
      for pict in post_pictures.split(","):
         img_list.append(pict)
      img_list.insert(post_id, 1)
      with open("post_pictures.csv", "a", encoding='utf_8', newline='') as csv_file:
         writer = csv.writer(csv_file, delimiter='|')
         writer.writerow(img_list)
      return img_list
   else:
      return None


def delete_post(name):
   """Удаляет строку из csv-файла списка постов, изображений и комментариев"""
   files = ['post_list.csv', 'post_pictures.csv', "comments.csv"]
   for file in files:
      with open(file, encoding='utf_8') as csv_file:
         reader = csv.reader(csv_file, delimiter='|')
         posts = []
         for row in reader:
            if name != row[0]:
               posts.append(row)
      with open(file, "w", encoding='utf_8', newline='') as csv_file:
         writer = csv.writer(csv_file, delimiter='|')
         for row in posts:
            writer.writerow(row)


def delete_post_string(name, file):
   """Удаляет строчку csv-файла"""
   with open(file, encoding='utf_8') as csv_file:
      reader = csv.reader(csv_file, delimiter='|')
      posts = []
      for row in reader:
         if name != row[0]:
            posts.append(row)
            
   with open(file, "w", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      for row in posts:
         writer.writerow(row)
