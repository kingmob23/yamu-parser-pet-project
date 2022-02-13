from flask import Flask, request, jsonify
import yamuparser
app = Flask(__name__)


@app.route('/links', methods=['POST'])
def new_user():
    link_b = request.get_data()
    link = link_b.decode()
    tracks = yamuparser.yamuparser(link)
    return jsonify(tracks)


if __name__ == '__main__':
    app.run()
