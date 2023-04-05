# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
from __future__ import absolute_import

import grpc

from . import progress_feedback_pb2 as progress__feedback__pb2


class ProgressFeedbackStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateProgress = channel.unary_unary(
        '/progress_feedback.ProgressFeedback/UpdateProgress',
        request_serializer=progress__feedback__pb2.ProgressUpdate.SerializeToString,
        response_deserializer=progress__feedback__pb2.ProgressResult.FromString,
        )


class ProgressFeedbackServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateProgress(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProgressFeedbackServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateProgress': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateProgress,
          request_deserializer=progress__feedback__pb2.ProgressUpdate.FromString,
          response_serializer=progress__feedback__pb2.ProgressResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'progress_feedback.ProgressFeedback', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
