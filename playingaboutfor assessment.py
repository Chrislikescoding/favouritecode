# import sys
# a = []
# b = a
# print(sys.getrefcount(a))
#
# print(a)

# no of references =  will be 3
#
# a= None
#
# # no of references =  will be 2
# b= x

# no of references will be 2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
