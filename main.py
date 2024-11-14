from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')

@app.route('/templates/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        if request.form.get('born_in_us') == 'no':
            return redirect(url_for('results_yes'))
        return render_template('question2.html')
    return render_template('question2.html')

@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        if request.form.get('us_citizen') == 'no':
            return redirect(url_for('results_yes'))
        return render_template('question3.html')
    return render_template('question3.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        if request.form.get('parents_citizens') == 'no':
            return redirect(url_for('results_yes'))
        return redirect(url_for('results_no'))
    return redirect(url_for('start'))

@app.route('/results_yes', methods=['GET'])
def results_yes():
    return render_template('results_yes.html')

@app.route('/results_no', methods=['GET'])
def results_no():
    return render_template('results_no.html')

if __name__ == '__main__':
    app.run(debug=True)
