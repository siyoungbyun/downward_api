#!/usr/local/bin/python3

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # container_name = ""
    pod_name = os.environ.get("POD_NAME", "Unknown")
    node_name = os.environ.get("NODE_NAME", "Unknown")
    namespace = os.environ.get("POD_NAMESPACE", "Unknown")
    template = f"Container EDU | POD Working : {pod_name} | nodename : {node_name} | namespace : {namespace}"
    return template


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")