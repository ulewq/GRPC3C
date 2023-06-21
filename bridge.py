import grpc
import asyncio

import streaming_pb2 as pb2
import streaming_pb2_grpc as pb2_grpc


class Bridge(pb2_grpc.StreamServerServicer):
    def __init__(self, target_server):
        self.target_server = target_server

    async def Streaming(self, request_iterator, context):
        async for request in request_iterator:
            # Forward request to the target server
            async for response in self.target_server.Streaming(iter([request])):
                # Forward response to the client
                yield response


async def serve():
    target_channel = grpc.aio.insecure_channel("localhost:50052")
    target_stub = pb2_grpc.StreamServerStub(target_channel)
    bridge_server = grpc.aio.server()
    pb2_grpc.add_StreamServerServicer_to_server(
        Bridge(target_stub), bridge_server
    )
    bridge_server.add_insecure_port("[::]:50051")
    await bridge_server.start()
    print("Bridge server started")
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        await bridge_server.stop(0)


if __name__ == "__main__":
    asyncio.run(serve())