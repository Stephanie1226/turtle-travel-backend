import os
from json import dumps
from flask import Flask, Response, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def turn_counterclockwise(direction): #L
  if direction == "North":
    return "West"
  elif direction == "West":
    return "South"
  elif direction == "South":
    return "East"
  else: #direction == "East"
    return "North"

def turn_clockwise(direction): #R
  if direction == "North":
    return "East"
  elif direction == "East":
    return "South"
  elif direction == "South":
    return "West"
  else:  #direction == "West"
    return "North"

def move_forward(x, y, direction, coor_data): #F

  def update_data(x, y):
    location = {}
    location.update([('x', x) , ('y', y)])
    coor_data.append(location)
    return coor_data

  if direction == "North":
    y += 1
    return x, y, update_data(x, y)
  elif direction == "East":
    x += 1
    return x, y, update_data(x, y) 
  elif direction == "South":
    y -= 1
    return x, y, update_data(x, y)
  else:  #direction == "West"
    x -= 1
    return x, y, update_data(x, y)


@app.route('/calculateroute', methods=['POST'])
def calculate_route():
  data = request.get_json()
  direction = "North"
  x_loc = 0
  y_loc = 0
  coordinate_data = [{'x': x_loc, 'y': y_loc}]

  for element in data:
    if element == "L":
      direction = turn_counterclockwise(direction)
    elif element == "R":
      direction = turn_clockwise(direction)
    else: # element == "F"
      x_loc, y_loc, coordinate_data = move_forward(x_loc, y_loc, direction, coordinate_data)

  return Response(dumps(coordinate_data), mimetype="application/json")


#if __name__ == '__main__':
#  app.run(port=5000)