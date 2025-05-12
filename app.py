from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return       "Name: Rodrigo Araoarao\n, Section: BSIT-III-\n, Subject: System Integration\n,\nSemi -Final Exam"




if __name__ == '__main__':
 port = int(os.environ.get("PORT", 0000))
 app.run(debug=True, host='0,0,0,0',port=port)

# if __name__ == 'main':
#  app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
