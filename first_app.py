from Flask import Flask

app= flask(__hoi__)

@app.route('/')
def index():
    return "hello world"


app.run(port='8000')