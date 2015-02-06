##encoding=UTF-8

"""
创建两个文本框, 点击Submit计算文本框中的两个数的总和。
点击Assign random value随机分配两个随机数
"""

import bottle
import random

@bottle.route("/")
def index():
    default_value1 = ""
    default_value2 = ""
    return bottle.template("index.tpl", {"default_value1": default_value1,
                                         "default_value2": default_value2,})

@bottle.post("/")
def index1():
    default_value1 = random.randint(1, 1000)
    default_value2 = random.randint(1, 1000)
    return bottle.template("index.tpl", {"default_value1": default_value1,
                                         "default_value2": default_value2,})
    
@bottle.post('/result')
def result():
    value1 = bottle.request.forms.get("value1")
    value2 = bottle.request.forms.get("value2")
    answer = int(value1) + int(value2)
    return bottle.template("result.tpl", {"value1": value1,
                                          "value2": value2,
                                          "answer": answer,})

bottle.run(host='localhost', port=7777, debug=True)
# bottle.run(host="10.255.210.132", port=7777, debug=False) # this is how 