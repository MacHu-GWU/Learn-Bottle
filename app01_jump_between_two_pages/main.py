##encoding=UTF-8

"""
在两个页面之间通过链接来回跳转
"""

import bottle

@bottle.route("/")
def home_page():
    return bottle.template("home_page")

@bottle.route("/welcome")
def welcome_page():
    return bottle.template("welcome_page")

# debug模式很危险, 因为其他人可以在服务器上运行代码。
# 通常我们使用bottle.run(debug=False)来运行我们的产品
bottle.debug(True)
bottle.run(host="localhost", port=7777)
