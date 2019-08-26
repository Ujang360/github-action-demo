import pytest_demo.some_functions as sf


def cli():
    hello_message = sf.compose_hello_to('Kresna')
    print(hello_message)
