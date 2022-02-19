from flask import Flask, render_template

app = Flask (__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pitagoras')
def pitagoras():
    return render_template('pitagoras.html')

@app.route('/squareroot')
def squareroot():
    return render_template('squareroot.html')


@app.route('/convert_number')
def convert():
    return render_template('convert_number.html')

if __name__ == '__main__':

    app.run()

    