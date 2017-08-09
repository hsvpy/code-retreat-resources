from bottle import run, get, post, static_file, request

examples = []

@post("/example")
def post_example():
    examples.append(request.json)

@get("/example")
def get_example():
    return {"examples": examples}

@get("/")
def home():
    return route_static("index.html")


@get("/<path:path>")
def route_static(path):
    return static_file(path, root="static")

run(host="0.0.0.0", port=8080)
