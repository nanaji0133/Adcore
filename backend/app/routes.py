from flask import request, jsonify
from . import app, mongo
from bson.objectid import ObjectId

# Route to get courses with pagination and search
@app.route('/api/courses', methods=['GET'])
def get_courses():
    search = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    query = {"$or": [
        {"university": {"$regex": search, "$options": "i"}},
        {"city": {"$regex": search, "$options": "i"}},
        {"country": {"$regex": search, "$options": "i"}},
        {"course_name": {"$regex": search, "$options": "i"}},
        {"course_description": {"$regex": search, "$options": "i"}}
    ]} if search else {}

    courses = mongo.db.courses.find(query).skip((page - 1) * per_page).limit(per_page)
    return jsonify([course for course in courses])


# Route to get a specific course by ID
@app.route('/api/courses/<id>', methods=['GET'])
def get_course(id):
    course = mongo.db.courses.find_one({"_id": ObjectId(id)})
    if course:
        course['_id'] = str(course['_id'])
        return jsonify(course)
    else:
        return jsonify({"error": "Course not found"}), 404

# Route to create a new course
@app.route('/api/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    result = mongo.db.courses.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)}), 201

# Route to update a course
@app.route('/api/courses/<id>', methods=['PUT'])
def update_course(id):
    data = request.get_json()
    result = mongo.db.courses.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"success": result.modified_count > 0})

# Route to delete a course
@app.route('/api/courses/<id>', methods=['DELETE'])
def delete_course(id):
    result = mongo.db.courses.delete_one({"_id": ObjectId(id)})
    return jsonify({"success": result.deleted_count > 0})
