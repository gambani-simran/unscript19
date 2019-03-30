from flask import Flask, render_template, request, jsonify
import aiml
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')


@app.route("/ask", methods=['POST'])
def ask():
	message = request.form['messageText'].encode('utf-8').strip()

	kernel = aiml.Kernel()
	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
		#print(type(message))
		#x = message.split("b")
		#message = x[1]
		print(type(message))
		if message == "quit":
			exit()
		elif message == "save":
			kernel.saveBrain("bot_brain.brn")
		else:
			b = message.decode('utf-8')
			print(b+"decoded msg")
			bot_response = kernel.respond(b)
			# type(bot_response)
			print(bot_response)
			return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
