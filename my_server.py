from flask import Flask, request

app = Flask("something")


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'POST':
        f=open('names.txt','a')
        f.write("\n"+request.values.get('a'))
        f.close()
        return "added"
    else:
        f=open('names.txt','r')
        content = f.read()
        f.close()
        return content
@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)
