from flask import Flask, request, jsonify

from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)

@app.route("/v1", method = ['POST']) # 경로 api
def convert_doc():
    data = request.get_json()

    if 'image' not in data:
        return "", 400
    
    doc_img_data = data
    #doc_img_data = () # 이미지 스캔화

    return doc_img_data, 200

@app.route("/", method = ['GET', 'POST'])
def index():
    print("check")
    return "<h1>check page</h1>"

if __name__ == "__main__":
    # https://stackoverflow.com/questions/63765727/unhandled-exception-connection-closed-while-receiving-data
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(threaded=True, host='0.0.0.0', port=5000)