def transliterate(name):
   """Транслитерация значения name"""
   slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
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
      'Є':'e'}
   for key in slovar:
      name = name.replace(key, slovar[key])
   return name.lower()

def added_pages():
   """Cкрипт N раз загружает случайную статью из Википедии"""
   import requests
   from bs4 import BeautifulSoup
   random_url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
   response = requests.get(random_url)
   soup = BeautifulSoup(response.text, "html.parser")
   page_info = []
   page_info.append(soup.find("h1", class_="firstHeading").text)
   page_info.append(transliterate(soup.find("h1", class_="firstHeading").text))
   page_info.append(soup.find("p").text)
   def content_extraction(soup):
      block = soup.find(class_="mw-parser-output")
      tags = block.findAll("p")
      content = tags[0].get_text()
      for string in tags[1:]:
         content = content + string.get_text()
      return content
   page_info.append(content_extraction(soup))
   def tag_extraction(soup):
      block = soup.find(id="mw-normal-catlinks")
      tags = block.findAll("a")
      tag_list = []
      for tag in tags[1:]:
         tag_list.append(tag.text)
      return {"tags" : tag_list}
   #page_info.append(tag_extraction(soup))
   #content = soup.findAll("p")
   
   #for img in soup.find_all('img'):
      #print(img.get('src'))
   return page_info

print(added_pages())
