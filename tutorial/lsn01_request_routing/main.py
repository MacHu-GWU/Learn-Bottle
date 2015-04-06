##encoding=UTF8

"""
在web中你每输入一个url, 这个就叫http request请求。也就是说比如你键入localhost:8080, 服务器端就需要啊根据
你的request, 生成一个页面返回给用户浏览器。这个页面在bottle框架中可以直接由route函数生成字符串, 但最佳的
方法是建立一个views的文件夹, 在里面放上.tpl模板文件, 按照模板生成html。
"""

import bottle

@bottle.route("/")
def homepage():
    return bottle.template("homepage")

@bottle.route("/welcome")
def welcome():
    return bottle.template("welcome")

@bottle.route("/<text>")
def print_text(text):
    """动态路由, 也就是服务器自动解析url中的参数, 然后根据参数生成不同的html
    还有更高级的路由方式, 可以根据一定规则例如正则解析url, 然后将元素转化成字符串, 整数等对象。具体方法
    请参考: http://bottlepy.org/docs/dev/tutorial.html#dynamic-routes
    """
    return bottle.template("print_text", {"text": text})
    
if __name__ == "__main__":
    # 注: debug模式很危险, 因为其他人可以在服务器上运行代码。
    # 通常我们使用bottle.run(debug=False)来运行我们的产品
    bottle.run(host="localhost", port=8080, debug=True)

