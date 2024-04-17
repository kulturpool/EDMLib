from typing import List, TypeAlias, Union
from rdflib import Literal, URIRef


MixedValuesList: TypeAlias = List[Union[Literal, URIRef]] | List[URIRef] | List[Literal]
