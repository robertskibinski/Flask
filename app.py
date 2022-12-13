from flask import Flask, request, redirect, render_template
app = Flask(__name__)


@app.route('/me')
def my():
    return render_template('name.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        print("We received GET")
        return render_template("form.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")


if __name__ == '__main__':
    app.debug = True
    app.run()
