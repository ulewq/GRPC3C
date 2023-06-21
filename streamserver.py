import time
import grpc
import asyncio

import streaming_pb2 as pb2
import streaming_pb2_grpc as pb2_grpc


class StreamServer(pb2_grpc.StreamServerServicer):
    async def Streaming(self, request_iterator, context):
        async for request in request_iterator:
            print("Received request: ", request)
            # Process the request and generate responses
            response = pb2.StreamingResponse()
            response.call_info.session_id = "123"
            response.call_info.media = "audio"
            yield response
            await asyncio.sleep(1)


async def serve():
    server = grpc.aio.server()
    pb2_grpc.add_StreamServerServicer_to_server(StreamServer(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    print("Server started")
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        await server.stop(0)


if __name__ == "__main__":
    asyncio.run(serve())
