from flask import Flask, render_template, request, jsonify
from business import business_object_miniatures as bus


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/data', methods=['GET'])
def get_data():
    field = request.args.get('field')
    value = request.args.get('value')
    page = request.args.get('page')

    data = bus.get_miniature_bo(field=field, value=value)

    return jsonify(data[page])


if __name__ == '__main__':
    app.run(debug=True)
