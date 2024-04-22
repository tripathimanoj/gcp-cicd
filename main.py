from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_output():
    user_input = request.form['userInput']
    # Here you would call your Generative AI model with the user input
    # For simplicity, let's just echo the user input as output
    return render_template('index.html', output=user_input)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="127.0.0.1", port=8080, debug=True)