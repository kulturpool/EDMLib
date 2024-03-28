# type: ignore
from pytest import fixture
import rdflib
from edm_python.edm import EDM_Record, EDM_ProvidedCHO, EDM_WebResource, ORE_Aggregation


# create fixtures to use in tests
@fixture(scope="session")
def record_input_data():
    data = {
        "provided_cho": {
            "id": "oai:fue.onb.at:eTravel:25fde500-1d2b-4ee2-a604-5f9d07331094",
            "edm_type": rdflib.term.Literal("IMAGE"),
            "dc_contributor": None,
            "dc_coverage": None,
            "dc_creator": None,
            "dc_date": [rdflib.term.Literal("1904-04-01")],
            "dc_description": [
                rdflib.term.Literal(
                    "Zeitung zu den Themen Reise, Tourismus, Fremdenverkehr", lang="de"
                ),
                rdflib.term.Literal(
                    "Journal on the themes of travel and tourism", lang="en"
                ),
            ],
            "dc_format": None,
            "dc_identifier": [
                rdflib.term.Literal(
                    "oai:fue.onb.at:eTravel:25fde500-1d2b-4ee2-a604-5f9d07331094"
                )
            ],
            "dc_language": [rdflib.term.Literal("de"), rdflib.term.Literal("en")],
            "dc_publisher": [rdflib.term.Literal("Dillinger", lang="de")],
            "dc_relation": None,
            "dc_rights": None,
            "dc_source": None,
            "dc_subject": [
                rdflib.term.Literal("Reise", lang="de"),
                rdflib.term.Literal("Tourimus", lang="de"),
                rdflib.term.Literal("Fremdenverkehr", lang="de"),
                rdflib.term.Literal("travel", lang="en"),
                rdflib.term.Literal("tourism", lang="en"),
            ],
            "dc_title": [
                rdflib.term.Literal(
                    "Dillingers Reiseführer : illustrierte Zeitschrift für internationalen Reise- und Fremdenverkehr, 1904-04-01",
                    lang="de",
                )
            ],
            "dc_type": [rdflib.term.Literal("Text", lang="de")],
            "dcterms_alternative": None,
            "dcterms_conformsTo": None,
            "dcterms_created": [rdflib.term.Literal("1904-04-01")],
            "dcterms_extent": None,
            "dcterms_hasFormat": None,
            "dcterms_hasPart": None,
            "dcterms_hasVersion": None,
            "dcterms_isFormatOf": None,
            "dcterms_isPartOf": [rdflib.term.Literal("Anno")],
            "dcterms_isReferencedBy": None,
            "dcterms_isReplacedBy": None,
            "dcterms_isRequiredBy": None,
            "dcterms_issued": None,
            "dcterms_isVersionOf": None,
            "dcterms_medium": None,
            "dcterms_provenance": None,
            "dcterms_references": None,
            "dcterms_replaces": None,
            "dcterms_requires": None,
            "dcterms_spatial": None,
            "dcterms_tableOfContents": None,
            "dcterms_temporal": [
                rdflib.term.Literal(
                    "Wien : 14.1903 - 24.1913 ; anfangs 2 x monatlich, später monatlich"
                )
            ],
            "edm_currentLocation": None,
            "edm_hasMet": None,
            "edm_hasType": None,
            "edm_incorporates": None,
            "edm_isDerivativeOf": None,
            "edm_IsNextInSequence": None,
            "edm_isRelatedTo": None,
            "edm_isRepresentationOf": None,
            "edm_isSimilarTo": None,
            "edm_isSuccessorOf": None,
            "edm_realizes": None,
            "owl_isSameAs": None,
        },
        "aggregation": {
            "id": "http://anno.onb.ac.at/cgi-content/anno?apm=0&aid=dil&datum=19040401",
            "edm_aggregatedCHO": rdflib.term.URIRef(
                "oai:fue.onb.at:eTravel:25fde500-1d2b-4ee2-a604-5f9d07331094"
            ),
            "edm_dataProvider": rdflib.term.Literal(
                "Österreichische Nationalbibliothek"
            ),
            "edm_provider": rdflib.term.Literal("Kulturpool"),
            "edm_rights": rdflib.term.URIRef("http://example.com/placeholder_rights"),
            "edm_hasView": None,
            "edm_isShownAt": rdflib.term.URIRef(
                "http://anno.onb.ac.at/cgi-content/anno?apm=0&aid=dil&datum=19040401"
            ),
            "edm_isShownBy": rdflib.term.URIRef(
                "http://anno.onb.ac.at/preview/dil/1904/19040401/00000001.png"
            ),
            "edm_object": rdflib.term.URIRef(
                "http://anno.onb.ac.at/preview/dil/1904/19040401/00000001.png"
            ),
            "dc_rights": None,
            "edm_ugc": None,
            "edm_intermediateProvider": None,
        },
        "web_resource": [],
        "skos_concept": [],
        "edm_agent": [],
        "edm_time_span": [],
        "edm_place": [],
        "cc_license": [],
        "svcs_service": None,
    }

    return data


@fixture(scope="session")
def web_resource_input_data():
    data = {}

    return data


def test_provided_cho(record_input_data):
    assert EDM_ProvidedCHO(
        **record_input_data["provided_cho"]
    ), f"Provided CHO init test failed"


def test_aggregation(record_input_data):
    assert ORE_Aggregation(**record_input_data["aggregation"])


def test_webresource(web_resource_input_data):
    assert EDM_WebResource(**web_resource_input_data), f"WebResource init test failed"


def test_record_init(record_input_data):
    assert (
        EDM_Record(**record_input_data).model_dump() == record_input_data
    ), f"record input data did not equal parsed and re-serialised data"


# test building of whole record


# test exceptions

# test functions on enums
