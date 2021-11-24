from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests

class Scrapper:
    def __init__(self, url):
        self.url = url
        self.source = BeautifulSoup(requests.get(url).text, 'html.parser')

    def getTitle(self):
        return self.source.title.text

    def getAllLinks(self):
        result = []
        datalistLink = self.source.find_all('a')
        for data in datalistLink:
            if (self.url[-1] == '/'):
                url = self.url[:-1]
                result.append(url + data['href'])
            else:
                result.append(self.url + data.get('href'))
        return result
    
    def getAllImages(self):
        result = []
        datalistImage = self.source.find_all('img')
        for data in datalistImage:
            if (self.url[-1] == '/'):
                url = self.url[:-1]
                result.append(url + data['src'])
            else:
                result.append(self.url + data.get('src'))
        return result

    def getAllItemIntoSomethingByClass(self, className):
        result = []
        datalist = self.source.find_all(class_=className)
        for data in datalist:
            result = data.contents
        return result

    def getAllItemIntoSomethingById(self, idName):
        result = []
        dataList = self.source.findAll(id=idName)
        if len(dataList) > 1:
            for data in dataList:
                result.append(data.contents)
            return result
        else:
            return dataList.contents


    def getContentOfHtmlPart(self, htmlpart, typedata):
        if (typedata == 'text'):
            return htmlpart.text
        elif (typedata == 'href'):
            return htmlpart.get('href')
        elif (typedata == 'src'):
            return htmlpart.get('src')
        elif (typedata == 'class'):
            return htmlpart.get('class')
        elif (typedata == 'id'):
            return htmlpart.get('id')
        elif (typedata == 'title'):
            return htmlpart.get('title')
        elif (typedata == 'alt'):
            return htmlpart.get('alt')
