# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import srv6_explicit_path_pb2 as srv6__explicit__path__pb2


class SRv6ExplicitPathStub(object):
  """Define the rpc service interface
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/srv6_explicit_path.SRv6ExplicitPath/Create',
        request_serializer=srv6__explicit__path__pb2.SRv6EPRequest.SerializeToString,
        response_deserializer=srv6__explicit__path__pb2.SRv6EPReply.FromString,
        )
    self.Remove = channel.unary_unary(
        '/srv6_explicit_path.SRv6ExplicitPath/Remove',
        request_serializer=srv6__explicit__path__pb2.SRv6EPRequest.SerializeToString,
        response_deserializer=srv6__explicit__path__pb2.SRv6EPReply.FromString,
        )


class SRv6ExplicitPathServicer(object):
  """Define the rpc service interface
  """

  def Create(self, request, context):
    """Create operation
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Remove(self, request, context):
    """Remove operation
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SRv6ExplicitPathServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=srv6__explicit__path__pb2.SRv6EPRequest.FromString,
          response_serializer=srv6__explicit__path__pb2.SRv6EPReply.SerializeToString,
      ),
      'Remove': grpc.unary_unary_rpc_method_handler(
          servicer.Remove,
          request_deserializer=srv6__explicit__path__pb2.SRv6EPRequest.FromString,
          response_serializer=srv6__explicit__path__pb2.SRv6EPReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'srv6_explicit_path.SRv6ExplicitPath', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))