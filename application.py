from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/signup")
def index():
    return render_template("index.html")

@app.route("/users", methods=["GET", "POST"])
def users():
    name = request.form.get("name")
    if len(name) < 6:
        e = 'Имя короче 6 символов'
        return e
    email = request.form.get("email")
    if not('@') in email:
        e = "Email неверный"    
        return e       
    password = request.form.get("password")
    if len(password) < 8:
        e = 'Пароль содержит меньше 8 символов'
        return e
    confirm_password = request.form.get("confirm_password")        
    if password != confirm_password:
        e = 'Пароли не совпадают!'
        return e      
    return render_template("users.html", name=name, email=email, password=password)


if __name__ == '__main__':
    app.run(debug=True)