from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Dummy users (in a real app, use a database)
users = {'admin': 'password'}

# Dummy movie data
movies = [
    {'title': 'Inception', 'rating': '8.8', 'logo': 'https://via.placeholder.com/50x75'},
    {'title': 'The Dark Knight', 'rating': '9.0', 'logo': 'https://via.placeholder.com/50x75'},
    # Add more movies here
]

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if users.get(username) == password:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@app.route('/movies')
def movie_list():
    return render_template('movies.html', movies=movies)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
