from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('question1.html')

@app.route('/question2', methods=['POST'])
def question2():
    if request.form.get('answer') == 'no':
        return redirect(url_for('question2_page'))
    return redirect(url_for('question2_page'))

@app.route('/question2_page')
def question2_page():
    return render_template('question2.html')

@app.route('/question3', methods=['POST'])
def question3():
    if request.form.get('answer') == 'no':
        return redirect(url_for('deportation_risk'))
    return redirect(url_for('question3_page'))

@app.route('/question3_page')
def question3_page():
    return render_template('question3.html')

@app.route('/process_final', methods=['POST'])
def process_final():
    if request.form.get('answer') == 'yes':
        return redirect(url_for('no_risk'))
    return redirect(url_for('deportation_risk'))

@app.route('/deportation_risk')
def deportation_risk():
    return render_template('yes_risk.html')

@app.route('/no_risk')
def no_risk():
    return render_template('no_risk.html')

if __name__ == '__main__':
    app.run(debug=True)
