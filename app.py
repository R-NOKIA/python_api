from flask import Flask, request, jsonify, make_response
import novel_list
import json
app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get_resource/novel', methods={"POST", "GET"})
def test():
        novel_name = request.values.get('novel_name')
        novel = novel_list.GetNovel()
        novel_dict = novel.search_novel(novel_name)
        return jsonify(novel_dict)


@app.errorhandler(500)
def errcode_500(error):
    return make_response(jsonify({"error_msg": "参数错误", "error_code": 500}), 500)


@app.errorhandler(404)
def errcode_404(error):
    return make_response(jsonify({"error_msg": "路径错误或api不存在", "error_code": 404}))


if __name__ == '__main__':
    app.run(debug=True)