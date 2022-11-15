from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def flaskproject():
    return """<xmp>
              Task : Setting up application enviroinment / create flask project
              flask project run successfully
              </xmp>"""