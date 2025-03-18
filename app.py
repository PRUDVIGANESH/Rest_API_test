from flask import Flask, jsonify

app = Flask(__name__)  # Correct Flask app initialization

students = [
    {
        'id': 1,
        'student_name': 'std1',
        'age': 20,
        'email': 'higuys23@gmail.com'
    },
    {
        'id': 2,
        'student_name': 'std2',
        'age': 23,
        'email': 'hello3@gmail.com'
    },
    {
        'id': 3,
        'student_name': 'std3',
        'age': 25,
        'email': 'higuys2@gmail.com'
    }
]

# Route to get the list of students
@app.route('/students_list')
def students_list():
    return jsonify(students)

# Route to get a student by ID
@app.route('/student/get/<int:id>')
def student_get_by_id(id):
    for std in students:
        if std['id'] == id:
            return jsonify(std)
    return jsonify({"error": "ID not found"}), 404  # Return JSON response with a 404 status

# Route to fetch students list from an external API
@app.route('/students-list/rest-api')
def student_list_rest_api():
    url = "https://restapi-test-xmj2.onrender.com/students_list"
    response = requests.get(url)  # Use .get() instead of .request("GET", url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
