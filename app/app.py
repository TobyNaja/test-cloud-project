from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Prodpai Cloud Demo"

@app.route('/health')
def health_check():
    return {"status": "healthy"}, 200

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return subprocess.check_output("ping -c1 " + host, shell=True).decode()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) # nosemgrep
