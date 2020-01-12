
'''

https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/09.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E8%BF%9B%E9%98%B6.md

'''


from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    '''宠物'''

    def __init__(self, nickName):
        self._nickName = nickName


    @abstractmethod
    def make_voice(self):
        '''发出声音'''
        pass



class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪。。。' % self._nickName)


class Cat(Pet):

    def make_voice(self):
        print('%s: 喵喵。。。' % self._nickName)


def main():
    pets = [Dog('大黄'), Cat('凯迪'), Cat('萨利')]
    for pet in pets:
        pet.make_voice()



if __name__ == '__main__':
    main()