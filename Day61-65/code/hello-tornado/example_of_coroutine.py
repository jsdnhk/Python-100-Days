"""
協程（coroutine）- 可以在需要時進行切換的相互協作的子程序
"""
import asyncio

from example_of_multiprocess import is_prime


def num_generator(m, n):
    """指定範圍的數字生成器"""
    for num in range(m, n + 1):
        print(f'generate number: {num}')
        yield num


async def prime_filter(m, n):
    """素數過濾器"""
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """主函數"""
    loop = asyncio.get_event_loop()
    start, end = 1, 100
    futures = asyncio.gather(prime_filter(start, end), square_mapper(start, end))
    futures.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(futures)
    loop.close()


if __name__ == '__main__':
    main()
