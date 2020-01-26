from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import random
import uuid


"""
This is a mock up for the pets
Using flask WSGI it listens to port 8080. 
"""


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}, r"/score/*": {"origins": "*"}})


@app.route("/")
def index():
    """
    this function is on the root path of the pets service.
    :return: html hello world string
    """
    return "<h1>Hello world - Pets</h1>"


@app.route("/all/activities/<user_id>", methods=['GET'])
def get_average_activity_time(user_id):
    """
    this function retrieves a collection of all activity times of all dogs

    :param user_id: id of user (currently not in use)
    :return: json object of activity times of all dogs.
    dog id is a uuit string and activity time is an integer
    """
    number_of_dogs = random.randint(1, 8)

    activity_times = list()
    for i in range(number_of_dogs):
        current_dog_id = str(uuid.uuid1())
        # current_activity_time = random.randint(0, 200)

        if i % 2 == 0:
            current_activity_time = random.randint(0, 200)
        else:
            current_activity_time = None
        this_dict = dict()
        this_dict["dog_id"] = current_dog_id
        this_dict["activity_time"] = current_activity_time
        activity_times.append(this_dict)

    return jsonify({"activity_times": activity_times}), 200


if __name__ == "__main__":
    """
    runs flask service
    """
    app.run(host="0.0.0.0", port=8080, debug=True)