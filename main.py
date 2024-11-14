from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/question2', methods=['POST'])
def question2():
    if request.form.get('born_in_us'):
        return render_template('question2.html')
    return redirect(url_for('results_yes'))

@app.route('/question3', methods=['POST'])
def question3():
    if request.form.get('us_citizen') == 'no':
        return redirect(url_for('results_yes'))
    return render_template('question3.html')

@app.route('/results', methods=['POST'])
def results():
    if request.form.get('parents_citizens') == 'no':
        return redirect(url_for('results_yes'))
    return redirect(url_for('results_no'))

@app.route('/results_yes')
def results_yes():
    return render_template('results_yes.html')

@app.route('/results_no')
def results_no():
    return render_template('results_no.html')

if __name__ == '__main__':
    app.run(debug=True)
