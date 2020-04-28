import csv
import requests
from bs4 import BeautifulSoup


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


def added_pages(N):
   """Cкрипт N раз загружает случайную статью из Википедии"""
   def down_pages():
      random_url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
      response = requests.get(random_url)
      soup = BeautifulSoup(response.text, "html.parser")
      page_info = []
      page_info.append(soup.find("h1", class_="firstHeading").text)                 #Извлекает тайтл
      link = transliterate(soup.find("h1", class_="firstHeading").text)
      page_info.append(link)                                                        #Траснлитерирует тайтл для создания ссылки
      
      def description_extraction(soup):
         """Извлекает описание"""
         description = soup.find("p").text
         description = description.replace("\n", "")
         description = description.encode().decode('utf-8', 'ignore')                             
         return description
      
      page_info.append(description_extraction(soup))
      
      def content_extraction(soup):
         """Извлекает текст для поста"""
         block = soup.find(class_="mw-parser-output")
         text = block.findAll("p")
         content = text[0].get_text()
         for string in text[1:]:
            content = content + string.get_text()
         content = content.replace("\n", "")
         content = content.encode().decode('utf-8', 'ignore')
         return content
      
      page_info.append(content_extraction(soup))
      
      def tag_extraction(soup):
         """Извлекает теги поста"""
         block = soup.find(id="mw-normal-catlinks")
         tags = block.findAll("a")
         if len(tags) >=2:
            tag_list = "tags"
            for tag in tags[1:]:
               tag_list += ";" + tag.text
            return tag_list
         else:
            return tags.text
         
      page_info.append(tag_extraction(soup))
      
      def image_extraction(soup, link):
         """Извлекает ссылки картинок и записывает их в файл"""
         blocks = soup.findAll(class_="infobox-image") + soup.findAll(class_="thumb")
         if blocks:
            img_list = [link]
            for block in blocks:
               image = block.find("img")
               img_list.append(image.get('src'))
            with open("post_pictures.csv", "a", encoding='utf_8', newline='') as csv_file:
               writer = csv.writer(csv_file)
               writer.writerow(img_list)
            return img_list
         else:
            return None
         
      image_extraction(soup, link)
      return page_info
   
   for i in range(N):
      data = down_pages()
      with open("post_list.csv", "a", encoding='utf_8', newline='') as csv_file:
         writer = csv.writer(csv_file, delimiter='|')
         writer.writerow(data)
   return "Success"

def entered_post(post_name, post_description, post_content, post_tags, post_pictures):
   """Функция компилирует введёные пользователем данные и записывает их в список постов и изображений"""
   page_info = []
   page_info.append(post_name)
   link = transliterate(post_name)
   page_info.append(link)
   page_info.append(post_description)
   page_info.append(post_content)
   page_info.append(post_tags)
   with open("post_list.csv", "a", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      writer.writerow(page_info)
   if post_pictures:
      img_list = [link]
      for image in post_pictures:
         img_list.append(image)
      with open("post_pictures.csv", "a", encoding='utf_8', newline='') as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow(img_list)
      return img_list
   else:
      return None

def delete_post(name):
   """Удаляет строку из csv-файла"""
   with open('post_list.csv', encoding='utf_8') as csv_file:
      reader = csv.reader(csv_file, delimiter='|')
      posts = []
      for row in reader:
         if name not in row:
            posts.append(row)
   with open("post_list.csv", "w", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      for row in posts:
         writer.writerow(row)
