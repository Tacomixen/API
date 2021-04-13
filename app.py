from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_cors import CORS

import os

import sqlite3
from sqlite3 import Error

import pymysql.cursors

app = Flask(__name__)
CORS(app)

#DB_PORT = os.getenv('DB_PORT')
#DB_HOST = os.getenv('DB_HOST')
#DB_NAME = os.getenv('DB_NAME')

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__



def create_db():

    print("Db created.")



def create_table(conn, create_table_sql):
    print("table created.")

def populate_initial_sensors(conn):
    initial_sensors = [
        {
            'id': 1,
            'name': u'Motion sensor 1',
            'description': u'IR motion sensor in location x.', 
            'active': 1
        },
        {
            'id': 2,
            'name': u'Accelerometer X',
            'description': u'X-axis accelerometer.', 
            'active': 0
        },
        {
            'id': 3,
            'name': u'Accelerometer Y',
            'description': u'Y-axis accelerometer.', 
            'active': 0
        }
    ]

    try:

        for initial_sensor in initial_sensors:

            print("Populating initial data.")

    except Error as e:
        print(e)

# -- CRUD --
# Create
# Read
# Update
# Delete
# -- CRUD --

# Create a sensor
@app.route('/api/v1/sensors', methods=['POST'])
def create_sensor():
    if not request.json or not 'name' in request.json:
        abort(400)

    sensor = dotdict({})
    sensor.name = request.json['name']
    sensor.description = request.json.get('description', "")
    sensor.active = request.json['active']

    # CREATE

    data = (sensor.name, sensor.description, sensor.active)
    
    # TODO: Get last id.
    print(f"Sensor: {sensor}")

    return jsonify({'sensor': sensor}), 201

# Read all sensors
@app.route('/api/v1/sensors', methods=['GET'])
def get_sensors():

    # GET ALL SENSORS

    # TODO: Get all sensors from db.
    json_sensors = []

    #for sensor in db_sensors:
    #    sensor = dotdict(sensor)
#
    #    json_sensors.append(sensor)
    return jsonify({'sensors': json_sensors})

# Read a sensor
@app.route('/api/v1/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):

    # TODO: Get the sensor from db.
    #json_sensor = dotdict(db_sensor)
#
    #if len(db_sensor) == 0:
    #    abort(404)

    # GET A SENSOR
    #return jsonify({'sensor': json_sensor})
    return jsonify({'result': True})

# Update a sensor
@app.route('/api/v1/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):


    # TODO: Get sensor then update it.
    #db_sensor = cur.fetchone()
    #db_sensor = dotdict(db_sensor)
#
    #new_sensor = dotdict(db_sensor)
#
    #if (db_sensor.name != request.json.get('name') and request.json.get('name')):
    #    new_sensor.name = request.json.get('name')
    #if (db_sensor.description != request.json.get('description') and request.json.get('description')):
    #    new_sensor.description = request.json.get('description')
    #if (db_sensor.active != request.json.get('active') and (request.json.get('active') == 1 or request.json.get('active') == 0)):
    #    new_sensor.active = request.json.get('active')
    #
    #sql = ''' UPDATE sensors SET id = %s, name = %s, description = %s, active = %s WHERE id = %s'''
#
    #data = (sensor_id, new_sensor.name, new_sensor.description, new_sensor.active, sensor_id)
    #
    #cur.execute(sql, data)
    #conn.commit()

    #return jsonify({'sensor': new_sensor})
    return({'result': True})

# Delete a sensor
@app.route('/api/v1/sensors/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    # DELETE
    #conn = create_connection()
    #cur = conn.cursor()
#
    #cur.execute(f"DELETE FROM sensors WHERE id={sensor_id}")
    #conn.commit()

    #return jsonify({'result': True})
    return({'result': True})

# Error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    create_db()
    app.run(host='0.0.0.0', port=8080, debug=True)