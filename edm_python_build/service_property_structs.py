from .fetch_types import PropertyStruct, Mandate, Cardinality, Valuetype


has_service = PropertyStruct(
    parent_class="EDM_WebResource",
    namespace="svcs",
    label="has_service",
    cardinality=Cardinality.ZERO_TO_MANY,
    mandate=Mandate.OPTIONAL,
    description="""The identifier of the svcs:Service required to consume the edm:WebResource. Example: 	
<svcs:has_service rdf:resource="http://www.example.org/Service/IIIF">""",
    value_type=Valuetype.REF,
)

is_referenced_by = PropertyStruct(
    parent_class="EDM_WebResource",
    namespace="dcterms",
    label="IsReferencedBy",
    cardinality=Cardinality.ZERO_TO_MANY,
    mandate=Mandate.OPTIONAL,
    description="""A related resource that references, cites, or otherwise points to the described resource. In IIIF, dcterms:isReferencedBy can be used to connect an edm:WebResource to a IIIF manifest URI. 
    Example: <dcterms:isReferencedBy rdf:resource="https://gallica.bnf.fr/iiif/ark:/12148/btv1b55001425m/manifest.json"/>""",
    value_type=Valuetype.REF,
)
