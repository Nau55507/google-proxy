from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    # URLパラメータから目的地を取得
    url = request.args.get('url')
    if not url:
        return "URLを指定してください (例: /proxy?url=https://www.google.com)"
    
    # 指定されたサイトへ代わりにアクセス
    res = requests.get(url)
    
    # 取得したデータをそのままブラウザに返す
    return Response(res.content, content_type=res.headers['Content-Type'])

if __name__ == "__main__":
    app.run()
