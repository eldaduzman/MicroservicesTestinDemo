from pprint import pprint

from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import requests

"""
This is a mock up for the users
Using flask WSGI it listens to port 80. 
"""

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}, r"/score/*": {"origins": "*"}})


@app.route("/")
def index():
    """
    this function is on the root path of the users service.
    :return: html hello world string
    """
    return "<h1>Hello world - Users</h1>"


@app.route("/activity/time/average/<user_id>", methods=['GET'])
def get_average_activity_time(user_id):
    """

    :param user_id: id of user, being sent to pets service
    :return: json object with a float number, the average activity time calculated from the response given by pets service
    """
    response = requests.get(url="http://service-pets:8080/all/activities/"+user_id)  # sends a request to pets service
    json = response.json()
    activities_array = json['activity_times']
    pprint(activities_array)
    avg = 0
    for activity_items in activities_array:
        activity_time = activity_items['activity_time']
        avg = avg+activity_time
    avg = round(avg/len(activities_array), 2)
    return jsonify({"avg_time": avg}), 200


if __name__ == "__main__":
    """
    runs flask service
    """
    app.run(host="0.0.0.0", port=80, debug=True)
