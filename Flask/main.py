from flask import Flask

app=Flask(__name__)

@app.route('/')
def main():
   return "<h1>Hello, world!</h1>"

@app.route('/info')
def info():
   return "<h1>Hello, brother!</h1>"

if __name__ == "__main__":
   app.run()