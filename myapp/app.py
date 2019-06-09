from flask import Flask
from penguin import pengin_main

app = Flask(__name__)

@app.route('/')
def hello():
    print(pengin_main.main())
    return "hello"

if __name__ == "__main__":
    app.run()