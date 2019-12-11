import random

x = []  # 实验结果
count = 0


def toss_coin_1():  # 硬币1正面朝上概率0.8
    if random.random() < 0.8:
        return 1
    else:
        return 0


def toss_coin_2():  # 硬币1正面朝上概率0.5
    if random.random() < 0.5:
        return 1
    else:
        return 0


def toss_coins(times, groups):  # 每组实验有几次 共几组实验
    for i in range(groups):
        result = []
        coin = random.randint(1, 2)
        if coin == 1:
            for j in range(times):
                result.append(toss_coin_1())
        elif coin == 2:
            for j in range(times):
                result.append(toss_coin_2())
        x.append(result)


# 做实验
times = 100  # 每组实验抛几次
groups = 100  # 实验组数
toss_coins(times, groups)

# 猜测theta值
t1 = 0.6
t2 = 0.3

while count < 100:
    # E步骤开始
    pa1b = []  # P(A_1|B)
    pa2b = []  # P(A_2|B)
    for i in range(groups):
        data = x[i]
        pa1b.append((t1 ** sum(data) * (1 - t1) ** (len(data) - sum(data)) * 0.5) / (
            (t1 ** sum(data) * (1 - t1) ** (len(data) - sum(data)) * 0.5) + (
                t2 ** sum(data) * (1 - t2) ** (len(data) - sum(data)) * 0.5)))
        pa2b.append((t2 ** sum(data) * (1 - t2) ** (len(data) - sum(data)) * 0.5) / (
            (t1 ** sum(data) * (1 - t1) ** (len(data) - sum(data)) * 0.5) + (
                t2 ** sum(data) * (1 - t2) ** (len(data) - sum(data)) * 0.5)))
    # M步骤开始
    headFromCoin1 = 0
    headFromCoin2 = 0
    tailFromCoin1 = 0
    tailFromCoin2 = 0
    for i in range(groups):
        data = x[i]
        headFromCoin1 += sum(data) * pa1b[i]
        tailFromCoin1 += (len(data) - sum(data)) * pa1b[i]
        headFromCoin2 += sum(data) * pa2b[i]
        tailFromCoin2 += (len(data) - sum(data)) * pa2b[i]
    t1old = t1
    t2old = t2
    t1 = headFromCoin1 / (headFromCoin1 + tailFromCoin1)
    t2 = headFromCoin2 / (headFromCoin2 + tailFromCoin2)

    # 输出
    count += 1
    print(count, t1, t2)

    # 退出循环
    if abs(t1old - t1) < 0.001 and abs(t2old - t2) < 0.001:
        break
