''''''
'''
【问题描述】
小蓝要和朋友合作开发一个时间显示的网站。在服务器上，朋友已经获取了当前的时间，用一个整数表示，值为从1970年1月1日00:00:00到当前时刻经过的毫秒数。
现在，小蓝要在客户端显示出这个时间。小蓝不用显示出年月日，只需要显示出时分秒即可，毫秒也不用显示，直接舍去即可。
给定一个用整数表示的时间，请将这个时间对应的时分秒输出。
【输入格式】
输入一行包含一个整数，表示时间。
【输出格式】
输出时分秒表示的当前时间，格式形如HH:MM:SS，其中 HH表示时，值为О到23，MM表示分，值为О到59，SS表示秒，值为О到59。时、分、秒不足两位时补前导0。
【样例输入1】46800999
【样例输出1】13:00:00
【样例输入2】1618708103123
'''
integer = int(input())
time = integer % (1000 * 60 * 60 * 24)
time = time // 1000  # 去掉多余的毫秒,多少秒
second = time % 60
minute = (time - second) // 60 % 60
hour = (time - second - 60 * minute) // 3600
print('{:02d}:{:02d}:{:02d}'.format(hour, minute, second))