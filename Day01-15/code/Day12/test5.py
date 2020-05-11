"""
不良內容過濾
"""
import re


def main():
    sentence = '你丫是傻叉嗎? 我操你大爺的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞筆',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)


if __name__ == '__main__':
    main()
