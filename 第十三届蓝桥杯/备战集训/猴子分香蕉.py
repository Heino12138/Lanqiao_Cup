''''''
'''
5 只猴子是好朋友，在海边的椰子树上睡着了。这期间，有商船把一大堆香蕉忘记在沙滩上离去。
第 1 只猴子醒来，把香蕉均分成 5 堆，还剩下 1个，就吃掉并把自己的一份藏起来继续睡觉。
第 2 只猴子醒来，把香蕉均分成 5 堆，还剩下 2 个，就吃掉并把自己的一份藏起来继续睡觉。
第 3 只猴子醒来，把香蕉均分成 5 堆，还剩下 3 个，就吃掉并把自己的一份藏起来继续睡觉。
第 4 只猴子醒来，把香蕉均分成 5 堆，还剩下 4 个，就吃掉并把自己的一份藏起来继续睡觉。
第 5 猴子醒来，重新把香蕉均分成 5 堆，哈哈，正好不剩！
请计算一开始最少有多少个香蕉。
'''
num = 0
while True:
    num += 1
    tmp = num
    if tmp % 5 == 1 and tmp >= 5:
        tmp = (tmp - 1) * 0.8
        if tmp % 5 == 2 and tmp >= 5:
            tmp = (tmp - 2) * 0.8
            if tmp % 5 == 3 and tmp >= 5:
                tmp = (tmp - 3) * 0.8
                if tmp % 5 == 4 and tmp >= 5:
                    tmp = (tmp - 4) * 0.8
                    if tmp % 5 == 0 and tmp >= 5:
                        print(num)
                        break
