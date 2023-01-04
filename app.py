import flask
app = flask.Flask(__name__)
@app.route('/')
def show_map():
    return flask.render_template('map.html')
if __name__ == '__main__':
    app.run(debug=True)

