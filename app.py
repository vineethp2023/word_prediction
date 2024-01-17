from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "World"  # Example data to pass to the template
    return render_template('index.html', name=name)

@app.route('/predict-word', methods=['POST'])
def predict_word():
    data = request.json
    incomplete_word = data.get('word')
    number_of_chars = int(data.get('number_of_chars'))

    # Load a word list or dictionary
    with open('english_words.txt', 'r') as f:
        words = set(word.strip() for word in f)

    # Filter matching words based on length and missing letters
    matching_words = set(word for word in words if len(word) == number_of_chars)
    for i, char in enumerate(incomplete_word):
        if char != ' ':
            matching_words = {word for word in matching_words if word[i] == char}

    # Find a suitable word from the filtered set
    result = 'invalid'  # Default if no valid word is found
    if matching_words:
        result = next(iter(matching_words))  # Pick any valid word

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
