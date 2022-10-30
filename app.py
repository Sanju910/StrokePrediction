from flask import Flask, render_template
from api_routes import bp1

app = Flask(__name__)

app.register_blueprint(bp1)

@app.route('/')
def index():
    return render_template('base2.html')

if __name__ == "__main__":
    app.run(debug=False)
