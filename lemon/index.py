from lemon.application import app

@app.route('/')
def index():
    return 'Welcome to lemon chat server!'