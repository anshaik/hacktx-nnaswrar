from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return render_template('hello.html')
	
@app.route('/displayUserDefinedMessage/')
@app.route('/displayUserDefinedMessage/<userMessage>')
def displayUserDefinedMessage(userMessage=None):
	if userMessage == None:
		userMessage = 'No user message has been supplied.'
    
	return render_template('displayUserDefinedMessage.html', passThisMessage=userMessage)


if __name__ == '__main__':
    app.run(host='0.0.0.0')