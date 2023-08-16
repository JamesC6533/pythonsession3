from flask import Flask, Response, request, url_for


app = Flask(__name__)
results = []

@app.route('/')
def hello_from_flask():
    return "Hello from Flask"


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object",mimetype='text/plain')


@app.route('/post/text',methods=['POST'])
def post_text():
    data_sent=request.data.decode('utf-8')
    return Response("You posted this data to flask app:"+data_sent,mimetype="text/plain")


@app.route('/dynamic/<word>')
def home(word):
    return word


@app.route('/square/<int:number>')
def square(number):
    squared = number**2
    line = "Your number squared is"+"  "+str(squared)
    return line


@app.route('/operation/<int:number1>/<int:number2>/<operator>')
def arithmetic(number1,number2,operator):
    result = 0
    if operator == '*':
        result = number1 * number2
    elif operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '/':
        result = number1 / number2

    return str(result)


@app.route('/hello/<name>')
def say_hello(name):
    return """
     <html>
     <head>
     <title>Sample - Flask routes</title>
     </head>
     <body>
      <h1>Name page</h1>
      <p>Hello{}!</p>
    </body>
     </html>
    """.format(name)


@app.route('/hello/<name>/<int:age>')
def say_hello2(name,age):
    return """
     <html>
     <head>
     <title>Sample - Flask routes</title>
     </head>
     <body>
      <h1>Name page</h1>
      <p>Hello{}!</p>
      <p>You are {} year(s)old</p>
    </body>
     </html>
    """.format(name,age)


@app.route('/list/<data>')
def add_to_list(data):
    results.append(data)
    return """
     <html>
     <head>
     <title>Sample - Flask routes</title>
      <head>
      <body>
        <section class="footer">
            <h4>About Us</h4>
            <p>{}</p>
            <p>More and more and more and more example text, if you don't want to put anything meanungful into a paragraph 
            just waffle abosolute nonsense to fill the space.</p>
            <div class="icons">
                <i class="fa fa-facebook"></i>
                <i class="fa fa-twitter"></i>
                <i class="fa fa-instagram"></i>
                <i class="fa fa-linkedin"></i>
            </div>
            <p>Made with <i class="fa fa-heart-o"></i> by Monty Python</p>
        </section>
      <body>
      <head>
    """.format(str(results[0]))


@app.route('/list/<data>')
def add_to_list2(data):
    results.append(data)
    return """
     <html>
     <head>
     <title>Sample - Flask routes</title>
      <head>
      <body>
        <section class="footer">
            <h4>About Us</h4>
            <p>{}</p>
            <p>More and more and more and more example text, if you don't want to put anything meanungful into a paragraph 
            just waffle abosolute nonsense to fill the space.</p>
            <div class="icons">
                <i class="fa fa-facebook"></i>
                <i class="fa fa-twitter"></i>
                <i class="fa fa-instagram"></i>
                <i class="fa fa-linkedin"></i>
            </div>
            <p>Made with <i class="fa fa-heart-o"></i> by Monty Python</p>
        </section>
      <body>
      <head>
    """.format(str(results[1]))



@app.route('/view')
def return_results():
    return results


if __name__=="__main__":
    app.run()


