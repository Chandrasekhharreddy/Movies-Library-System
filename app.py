from flask import Flask
app=Flask(__name__)

@app.route('/')
#jiii
def function():
    return "Hello World"

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)