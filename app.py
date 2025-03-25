from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Function to generate a password
def generate_password(length, use_numbers, use_special):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a PIN (only numbers)
def generate_pin(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json  # Get JSON data from AJAX request

    generate_type = data.get("generate_type")
    length = int(data.get("length"))

    # Validation: Check if length is within valid range
    if generate_type == "password" and (length < 4 or length > 32):
        return jsonify({"error": "Password length must be between 4 and 32 characters"}), 400
    if generate_type == "pin" and (length < 4 or length > 10):
        return jsonify({"error": "PIN length must be between 4 and 10 digits"}), 400

    # Password-specific validation
    if generate_type == "password":
        use_numbers = data.get("numbers")
        use_special = data.get("special")

        if not use_numbers and not use_special:
            return jsonify({"error": "At least one option (Numbers or Special Characters) must be selected for passwords"}), 400

        generated_value = generate_password(length, use_numbers, use_special)
    else:
        generated_value = generate_pin(length)

    return jsonify({"generated_value": generated_value})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
