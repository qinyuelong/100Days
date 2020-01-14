'''
五人分鱼
'''


# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼


def fish():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1




'''

贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
'''

class Thing(object):
    '''物品'''

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


    @property
    def value(self):
        '''价格重量比'''
        return self.price / self.weight


def input_thing():
    '''输入物品信息'''
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def xiaotou_main():
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
        all_things.sort(key=lambda x: x.value, reverse=True)
        total_weight = 0
        total_price = 0
        for thing in all_things:
            if total_weight + thing.weight <= max_weight:
                print(f'小偷拿走了{thing.name}')
                total_weight += thing.weight
                total_price += thing.price
        print(f'总价值{total_price}美元')



if __name__ == '__main__':
    fish()