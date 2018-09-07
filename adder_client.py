from __future__ import print_function

import grpc

import addition_pb2
import addition_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = addition_pb2_grpc.AdderStub(channel)
    response = stub.Add(addition_pb2.AddRequest(a=1, b=2))
    print("Sum is " + response.c)
if __name__ == '__main__':
    run()
