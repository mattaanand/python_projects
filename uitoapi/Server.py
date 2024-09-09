from flask import Flask, request, jsonify, render_template

companies = "Login"

api = Flask(__name__, template_folder='template', static_folder='static', static_url_path='')

@api.route('/')
def home():
   return render_template('index.html')

def vaidate_user(uname, pwd):
    print("in validate_user")
    if "Anand" == uname and "pass" == pwd:
        return True
    else:
        return False


@api.route('/login', methods=['POST'])
def login():
    print("in login")
    if vaidate_user(request.form.get('uname'), request.form.get('pwd')):
        return jsonify({"status": 201,
                    "reason": "Login success"})
    else:
        return jsonify({"status": 401, "reason": "Wrong username or password"})



if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8000, debug=True)