from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dev')
def desenvolvedor():
    return jsonify({'nome':'Marcos'})

if __name__ == '__main__':
    app.run()