#socket_server.py
from flask import Flask, Response
import json

app = Flask(__name__)

# 간단한 사전 데이터를 생성합니다.
translations = {
    "apple": "사과",
    "banana": "바나나",
    "cat": "고양이",
    "orange": "오렌지",
    # 추가적인 번역 데이터를 여기에 추가할 수 있습니다.
}

@app.route('/translate/<word>', methods=['GET'])
def translate_word(word):
    translation = translations.get(word, "번역을 찾을 수 없습니다.")
    
    response_data = {
        "word": word,
        "translation": translation
    }
    
    response = Response(json.dumps(response_data, ensure_ascii=False), content_type='application/json; charset=utf-8')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
