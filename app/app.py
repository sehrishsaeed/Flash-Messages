from flask import Flask, redirect, url_for, request, render_template, flash
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods = ['GET','POST'])
def calc():
    new_csv=[]
    try:
        with open('history.csv', 'r') as reader:
            csv = reader.read().split('\n')
        for line in csv:
            new_csv.append(line.split(','))
    except Exception as e:
        print(e)
    if request.method == 'GET':
        return render_template('calculator.html', left='1', middle='+', right='1', res='2', csv=reversed(new_csv))

    left, middle, right = request.form['left'], request.form['middle'], request.form['right']
    res = ''
    if not left or not right:
        flash("Missing Value")
        return render_template('calculator.html', left='1', middle='+', right='1', res='2', csv=reversed(new_csv))

    if middle == '+':
        res = str(float(left) + float(right))
    elif middle == '-':
        res = str(float(left) - float(right))
    else:
        flash("Not Supported OP")
        return render_template('calculator.html',left='1', middle='+', right='1', res='2',csv=reversed(new_csv))

    with open('history.csv', 'a+') as writer:
        line = f'{left},{middle},{right},{res}\n'
        writer.write(line)
    with open('history.csv', 'r') as reader:
        csv = reader.read().split('\n')
    new_csv=[]
    for line in csv:
        new_csv.append(line.split(','))
    return render_template('calculator.html', left=left, middle=middle, right=right, res=res, csv=reversed(new_csv))

if __name__ == '__main__':
   app.run(debug = True)