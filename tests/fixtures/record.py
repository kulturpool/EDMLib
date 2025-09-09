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


@pytest.fixture(scope="session")
def xml_with_gyear() -> str:
    return """
        <rdf:RDF xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:dcterms="http://purl.org/dc/terms/" xmlns:doap="http://usefulinc.com/ns/doap#"
      xmlns:edm="http://www.europeana.eu/schemas/edm/" xmlns:ore="http://www.openarchives.org/ore/terms/"
      xmlns:rdagr2="http://rdvocab.info/ElementsGr2/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:skos="http://www.w3.org/2004/02/skos/core#" xmlns:svcs="http://rdfs.org/sioc/services#"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <ore:Aggregation rdf:about="ABSB9-001_Aggregation">
        <edm:aggregatedCHO rdf:resource="ABSB9-001" />
        <edm:dataProvider xml:lang="de">Alban Berg Stiftung</edm:dataProvider>
        <edm:rights rdf:resource="http://creativecommons.org/licenses/by-nc-nd/4.0/" />
        <edm:isShownAt
          rdf:resource="https://www.absw.at/bibliothekseintrag.php?id_bibliothekseintrag=1087&amp;action=view" />
        <edm:isShownBy rdf:resource="https://www.absw.at/bibliothek-pdf/B9-001_sml.pdf" />
        <edm:hasView rdf:resource="https://www.absw.at/bibliothek-pdf/B9-001.pdf" />
        <edm:object rdf:resource="https://www.absw.at/phpThumb.php?src=bilddaten/ersteSeiten%2FB9-001_S1.pdf&amp;w=350" />
        <edm:provider>Kulturpool</edm:provider>
      </ore:Aggregation>
      <edm:ProvidedCHO rdf:about="ABSB9-001">
        <edm:type>TEXT</edm:type>
        <dc:identifier>B9-001</dc:identifier>
        <dc:language>de</dc:language>
        <dc:rights xml:lang="de">Alban Berg Stiftung</dc:rights>
        <dcterms:isPartOf xml:lang="de">Alban Berg Stiftung / Bibliothek</dcterms:isPartOf>
        <dc:title xml:lang="de">Villach</dc:title>
        <dc:type>Buch</dc:type>
        <dc:publisher rdf:resource="https://d-nb.info/gnd/117238031" /><!-- GND-Referenz zu Stein, Erwin Otto -->
        <dc:publisher>Deutscher Kommunal-Verlag G. m. b. H., Berlin-Friedenau</dc:publisher>
        <dcterms:created>1931</dcterms:created>
        <dcterms:extent>226, [42] (Reklame; Postkraftwagenfahrten etc.) S.</dcterms:extent>
        <dcterms:extent>20,2*27,8*2,5 cm</dcterms:extent>
        <edm:currentLocation>Alban Berg Stiftung, Wien</edm:currentLocation>
      </edm:ProvidedCHO>
      <edm:Agent xmlns:dnbt="https://d-nb.info/standards/elementset/dnb#"
        xmlns:gndo="https://d-nb.info/standards/elementset/gnd#" xmlns:owl="http://www.w3.org/2002/07/owl#"
        rdf:about="https://d-nb.info/gnd/117238031">
        <owl:sameAs rdf:resource="http://viaf.org/viaf/167340506" />
        <owl:sameAs rdf:resource="https://isni.org/isni/0000000118677552" />
        <owl:sameAs rdf:resource="http://www.wikidata.org/entity/Q95254987" />
        <owl:sameAs rdf:resource="https://d-nb.info/gnd/139935851" />
        <owl:sameAs rdf:resource="https://d-nb.info/gnd/1232951811" />
        <rdagr2:dateOfBirth rdf:datatype="http://www.w3.org/2001/XMLSchema#gYear">1885</rdagr2:dateOfBirth>
        <skos:altLabel>Stein, Erwin Otto</skos:altLabel>
        <skos:altLabel>Dr. Timo</skos:altLabel>
        <rdagr2:dateOfDeath rdf:datatype="http://www.w3.org/2001/XMLSchema#gYear">1938</rdagr2:dateOfDeath>
        <skos:prefLabel>Stein, Erwin</skos:prefLabel>
      </edm:Agent>
    </rdf:RDF>
    """


@pytest.fixture(scope="session")
def get_record_with_missing_edm_rights() -> str:
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
                </rdf:RDF>"""


@pytest.fixture(scope="session")
def get_record_with_https_edm_rights() -> str:
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
                        <edm:rights rdf:resource="https://creativecommons.org/publicdomain/mark/1.0/"/>
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
                        <edm:rights rdf:resource="https://creativecommons.org/publicdomain/mark/1.0/"/>
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
                </rdf:RDF>"""


@pytest.fixture(scope="session")
def get_record_with_http_edm_rights() -> str:
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
                </rdf:RDF>"""
