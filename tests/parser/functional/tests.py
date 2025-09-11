from pytest import fixture
from rdflib import Graph
import os


@fixture(scope="session")
def example_graphs():
    return [Graph().parse(filename, format="xml") for filename in os.listdir("./xml")]
