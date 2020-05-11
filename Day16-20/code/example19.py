"""
擴展性系統性能
- 垂直擴展 - 增加單節點處理能力
- 水平擴展 - 將單節點變成多節點（讀寫分離/分佈式集羣）
併發編程 - 加速程序執行 / 改善用戶體驗
耗時間的任務都儘可能獨立的執行，不要阻塞代碼的其他部分
- 多線程
1. 創建Thread對象指定target和args屬性並通過start方法啓動線程
2. 繼承Thread類並重寫run方法來定義線程執行的任務
3. 創建線程池對象ThreadPoolExecutor並通過submit來提交要執行的任務
第3種方式可以通過Future對象的result方法在將來獲得線程的執行結果
也可以通過done方法判定線程是否執行結束
- 多進程
- 異步I/O
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


# class ThumbnailThread(Thread):

#     def __init__(self, infile):
#         self.infile = infile
#         super().__init__()

#     def run(self):
#         file, ext = os.path.splitext(self.infile)
#         filename = file[file.rfind('/') + 1:]
#         for size in (32, 64, 128):
#             outfile = f'thumbnails/{filename}_{size}_{size}.png'
#             image = Image.open(self.infile)
#             image.thumbnail((size, size))
#             image.save(outfile, format='PNG')


def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')


# def main():
#     start = time.time()
#     threads = []
#     for infile in glob.glob('images/*'):
#         # t = Thread(target=gen_thumbnail, args=(infile, ))
#         t = ThumbnailThread(infile)
#         t.start()
#         threads.append(t)
#     for t in threads:
#         t.join()
#     end = time.time()
#     print(f'耗時: {end - start}秒')


def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    for infile in glob.glob('images/*'):
        # submit方法是非阻塞式的方法 
        # 即便工作線程數已經用完，submit方法也會接受提交的任務 
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        # result方法是一個阻塞式的方法 如果線程還沒有結束
        # 暫時取不到線程的執行結果 代碼就會在此處阻塞
        future.result()
    end = time.time()
    print(f'耗時: {end - start}秒')
    # shutdown也是非阻塞式的方法 但是如果已經提交的任務還沒有執行完
    # 線程池是不會停止工作的 shutdown之後再提交任務就不會執行而且會產生異常
    pool.shutdown()


if __name__ == '__main__':
    main()







