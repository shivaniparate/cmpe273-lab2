from concurrent import futures
import time

import grpc

import addition_pb2
import addition_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Adder(addition_pb2_grpc.AdderServicer):

	def Add(self, request, context):
		summ = request.a+request.b 
		return addition_pb2.AddReply(c = '%d' % summ)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addition_pb2_grpc.add_AdderServicer_to_server(Adder(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
