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
def get_xml_with_xsdtypes() -> str:
    return """<rdf:RDF xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:dcterms="http://purl.org/dc/terms/" xmlns:doap="http://usefulinc.com/ns/doap#"
    xmlns:edm="http://www.europeana.eu/schemas/edm/" xmlns:ore="http://www.openarchives.org/ore/terms/"
    xmlns:rdagr2="http://rdvocab.info/ElementsGr2/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:skos="http://www.w3.org/2004/02/skos/core#" xmlns:svcs="http://rdfs.org/sioc/services#"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <ore:Aggregation rdf:about="ABSC12-042_Aggregation">
        <edm:aggregatedCHO rdf:resource="ABSC12-042" />
        <edm:dataProvider xml:lang="de">Alban Berg Stiftung</edm:dataProvider>
        <edm:rights rdf:resource="http://creativecommons.org/licenses/by-nc-nd/4.0/" />
        <edm:isShownAt
            rdf:resource="https://www.absw.at/bibliothekseintrag.php?id_bibliothekseintrag=1667&amp;action=view" />
        <edm:isShownBy rdf:resource="https://www.absw.at/bilddaten/ersteSeiten/C12-042_S1_sml.pdf" />
        <edm:hasView rdf:resource="https://www.absw.at/bilddaten/ersteSeiten/C12-042_S1.pdf" />
        <edm:object
            rdf:resource="https://www.absw.at/phpThumb.php?src=bilddaten/ersteSeiten%2FC12-042_S1.pdf&amp;w=350" />
        <edm:provider>Kulturpool</edm:provider>
    </ore:Aggregation>
    <edm:ProvidedCHO rdf:about="ABSC12-042">
        <edm:type>TEXT</edm:type>
        <dc:identifier>C12-042</dc:identifier>
        <dc:language>de</dc:language>
        <dc:rights xml:lang="de">Alban Berg Stiftung</dc:rights>
        <dcterms:isPartOf xml:lang="de">Alban Berg Stiftung / Bibliothek</dcterms:isPartOf>
        <dc:title xml:lang="de">Deutsches Musiker-Lexikon</dc:title>
        <dc:description xml:lang="de">Gebunden (blau, gold)</dc:description>
        <dc:type>Buch</dc:type>
        <dc:publisher rdf:resource="https://d-nb.info/gnd/118924133" /><!-- GND-Referenz zu M&#252;ller von Asow,
        Erich Hermann -->
        <dc:publisher>Wilhelm Limpert-Verlag, Dresden</dc:publisher>
        <dcterms:created>1929</dcterms:created>
        <dcterms:extent>&lt;8&gt;, VIII Sp., &lt;4&gt;, [1644] Sp., &lt;12&gt; S.</dcterms:extent>
        <dcterms:extent>22,5*29,2*5,8 cm</dcterms:extent>
        <edm:currentLocation>Alban Berg Stiftung, Wien</edm:currentLocation>
    </edm:ProvidedCHO>
    <edm:Agent xmlns:dnbt="https://d-nb.info/standards/elementset/dnb#"
        xmlns:gndo="https://d-nb.info/standards/elementset/gnd#" xmlns:owl="http://www.w3.org/2002/07/owl#"
        rdf:about="https://d-nb.info/gnd/118924133">
        <owl:sameAs rdf:resource="http://viaf.org/viaf/62347536" />
        <owl:sameAs rdf:resource="https://isni.org/isni/0000000109081511" />
        <owl:sameAs rdf:resource="http://www.wikidata.org/entity/Q26160311" />
        <owl:sameAs rdf:resource="http://id.loc.gov/rwo/agents/n85207029" />
        <owl:sameAs rdf:resource="https://d-nb.info/gnd/1157512356" />
        <rdagr2:dateOfBirth rdf:datatype="http://www.w3.org/2001/XMLSchema#date">1892-08-31</rdagr2:dateOfBirth>
        <skos:altLabel>Müller von Asow, Erich H.</skos:altLabel>
        <skos:altLabel>Müller, Erich H.</skos:altLabel>
        <skos:altLabel>Müller-Dresden, Erich Hermann</skos:altLabel>
        <skos:altLabel>Müller-Dresden, Erich H.</skos:altLabel>
        <skos:altLabel>Mueller- von Asow, Erich Hermann</skos:altLabel>
        <skos:altLabel>Mueller von Asow, E. H.</skos:altLabel>
        <skos:altLabel>Mueller von Asow, Erich Hermann</skos:altLabel>
        <skos:altLabel>Asow, Erich Hermann Müller von</skos:altLabel>
        <skos:altLabel>Asow, Erich H. Müller von</skos:altLabel>
        <skos:altLabel>Asow, Erich Hermann Mueller von</skos:altLabel>
        <skos:altLabel>Asow, E. H. Mueller von</skos:altLabel>
        <skos:altLabel>Asow, E.H. Mueller von</skos:altLabel>
        <skos:altLabel>Dresden, Erich Hermann Müller-</skos:altLabel>
        <skos:altLabel>Müller, Erich Hermann</skos:altLabel>
        <skos:altLabel>Asow, Erich Hermann von</skos:altLabel>
        <skos:altLabel>Müller, Erich Hermann</skos:altLabel>
        <rdagr2:dateOfDeath rdf:datatype="http://www.w3.org/2001/XMLSchema#date">1964-06-04</rdagr2:dateOfDeath>
        <skos:prefLabel>Müller von Asow, Erich Hermann</skos:prefLabel>
    </edm:Agent>
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
