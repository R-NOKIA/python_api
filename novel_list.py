from bs4 import BeautifulSoup
import requests

class GetNovel(object):

    def __init__(self):
        # 主网站链接
        self.server = 'https://www.sbiquge.com'
        # 小说链接
        self.novelTarget = ""
        # 小说名字
        self.novelName = ""
        # 小说章节数量
        self.chapterNum = 0
        # 小说章节名字
        self.chapterName = []
        # 小说章节链接
        self.chapterUrls = []

    def search_novel(self, search_name):
        novels = []
        print(search_name)
        req_tail = "/s.php?ie=gbk&q="
        req = requests.get(self.server+req_tail+search_name)
        if req.status_code == requests.codes.ok:
            html = req.text
            boxdiv = BeautifulSoup(html, "lxml").find_all('div', class_='bookbox')
            search_num = len(boxdiv)
            for box in boxdiv:
                novel_dict = {}
                bookinfo = BeautifulSoup(str(box), "lxml").find_all('div', class_="bookinfo")
                for info in bookinfo:
                    novel_dict['name'] = info.h4.string
                    novel_dict['author'] = info.div.next_sibling.string.split("：")[1]
                    novel_dict['cat'] = info.div.string.split("：")[1]
                    novel_dict['img_url'] = self.server+box.img['src']
                    novel_dict['novel_url'] = self.server+box.a['href']
                novels.append(novel_dict)
            # print(novels)
            name = [x['name'] for x in novels]
            novel_dict = dict(zip(name, novels))
            return novel_dict


'''if __name__ == '__main__':
    novel = GetNovel()
    novel.search_novel("一")'''

