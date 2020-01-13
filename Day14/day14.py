'''
https://www.tianapi.com/console/
https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/14.%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8%E5%92%8C%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91.md
'''


from time import time
from threading import Thread
import requests
import json
class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open('./'+filename, 'wb') as f:
            f.write(resp.content)



def download_main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=28e22a8c41b303392bf0a15ef44e44e4&num=10')
    data_model = resp.json()
    # with open('./meinv.txt', 'w') as f:
    #     f.write(json.dumps(data_model))

    print(data_model)
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()


if __name__ == '__main__':
    download_main()
