from app import create_app

# 1. Trigger the factory function from File 7 to build the engine
app = create_app()

# 2. Turn the engine on!
if __name__ == "__main__":
    app.run(debug=True, port=5000)