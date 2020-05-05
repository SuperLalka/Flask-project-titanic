import csv
import requests
import sys
from bs4 import BeautifulSoup
from post_functions import post_info


def add_posts(N):
   """Cкрипт N раз загружает случайную статью из Википедии"""
   page_id = int(post_info()[-1][0]) + 1
   def down_pages():
      random_url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
      response = requests.get(random_url)
      soup = BeautifulSoup(response.text, "html.parser")
      page_info = []
      page_info.append(page_id)
      page_info.append(soup.find("h1", class_="firstHeading").text)                 #Извлекает тайтл
      
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
            img_list = [page_id]
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
   
   with open("post_list.csv", "a", encoding='utf_8', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter='|')
      for i in range(N):
         data = down_pages()
         writer.writerow(data)
         page_id += 1
         

if __name__== "__main__":
   add_posts(int(sys.argv[1]))
