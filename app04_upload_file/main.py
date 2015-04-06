##encoding=UTF-8

import bottle
from bottle import route, request
import os

@bottle.route("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/upload")
def do_upload():
    category   = request.forms.get('category')
    upload     = request.files.get('upload')
    print(category, type(category))
    print(upload.filename)
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = get_save_path_for_category(category)
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'

if __name__ == "__main__":
    bottle.run(host='localhost', port=7777, debug=True)