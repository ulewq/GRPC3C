# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import streaming_pb2 as streaming__pb2


class StreamServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Streaming = channel.stream_stream(
                '/grpc.testing.StreamServer/Streaming',
                request_serializer=streaming__pb2.StreamingRequest.SerializeToString,
                response_deserializer=streaming__pb2.StreamingResponse.FromString,
                )


class StreamServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Streaming(self, request_iterator, context):
        """Makes a phone call and communicate states via a stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Streaming': grpc.stream_stream_rpc_method_handler(
                    servicer.Streaming,
                    request_deserializer=streaming__pb2.StreamingRequest.FromString,
                    response_serializer=streaming__pb2.StreamingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.testing.StreamServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Streaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/grpc.testing.StreamServer/Streaming',
            streaming__pb2.StreamingRequest.SerializeToString,
            streaming__pb2.StreamingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
