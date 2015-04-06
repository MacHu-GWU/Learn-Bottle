##encoding=UTF8

import bottle

@bottle.route("/")
def homepage():
    return bottle.template("homepage")

@bottle.post("/")
def result():
    name_value = bottle.request.forms.getunicode("number_value")
    print(name_value, type(name_value))
    text_value = bottle.request.forms.getunicode("text_value")
    print(text_value, type(text_value))
    date_value = bottle.request.forms.getunicode("date_value")
    print(date_value, type(text_value))
    datetime_value = bottle.request.forms.getunicode("datetime_value")
    print(datetime_value, type(text_value))
    
    # 勾选, 单选, 下拉菜单
    checkbox_value = bottle.request.forms.get("checkbox_value")
    print(checkbox_value, type(checkbox_value))
    radio_value = bottle.request.forms.get("radio_value")
    print(radio_value, type(radio_value))
    select_value = bottle.request.forms.get("select_value")
    print(select_value, type(select_value))
    
    return bottle.template("result")

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, debug=True)
