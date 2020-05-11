"""
單元測試 - 針對程序中最小的功能模塊（函數和方法）的測試
測試方法：
- 白盒測試：程序自己寫的測試
- 黑盒測試：測試人員或QA，不知道代碼實現細節，只關注功能
編寫Python單元測試 - 定義類繼承TestCase，寫測試方法(test_開頭)
執行單元測試：
- unittest.main()
- python3 -m unittest test_example01.py
第三方庫 - nose2 / pytest
pip install pytest pytest-cov
pytest -v --cov
------------------------------
pip install nose2 cov-core
nose2 -v -C
"""
from unittest import TestCase

from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """測試查找函數的測試用例"""

    # 執行每個測試函數之前要執行的方法
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]

    # 執行每個測試函數之後要執行的方法
    def tearDown(self):
        pass

    def test_seq_search(self):
        """測試順序查找"""
        self.assertEqual(0, seq_search(self.data1, 35))
        self.assertEqual(2, seq_search(self.data1, 12))
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 99))
        self.assertEqual(-1, seq_search(self.data1, 7))

    def test_bin_search(self):
        """測試二分查找"""
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(2, bin_search(self.data2, 40))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(-1, bin_search(self.data2, 7))
        self.assertEqual(-1, bin_search(self.data2, 99))
