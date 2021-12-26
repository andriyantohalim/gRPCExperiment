# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# https://www.grpc.io/docs/what-is-grpc/introduction/
# https://www.grpc.io/docs/what-is-grpc/core-concepts/
# https://grpc.io/docs/languages/python/basics/

# https://grpc.io/docs/languages/python/quickstart/
# https://github.com/grpc/grpc/blob/v1.42.0/examples/protos/helloworld.proto
# https://github.com/grpc/grpc/tree/v1.42.0/examples/python/helloworld

# https://github.com/grpc/grpc/blob/v1.42.0/examples/python/helloworld/greeter_client.py
# https://github.com/grpc/grpc/blob/v1.42.0/examples/python/helloworld/greeter_server.py

# python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./helloworld.proto