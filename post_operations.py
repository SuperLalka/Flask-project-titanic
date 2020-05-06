import csv


def add_favor(post):
   """Функция записывает пост в csv-файл со списком избранных постов"""
   with open("favor_list.csv", "a", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      writer.writerow(post)


def del_favor(name):
   """Функция удаляет пост из csv-файла со списком избранных постов"""
   with open('favor_list.csv', encoding='utf_8') as csv_file:
      reader = csv.reader(csv_file, delimiter='|')
      posts = []
      for row in reader:
         if name != row[0]:
            posts.append(row)
            
   with open("favor_list.csv", "w", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      for row in posts:
         writer.writerow(row)

def entered_post(post_id, post_name, post_description, post_content, post_tags, post_pictures):
   """Функция компилирует введёные пользователем данные и записывает их в список постов и изображений"""
   page_info = []
   page_info.append(post_id)
   page_info.append(post_name)
   page_info.append(post_description)
   page_info.append(post_content)

   if "tags" not in post_tags.split(";"):
      post_tags = "tags;" + post_tags
   page_info.append(post_tags)
   
   with open("post_list.csv", "a", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      writer.writerow(page_info)
      
   if post_pictures:
      img_list = [post_id]
      for pict in post_pictures.split(","):
         img_list.append(pict)
      with open("post_pictures.csv", "a", encoding='utf_8', newline='') as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow(img_list)
      return img_list
   else:
      return None


def delete_post(name):
   """Удаляет строку из csv-файла списка постов"""
   with open('post_list.csv', encoding='utf_8') as csv_file:
      reader = csv.reader(csv_file, delimiter='|')
      posts = []
      for row in reader:
         if name != row[0]:
            posts.append(row)
            
   with open("post_list.csv", "w", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      for row in posts:
         writer.writerow(row)
         
   """Удаляет строку из csv-файла списка изображений"""
   with open('post_pictures.csv', encoding='utf_8') as csv_file:
      reader = csv.reader(csv_file)
      posts = []
      for row in reader:
         if name != row[0]:
            posts.append(row)
            
   with open("post_pictures.csv", "w", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file)
      for row in posts:
         writer.writerow(row)
         
   """Удаляет строки из csv-файла списка комментариев"""
   with open('comments.csv', encoding='utf_8') as csv_file:
      reader = csv.reader(csv_file, delimiter='|')
      posts = []
      for row in reader:
         if name != row[0]:
            posts.append(row)
            
   with open("comments.csv", "w", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      for row in posts:
         writer.writerow(row)
