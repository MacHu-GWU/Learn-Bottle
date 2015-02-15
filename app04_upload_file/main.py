##encoding=UTF-8

import bottle

@bottle.route("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/")
def index():
    return bottle.template("index.tpl")

if __name__ == "__main__":
    bottle.run(host='localhost', port=7777, debug=True)