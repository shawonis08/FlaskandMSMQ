from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
app = Flask( __name__ )


@app.route( '/' )
def hello_world():
    return 'Hello World!'


# @app.route("/upload", methods=["POST", "GET"])
# def upload():
#     if request.method == "POST":
#         save_file = request.files["file"]
#         save_file_name = secure_filename(save_file.filename)
#         save_file.save(save_file_name)
#         return jsonify("file save to queue"), 200
#     else:
#         return jsonify("Request method error"), 200


if __name__ == '__main__':
    app.run()
