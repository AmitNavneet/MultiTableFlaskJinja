from flask import Flask,render_template
from flask import request
app=Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/printMultiTable',methods=["POST"])
def printMultiTable():
    startNum=request.form['startNum']
    stopNum=request.form.get('stopNum')

    startNum=int(startNum)
    stopNum=int(stopNum)
    return render_template('printMultiTable.html',startNum=startNum,stopNum=stopNum)

if __name__=='__main__':
    app.run(debug=True)