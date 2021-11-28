

import grpc
import alerts_pb2
import alerts_pb2_grpc

def alert(camera_id):
    print("Start service")
    try:
      channel = grpc.insecure_channel('0.0.0.0:3000')
      stub = alerts_pb2_grpc.AlertingStub(channel)
      alertRequest = alerts_pb2.AlertRequest(cameraId=camera_id)
      alertResponse = stub.Alert(alertRequest)

      print("--------------", alertResponse)

      return alertResponse.alerted
    
    except Exception as e:
      print(e)
      return e
