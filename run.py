from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    
# The create_app function is imported from the app package. 