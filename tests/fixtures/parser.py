#  example graphs to be used to be parsed into and edm_record by the parser
from pytest import fixture
import json


@fixture(scope="session")
def get_ref_lit_xml() -> str:
    return """<rdf:RDF 
            xmlns:rdaGr2="http://rdvocab.info/ElementsGr2/" 
            xmlns:xs="http://www.w3.org/2001/XMLSchema" 
            xmlns:wgs84_pos="http://www.w3.org/2003/01/geo/wgs84_pos#" 
            xmlns:t="http://www.tei-c.org/ns/1.0" 
            xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" 
            xmlns:europeana="http://www.europeana.eu/schemas/ese/" 
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
            xmlns:ore="http://www.openarchives.org/ore/terms/" 
            xmlns:edm="http://www.europeana.eu/schemas/edm/" 
            xmlns:skos="http://www.w3.org/2004/02/skos/core#" 
            xmlns:dcterms="http://purl.org/dc/terms/" 
            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
            xmlns:rdagr2="http://rdvocab.info/ElementsGr2/" 
            xmlns:owl="http://www.w3.org/2002/07/owl#" 
            xmlns:dc="http://purl.org/dc/elements/1.1/" 
            xmlns:svcs="http://rdfs.org/sioc/services#" 
            xmlns:doap="http://usefulinc.com/ns/doap#"
            xsi:schemaLocation="http://www.w3.org/1999/02/22-rdf-syntax-ns# https://gams.uni-graz.at/edm/2017-08/EDM.xsd">
        <ore:Aggregation rdf:about="https://gzu.jacq.org/GZU000274120">
          <edm:aggregatedCHO rdf:resource="https://gzu.jacq.org/GZU000274120#CHO"/>
          <edm:dataProvider>University of Graz, Institute of Plant Sciences - Herbarium GZU</edm:dataProvider>
          <edm:isShownAt rdf:resource="https://gzu.jacq.org/GZU000274120"/>
          <edm:isShownBy rdf:resource="https://services.jacq.org/jacq-services/rest/images/europeana/38321?withredirect=1"/>
          <edm:provider>Kulturpool</edm:provider>
          <edm:rights rdf:resource="http://creativecommons.org/licenses/by/4.0/"/>
          <edm:object rdf:resource="https://services.jacq.org/jacq-services/rest/images/europeana/38321?withredirect=1"/>
        </ore:Aggregation>
        <edm:ProvidedCHO rdf:about="https://gzu.jacq.org/GZU000274120#CHO">
          <dc:title>Adinandra acutifolia Hand.-Mazz.</dc:title>
          <dc:description xml:lang="en">A PreservedSpecimen of Adinandra acutifolia Hand.-Mazz. collected by Handel-Mazzetti,H.R.E. von</dc:description>
          <dc:identifier>https://gzu.jacq.org/GZU000274120</dc:identifier>
          <dc:language>und</dc:language>
          <edm:type>IMAGE</edm:type>
          <dc:type rdf:resource="http://rs.tdwg.org/dwc/terms/PreservedSpecimen"/>
          <dcterms:spatial>China, Guizhou, Prov. Kweitschou: in dumetis ad pagum Badschai. 950 m.</dcterms:spatial>
          <dc:date>1917-07-14</dc:date>
          <dc:creator>Handel-Mazzetti,H.R.E. von</dc:creator>
        </edm:ProvidedCHO>
        <edm:WebResource rdf:about="https://gzu.jacq.org/GZU000274120"/>
        <edm:WebResource rdf:about="https://services.jacq.org/jacq-services/rest/images/europeana/38321?withredirect=1">
          <dc:rights>University of Graz, Institute of Plant Sciences - Herbarium GZU</dc:rights>
          <edm:rights rdf:resource="http://creativecommons.org/licenses/by/4.0/"/>
        </edm:WebResource>
        <skos:Concept rdf:about="http://rs.tdwg.org/dwc/terms/PreservedSpecimen">
          <skos:prefLabel xml:lang="en">Preserved Specimen</skos:prefLabel>
          <skos:altLabel xml:lang="en">Preserved Specimen</skos:altLabel>
        </skos:Concept>
      </rdf:RDF>"""


@fixture(scope="session")
def get_ref_lit_json() -> dict:
    return json.loads("""{
                "provided_cho": {
                    "id": {
                        "value": "https://gzu.jacq.org/GZU000274120#CHO",
                    },
                    "edm_type": {
                        "value": "IMAGE",
                        "lang": null,
                        "datatype": null,
                        "normalize": false
                    },
                    "dc_contributor": null,
                    "dc_coverage": null,
                    "dc_creator": [
                        {
                            "value": "Handel-Mazzetti,H.R.E. von",
                            "lang": null,
                            "datatype": null,
                            "normalize": false
                        }
                    ],
                    "dc_date": [
                        {
                            "value": "1917-07-14",
                            "lang": null,
                            "datatype": null,
                            "normalize": false
                        }
                    ],
                    "dc_description": [
                        {
                            "value": "A PreservedSpecimen of Adinandra acutifolia Hand.-Mazz. collected by Handel-Mazzetti,H.R.E. von",
                            "lang": "en",
                            "datatype": null,
                            "normalize": false
                        }
                    ],
                    "dc_format": null,
                    "dc_identifier": [
                        {
                            "value": "https://gzu.jacq.org/GZU000274120",
                            "lang": null,
                            "datatype": null,
                            "normalize": false
                        }
                    ],
                    "dc_language": [
                        {
                            "value": "und",
                            "lang": null,
                            "datatype": null,
                            "normalize": false
                        }
                    ],
                    "dc_publisher": null,
                    "dc_relation": null,
                    "dc_rights": null,
                    "dc_source": null,
                    "dc_subject": null,
                    "dc_title": [
                        {
                            "value": "Adinandra acutifolia Hand.-Mazz.",
                            "lang": null,
                            "datatype": null,
                            "normalize": false
                        }
                    ],
                    "dc_type": [
                        {
                            "value": "http://rs.tdwg.org/dwc/terms/PreservedSpecimen"
                        }
                    ],
                    "dcterms_alternative": null,
                    "dcterms_conformsTo": null,
                    "dcterms_created": null,
                    "dcterms_extent": null,
                    "dcterms_hasFormat": null,
                    "dcterms_hasPart": null,
                    "dcterms_hasVersion": null,
                    "dcterms_isFormatOf": null,
                    "dcterms_isPartOf": null,
                    "dcterms_isReferencedBy": null,
                    "dcterms_isReplacedBy": null,
                    "dcterms_isRequiredBy": null,
                    "dcterms_issued": null,
                    "dcterms_isVersionOf": null,
                    "dcterms_medium": null,
                    "dcterms_provenance": null,
                    "dcterms_references": null,
                    "dcterms_replaces": null,
                    "dcterms_requires": null,
                    "dcterms_spatial": [
                        {
                            "value": "China, Guizhou, Prov. Kweitschou: in dumetis ad pagum Badschai. 950 m.",
                            "lang": null,
                            "datatype": null,
                            "normalize": false
                        }
                    ],
                    "dcterms_tableOfContents": null,
                    "dcterms_temporal": null,
                    "edm_currentLocation": null,
                    "edm_hasMet": null,
                    "edm_hasType": null,
                    "edm_incorporates": null,
                    "edm_isDerivativeOf": null,
                    "edm_isNextInSequence": null,
                    "edm_isRelatedTo": null,
                    "edm_isRepresentationOf": null,
                    "edm_isSimilarTo": null,
                    "edm_isSuccessorOf": null,
                    "edm_realizes": null,
                    "owl_isSameAs": null
                },
                "aggregation": {
                    "id": {
                        "value": "https://gzu.jacq.org/GZU000274120"
                    },
                    "edm_aggregatedCHO": {
                        "value": "https://gzu.jacq.org/GZU000274120#CHO"
                    },
                    "edm_dataProvider": {
                        "value": "University of Graz, Institute of Plant Sciences - Herbarium GZU",
                        "lang": null,
                        "datatype": null,
                        "normalize": false
                    },
                    "edm_provider": {
                        "value": "Kulturpool",
                        "lang": "de",
                        "datatype": null,
                        "normalize": false
                    },
                    "edm_rights": {
                        "value": "http://creativecommons.org/licenses/by/4.0/"
                    },
                    "edm_hasView": null,
                    "edm_isShownAt": {
                        "value": "https://gzu.jacq.org/GZU000274120"
                    },
                    "edm_isShownBy": {
                        "value": "https://services.jacq.org/jacq-services/rest/images/europeana/38321?withredirect=1"
                    },
                    "edm_object": {
                        "value": "https://services.jacq.org/jacq-services/rest/images/europeana/38321?withredirect=1"
                    },
                    "dc_rights": null,
                    "edm_ugc": null,
                    "edm_intermediateProvider": null
                },
                "web_resource": [
                    {
                        "id": {
                            "value": "https://gzu.jacq.org/GZU000274120"
                        },
                        "dc_creator": null,
                        "dc_description": null,
                        "dc_format": null,
                        "dc_rights": null,
                        "dc_source": null,
                        "dc_type": null,
                        "dcterms_conformsTo": null,
                        "dcterms_created": null,
                        "dcterms_extent": null,
                        "dcterms_hasPart": null,
                        "dcterms_isFormatOf": null,
                        "dcterms_isPartOf": null,
                        "dcterms_isReferencedBy": null,
                        "dcterms_issued": null,
                        "edm_isNextInSequence": null,
                        "edm_rights": {
                            "value": "http://creativecommons.org/licenses/by/4.0/"
                        },
                        "owl_sameAs": null,
                        "svcs_has_service": null
                    },
                    {
                        "id": {
                            "value": "https://services.jacq.org/jacq-services/rest/images/europeana/38321?withredirect=1"
                        },
                        "dc_creator": null,
                        "dc_description": null,
                        "dc_format": null,
                        "dc_rights": [
                            {
                                "value": "University of Graz, Institute of Plant Sciences - Herbarium GZU",
                                "lang": null,
                                "datatype": null,
                                "normalize": false
                            }
                        ],
                        "dc_source": null,
                        "dc_type": null,
                        "dcterms_conformsTo": null,
                        "dcterms_created": null,
                        "dcterms_extent": null,
                        "dcterms_hasPart": null,
                        "dcterms_isFormatOf": null,
                        "dcterms_isPartOf": null,
                        "dcterms_isReferencedBy": null,
                        "dcterms_issued": null,
                        "edm_isNextInSequence": null,
                        "edm_rights": {
                            "value": "http://creativecommons.org/licenses/by/4.0/"
                        },
                        "owl_sameAs": null,
                        "svcs_has_service": null
                    }
                ],
                "skos_concept": [
                    {
                        "id": {
                            "value": "http://rs.tdwg.org/dwc/terms/PreservedSpecimen"
                        },
                        "skos_prefLabel": [
                            {
                                "value": "Preserved Specimen",
                                "lang": "en",
                                "datatype": null,
                                "normalize": false
                            }
                        ],
                        "skos_altLabel": [
                            {
                                "value": "Preserved Specimen",
                                "lang": "en",
                                "datatype": null,
                                "normalize": false
                            }
                        ],
                        "skos_broader": null,
                        "skos_narrower": null,
                        "skos_related": null,
                        "skos_broadMatch": null,
                        "skos_narrowMatch": null,
                        "skos_relatedMatch": null,
                        "skos_exactMatch": null,
                        "skos_closeMatch": null,
                        "skos_note": null,
                        "skos_notation": null,
                        "skos_inScheme": null
                    }
                ],
                "edm_agent": [],
                "edm_time_span": [],
                "edm_place": [],
                "cc_license": [],
                "svcs_service": []
            }""")
