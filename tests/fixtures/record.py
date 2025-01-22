from typing import Any
from edmlib.edm import EDM_Record
import pytest
import json


@pytest.fixture(scope="session")
def get_record() -> None:
    pass


@pytest.fixture(scope="session")
def valid_json_samples() -> list[dict[str, Any]]:
    return []


@pytest.fixture(scope="session")
def invalid_json_samples() -> list[dict[str, Any]]:
    return []


@pytest.fixture(scope="session")
def valid_record_samples() -> list[EDM_Record]:
    return []


@pytest.fixture(scope="session")
def cho_id_missmatch() -> dict[str, Any]:
    # Record is valid, but cho id has other value than ore-aggregation.aggregated_cho
    return json.loads(
        """{"provided_cho":{"id":{"value":"https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c72342/cho"},"edm_type":{"value":"IMAGE","lang":null,"datatype":null,"normalize":false},"dc_contributor":null,"dc_coverage":null,"dc_creator":[{"value":"http://d-nb.info/gnd/11869703X"}],"dc_date":null,"dc_description":null,"dc_format":null,"dc_identifier":[{"value":"DG1949/697","lang":null,"datatype":null,"normalize":false}],"dc_language":[{"value":"de","lang":null,"datatype":null,"normalize":false}],"dc_publisher":null,"dc_relation":null,"dc_rights":[{"value":"Albertina, Wien, Österreich","lang":null,"datatype":null,"normalize":false}],"dc_source":null,"dc_subject":null,"dc_title":[{"value":"Die Erweckung des Lazarus","lang":"german","datatype":null,"normalize":false}],"dc_type":[{"value":"http://vocab.getty.edu/aat/300041273"}],"dcterms_alternative":null,"dcterms_conformsTo":null,"dcterms_created":[{"value":"1506","lang":null,"datatype":null,"normalize":false}],"dcterms_extent":[{"value":"22,5 x 15,9 cm (laut Hollstein)","lang":null,"datatype":null,"normalize":false}],"dcterms_hasFormat":null,"dcterms_hasPart":null,"dcterms_hasVersion":null,"dcterms_isFormatOf":null,"dcterms_isPartOf":[{"value":"Graphische Sammlung","lang":null,"datatype":null,"normalize":false}],"dcterms_isReferencedBy":null,"dcterms_isReplacedBy":null,"dcterms_isRequiredBy":null,"dcterms_issued":null,"dcterms_isVersionOf":null,"dcterms_medium":[{"value":"Holzschnitt","lang":null,"datatype":null,"normalize":false}],"dcterms_provenance":null,"dcterms_references":null,"dcterms_replaces":null,"dcterms_requires":null,"dcterms_spatial":null,"dcterms_tableOfContents":null,"dcterms_temporal":null,"edm_currentLocation":null,"edm_hasMet":null,"edm_hasType":null,"edm_incorporates":null,"edm_isDerivativeOf":null,"edm_isNextInSequence":null,"edm_isRelatedTo":null,"edm_isRepresentationOf":null,"edm_isSimilarTo":null,"edm_isSuccessorOf":null,"edm_realizes":null,"owl_isSameAs":null},"aggregation":{"id":{"value":"https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/aggregation"},"edm_aggregatedCHO":{"value":"https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/cho"},"edm_dataProvider":{"value":"Albertina","lang":null,"datatype":null,"normalize":false},"edm_provider":{"value":"Kulturpool","lang":"de","datatype":null,"normalize":false},"edm_rights":{"value":"http://creativecommons.org/publicdomain/mark/1.0/"},"edm_hasView":[{"value":"https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&port=15001&filename=images/DG1949_697.jpg&cache=yes"}],"edm_isShownAt":{"value":"https://sammlungenonline.albertina.at/?query=search=/record/objectnumbersearch=[DG1949/697]&showtype=record"},"edm_isShownBy":{"value":"https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&port=15001&filename=images/DG1949_697.jpg&cache=yes"},"edm_object":{"value":"https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&port=15001&filename=images/DG1949_697.jpg&cache=yes&maxwidth=400"},"dc_rights":null,"edm_ugc":null,"edm_intermediateProvider":null},"web_resource":[{"id":{"value":"https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&port=15001&filename=images/DG1949_697.jpg&cache=yes"},"dc_creator":null,"dc_description":null,"dc_format":null,"dc_rights":[{"value":"Albertina, Wien, Österreich","lang":null,"datatype":null,"normalize":false}],"dc_source":null,"dc_type":null,"dcterms_conformsTo":null,"dcterms_created":null,"dcterms_extent":null,"dcterms_hasPart":null,"dcterms_isFormatOf":null,"dcterms_isPartOf":null,"dcterms_isReferencedBy":[{"value":"https://sammlungenonline.albertina.at/iiif/tms_101507/manifest.json"}],"dcterms_issued":null,"edm_isNextInSequence":null,"edm_rights":{"value":"http://creativecommons.org/publicdomain/mark/1.0/"},"owl_sameAs":null,"svcs_has_service":[{"value":"https://sammlungenonline.albertina.at/iiif/images/DG1949_697.JPG"}]}],"skos_concept":[{"id":{"value":"http://vocab.getty.edu/aat/300041273"},"skos_prefLabel":{"value":"Druckgraphik","lang":null,"datatype":null,"normalize":false},"skos_altLabel":null,"skos_broader":null,"skos_narrower":null,"skos_related":null,"skos_broadMatch":null,"skos_narrowMatch":null,"skos_relatedMatch":null,"skos_exactMatch":null,"skos_closeMatch":null,"skos_note":null,"skos_notation":null,"skos_inScheme":null}],"edm_agent":[{"id":{"value":"http://d-nb.info/gnd/11869703X"},"skos_prefLabel":{"value":"Urs Graf d. Ä.","lang":null,"datatype":null,"normalize":false},"skos_altLabel":null,"skos_note":null,"dc_date":null,"dc_identifier":null,"dcterms_hasPart":null,"dcterms_isPartOf":null,"edm_begin":null,"edm_end":null,"edm_hasMet":null,"edm_isRelatedTo":null,"foaf_name":null,"rdagr2_biographicalInformation":[{"value":"Solothurn um 1485 - 1527/28 Basel","lang":null,"datatype":null,"normalize":false}],"rdagr2_dateOfBirth":null,"rdagr2_dateOfDeath":null,"rdagr2_dateOfEstablishment":null,"rdagr2_dateOfTermination":null,"rdagr2_gender":null,"rdagr2_placeOfBirth":null,"rdagr2_placeOfDeath":null,"rdagr2_professionOrOccupation":null,"owl_sameAs":[{"value":"http://d-nb.info/gnd/11869703X"},{"value":"http://de.wikipedia.org/wiki/Urs_Graf_der_%C3%84ltere"}]}],"edm_time_span":[],"edm_place":[],"cc_license":[],"svcs_service":[{"id":{"value":"https://sammlungenonline.albertina.at/iiif/images/DG1949_697.JPG"},"dcterms_conformsTo":[{"value":"http://iiif.io/api/image"}],"doap_implements":{"value":"http://iiif.io/api/image/2/level2.json"}}]}"""
    )


@pytest.fixture(scope="session")
def xml_string() -> str:
    return """ <rdf:RDF 
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
                    >
                    <ore:Aggregation rdf:about="https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/aggregation">
                        <edm:aggregatedCHO rdf:resource="https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/cho"/>
                        <edm:dataProvider>Albertina</edm:dataProvider>
                        <edm:provider xml:lang="de">Kulturpool</edm:provider>
                        <edm:rights rdf:resource="http://creativecommons.org/publicdomain/mark/1.0/"/>
                        <edm:hasView rdf:resource="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes"/>
                        <edm:isShownAt rdf:resource="https://sammlungenonline.albertina.at/?query=search=/record/objectnumbersearch=[DG1949/697]&amp;showtype=record"/>
                        <edm:isShownBy rdf:resource="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes"/>
                        <edm:object rdf:resource="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes&amp;maxwidth=400"/>
                    </ore:Aggregation>
                    <edm:Agent rdf:about="http://d-nb.info/gnd/11869703X">
                        <skos:prefLabel>Urs Graf d. Ä.</skos:prefLabel>
                        <rdagr2:biographicalInformation>Solothurn um 1485 - 1527/28 Basel</rdagr2:biographicalInformation>
                        <owl:sameAs rdf:resource="http://d-nb.info/gnd/11869703X"/>
                        <owl:sameAs rdf:resource="http://de.wikipedia.org/wiki/Urs_Graf_der_%C3%84ltere"/>
                    </edm:Agent>
                    <skos:Concept rdf:about="http://vocab.getty.edu/aat/300041273">
                        <skos:prefLabel>Druckgraphik</skos:prefLabel>
                    </skos:Concept>
                    <edm:WebResource rdf:about="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes">
                        <dc:rights>Albertina, Wien, Österreich</dc:rights>
                        <dcterms:isReferencedBy rdf:resource="https://sammlungenonline.albertina.at/iiif/tms_101507/manifest.json"/>
                        <edm:rights rdf:resource="http://creativecommons.org/publicdomain/mark/1.0/"/>
                        <svcs:has_service rdf:resource="https://sammlungenonline.albertina.at/iiif/images/DG1949_697.JPG"/>
                    </edm:WebResource>
                    <svcs:Service rdf:about="https://sammlungenonline.albertina.at/iiif/images/DG1949_697.JPG">
                        <dcterms:conformsTo rdf:resource="http://iiif.io/api/image"/>
                        <doap:implements rdf:resource="http://iiif.io/api/image/2/level2.json"/>
                    </svcs:Service>
                    <edm:ProvidedCHO rdf:about="https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/cho">
                        <edm:type>IMAGE</edm:type>
                        <dc:creator rdf:resource="http://d-nb.info/gnd/11869703X"/>
                        <dc:identifier>DG1949/697</dc:identifier>
                        <dc:language>de</dc:language>
                        <dc:rights>Albertina, Wien, Österreich</dc:rights>
                        <dc:title xml:lang="german">Die Erweckung des Lazarus</dc:title>
                        <dc:type rdf:resource="http://vocab.getty.edu/aat/300041273"/>
                        <dcterms:created>1506</dcterms:created>
                        <dcterms:extent>22,5 x 15,9 cm (laut Hollstein)</dcterms:extent>
                        <dcterms:isPartOf>Graphische Sammlung</dcterms:isPartOf>
                        <dcterms:medium>Holzschnitt</dcterms:medium>
                    </edm:ProvidedCHO>
                </rdf:RDF>
            """


@pytest.fixture(scope="session")
def xml_with_lang_in_edm_type() -> str:
    return """ <rdf:RDF 
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
                    >
                    <ore:Aggregation rdf:about="https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/aggregation">
                        <edm:aggregatedCHO rdf:resource="https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/cho"/>
                        <edm:dataProvider>Albertina</edm:dataProvider>
                        <edm:provider xml:lang="de">Kulturpool</edm:provider>
                        <edm:rights rdf:resource="http://creativecommons.org/publicdomain/mark/1.0/"/>
                        <edm:hasView rdf:resource="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes"/>
                        <edm:isShownAt rdf:resource="https://sammlungenonline.albertina.at/?query=search=/record/objectnumbersearch=[DG1949/697]&amp;showtype=record"/>
                        <edm:isShownBy rdf:resource="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes"/>
                        <edm:object rdf:resource="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes&amp;maxwidth=400"/>
                    </ore:Aggregation>
                    <edm:Agent rdf:about="http://d-nb.info/gnd/11869703X">
                        <skos:prefLabel>Urs Graf d. Ä.</skos:prefLabel>
                        <rdagr2:biographicalInformation>Solothurn um 1485 - 1527/28 Basel</rdagr2:biographicalInformation>
                        <owl:sameAs rdf:resource="http://d-nb.info/gnd/11869703X"/>
                        <owl:sameAs rdf:resource="http://de.wikipedia.org/wiki/Urs_Graf_der_%C3%84ltere"/>
                    </edm:Agent>
                    <skos:Concept rdf:about="http://vocab.getty.edu/aat/300041273">
                        <skos:prefLabel>Druckgraphik</skos:prefLabel>
                    </skos:Concept>
                    <edm:WebResource rdf:about="https://sammlungenonline.albertina.at/cc/imageproxy.ashx?server=localhost&amp;port=15001&amp;filename=images/DG1949_697.jpg&amp;cache=yes">
                        <dc:rights>Albertina, Wien, Österreich</dc:rights>
                        <dcterms:isReferencedBy rdf:resource="https://sammlungenonline.albertina.at/iiif/tms_101507/manifest.json"/>
                        <edm:rights rdf:resource="http://creativecommons.org/publicdomain/mark/1.0/"/>
                        <svcs:has_service rdf:resource="https://sammlungenonline.albertina.at/iiif/images/DG1949_697.JPG"/>
                    </edm:WebResource>
                    <svcs:Service rdf:about="https://sammlungenonline.albertina.at/iiif/images/DG1949_697.JPG">
                        <dcterms:conformsTo rdf:resource="http://iiif.io/api/image"/>
                        <doap:implements rdf:resource="http://iiif.io/api/image/2/level2.json"/>
                    </svcs:Service>
                    <edm:ProvidedCHO rdf:about="https://id.kulturpool.at/000056bf-fe34-4e7f-ad3c-eb7bfff37c70/cho">
                        <edm:type xml:lang="en">IMAGE</edm:type>
                        <dc:creator rdf:resource="http://d-nb.info/gnd/11869703X"/>
                        <dc:identifier>DG1949/697</dc:identifier>
                        <dc:language>de</dc:language>
                        <dc:rights>Albertina, Wien, Österreich</dc:rights>
                        <dc:title xml:lang="german">Die Erweckung des Lazarus</dc:title>
                        <dc:type rdf:resource="http://vocab.getty.edu/aat/300041273"/>
                        <dcterms:created>1506</dcterms:created>
                        <dcterms:extent>22,5 x 15,9 cm (laut Hollstein)</dcterms:extent>
                        <dcterms:isPartOf>Graphische Sammlung</dcterms:isPartOf>
                        <dcterms:medium>Holzschnitt</dcterms:medium>
                    </edm:ProvidedCHO>
                </rdf:RDF>
            """
