from flask import Flask , render_template,request
# フラスク使いますよ～
app = Flask(__name__)
# フラスクの機能をつかうのにFlask(__name__)
# appにまとめよう(appが使われてるところ大事)

@app.route("/")
def index():
    # returnの後ろが表示される
    return "こんにちはフラスコ"

# （）内のURLにアクセスがあったら動く
@app.route('/user/<username>')
def show_user_profile(username):

    # username は URL の <username> 部分に入る値が渡される
    return f"Hello, {username}!"  # 例: /user/Alice にアクセスすると "Hello, Alice!" を表示

# <変数>は基本的に文字列
# <変数>を数字として扱いたい場合は:intを使う
@app.route("/test/<int:num>")
def test_num(num):
    print( type(num) )
    return f"あなたの入力した文字は{num}です"

# ----
# AssertionError
# @app.route('/hello/')
# def hello():
#     return "hello!!"


@app.route('/hello/')
def hello():
    # render_template を使ってテンプレートをレンダリング
    # Pythonのデータをテンプレートに渡すこともできる\
    # hello.htmlにnameというデータを渡してる
    return render_template('hello.html', name="Flask Beginner")  # name に動的データを渡す

# GETメソッドでのルーティング：フォームを表示
@app.route("/login", methods=["GET"])
def login_get():
    py_name = "ゲスト"  # 初期状態ではゲスト表示
    # フォームを含むlogin.htmlを表示
    return render_template("login.html", name=py_name)


# POSTメソッドでのルーティング：フォームデータを処理
@app.route("/login", methods=["POST"])
def login_post():
    error = None  # エラーメッセージの初期値
    username = request.form.get("username")  # フォームからユーザー名取得
    password = request.form.get("password")  # フォームからパスワード取得

    # ダミーのログイン検証処理
    if username == "admin" and password == "password123":
        return f"ようこそ、{username}さん！"  # ログイン成功時のメッセージ
    else:
        error = "ユーザー名またはパスワードが間違っています"
        # エラーとともに再度フォームを表示
        return render_template("login.html", error=error, name="ゲスト")


if __name__ == "__main__" :
    app.run(debug=True)
    # フラスコを動かしますよ