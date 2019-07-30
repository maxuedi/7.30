from flask import Flask
app=Flask(__name__)
@app.route('/<maxuedi>') 
def index(maxuedi) :
     return 'hello, %s!' %maxuedi
#保证在运行mian.py文件时才执行
if __name__=="__main__":
     app.run(debug = True)#启用调试