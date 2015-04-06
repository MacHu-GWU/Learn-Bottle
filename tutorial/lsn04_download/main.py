##encoding=UTF8

import bottle

@bottle.route("/<filename>")
def serve_static(filename):
    """bottle使用bottle.static_file为静态文件提供url链接服务。
    static_file(filename, root)意味着：
        http://localhost:8080/filename url是去root文件夹下寻找filename的文件
    """
    return bottle.static_file(filename, root="static")

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True)