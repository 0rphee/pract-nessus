from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# HTML template for the single-page app
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Search Page</title>
</head>
<body>
    <h1>Search for a Name</h1>
    <form method="GET">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Search</button>
    </form>

    {% if results %}
        <h2>Search Results:</h2>
        <ul>
            {% for result in results %}
                <li>{{ result }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
'''

def query_database(search_name):
    """Function to query the SQLite database by name."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE name LIKE ?", (f"%{search_name}%",))
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    return results

@app.route('/', methods=['GET'])
def search():
    search_name = request.args.get('name')
    results = query_database(search_name) if search_name else []
    return render_template_string(html_template, results=results)

if __name__ == '__main__':
    app.run(debug=True)
