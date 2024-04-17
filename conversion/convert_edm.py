from edm_python.parsers import EDM_Parser
from rdflib import Graph

data = Graph().parse("conversion/output/albertina/graph_0.ttl")
edm = EDM_Parser(graph=data).parse()
print(edm.model_dump_json())

with open("new_test.json", "w") as file:
    file.write(edm.model_dump_json())
