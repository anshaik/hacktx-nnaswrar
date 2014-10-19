from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

#Call this function to fetch the statis HTML page.
#Example: http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    return render_template('hello.html')

#Call this function with an argument.
#Example: http://127.0.0.1:5000/displayUserDefinedMessage/?userMessage=This is a message to display!
@app.route('/displayUserDefinedMessage/')
def displayUserDefinedMessage():
	print request.args['userMessage']
	return render_template('displayUserDefinedMessage.html', passThisMessage=request.args['userMessage'])


if __name__ == '__main__':
    app.run(host='0.0.0.0')