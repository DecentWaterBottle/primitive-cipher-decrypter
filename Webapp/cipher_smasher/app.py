from flask import Flask, render_template, request, jsonify
from breaker import hill_climbing

app = Flask(__name__)

default_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt_text(text, alphabet):
    full_alphabet = alphabet + alphabet.upper()
    mapping = str.maketrans(default_alphabet, full_alphabet)
    encrypted_text = text.translate(mapping)
    return encrypted_text


@app.route('/')
def decrypter():
    return render_template("decrypter.html")


@app.route('/encrypter')
def encrypter():
    return render_template("encrypter.html")


@app.route('/encrypt-text', methods=("GET", "POST"))
def encrypt():
    data = request.get_json()
    print(data)
    text = data["text"]
    alphabet = data["alphabet"]
    encrypted_text = encrypt_text(text, alphabet)
    response = {"encrypted_text": encrypted_text}
    return jsonify(response)


@app.route("/decrypt-text", methods=("GET", "POST"))
def decrypt():
    data = request.get_json()
    print(data)
    plain_text, best_key, best_score = hill_climbing(data["data"])
    response = {"decrypted_text": plain_text}

    return jsonify(response)


if __name__ == "__main__":
    app.run()
