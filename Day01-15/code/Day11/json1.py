"""
讀取JSON數據

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""

import json
import csv2

json_str = '{"name": "駱昊", "age": 38, "title": "叫獸"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

# 把轉換得到的字典作爲關鍵字參數傳入Teacher的構造器
teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)

# 請思考如何將下面JSON格式的天氣數據轉換成對象並獲取我們需要的信息
# 稍後我們會講解如何通過網絡API獲取我們需要的JSON格式的數據
"""
    {
        "wendu": "29",
        "ganmao": "各項氣象條件適宜，發生感冒機率較低。但請避免長期處於空調房間中，以防感冒。",
        "forecast": [
            {
                "fengxiang": "南風",
                "fengli": "3-4級",
                "high": "高溫 32℃",
                "type": "多雲",
                "low": "低溫 17℃",
                "date": "16日星期二"
            },
            {
                "fengxiang": "南風",
                "fengli": "微風級",
                "high": "高溫 34℃",
                "type": "晴",
                "low": "低溫 19℃",
                "date": "17日星期三"
            },
            {
                "fengxiang": "南風",
                "fengli": "微風級",
                "high": "高溫 35℃",
                "type": "晴",
                "low": "低溫 22℃",
                "date": "18日星期四"
            },
            {
                "fengxiang": "南風",
                "fengli": "微風級",
                "high": "高溫 35℃",
                "type": "多雲",
                "low": "低溫 22℃",
                "date": "19日星期五"
            },
            {
                "fengxiang": "南風",
                "fengli": "3-4級",
                "high": "高溫 34℃",
                "type": "晴",
                "low": "低溫 21℃",
                "date": "20日星期六"
            }
        ],
        "yesterday": {
            "fl": "微風",
            "fx": "南風",
            "high": "高溫 28℃",
            "type": "晴",
            "low": "低溫 15℃",
            "date": "15日星期一"
        },
        "aqi": "72",
        "city": "北京"
    }
"""
