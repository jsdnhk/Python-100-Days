#!/usr/bin/python3
# coding: utf-8
from random import randint


def main():
    answer = randint(1, 100)
    while True:
        number = int(input('請輸入: '))
        if number < answer:
            print('大一點')
        elif number > answer:
            print('小一點')
        else:
            print('恭喜你猜對了!')
            break


if __name__ == '__main__':
    main()
