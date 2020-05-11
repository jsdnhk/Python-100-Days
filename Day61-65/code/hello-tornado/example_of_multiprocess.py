"""
用下面的命令運行程序並查看執行時間，例如：
time python3 example05.py
real    0m20.657s
user    1m17.749s
sys     0m0.158s
使用多進程後實際執行時間爲20.657秒，而用戶時間1分17.749秒約爲實際執行時間的4倍
這就證明我們的程序通過多進程使用了CPU的多核特性，而且這臺計算機配置了4核的CPU
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(num):
    """判斷素數"""
    assert num > 0
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return num != 1


def main():
    """主函數"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()
