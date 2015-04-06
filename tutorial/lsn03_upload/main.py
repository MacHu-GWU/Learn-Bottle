##encoding=UTF8

import bottle

@bottle.route("/")
def homepage():
    return bottle.template("homepage")

@bottle.post("/upload")
def do_upload():
    """bottle使用bottle.request.files.get(tagname)方法获得文件对象, 然后可以使用.save方法将其按照原
    文件名存储在指定目录下
    """
    # upload.raw_filename, the raw filename
    # upload.file, the file object, use file.read() to read file
    upload = bottle.request.files.get("upload")
    upload.save("user_uploaded") # appends upload.filename automatically
    return "OK"

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True)