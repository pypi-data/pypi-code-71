# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from admobilize.proto.datagateway.v1alpha1 import datagateway_service_pb2 as admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2


class DataGatewayServiceStub(object):
    """Bridge between client and data on AdMobilize infrastrucure.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateJob = channel.unary_unary(
                '/admobilize.datagateway.v1alpha1.DataGatewayService/CreateJob',
                request_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.CreateJobRequest.SerializeToString,
                response_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.Job.FromString,
                )
        self.GetJob = channel.unary_unary(
                '/admobilize.datagateway.v1alpha1.DataGatewayService/GetJob',
                request_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetJobRequest.SerializeToString,
                response_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.Job.FromString,
                )
        self.GetJobResults = channel.unary_unary(
                '/admobilize.datagateway.v1alpha1.DataGatewayService/GetJobResults',
                request_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetJobResultRequests.SerializeToString,
                response_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetDatapointsResponse.FromString,
                )
        self.ExportResults = channel.unary_unary(
                '/admobilize.datagateway.v1alpha1.DataGatewayService/ExportResults',
                request_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.ExportResultsRequest.SerializeToString,
                response_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.ExportResultsResponse.FromString,
                )


class DataGatewayServiceServicer(object):
    """Bridge between client and data on AdMobilize infrastrucure.
    """

    def CreateJob(self, request, context):
        """Starts a job do retrieve user datapoints.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJob(self, request, context):
        """Retrieve information about a job running.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJobResults(self, request, context):
        """Retrieve results from a specific job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportResults(self, request, context):
        """Export results in a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataGatewayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateJob,
                    request_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.CreateJobRequest.FromString,
                    response_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.Job.SerializeToString,
            ),
            'GetJob': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJob,
                    request_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetJobRequest.FromString,
                    response_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.Job.SerializeToString,
            ),
            'GetJobResults': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJobResults,
                    request_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetJobResultRequests.FromString,
                    response_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetDatapointsResponse.SerializeToString,
            ),
            'ExportResults': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportResults,
                    request_deserializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.ExportResultsRequest.FromString,
                    response_serializer=admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.ExportResultsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'admobilize.datagateway.v1alpha1.DataGatewayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataGatewayService(object):
    """Bridge between client and data on AdMobilize infrastrucure.
    """

    @staticmethod
    def CreateJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.datagateway.v1alpha1.DataGatewayService/CreateJob',
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.CreateJobRequest.SerializeToString,
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.Job.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.datagateway.v1alpha1.DataGatewayService/GetJob',
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetJobRequest.SerializeToString,
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.Job.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJobResults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.datagateway.v1alpha1.DataGatewayService/GetJobResults',
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetJobResultRequests.SerializeToString,
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.GetDatapointsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportResults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/admobilize.datagateway.v1alpha1.DataGatewayService/ExportResults',
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.ExportResultsRequest.SerializeToString,
            admobilize_dot_datagateway_dot_v1alpha1_dot_datagateway__service__pb2.ExportResultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
