import time
import grpc
import asyncio
import logging

import streaming_pb2 as pb2
import streaming_pb2_grpc as pb2_grpc


class TargetServer(pb2_grpc.StreamServerServicer):
    async def Streaming(self, request_iterator, context):
        async for request in request_iterator:
            print("Received request: ", request)
            # Process the request and generate responses
            response = pb2.StreamingResponse()
            response.call_info.session_id = "456"
            response.call_info.media = "video"
            yield response
            await asyncio.sleep(1)


async def serve():
    server = grpc.aio.server()
    pb2_grpc.add_StreamServerServicer_to_server(TargetServer(), server)
    server.add_insecure_port("[::]:50052")
    await server.start()
    print("Target server started")
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        await server.stop(0)

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.StreamServerStub(channel)
        
        # Create streaming request
        request = pb2.StreamingRequest()
        request.ip_address = "127.0.0.1"
        request.port = "50052"
        
        # Perform streaming call
        responses = stub.Streaming(iter([request]))
        
        for response in responses:
            if response.HasField("call_info"):
                call_info = response.call_info
                print("Received call info:")
                print("Session ID:", call_info.session_id)
                print("Media:", call_info.media)
            elif response.HasField("call_state"):
                call_state = response.call_state
                print("Received call state:")
                print("State:", call_state.state)
                if call_state.state == pb2.ServerState.CONNECTED:
                    print("CONNECTED")
                    # Perform some actions when call is connected
                    pass
                elif call_state.state == pb2.ServerState.STREAMING:
                    print("STREAMING")
                    # Perform some actions when call is streaming
                    pass
                elif call_state.state == pb2.ServerState.ENDED:
                    PRINT("ENDED")
                    # Perform some actions when call is ended
                    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
