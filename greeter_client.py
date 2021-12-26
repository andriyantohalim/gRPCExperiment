import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel1:
        stub = helloworld_pb2_grpc.GreeterStub(channel1)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="You"))
    print("Greeter client received: " + response.message)

    with grpc.insecure_channel('localhost:50051') as channel2:
        stub = helloworld_pb2_grpc.GreeterStub(channel2)
        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name="You"))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
