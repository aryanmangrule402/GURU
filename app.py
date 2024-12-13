from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Main content page

@app.route('/home')
def loading():
    return render_template('home.html')  # Loading animation page

@app.route('/adhyay14')
def adhyay14():
    return render_template('adhyay14.html')

@app.route('/adhyay18')
def adhyay18():
    return render_template('adhyay18.html')

if __name__ == '__main__':
    app.run(debug=True)
