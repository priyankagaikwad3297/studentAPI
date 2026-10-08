import requests
from flask import Flask, request, jsonify
app = Flask(__name__)
students=[]

#GET API
@app.route("/students", methods=['GET'])
def get_students():
    return jsonify(students)

#POST API
@app.route("/students", methods=['POST'])
def add_student():
    student=request.json
    students.append(student)
    return jsonify({
        "message": "Student added successfully",
    })

@app.route("/students/<int:id>", methods=['PUT'])
def update_student(id):

    for student in students:

        if student["id"] == id:

            student["Name"] = request.json["Name"]
            student["Course"] = request.json["Course"]
            return jsonify({
                "message": "Student updated successfully",
                "student": student
          })
        return jsonify({"message": "Student not found"}),404

@app.route("/students/<int:id>", methods=['DELETE'])
def delete_student(id):
    for student in students:

        if student["Id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)

    #NOTE : Inside url write: http://127.0.0.1:5000/students