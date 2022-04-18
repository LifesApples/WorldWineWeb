from website import create_app

# funktionen create_app som ligger i __init__.py körs. 
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)