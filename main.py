from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Welcome to Vehicle Parking App'
