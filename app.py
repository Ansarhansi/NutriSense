from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_ingredient(data):
    # Basic example logic — you can customize as needed
    calories = float(data.get('calories', 0))
    fat = float(data.get('fat', 0))
    fiber = float(data.get('fiber', 0))
    sugar = float(data.get('sugar', 0))

    result = "Neutral"
    reason = ""

    if calories > 500 or fat > 20 or sugar > 30:
        result = "Harmful"
        reason = "High calories/fat/sugar content"
    elif fiber >= 5:
        result = "Beneficial"
        reason = "Good fiber content"
    else:
        reason = "Moderate nutrition values"

    return result, reason

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis = None
    if request.method == 'POST':
        # Collect form data
        data = {
            'calories': request.form.get('calories', 0),
            'protein': request.form.get('protein', 0),
            'carbohydrates': request.form.get('carbohydrates', 0),
            'fat': request.form.get('fat', 0),
            'fiber': request.form.get('fiber', 0),
            'sugar': request.form.get('sugar', 0),
            'sodium': request.form.get('sodium', 0),
            'cholesterol': request.form.get('cholesterol', 0)
        }
        # Analyze nutrition data
        analysis = analyze_ingredient(data)
    return render_template('index.html', analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
