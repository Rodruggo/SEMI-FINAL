from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "Name: Rodrigo Araoarao\n"
        "Section: BSIT-III-\n"
        "Subject: System Integration\n"
        "\nSemi -Final Exam"

    )

if __name__ == '__main__':
    app.run(debug=True)
