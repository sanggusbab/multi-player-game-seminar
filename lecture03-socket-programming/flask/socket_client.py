import requests

def get_translation(word):
    base_url = "http://163.152.174.97:5000/translate"  # 서버의 IP 주소를 여기에 입력하세요
    response = requests.get(f"{base_url}/{word}")  # 요청 파라미터를 URL 경로에 추가
    if response.status_code == 200:
        data = response.json()
        return data["translation"]  # 서버 응답의 키를 "translation"으로 수정
    else:
        return "Error: Word not found."

if __name__ == "__main__":
    while True:
        user_input = input("단어를 입력하세요 (종료하려면 'exit'를 입력하세요): ")
        if user_input.lower() == "exit":
            break
        translation = get_translation(user_input)
        print(f"{user_input}의 번역: {translation}")
