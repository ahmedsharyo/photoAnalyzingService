
from flask import Flask
from flask import jsonify

app = Flask(__name__)

import grpc
import alerts_pb2
import alerts_pb2_grpc

def obj_to_dict(obj):
    return obj.__dict__

@app.route('/<alert>')
def alert(alert):
    print("Start service")
    try:
      channel = grpc.insecure_channel('0.0.0.0:3000')
      stub = alerts_pb2_grpc.AlertingStub(channel)
      alertRequest = alerts_pb2.AlertRequest(cameraId=alert)
      alertResponse = stub.Alert(alertRequest)

      print("--------------", alertResponse)

      return jsonify({
          "alerted": alertResponse.alerted
      })
    except Exception as e:
      print(e)
      return e

if __name__ == '__main__':
    app.run()
   
    