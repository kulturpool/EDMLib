# Python Library for Europeana Data Model

A Python library providing utilities for working with the **Europeana Data Model (EDM)**. This library maps all EDM classes and properties to Pydantic models, enabling type-safe validation, parsing, and serialization of EDM records.

## Features

- **Validation**: Built-in validation for EDM record structure and property constraints
- **Type-safe EDM**: All EDM classes implemented as Pydantic models
- **XML/RDF parsing**: Parse EDM records from XML or RDF formats
- **RDF serialization**: Export EDM records back to RDF formats

## Setup

Using virtualenv and pip:

```bash
GITLAB_TOKEN_NAME='<personal_access_token_name>'
GITLAB_TOKEN='<personal_access_token>'

virtualenv .venv && source .venv/bin/activate && pip install --index-url "https://$GITLAB_TOKEN_NAME:$GITLAB_TOKEN@git.kpool.at/api/v4/projects/359/packages/pypi/simple" edmlib
```

Using poetry, `pyproject.toml` and `${HOME}/.config/kpool/.env`:

```toml
[tool.poetry.dependencies]
python = ">=3.10,<4.0.0"
edmlib = { version = "^2.4.3", source = "edmlib" }

[[tool.poetry.source]]
name = "edmlib"
url = "https://git.kpool.at/api/v4/projects/359/packages/pypi/simple"
priority = "supplemental"
```

## Quick Start

EDM specifications are encapsulated in `EDM_Record`. All data is validated at instantiation, ensuring compliance with EDM.

### Parse EDM Records

```python
from edmlib import EDM_Parser

# Parse from string
record = EDM_Parser.from_string("""<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:ore="http://www.openarchives.org/ore/terms/"
    xmlns:edm="http://www.europeana.eu/schemas/edm/"
    xmlns:dc="http://purl.org/dc/elements/1.1/">
    <edm:ProvidedCHO
        rdf:about="http://uri.test/edm123#CHO">
        <dc:type xml:lang="en">Text</dc:type>
        <dc:title xml:lang="de">Titel</dc:title>
        <dc:identifier>123</dc:identifier>
        <dc:language>de</dc:language>
        <edm:type>TEXT</edm:type>
    </edm:ProvidedCHO>
    <ore:Aggregation
        rdf:about="http://uri.test/edm123#Aggregation">
        <edm:aggregatedCHO
            rdf:resource="http://uri.test/edm123#CHO" />
        <edm:dataProvider>Test</edm:dataProvider>
        <edm:isShownAt
            rdf:resource="http://uri.test/edm123.jpg" />
        <edm:isShownBy
            rdf:resource="http://uri.test/edm123.jpg" />
        <edm:provider>Kulturpool</edm:provider>
        <edm:rights rdf:resource="http://creativecommons.org/licenses/by-nc-sa/4.0/" />
    </ore:Aggregation>
</rdf:RDF>
""").parse()

# Parse from file
record = EDM_Parser.from_file("edm_record.xml").parse()

# Parse other formats
record = EDM_Parser.from_file("edm_record.ttl", format="ttl").parse()
```

### Create EDM Records programmatically

```python
from edmlib import EDM_Record, EDM_ProvidedCHO, ORE_Aggregation, Ref, Lit

record = EDM_Record(
    provided_cho=EDM_ProvidedCHO(
        id=Ref(value="http://uri.test/edm123#CHO"),
        dc_type=[Lit(value="Text", lang="en")],
        dc_title=[Lit(value="Titel", lang="de")],
        dc_identifier=[Lit(value="123")],
        dc_language=[Lit(value="de")],
        edm_type=Lit(value="TEXT")
    ),
    aggregation=ORE_Aggregation(
        id=Ref(value="http://uri.test/edm123#Aggregation"),
        edm_aggregatedCHO=Ref(value="http://uri.test/edm123#CHO"),
        edm_dataProvider=Lit(value="Test"),
        edm_isShownAt=Ref(value="http://uri.test/edm123.jpg"),
        edm_isShownBy=Ref(value="http://uri.test/edm123.jpg"),
        edm_provider=Lit(value="Kulturpool"),
        edm_rights=Ref(value="http://creativecommons.org/licenses/by-nc-sa/4.0/")
    )
)
```

### Work with EDM Records

```python
from edmlib import EDM_ProvidedCHO, ORE_Aggregation, EDM_WebResource, EDM_Agent, EDM_Place, EDM_TimeSpan, SKOS_Concept, CC_License, SVCS_Service

# Access record components
assert record.provided_cho.id == Ref(value="http://uri.test/edm123#CHO")
assert record.aggregation.id == Ref(value="http://uri.test/edm123#Aggregation")
```

### Serialize

Multiple serialization formats for exporting EDM records are supported:

```python
# Pretty-XML format
xml_str = record.serialize()

# JSON-LD format
jsonld_str = record.serialize(format="json-ld")
```

All rdflib graph serialization formats are supported, including XML, Turtle (TTL), and others.


## Component Classes

- `EDM_ProvidedCHO` - Cultural Heritage Object (CHO)
- `ORE_Aggregation` - Resource aggregation
- `EDM_WebResource` - Web resources
- `EDM_Agent` - Agents (persons, organizations)
- `EDM_Place` - Places and locations
- `EDM_TimeSpan` - Time periods
- `SKOS_Concept` - Concepts and classifications
- `CC_License` - Creative Commons licenses
- `SVCS_Service` - SIOC Services

### Composition
```python
assert isinstance(          record.provided_cho,    EDM_ProvidedCHO)
assert isinstance(          record.aggregation,     ORE_Aggregation)

assert isinstance(next(iter(record.web_resource)),  EDM_WebResource) # optional
assert isinstance(next(iter(record.skos_concept)),  SKOS_Concept)    # optional
assert isinstance(next(iter(record.edm_agent)),     EDM_Agent)       # optional
assert isinstance(next(iter(record.edm_time_span)), EDM_TimeSpan)    # optional
assert isinstance(next(iter(record.edm_place)),     EDM_Place)       # optional
assert isinstance(next(iter(record.cc_license)),    CC_License)      # optional
assert isinstance(next(iter(record.svcs_service)),  SVCS_Service)    # optional
```

## Development

### Setup

```bash
# Clone repository
git clone https://git.kpool.at/kulturpool/development/aggregation/libraries/edmlib.git

cd edmlib

# Install dependencies
poetry install

# Run tests
pytest .
```

### Requirements

- Python >=3.10,<4.0.0
- Dependencies: 
  - rdflib ^7.0.0
  - lxml ^5.1.0
  - pydantic ^2.10.3
  - pyld ^2.0.3
  - requests ^2.32.3



<!--pdoc-start-->
## API documentation


<!--### Modules-->
*  <a href="#EDM_Record">EDM_Record</a>             
    *  <a href="#EDM_Record.provided_cho">provided_cho</a>  
    *  <a href="#EDM_Record.aggregation">aggregation</a>  
    *  <a href="#EDM_Record.web_resource">web_resource</a>  
    *  <a href="#EDM_Record.skos_concept">skos_concept</a>  
    *  <a href="#EDM_Record.edm_agent">edm_agent</a>  
    *  <a href="#EDM_Record.edm_time_span">edm_time_span</a>  
    *  <a href="#EDM_Record.edm_place">edm_place</a>  
    *  <a href="#EDM_Record.cc_license">cc_license</a>  
    *  <a href="#EDM_Record.svcs_service">svcs_service</a>  
    *  <a href="#EDM_Record.get_rdf_graph">get_rdf_graph</a>  
    *  <a href="#EDM_Record.serialize">serialize</a>  
    *  <a href="#EDM_Record.get_framed_json_ld">get_framed_json_ld</a>  
    *  <a href="#EDM_Record.validate_provided_cho_identity">validate_provided_cho_identity</a>  
    *  <a href="#EDM_Record.fetch_edm_isShownBy_head">fetch_edm_isShownBy_head</a>  
    *  <a href="#EDM_Record.has_edm_object">has_edm_object</a>  
    *  <a href="#EDM_Record.fetch_edm_object_head">fetch_edm_object_head</a>  
    *  <a href="#EDM_Record.has_edm_hasView">has_edm_hasView</a>  
    *  <a href="#EDM_Record.fetch_edm_hasView_heads">fetch_edm_hasView_heads</a>  
    *  <a href="#EDM_Record.fetch_edm_isShownAt_head">fetch_edm_isShownAt_head</a>  
    *  <a href="#EDM_Record.model_config">model_config</a>  

*  <a href="#EDM_ProvidedCHO">EDM_ProvidedCHO</a>             
    *  <a href="#EDM_ProvidedCHO.edm_type">edm_type</a>  
    *  <a href="#EDM_ProvidedCHO.dc_contributor">dc_contributor</a>  
    *  <a href="#EDM_ProvidedCHO.dc_coverage">dc_coverage</a>  
    *  <a href="#EDM_ProvidedCHO.dc_creator">dc_creator</a>  
    *  <a href="#EDM_ProvidedCHO.dc_date">dc_date</a>  
    *  <a href="#EDM_ProvidedCHO.dc_description">dc_description</a>  
    *  <a href="#EDM_ProvidedCHO.dc_format">dc_format</a>  
    *  <a href="#EDM_ProvidedCHO.dc_identifier">dc_identifier</a>  
    *  <a href="#EDM_ProvidedCHO.dc_language">dc_language</a>  
    *  <a href="#EDM_ProvidedCHO.dc_publisher">dc_publisher</a>  
    *  <a href="#EDM_ProvidedCHO.dc_relation">dc_relation</a>  
    *  <a href="#EDM_ProvidedCHO.dc_rights">dc_rights</a>  
    *  <a href="#EDM_ProvidedCHO.dc_source">dc_source</a>  
    *  <a href="#EDM_ProvidedCHO.dc_subject">dc_subject</a>  
    *  <a href="#EDM_ProvidedCHO.dc_title">dc_title</a>  
    *  <a href="#EDM_ProvidedCHO.dc_type">dc_type</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_alternative">dcterms_alternative</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_conformsTo">dcterms_conformsTo</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_created">dcterms_created</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_extent">dcterms_extent</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_hasFormat">dcterms_hasFormat</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_hasPart">dcterms_hasPart</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_hasVersion">dcterms_hasVersion</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_isFormatOf">dcterms_isFormatOf</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_isPartOf">dcterms_isPartOf</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_isReferencedBy">dcterms_isReferencedBy</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_isReplacedBy">dcterms_isReplacedBy</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_isRequiredBy">dcterms_isRequiredBy</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_issued">dcterms_issued</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_isVersionOf">dcterms_isVersionOf</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_medium">dcterms_medium</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_provenance">dcterms_provenance</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_references">dcterms_references</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_replaces">dcterms_replaces</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_requires">dcterms_requires</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_spatial">dcterms_spatial</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_tableOfContents">dcterms_tableOfContents</a>  
    *  <a href="#EDM_ProvidedCHO.dcterms_temporal">dcterms_temporal</a>  
    *  <a href="#EDM_ProvidedCHO.edm_currentLocation">edm_currentLocation</a>  
    *  <a href="#EDM_ProvidedCHO.edm_hasMet">edm_hasMet</a>  
    *  <a href="#EDM_ProvidedCHO.edm_hasType">edm_hasType</a>  
    *  <a href="#EDM_ProvidedCHO.edm_incorporates">edm_incorporates</a>  
    *  <a href="#EDM_ProvidedCHO.edm_isDerivativeOf">edm_isDerivativeOf</a>  
    *  <a href="#EDM_ProvidedCHO.edm_isNextInSequence">edm_isNextInSequence</a>  
    *  <a href="#EDM_ProvidedCHO.edm_isRelatedTo">edm_isRelatedTo</a>  
    *  <a href="#EDM_ProvidedCHO.edm_isRepresentationOf">edm_isRepresentationOf</a>  
    *  <a href="#EDM_ProvidedCHO.edm_isSimilarTo">edm_isSimilarTo</a>  
    *  <a href="#EDM_ProvidedCHO.edm_isSuccessorOf">edm_isSuccessorOf</a>  
    *  <a href="#EDM_ProvidedCHO.edm_realizes">edm_realizes</a>  
    *  <a href="#EDM_ProvidedCHO.owl_sameAs">owl_sameAs</a>  
    *  <a href="#EDM_ProvidedCHO.validate_dependent_edm">validate_dependent_edm</a>  
    *  <a href="#EDM_ProvidedCHO.model_config">model_config</a>  

*  <a href="#ORE_Aggregation">ORE_Aggregation</a>             
    *  <a href="#ORE_Aggregation.edm_aggregatedCHO">edm_aggregatedCHO</a>  
    *  <a href="#ORE_Aggregation.edm_dataProvider">edm_dataProvider</a>  
    *  <a href="#ORE_Aggregation.edm_provider">edm_provider</a>  
    *  <a href="#ORE_Aggregation.edm_rights">edm_rights</a>  
    *  <a href="#ORE_Aggregation.edm_hasView">edm_hasView</a>  
    *  <a href="#ORE_Aggregation.edm_isShownAt">edm_isShownAt</a>  
    *  <a href="#ORE_Aggregation.edm_isShownBy">edm_isShownBy</a>  
    *  <a href="#ORE_Aggregation.edm_object">edm_object</a>  
    *  <a href="#ORE_Aggregation.dc_rights">dc_rights</a>  
    *  <a href="#ORE_Aggregation.edm_ugc">edm_ugc</a>  
    *  <a href="#ORE_Aggregation.edm_intermediateProvider">edm_intermediateProvider</a>  
    *  <a href="#ORE_Aggregation.validate_conditional_attributes">validate_conditional_attributes</a>  
    *  <a href="#ORE_Aggregation.model_config">model_config</a>  

*  <a href="#EDM_WebResource">EDM_WebResource</a>             
    *  <a href="#EDM_WebResource.dc_creator">dc_creator</a>  
    *  <a href="#EDM_WebResource.dc_description">dc_description</a>  
    *  <a href="#EDM_WebResource.dc_format">dc_format</a>  
    *  <a href="#EDM_WebResource.dc_rights">dc_rights</a>  
    *  <a href="#EDM_WebResource.dc_source">dc_source</a>  
    *  <a href="#EDM_WebResource.dc_type">dc_type</a>  
    *  <a href="#EDM_WebResource.dcterms_conformsTo">dcterms_conformsTo</a>  
    *  <a href="#EDM_WebResource.dcterms_created">dcterms_created</a>  
    *  <a href="#EDM_WebResource.dcterms_extent">dcterms_extent</a>  
    *  <a href="#EDM_WebResource.dcterms_hasPart">dcterms_hasPart</a>  
    *  <a href="#EDM_WebResource.dcterms_isFormatOf">dcterms_isFormatOf</a>  
    *  <a href="#EDM_WebResource.dcterms_isPartOf">dcterms_isPartOf</a>  
    *  <a href="#EDM_WebResource.dcterms_isReferencedBy">dcterms_isReferencedBy</a>  
    *  <a href="#EDM_WebResource.dcterms_issued">dcterms_issued</a>  
    *  <a href="#EDM_WebResource.edm_isNextInSequence">edm_isNextInSequence</a>  
    *  <a href="#EDM_WebResource.edm_rights">edm_rights</a>  
    *  <a href="#EDM_WebResource.owl_sameAs">owl_sameAs</a>  
    *  <a href="#EDM_WebResource.svcs_has_service">svcs_has_service</a>  
    *  <a href="#EDM_WebResource.validate_web_resource">validate_web_resource</a>  
    *  <a href="#EDM_WebResource.model_config">model_config</a>  

*  <a href="#CC_License">CC_License</a>             
    *  <a href="#CC_License.odrl_inheritFrom">odrl_inheritFrom</a>  
    *  <a href="#CC_License.cc_deprecatedOn">cc_deprecatedOn</a>  
    *  <a href="#CC_License.model_config">model_config</a>  

*  <a href="#SKOS_Concept">SKOS_Concept</a>             
    *  <a href="#SKOS_Concept.skos_prefLabel">skos_prefLabel</a>  
    *  <a href="#SKOS_Concept.skos_altLabel">skos_altLabel</a>  
    *  <a href="#SKOS_Concept.skos_broader">skos_broader</a>  
    *  <a href="#SKOS_Concept.skos_narrower">skos_narrower</a>  
    *  <a href="#SKOS_Concept.skos_related">skos_related</a>  
    *  <a href="#SKOS_Concept.skos_broadMatch">skos_broadMatch</a>  
    *  <a href="#SKOS_Concept.skos_narrowMatch">skos_narrowMatch</a>  
    *  <a href="#SKOS_Concept.skos_relatedMatch">skos_relatedMatch</a>  
    *  <a href="#SKOS_Concept.skos_exactMatch">skos_exactMatch</a>  
    *  <a href="#SKOS_Concept.skos_closeMatch">skos_closeMatch</a>  
    *  <a href="#SKOS_Concept.skos_note">skos_note</a>  
    *  <a href="#SKOS_Concept.skos_notation">skos_notation</a>  
    *  <a href="#SKOS_Concept.skos_inScheme">skos_inScheme</a>  
    *  <a href="#SKOS_Concept.validate_skos_pref_label">validate_skos_pref_label</a>  
    *  <a href="#SKOS_Concept.model_config">model_config</a>  

*  <a href="#EDM_Agent">EDM_Agent</a>             
    *  <a href="#EDM_Agent.skos_prefLabel">skos_prefLabel</a>  
    *  <a href="#EDM_Agent.skos_altLabel">skos_altLabel</a>  
    *  <a href="#EDM_Agent.skos_note">skos_note</a>  
    *  <a href="#EDM_Agent.dc_date">dc_date</a>  
    *  <a href="#EDM_Agent.dc_identifier">dc_identifier</a>  
    *  <a href="#EDM_Agent.dcterms_hasPart">dcterms_hasPart</a>  
    *  <a href="#EDM_Agent.dcterms_isPartOf">dcterms_isPartOf</a>  
    *  <a href="#EDM_Agent.edm_begin">edm_begin</a>  
    *  <a href="#EDM_Agent.edm_end">edm_end</a>  
    *  <a href="#EDM_Agent.edm_hasMet">edm_hasMet</a>  
    *  <a href="#EDM_Agent.edm_isRelatedTo">edm_isRelatedTo</a>  
    *  <a href="#EDM_Agent.foaf_name">foaf_name</a>  
    *  <a href="#EDM_Agent.rdagr2_biographicalInformation">rdagr2_biographicalInformation</a>  
    *  <a href="#EDM_Agent.rdagr2_dateOfBirth">rdagr2_dateOfBirth</a>  
    *  <a href="#EDM_Agent.rdagr2_dateOfDeath">rdagr2_dateOfDeath</a>  
    *  <a href="#EDM_Agent.rdagr2_dateOfEstablishment">rdagr2_dateOfEstablishment</a>  
    *  <a href="#EDM_Agent.rdagr2_dateOfTermination">rdagr2_dateOfTermination</a>  
    *  <a href="#EDM_Agent.rdagr2_gender">rdagr2_gender</a>  
    *  <a href="#EDM_Agent.rdagr2_placeOfBirth">rdagr2_placeOfBirth</a>  
    *  <a href="#EDM_Agent.rdagr2_placeOfDeath">rdagr2_placeOfDeath</a>  
    *  <a href="#EDM_Agent.rdagr2_professionOrOccupation">rdagr2_professionOrOccupation</a>  
    *  <a href="#EDM_Agent.owl_sameAs">owl_sameAs</a>  
    *  <a href="#EDM_Agent.validate_skos_pref_label">validate_skos_pref_label</a>  
    *  <a href="#EDM_Agent.model_config">model_config</a>  

*  <a href="#EDM_TimeSpan">EDM_TimeSpan</a>             
    *  <a href="#EDM_TimeSpan.skos_prefLabel">skos_prefLabel</a>  
    *  <a href="#EDM_TimeSpan.skos_altLabel">skos_altLabel</a>  
    *  <a href="#EDM_TimeSpan.skos_note">skos_note</a>  
    *  <a href="#EDM_TimeSpan.dcterms_hasPart">dcterms_hasPart</a>  
    *  <a href="#EDM_TimeSpan.dcterms_isPartOf">dcterms_isPartOf</a>  
    *  <a href="#EDM_TimeSpan.edm_begin">edm_begin</a>  
    *  <a href="#EDM_TimeSpan.edm_end">edm_end</a>  
    *  <a href="#EDM_TimeSpan.edm_isNextInSequence">edm_isNextInSequence</a>  
    *  <a href="#EDM_TimeSpan.owl_sameAs">owl_sameAs</a>  
    *  <a href="#EDM_TimeSpan.validate_skos_pref_label">validate_skos_pref_label</a>  
    *  <a href="#EDM_TimeSpan.model_config">model_config</a>  

*  <a href="#EDM_Place">EDM_Place</a>             
    *  <a href="#EDM_Place.wgs84_pos_lat">wgs84_pos_lat</a>  
    *  <a href="#EDM_Place.wgs84_pos_long">wgs84_pos_long</a>  
    *  <a href="#EDM_Place.wgs84_pos_alt">wgs84_pos_alt</a>  
    *  <a href="#EDM_Place.skos_prefLabel">skos_prefLabel</a>  
    *  <a href="#EDM_Place.skos_altLabel">skos_altLabel</a>  
    *  <a href="#EDM_Place.skos_note">skos_note</a>  
    *  <a href="#EDM_Place.dcterms_hasPart">dcterms_hasPart</a>  
    *  <a href="#EDM_Place.dcterms_isPartOf">dcterms_isPartOf</a>  
    *  <a href="#EDM_Place.edm_isNextInSequence">edm_isNextInSequence</a>  
    *  <a href="#EDM_Place.owl_sameAs">owl_sameAs</a>  
    *  <a href="#EDM_Place.validate_skos_pref_label">validate_skos_pref_label</a>  
    *  <a href="#EDM_Place.model_config">model_config</a>  

*  <a href="#SVCS_Service">SVCS_Service</a>             
    *  <a href="#SVCS_Service.dcterms_conformsTo">dcterms_conformsTo</a>  
    *  <a href="#SVCS_Service.doap_implements">doap_implements</a>  
    *  <a href="#SVCS_Service.model_config">model_config</a>  

*  <a href="#MixedValuesList">MixedValuesList</a>  
*  <a href="#EDM_Parser">EDM_Parser</a>             
    *  <a class="function" href="#EDM_Parser.__init__">EDM_Parser</a>  
    *  <a href="#EDM_Parser.from_file">from_file</a>  
    *  <a href="#EDM_Parser.from_string">from_string</a>  
    *  <a href="#EDM_Parser.graph">graph</a>  
    *  <a href="#EDM_Parser.get_single_ref">get_single_ref</a>  
    *  <a href="#EDM_Parser.get_many_ref">get_many_ref</a>  
    *  <a href="#EDM_Parser.get_triples">get_triples</a>  
    *  <a href="#EDM_Parser.get_aggregation">get_aggregation</a>  
    *  <a href="#EDM_Parser.get_webresources">get_webresources</a>  
    *  <a href="#EDM_Parser.get_instance_triples">get_instance_triples</a>  
    *  <a href="#EDM_Parser.parse_single_class">parse_single_class</a>  
    *  <a href="#EDM_Parser.parse_many_class">parse_many_class</a>  
    *  <a href="#EDM_Parser.parse">parse</a>  

*  <a href="#Ref">Ref</a>             
    *  <a href="#Ref.value">value</a>  
    *  <a href="#Ref.is_ref">is_ref</a>  
    *  <a href="#Ref.validate_value_as_uri">validate_value_as_uri</a>  
    *  <a href="#Ref.to_rdflib">to_rdflib</a>  
    *  <a href="#Ref.model_config">model_config</a>  

*  <a href="#Lit">Lit</a>             
    *  <a href="#Lit.value">value</a>  
    *  <a href="#Lit.lang">lang</a>  
    *  <a href="#Lit.datatype">datatype</a>  
    *  <a href="#Lit.normalize">normalize</a>  
    *  <a href="#Lit.validate_consistency">validate_consistency</a>  
    *  <a href="#Lit.to_rdflib">to_rdflib</a>  
    *  <a href="#Lit.model_config">model_config</a>  








<section id="EDM_Record">

###    class EDM_Record<wbr>(<span class="base">pydantic.main.BaseModel</span>): 

<a class="headerlink" href="#EDM_Record"></a>

<div class="docstring"><p>Pydantic model representing an edm record, as a fully typed structure.
All contained non-standard types are themselves BaseModels, and the fields are always also either BaseModels or
standard-types. This ensures that without further conversion, an instance of this class can be
dumped as a dict (or json) and restored from such a dict (or json).</p>

<p>Validation:
This model is responsible for validating the overall structure, order and completeness
of the record.
The individual models for each of its properties are responsible for validating their own attributes –
their completeness, cardinality and structure.
Finally, the special type models - Ref and Lit - within those container types are responsible for validating
the indiviudal values.</p>
</div> 

<div id="EDM_Record.provided_cho" class="classattr">

#### provided_cho: edmlib.edm.classes.core.EDM_ProvidedCHO 

<a class="headerlink" href="#EDM_Record.provided_cho"></a>



</div>
<div id="EDM_Record.aggregation" class="classattr">

#### aggregation: edmlib.edm.classes.core.ORE_Aggregation 

<a class="headerlink" href="#EDM_Record.aggregation"></a>



</div>
<div id="EDM_Record.web_resource" class="classattr">

#### web_resource: Optional[List[edmlib.edm.classes.core.EDM_WebResource]] 

<a class="headerlink" href="#EDM_Record.web_resource"></a>



</div>
<div id="EDM_Record.skos_concept" class="classattr">

#### skos_concept: Optional[List[edmlib.edm.classes.context.SKOS_Concept]] 

<a class="headerlink" href="#EDM_Record.skos_concept"></a>



</div>
<div id="EDM_Record.edm_agent" class="classattr">

#### edm_agent: Optional[List[edmlib.edm.classes.context.EDM_Agent]] 

<a class="headerlink" href="#EDM_Record.edm_agent"></a>



</div>
<div id="EDM_Record.edm_time_span" class="classattr">

#### edm_time_span: Optional[List[edmlib.edm.classes.context.EDM_TimeSpan]] 

<a class="headerlink" href="#EDM_Record.edm_time_span"></a>



</div>
<div id="EDM_Record.edm_place" class="classattr">

#### edm_place: Optional[List[edmlib.edm.classes.context.EDM_Place]] 

<a class="headerlink" href="#EDM_Record.edm_place"></a>



</div>
<div id="EDM_Record.cc_license" class="classattr">

#### cc_license: Optional[List[edmlib.edm.classes.context.CC_License]] 

<a class="headerlink" href="#EDM_Record.cc_license"></a>



</div>
<div id="EDM_Record.svcs_service" class="classattr">

#### svcs_service: Optional[List[edmlib.edm.classes.service.SVCS_Service]] 

<a class="headerlink" href="#EDM_Record.svcs_service"></a>



</div>
<div id="EDM_Record.get_rdf_graph" class="classattr">

####     def get_rdf_graph(self)  

<a class="headerlink" href="#EDM_Record.get_rdf_graph"></a>

<div class="docstring"><p>Return whole record as as an RDF - rdflib.Graph object.</p>
</div> 

</div>
<div id="EDM_Record.serialize" class="classattr">

####     def serialize(self, format: str = &#39;pretty-xml&#39;, max_depth: int = 1) -&gt; str  

<a class="headerlink" href="#EDM_Record.serialize"></a>

<div class="docstring"><p>Serialize graph to rdf/xml with pretty-formatting.</p>
</div> 

</div>
<div id="EDM_Record.get_framed_json_ld" class="classattr">

####     def get_framed_json_ld(self)  

<a class="headerlink" href="#EDM_Record.get_framed_json_ld"></a>



</div>
<div id="EDM_Record.validate_provided_cho_identity" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_provided_cho_identity(self) -&gt; Self  

<a class="headerlink" href="#EDM_Record.validate_provided_cho_identity"></a>



</div>
<div id="EDM_Record.fetch_edm_isShownBy_head" class="classattr">

####     def fetch_edm_isShownBy_head(self, **kwargs) -&gt; requests.models.Response  

<a class="headerlink" href="#EDM_Record.fetch_edm_isShownBy_head"></a>



</div>
<div id="EDM_Record.has_edm_object" class="classattr">

####     def has_edm_object(self) -&gt; bool  

<a class="headerlink" href="#EDM_Record.has_edm_object"></a>



</div>
<div id="EDM_Record.fetch_edm_object_head" class="classattr">

####     def fetch_edm_object_head(self, **kwargs) -&gt; requests.models.Response  

<a class="headerlink" href="#EDM_Record.fetch_edm_object_head"></a>



</div>
<div id="EDM_Record.has_edm_hasView" class="classattr">

####     def has_edm_hasView(self) -&gt; bool  

<a class="headerlink" href="#EDM_Record.has_edm_hasView"></a>



</div>
<div id="EDM_Record.fetch_edm_hasView_heads" class="classattr">

####     def fetch_edm_hasView_heads(self, **kwargs) -&gt; list[requests.models.Response]  

<a class="headerlink" href="#EDM_Record.fetch_edm_hasView_heads"></a>



</div>
<div id="EDM_Record.fetch_edm_isShownAt_head" class="classattr">

####     def fetch_edm_isShownAt_head(self, **kwargs) -&gt; requests.models.Response  

<a class="headerlink" href="#EDM_Record.fetch_edm_isShownAt_head"></a>



</div>
<div id="EDM_Record.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#EDM_Record.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="EDM_ProvidedCHO">

###    class EDM_ProvidedCHO<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#EDM_ProvidedCHO"></a>

<div class="docstring"><p>mandatory-properties: DC_description, DC_language, DC_subject, DC_title, DC_type, DCTERMS_spatial, DCTERMS_temporal, EDM_type</p>

<p>optional-properties: DC_coverage, DC_format, DC_relation, DC_rights, DCTERMS_conformsTo, DCTERMS_extent, DCTERMS_hasFormat, DCTERMS_hasPart, DCTERMS_hasVersion, DCTERMS_isFormatOf, DCTERMS_isReferencedBy, DCTERMS_isReplacedBy, DCTERMS_isRequiredBy, DCTERMS_isVersionOf, DCTERMS_medium, DCTERMS_provenance, DCTERMS_references, DCTERMS_replaces, DCTERMS_requires, DCTERMS_tableOfContents , EDM_currentLocation, EDM_hasMet, EDM_hasType, EDM_incorporates, EDM_isDerivativeOf, EDM_isRelatedTo, EDM_isRepresentationOf, EDM_isSimilarTo, EDM_isSuccessorOf, EDM_realizes, OWL_sameAs</p>

<p>recommended-properties: DC_contributor, DC_creator, DC_date, DC_identifier, DC_publisher, DC_source, DCTERMS_alternative, DCTERMS_created, DCTERMS_isPartOf, DCTERMS_issued, EDM_IsNextInSequence</p>
</div> 

<div id="EDM_ProvidedCHO.edm_type" class="classattr">

#### edm_type: edmlib.edm.value_types.Lit 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_type"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
exactly_one</p>

<p>Value-Type:
Lit</p>

<p>Description: </p>

<p>The value must be one of the types accepted by Europeana as it will support portal fun
ctionality: TEXT, VIDEO, SOUND, IMAGE, 3D. (For 3D, when applicable, use the value “3D
‐PDF” in dc:format ) <edm:type>IMAGE</edm:type> (upper-­case &amp; case sensitive) <edm:ty
pe>3D</edm:type> (upper-­case &amp; case sensitive)</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_contributor" class="classattr">

#### dc_contributor: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_contributor"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Use for contributors to the CHO. If possible supply the identifier of the contributor 
from an authority source. Providers with richer role terms can elect to map a subset t
o dc:contributor and others to dc:creator. Repeat for multiple contributors. <dc:contr
ibutor>Maria Callas</dc:contributor> or create a reference to an instance of the Agent
class <dc:contributor rdf:resource=“http://www.example.com/MariaCallas”&gt;For recommend
ations on medata quality see Tier A-C requirements ,</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_coverage" class="classattr">

#### dc_coverage: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_coverage"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The spatial or temporal topic of the CHO. Use the more precise dcterms:spatial or dcte
rms:temporal properties if the data will support it. <dc:coverage>1995-­1996</dc:cover
age> or <dc:coverage>Berlin</dc:coverage> or create a reference to an instance of a co
ntextual class, for example, a Place class <dc:coverage rdf:resource=“<a href="https://sws.geon">https://sws.geon</a>
ames.org/2950159/ ”/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_creator" class="classattr">

#### dc_creator: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_creator"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>For the creator of the CHO. If possible supply the identifier of the creator from an a
uthority source. Repeat for multiple creators.  <dc:creator>Shakespeare, William</dc:c
reator> or create a reference to an instance of the Agent class <dc:creator rdf:resour
ce=“http://viaf.org/viaf/96994048”/>For recommendations on medata quality see Tier A-C
requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_date" class="classattr">

#### dc_date: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_date"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Use for a significant date in the life of the CHO.  Europeana recommends date conformi
ng to ISO 8601 starting with the year and with hyphens (YYYY-­MM-DD). NB: other EDM el
ements are relevant for expressing dates of different events in the life of the CHO: d
cterms:temporal, dcterms:created and dcterms:issued. Be careful and choose the most ap
propriate one! <dc:date>Early 20th century</dc:date> or <dc:date>1919</dc:date> or cre
ate a reference to an instance of the TimeSpan class <dc:date rdf:resource=“<a href="http://sem">http://sem</a>
ium.org/time/19xx_1_third”/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_description" class="classattr">

#### dc_description: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_description"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A description of the CHO. If there is no dc:description for an object, there must be a
dc:title. If both are  available, provide both. <dc:description>Illustrated guide to 
airport markings and lighting signals, with particular reference to SMGCS  (Surface Mo
vement Guidance and Control System) for airports with low visibility conditions.</dc:d
escription></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_format" class="classattr">

#### dc_format: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_format"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Use for the terms generally applied to indicate the format of the cultural heritage ob
ject or the file format of a born digital object. Use the value “3D-­PDF” if appropria
te. <dc:format>paper</dc:format>For recommendations on medata quality see Tier A-C req
uirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_identifier" class="classattr">

#### dc_identifier: List[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_identifier"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>An identifier of the original CHO. <dc:identifier>RP-­T-­1952-­380</dc:identifier></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_language" class="classattr">

#### dc_language: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_language"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>The language of text CHOs and also for other types of CHO if there is a language aspec
t. Mandatory for TEXT objects, strongly recommended for other object types with a lang
uage element. Best practice is to use ISO 639 two- or three-letter primary language ta
gs.Repeat for multiple languages. We also recommend the use of the ISO 639-­2 code for
no linguistic content (ZXX).</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_publisher" class="classattr">

#### dc_publisher: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_publisher"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The name of the publisher of the CHO. If possible supply the identifier of the publish
er from an authority source. <dc:publisher>Oxford University Press</dc:publisher> or c
reate a reference to an instance of the Agent class <dc:publisher rdf:resource=“http:/
/www.oup.com/”/>For recommendations on medata quality see Tier A-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_relation" class="classattr">

#### dc_relation: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_relation"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The name or identifier of a related resource, generally used for other related CHOs. C
f edm:isRelatedTo. <dc:relation>maps.crace.1/33</dc:relation> (Shelf mark) Or to provi
de a link to another object: <dc:relation rdf:resource=“<a href="http://www.identifier/relatedO">http://www.identifier/relatedO</a>
bject”/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_rights" class="classattr">

#### dc_rights: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_rights"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Use to give the name of the rights holder of the CHO if possible or for more general r
ights information. (Note that the controlled edm:rights property relates to the digita
l objects and applies to the edm:WebResource and/or edm:Aggregation). <dc:rights>Copyr
ight © British Library Board</dc:rights></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_source" class="classattr">

#### dc_source: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_source"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A related resource from which the described resource is derived in whole or in part i.
e. the source of the original CHO.  (Not the name of the content holder: for this see 
edm:dataProvider.) <dc:source>Security Magazine pp 3-12</dc:source></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_subject" class="classattr">

#### dc_subject: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_subject"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The subject of the CHO.One of dc:subject or dc:type or dcterms:spatial or dcterms:temp
oral must be  provided; if more than one of these properties is available, please prov
ide them all. High-­level dc:subject  values like 'archaeology' are allowed, especiall
y when there is no other subject that can be easily filled in. <dc:subject>archeology&lt;
/dc:subject>or create a reference to an instance of the Concept class <skos:Concept rd
f:about="http://semantics.gr/authorities/ekt-unesco/560215094">   <skos:prefLabel xml:
lang="el">Αρχαιολογία</skos:prefLabel>   <skos:prefLabel xml:lang="en">Archaeology</sk
os:prefLabel></skos:Concept>For recommendations on medata quality see Tier A-C require
ments .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_title" class="classattr">

#### dc_title: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_title"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>A name given to the CHO. dc:title should be present; but if there is no dc:title avail
able, it is acceptable to have dc:description instead. dc:title and dc:description sho
uld be distinct. Exact translations of the title can be  provided using appropriate xm
l language attributes. <dc:title xml:lang=“en”&gt;Eight Weeks</dc:title> <dc:title xml:la
ng=“it”&gt;Ocho semanas</ dc:title></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dc_type" class="classattr">

#### dc_type: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dc_type"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The nature or genre of the CHO. Ideally the term(s) will be taken from a controlled vo
cabulary. One of dc:type or dc:subject or dcterms:spatial or dcterms:temporal must be 
provided; if more than one of these properties is available, please provide them all. 
dc:type should not be (strictly) identical to edm:type. <dc:type>Book</dc:type> or <dc
:type>trombone</dc:type> or create a reference to an instance of the Concept class <dc
:type rdf:resource=“http://www.mimo-­db.eu/HornbostelAndSachs/356/”&gt;For recommendation
s on medata quality see Tier A-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_alternative" class="classattr">

#### dcterms_alternative: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_alternative"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Any alternative title of the CHO including abbreviations or translations that may not 
be exact. <dcterms:alternativexml:lang=“en”&gt;Eight weeks: a novel</dcterms:alternative></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_conformsTo" class="classattr">

#### dcterms_conformsTo: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_conformsTo"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>An established standard to which the CHO conforms. <dcterms:conformsTo>W3C WCAG 2.0</d
cterms:conformsTo> (conforms to web content accessibility guidelines). Or link to the 
resource <dcterms:conformsTo rdf:resource=“http://www.w3.org/TR/WCAG/”/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_created" class="classattr">

#### dcterms_created: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_created"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The date of creation of the CHO. Europeana recommends date conforming to ISO 8601 star
ting with the year and with hyphens (YYYY-­MM-DD). NB: other EDM elements are relevant
for expressing dates of different events in the life of the CHO: dc:date, dcterms:tem
poral and dcterms:issued. Be careful and choose the most appropriate one! <dcterms:cre
ated>Mid 16th century</dcterms:created> or <dcterms:created>1584</dcterms:created> or 
create a reference to an instance of the TimeSpan class<dcterms:created rdf:resource=“
http://semium.org/time/15xx_3_third”/>For recommendations on medata quality see Tier A
-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_extent" class="classattr">

#### dcterms_extent: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_extent"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The size or duration of the CHO. <dcterms:extent>13 cm</dcterms:extent> (the width of 
an original object). <dcterms:extent>34 minutes</dcterms:extent> (the duration of an a
udio file)</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_hasFormat" class="classattr">

#### dcterms_hasFormat: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_hasFormat"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A resource related to the CHO that is substantially the same as the CHO but in another
format. <dcterms:hasFormat><a href="http://upload.wikimedia.org/wikipedia/en/f/f3/Europeana_lo">http://upload.wikimedia.org/wikipedia/en/f/f3/Europeana_lo</a>
go.png</dcterms:hasFormat> for a png image file of the described tiff resource Or as a
link to a resource <dcterms:hasFormat rdf:resource=“<a href="http://upload.wikimedia.org/wikip">http://upload.wikimedia.org/wikip</a>
edia/en/f/f3/Europeana_logo.png’’/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_hasPart" class="classattr">

#### dcterms_hasPart: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_hasPart"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A resource that is included either physically or logically in the CHO. It is possible 
to use either dcterms:isPartOf or dcterms:hasPart to express relation between objects 
in a hierarchy. However in many cases (especially when a parent object has many childr
en) it is preferable to use dcterms:isPartOf. <dcterms:hasPart>Vol.2. Issue 1</dcterms
:hasPart></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_hasVersion" class="classattr">

#### dcterms_hasVersion: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_hasVersion"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another, later resource that is a version, edition or adaptation of the CHO demonstrat
ing substantive changes in content rather than format. <dcterms:hasVersion>The Sorcere
r’s Apprentice (translation by Edwin Zeydel, 1955)</dcterms:hasVersion> In this exampl
e the 1955 translation is a version of the described resource.</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_isFormatOf" class="classattr">

#### dcterms_isFormatOf: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_isFormatOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another resource that is substantially the same as the CHO but in another format. <dct
erms:isFormatOf>Europeana_logo.tiff</dcterms:isFormatOf> where the resource being desc
ribed is a png image file</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_isPartOf" class="classattr">

#### dcterms_isPartOf: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_isPartOf"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A resource in which the CHO is physically or logically included. This property can be 
used for objects that are part of a hierarchy and will be used to support an appropria
te display in the portal. For that purpose it will be necessary to supply a reference 
as the value. See the Task Force report on representing hierarchical entities.  It is 
possible to use either dcterms:isPartOf or dcterms:hasPart to express relation between
objects in a hierarchy. However in many cases (especially when a parent object has ma
ny children) it is preferable to use dcterms:isPartOf. <dcterms:isPartOf>Crace Collect
ion of Maps of London</dcterms:isPartOf></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_isReferencedBy" class="classattr">

#### dcterms_isReferencedBy: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_isReferencedBy"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another resource that references, cites or otherwise points to the CHO. <dcterms:isRef
erencedBy>Till, Nicholas (1994) Mozart and the Enlightenment: Truth, Virtue and Beauty
in Mozart’s Operas, W. W. Norton &amp; Company</dcterms:isReferencedBy></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_isReplacedBy" class="classattr">

#### dcterms_isReplacedBy: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_isReplacedBy"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another resource that supplants , displaces, or supersedes the CHO. <dcterms:isReplace
dBy><a href="http://dublincore.org/about/2009/01/05/bylaws/">http://dublincore.org/about/2009/01/05/bylaws/</a></dcterms:isReplacedBy> where the re
source described is an older version (<a href="http://dublincore.org/about/2006/01/01/bylaws/">http://dublincore.org/about/2006/01/01/bylaws/</a>) 
or link <dcterms:isReplacedBy rdf:resource=“<a href="http://dublincore.org/about/2009/01/05/byl">http://dublincore.org/about/2009/01/05/byl</a>
aws/”/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_isRequiredBy" class="classattr">

#### dcterms_isRequiredBy: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_isRequiredBy"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another related resource that requires the CHO to support its function, delivery or co
herence <isRequiredBy><a href="http://www.myslides.com/myslideshow.ppt">http://www.myslides.com/myslideshow.ppt</a></isRequiredBy> where the
image being described is required for an online slideshow.</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_issued" class="classattr">

#### dcterms_issued: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_issued"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Date of formal issuance or publication of the CHO. Europeana recommends date conformin
g to ISO 8601  starting with the year and with hyphens (YYYY-­MM-DD). NB: other EDM el
ements are relevant for expressing dates of different events in the life of the CHO: d
c:date, dcterms:temporal and dcterms:created. Be careful and choose the most appropria
te one! <dcterms:issued>1993</dcterms:issued> or create a reference to an instance of 
the TimeSpan class <dcterms:issued rdf:resource=“<a href="http://semium.org/time/17xx_3_third”/">http://semium.org/time/17xx_3_third”/</a></p>

<blockquote>
<p>(late 18th century)For recommendations on medata quality see Tier A-C requirements .</p>
</blockquote>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_isVersionOf" class="classattr">

#### dcterms_isVersionOf: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_isVersionOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another, earlier resource of which the CHO is a version, edition or adaptation, demons
trating substantive changes in content rather than format. <dcterms:isVersionOf>The So
rcerer’s Apprentice<dcterms:isVersionOf>In this example The Sorcerer’s Apprentice (tra
nslation by Edwin Zeydel, 1955) is the resource being described.</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_medium" class="classattr">

#### dcterms_medium: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_medium"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The material or physical carrier of the CHO.  <dcterms:medium>metal</dcterms:medium>Fo
r recommendations on medata quality see Tier A-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_provenance" class="classattr">

#### dcterms_provenance: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_provenance"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A statement of changes in ownership and custody of the CHO since its creation. Signifi
cant for authenticity, integrity and interpretation. <dcterms:provenance>Donated to Th
e National Library in 1965</dcterms:provenance></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_references" class="classattr">

#### dcterms_references: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_references"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Other resources referenced, cited or otherwise pointed to by the CHO. <dcterms:referen
ces>Honderd jaar Noorse schilderkunst </dcterms:references></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_replaces" class="classattr">

#### dcterms_replaces: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_replaces"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A related resource that is supplanted, displaced, or superseded by the CHO. <dcterms:r
eplaces><a href="http://dublincore.org/about/2006/01/01/bylaws/">http://dublincore.org/about/2006/01/01/bylaws/</a></dcterms:replaces> where the re
source described is a newer version (<a href="http://dublincore.org/about/2009/01/05/bylaws/">http://dublincore.org/about/2009/01/05/bylaws/</a>) o
r link to resource <dcterms:replaces rdf:resource=“<a href="http://dublincore.org/about/2006/01">http://dublincore.org/about/2006/01</a>
/01/bylaws/”/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_requires" class="classattr">

#### dcterms_requires: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_requires"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another resource that is required by the described resource to support its function, d
elivery or coherence. <dcterms:requires><a href="http://ads.ahds.ac.uk/project/userinfo/css/old">http://ads.ahds.ac.uk/project/userinfo/css/old</a>
browsers.css </dcterms:requires> where the resource described is an HTML file at http:
//ads.ahds.ac.uk/project/userinfo/digitalTextArchiving.html</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_spatial" class="classattr">

#### dcterms_spatial: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_spatial"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Spatial characteristics of the CHO. i.e. what the CHO represents or depicts in terms o
f space (e.g. a location, coordinate or place). Either dcterms:spatial or dc:type or d
c:subject or dcterms:temporal must be provided; if more than one of these properties i
s available, please provide them all. dcterms:spatial is used to record the place depi
cted in the CHO and other locations associated with it as opposed to edm:currentLocati
on which is used only to record the place where the CHO is currently held (e.g. a muse
um or gallery). Be careful to choose the most appropriate one! <dcterms:spatial>Portug
al</dcterms:spatial> or create a reference to an instance of the Place class <dcterms:
spatial rdf:resource=“<a href="https://sws.geonames.org/2264397/">https://sws.geonames.org/2264397/</a> ”/>For recommendations on meda
ta quality see Tier A-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_tableOfContents" class="classattr">

#### dcterms_tableOfContents: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_tableOfContents"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>A list of sub‐units of the CHO.<dcterms:tableOfContents>Chapter 1. Introduction, Chapt
er 2. History </dcterms:tableOfContents></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.dcterms_temporal" class="classattr">

#### dcterms_temporal: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.dcterms_temporal"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Temporal characteristics of the CHO. i.e. what the CHO is about or depicts in terms of
time (e.g. a period, date or date range.) Either dcterms:temporal or dc:type or dc:su
bject or dcterms:spatial must be provided; if more than one of these properties is ava
ilable, please provide them all. Europeana recommends date conforming to ISO 8601 star
ting with the year and with hyphens (YYYY-MM-DD). NB: other EDM elements are relevant 
for expressing dates of different events in the life of the CHO: dc:date, dcterms:crea
ted and dcterms:issued. Be careful and choose the most appropriate one! <dcterms:tempo
ral>Roman Empire</dcterms:temporal> or create a reference to an instance of the TimeSp
an class <dcterms:temporal rdf:resource=“http://semium.org/time/roman_empire”/>For rec
ommendations on medata quality see Tier A-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_currentLocation" class="classattr">

#### edm_currentLocation: Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref, NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_currentLocation"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Union[Lit, Ref]]</p>

<p>Description: </p>

<p>The geographic location whose boundaries presently include the CHO. This location must
have a position within an established positioning system: a location with coordinates
or address or inside another location that has a position, such as a room within a (m
useum) building. Ideally this position should be provided with the value of the proper
ty, either by using a reference (to a Place entity) that has coordinates or an address
attribute, or as a simple Lit. edm:currentLocation is used only to record the pla
ce where the CHO is currently held (e.g. a museum or gallery)dcterms:spatial is used t
o record the place depicted in the CHO and other locations associated with itBe carefu
l to choose the most appropriate one!<edm:currentLocation rdf:resource=“<a href="https://sws.ge">https://sws.ge</a>
onames.org/2950159/”&gt; (Identifier for Berlin)For recommendations on medata quality see
Tier A-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_hasMet" class="classattr">

#### edm_hasMet: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_hasMet"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of an agent, a place, a time period or any other identifiable entity th
at the CHO may have “met” in its life. <edm:hasMet rdf:resource=“<a href="http://viaf.org/viaf/">http://viaf.org/viaf/</a>
96994048/”&gt; (Identifier for William Shakespeare) <edm:hasMet rdf:resource=“<a href="https://sws">https://sws</a>
.geonames.org/6620265/ ”&gt; (location identifier for Shakespeare’s Globe theatre.)For re
commendations on medata quality see Tier A-C requirements .</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_hasType" class="classattr">

#### edm_hasType: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_hasType"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The identifier of a concept, or a word or phrase from a controlled vocabulary (thesaur
us etc) giving the type of the CHO. E.g. Painting from the AAT thesaurus. This propert
y can be seen as a super-­property of e.g. dc:format or dc:type to support “What” ques
tions. <edm:hasType>Painting</edm:hasType></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_incorporates" class="classattr">

#### edm_incorporates: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_incorporates"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of another resource that is incorporated in the described CHO. E.g. the
movie “A Clockwork Orange” incorporates Rossini’s La Gazza Ladra” in its soundtrack. 
<edm:incorporates rdf:resource=“http://www.identifier/IncorporatedResource/“&gt;</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_isDerivativeOf" class="classattr">

#### edm_isDerivativeOf: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_isDerivativeOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of another resource from which the described CHO has been derived. E.g.
the identifier of Moby Dick when the Italian translation is the described CHO. <edm:i
sDerivativeOf rdf:resource=“http://www.identifier/SourceResource/”&gt;</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_isNextInSequence" class="classattr">

#### edm_isNextInSequence: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_isNextInSequence"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of the preceding object where both objects are part of the same overall
resource. Use this for objects that are part of a hierarchy or sequence to ensure cor
rect display in the portal. <edm:isNextInSequence rdf:resource=“<a href="http://www.identifier/">http://www.identifier/</a>
PrecedingResource”/</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_isRelatedTo" class="classattr">

#### edm_isRelatedTo: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_isRelatedTo"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The identifier or name of a concept or other resource to which the described CHO is re
lated. E.g. Moby Dick is related to XIX Century literature. Cf dc:relation. <edm:isRel
atedTo>Literature</edm:isRelatedTo> Or link to resource <edm:isRelatedTo rdf:resource=
“http://www.eionet.europa.eu/gemet/concept?cp=4850/”&gt;</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_isRepresentationOf" class="classattr">

#### edm_isRepresentationOf: Optional[edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_isRepresentationOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Ref]</p>

<p>Description: </p>

<p>The identifier of another object of which the described CHO is a representation. E.g. 
the identifier of the statue when the CHO being described is a painting of that statue
. <edm:isRepresentativeOf rdf:resource=“http://www.identifier/RepresentedResource/”&gt;</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_isSimilarTo" class="classattr">

#### edm_isSimilarTo: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_isSimilarTo"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of another resource to which the described CHO is similar. <edm:isSimil
arTo rdf:resource=“http://www.identifier/SimilarResource”/></p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_isSuccessorOf" class="classattr">

#### edm_isSuccessorOf: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_isSuccessorOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of a resource to which the described CHO is a successor. E.g. “The Two
Towers” is a successor of “Fellowship of the Ring”. <edm:isSuccessorOf rdf:resource=“
http://dbpedia.org/resource/The_Fellowship_of_the_Ring/”&gt;</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.edm_realizes" class="classattr">

#### edm_realizes: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.edm_realizes"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>If the CHO described is of type edm:PhysicalThing it may realize an information object
. E.g. a copy of the Gutenberg publication realizes the Bible.</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.owl_sameAs" class="classattr">

#### owl_sameAs: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_ProvidedCHO.owl_sameAs"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Use to point to your own (linked data) representation of the object, if you have already minted a URI identifier for it. It is also possible to provide URIs minted by third-parties for the object. <owl:sameAs rdf:resource=“http://www.identifier/SameResourceElsewhere/”&gt;</p>
</div> 

</div>
<div id="EDM_ProvidedCHO.validate_dependent_edm" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_dependent_edm(self) -&gt; Self  

<a class="headerlink" href="#EDM_ProvidedCHO.validate_dependent_edm"></a>



</div>
<div id="EDM_ProvidedCHO.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#EDM_ProvidedCHO.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="ORE_Aggregation">

###    class ORE_Aggregation<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#ORE_Aggregation"></a>

<div class="docstring"><p>ORE Aggregation</p>

<p>mandatory-properties: EDM_aggregatedCHO, EDM_dataProvider, EDM_isShownAt, EDM_isShownBy, EDM_provider, EDM_rights</p>

<p>optional-properties: EDM_hasView, DC_rights, EDM_ugc</p>

<p>recommended-properties: EDM_object, EDM_intermediateProvider</p>
</div> 

<div id="ORE_Aggregation.edm_aggregatedCHO" class="classattr">

#### edm_aggregatedCHO: edmlib.edm.value_types.Ref 

<a class="headerlink" href="#ORE_Aggregation.edm_aggregatedCHO"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
exactly_one</p>

<p>Value-Type:
Ref</p>

<p>Description: </p>

<p>The identifier of the source object e.g. the Mona Lisa itself. This could be a full li
nked open data URI or an internal identifier. <edm:aggregatedCHO rdf:resource=“#UEDIN:
214”/></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_dataProvider" class="classattr">

#### edm_dataProvider: Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#ORE_Aggregation.edm_dataProvider"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
exactly_one</p>

<p>Value-Type:
Union[Lit, Ref]</p>

<p>Description: </p>

<p>The name or identifier of the data provider of the object (i.e. the organisation provi
ding data to an aggregator). Identifiers will not be available until Europeana has imp
lemented its Organization profile.  In the case of the data provider Zuidwestbrabants 
Museum, which delivers data through Erfgoedplus.be to LoCloud, the properties would lo
ok like this: <edm:dataProvider>Zuidwestbrabants  Museum</edm:dataProvider> <edm:inter
mediateProvider>Erfgoedplus.be</edm:intermediateProvider> <edm:provider>LoCloud</edm:p
rovider></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_provider" class="classattr">

#### edm_provider: Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#ORE_Aggregation.edm_provider"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
exactly_one</p>

<p>Value-Type:
Union[Lit, Ref]</p>

<p>Description: </p>

<p>The name or identifier of the provider of the object (i.e. the organisation providing 
data directly to Europeana). Identifiers will not be available until Europeana has imp
lemented its Organization profile.  In the case of the provider LoCloud, which collect
s data from the data provider Zuidwestbrabants Museum through Erfgoedplus.be, the prop
erties would look like this: <edm:dataProvider>Zuidwestbrabants Museum</edm:dataProvid
er> <edm:intermediateProvider>Erfgoedplus.be</edm:intermediateProvider><edm:provider>L
oCloud</edm:provider></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_rights" class="classattr">

#### edm_rights: edmlib.edm.value_types.Ref 

<a class="headerlink" href="#ORE_Aggregation.edm_rights"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
exactly_one</p>

<p>Value-Type:
Ref</p>

<p>Description: </p>

<p>This is a mandatory property and the value given here should be the rights statement t
hat applies to the digital representation as given (for example) in edm:object or edm:
isShownAt/By, when these resources are not provided with their own edm:rights (see edm
:rights documentation). The value for the rights statement in this element must be a U
RI from the list of available values. Note: rights statements must be exactly as speci
fied there, which means they must start with http and not https. (For assesing rights 
imformation check <a href="https://pro.europeana.eu/page/available-rights-statements">https://pro.europeana.eu/page/available-rights-statements</a> ) The righ
ts statement given in this property will also by default apply to the previews used in
the portal and will support portal search and display functionality.  Where there are
several web resources attached to one edm:ProvidedCHO the rights statement given here
will be regarded as the “reference” value for all the web resources. Therefore a suit
able value should be chosen with care if the rights statements vary between different 
resources. In fact in such cases Europeana encourages the provision of separate rights
statements for each individual web resource. Please note that the object page on http
://europeana.eu   displays the rights of the digital representation selected in the vi
ewer, which is found in the edm:rights of the WebResource that corresponds to the sele
cted edm:isShownBy or edm:hasView. If there is no such edm:isShownBy or edm:hasView re
presentation available, or if there is one but there is no specific edm:rights attache
d to it, then by default the page displays the edm:rights attached to the ore:Aggregat
ion.For example, a low­‐resolution of a JPEG file could be CC‐BY, while the high resol
ution version or a video showing the object would be CC-­BY-­NC. In such cases the rig
hts statements given for the individual web resources would ‘override’ the one specifi
ed at the ore:Aggregation level. Any other associated web resources would still be gov
erned by the edm:rights of the ore:Aggregation.   <edm:rights rdf:resource=“<a href="http://cre">http://cre</a>
ativecommons.org/publicdomain/mark/1.0/”/> <edm:rights rdf:resource=“<a href="http://rightsstat">http://rightsstat</a>
ements.org/vocab/InC/1.0/”/>  Or create a reference to an instance of the cc:License c
lass where additional details of the rights can be provided (such as an expiry date fo
r the restrictions): <a href="http://rightsstatements.org/vocab/NoC-­NC/1.0/">http://rightsstatements.org/vocab/NoC-­NC/1.0/</a> or <edm:rights rdf
:resource="#statement_3000095353971"/></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_hasView" class="classattr">

#### edm_hasView: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#ORE_Aggregation.edm_hasView"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The URL of a web resource which is a digital representation of the CHO. This may be th
e source object itself in the case of a born digital cultural heritage object. edm:has
View should only be used where there are several views of the CHO and one (or both) of
the mandatory edm:isShownAt or edm:isShownBy properties have already been used. It is
for cases where one CHO has several views of the same object. (e.g. a shoe and a deta
il of the label of the shoe)  <edm:hasView rdf:resource="<a href="http://www.mimo‐db.eu/media/U">http://www.mimo‐db.eu/media/U</a>
EDIN/VIDEO/0032195v.mpg"/> <edm:hasView rdf:resource="<a href="http://www.mimo-­db.eu/media/UED">http://www.mimo-­db.eu/media/UED</a>
IN/AUDIO/0032195s.mp3"/></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_isShownAt" class="classattr">

#### edm_isShownAt: Optional[edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#ORE_Aggregation.edm_isShownAt"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Ref]</p>

<p>Description: </p>

<p>The URL of a web view of the object in full information context. An edm:isShownAt must
be provided. If there is no edm:isShownAt for an object, there must be a edm:isShownB
y. If both are available, provide both. The use of edm:isShownBy is preferred. Providi
ng an edm:isShownAt is strongly recommended in all cases.<edm:isShownAt rdf:resource="
http://www.mimo-­‐db.eu/UEDIN/214"/></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_isShownBy" class="classattr">

#### edm_isShownBy: Optional[edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#ORE_Aggregation.edm_isShownBy"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Ref]</p>

<p>Description: </p>

<p>The URL of a web view of the object. An edm:isShownBy must be provided. If there is no
edm:isShownBy for an object, there must be a edm:isShownAt. The use of edm:isShownBy 
is preferred. Europeana generates previews for any direct link to an image file. See E
uropeana Media Policy or information regarding the specifications of previews. <edm:is
ShownBy rdf:resource="http://www.mimo‐db.eu/media/UEDIN/IMAGE/0032195c.jpg"/></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_object" class="classattr">

#### edm_object: Optional[edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#ORE_Aggregation.edm_object"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Ref]</p>

<p>Description: </p>

<p>The URL of a representation of the CHO which will be used for generating previews for 
use in the Europeana portal. This may be the same URL as edm:isShownBy.See Europeana M
edia Policy for information regarding the specifications of previews. This must be an 
image, even if it is for a sound object. <edm:object rdf:resource="<a href="http://www.mimo-‐db">http://www.mimo-‐db</a>
.eu/media/UEDIN/IMAGE/0032195c.jpg"/>In accordance with Europeana's 2023 data publicat
ion approach, objects with edm:type=IMAGE that have no edm:isShownBy nor edm:object wi
ll not be published in Europeana. (See also ContentTier 1: Image type )</p>
</div> 

</div>
<div id="ORE_Aggregation.dc_rights" class="classattr">

#### dc_rights: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#ORE_Aggregation.dc_rights"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Ideally this should be applied to the edm:WebResource or the edm:ProvidedCHO. It is in
cluded here for the conversion of data from ESE where it is not known which object the
rights apply to.</p>
</div> 

</div>
<div id="ORE_Aggregation.edm_ugc" class="classattr">

#### edm_ugc: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#ORE_Aggregation.edm_ugc"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>This is a mandatory property for objects that are user generated or user created that 
have been collected by crowdsourcing or project activity. The property is used to iden
tify such content and can only take the value “true” (lower case). <edm:ugc>true</edm:
ugc></p>
</div> 

</div>
<div id="ORE_Aggregation.edm_intermediateProvider" class="classattr">

#### edm_intermediateProvider: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#ORE_Aggregation.edm_intermediateProvider"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The name or identifier of the intermediate organization that selects, collates, or cur
ates data from a Data Provider that is then aggregated by a Provider from which Europe
ana harvests. The Intermediate Provider must be distinct from both the Data Provider a
nd the Provider in the data supply chain. Identifiers will not be available until Euro
peana has implemented its Organization profile. In the case of the Erfgoedplus.be, whi
ch collects data from Zuidwestbrabants Museum and provides it to LoCloud, the properti
es would look like this: <edm:dataProvider>Zuidwestbrabants Museum</edm:dataProvider> 
<edm:provider>LoCloud</edm:provider> <edm:intermediateProvider>Erfgoedplus.be</edm:int
ermediateProvider></p>
</div> 

</div>
<div id="ORE_Aggregation.validate_conditional_attributes" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_conditional_attributes(self) -&gt; Self  

<a class="headerlink" href="#ORE_Aggregation.validate_conditional_attributes"></a>



</div>
<div id="ORE_Aggregation.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#ORE_Aggregation.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="EDM_WebResource">

###    class EDM_WebResource<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#EDM_WebResource"></a>

<div class="docstring"><p>optional-properties: DC_creator, DC_description, DC_format, DC_rights, DC_source, DC_type, DCTERMS_conformsTo, DCTERMS_created, DCTERMS_extent, DCTERMS_hasPart, DCTERMS_isFormatOf, DCTERMS_isPartOf, DCTERMS_isReferencedBy, DCTERMS_issued, EDM_isNextInSequence, OWL_sameAs, SVCS_has_service, DCTERMS_IsReferencedBy</p>

<p>recommended-properties: EDM_rights</p>
</div> 

<div id="EDM_WebResource.dc_creator" class="classattr">

#### dc_creator: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dc_creator"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>For the creator of the web resource. If possible supply the identifier of the creator 
from an authority source. Repeat for multiple creators. <dc:creator xml:lang=“es”&gt;Bibl
icoteca Nacional de España</dc:creator> or create a reference to an instance of the Ag
ent class <dc:creator rdf:resource=“http://viaf.org/viaf/147143794/”/></p>
</div> 

</div>
<div id="EDM_WebResource.dc_description" class="classattr">

#### dc_description: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dc_description"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Use for an account or description of this digital representation <dc:description>Perfo
rmance with Buccin trombone</dc:description></p>
</div> 

</div>
<div id="EDM_WebResource.dc_format" class="classattr">

#### dc_format: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dc_format"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Use for the format of this digital representation. (Use the value “3D‐PDF” if appropri
ate.)<dc:format>image/jpeg</dc:format></p>
</div> 

</div>
<div id="EDM_WebResource.dc_rights" class="classattr">

#### dc_rights: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dc_rights"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Use for the name of the rights holder of this digital representation if possible or fo
r more general rights information. Note the difference between this property and the m
andatory, controlled edm:rights property below. <dc:rights> Copyright © British Librar
y Board</dc:rights></p>
</div> 

</div>
<div id="EDM_WebResource.dc_source" class="classattr">

#### dc_source: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dc_source"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A related resource from which the Web resource is derived in whole or in part. <dc:sou
rce>The name of the source video tape <dc:source></p>
</div> 

</div>
<div id="EDM_WebResource.dc_type" class="classattr">

#### dc_type: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dc_type"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The nature or genre of the digital representation. Ideally the term(s) will be taken f
rom a controlled vocabulary.dc:type should not be (strictly) identical to edm:type. <d
c:type>video</dc:type> or create a reference to an instance of the Concept class <dc:t
ype rdf:about= “<a href="http://schema.org/VideoObject”">http://schema.org/VideoObject”</a> &gt;</p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_conformsTo" class="classattr">

#### dcterms_conformsTo: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dcterms_conformsTo"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>An established standard to which the web resource conforms. <dcterms:conformsTo>W3C WC
AG 2.0</dcterms:conformsTo> (web content accessibility guidelines).</p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_created" class="classattr">

#### dcterms_created: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dcterms_created"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Date of creation of the Web resource. Europeana recommends date conforming to ISO 8601
starting with the year and with hyphens (YYYY-MM-DD). <dcterms:created>2010</dcterms:
created> or create a reference to an instance of the TimeSpan class <dc:date rdf:resou
rce=“http://semium.org/time/2010”/></p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_extent" class="classattr">

#### dcterms_extent: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dcterms_extent"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The size or duration of the digital resource. <dcterms:extent>1h 26 min 41 sec</dcterm
s:extent></p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_hasPart" class="classattr">

#### dcterms_hasPart: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_WebResource.dcterms_hasPart"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>A resource that is included either physically or logically in the web resource. <dcter
ms:hasPart rdf:resource=“http://www.identifier/Part”/></p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_isFormatOf" class="classattr">

#### dcterms_isFormatOf: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dcterms_isFormatOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Another resource that is substantially the same as the web resource but in another for
mat.  <dcterms:isFormatOf><a href="http://upload.wikimedia.org/wikipedia/en/f/f3/Europeana_logo">http://upload.wikimedia.org/wikipedia/en/f/f3/Europeana_logo</a>
.png</dcterms:isFormatOf> for a png image file of the described tiff web resource. Or 
as a link to a resource <dcterms:isFormatOf rdf:resource=“<a href="http://upload.wikimedia.org/">http://upload.wikimedia.org/</a>
wikipedia/en/f/f3/Europeana_logo.png”/></p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_isPartOf" class="classattr">

#### dcterms_isPartOf: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_WebResource.dcterms_isPartOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>A resource in which the WebResource is physically or logically included. This property
can be used for web resources that are part of a hierarchy. Hierarchies can be repres
ented as hierarchies of ProvidedCHOs or hierarchies of web resources but not both at t
he same time. See the Task Force report on representing hierarchical entities. <dcterm
s:isPartOf rdf:resource=“<a href="http://data.europeana.eu/item/08701/1B0BACAA44D5A807E43D9B411">http://data.europeana.eu/item/08701/1B0BACAA44D5A807E43D9B411</a>
C9781AAD2F96E65”/></p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_isReferencedBy" class="classattr">

#### dcterms_isReferencedBy: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dcterms_isReferencedBy"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A related resource that references, cites, or otherwise points to the described resour
ce. In a IIIF implementation, dcterms:isReferencedBy can be used to connect a edm:WebR
esource to a IIIF manifest URI. <dcterms:isReferencedBy rdf:resource="<a href="https://gallica">https://gallica</a>.
bnf.fr/iiif/ark:/12148/btv1b55001425m/manifest.json"/></p>
</div> 

</div>
<div id="EDM_WebResource.dcterms_issued" class="classattr">

#### dcterms_issued: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_WebResource.dcterms_issued"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>Date of formal issuance or publication of the web resource. Europeana recommends date 
conforming to ISO 8601 starting with the year and with hyphens (YYYY‐MM-DD). <dcterms:
issued>1999</dcterms:issued> or create a reference to an instance of the TimeSpan clas
s<dcterms:issued rdf:resource=“http://semium.org/time/2010”/></p>
</div> 

</div>
<div id="EDM_WebResource.edm_isNextInSequence" class="classattr">

#### edm_isNextInSequence: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_WebResource.edm_isNextInSequence"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Where one CHO has several web resources, shown by multiple instances of the edm:hasVie
w property on the ore:Aggregation this property can be used to show the sequence of th
e objects. Each web resource (apart from the first in the sequence) should use this pr
operty to give the URI of the preceding resource in the sequence.</p>
</div> 

</div>
<div id="EDM_WebResource.edm_rights" class="classattr">

#### edm_rights: Optional[edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#EDM_WebResource.edm_rights"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Ref]</p>

<p>Description: </p>

<p>The value in this element will indicate the copyright, usage and access rights that ap
ply to this digital representation. It is strongly recommended that a value is supplie
d for this property for each instance of a web resource.The value for the rights state
ment in this element must be a URI from the list of available values. Note: rights sta
tements must be exactly as specified there, which means they must start with http and 
not https. The rights statement specified at the level of the web resource will ‘overr
ide’ the statement specified at the level of the aggregation. <edm:rights rdf:resource
=“http://creativecommons.org/publicdomain/mark/1.0/”/> <edm:rights rdf:resource=“http:
//rightsstatements.org/vocab/InC/1.0/”/>  Or create a reference to an instance of the 
cc:License class where additional details of the rights can be provided (such as an ex
piry date for the restrictions): <a href="http://rightsstatements.org/vocab/NoC-NC/1.0/or">http://rightsstatements.org/vocab/NoC-NC/1.0/or</a> <edm:
rights rdf:resource="#statement_3000095353971"/>This is a recommended property.</p>
</div> 

</div>
<div id="EDM_WebResource.owl_sameAs" class="classattr">

#### owl_sameAs: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_WebResource.owl_sameAs"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Provide the URI of another web representation of the same resource. <owl:sameAs rdf:re
source=”urn:soundcloud:150424305></p>
</div> 

</div>
<div id="EDM_WebResource.svcs_has_service" class="classattr">

#### svcs_has_service: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_WebResource.svcs_has_service"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<pre><code>Cardinality: 
zero_to_many

Value-Type:
Optional[List[Ref]]

Description: 

The identifier of the svcs:Service required to consume the edm:WebResource. Example:
</code></pre>

<p><svcs:has_service rdf:resource="http://www.example.org/Service/IIIF"></p>
</div> 

</div>
<div id="EDM_WebResource.validate_web_resource" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_web_resource(self) -&gt; Self  

<a class="headerlink" href="#EDM_WebResource.validate_web_resource"></a>



</div>
<div id="EDM_WebResource.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#EDM_WebResource.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="CC_License">

###    class CC_License<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#CC_License"></a>

<div class="docstring"><p>mandatory-properties: ODRL_inheritFrom</p>

<p>optional-properties: CC_deprecatedOn</p>
</div> 

<div id="CC_License.odrl_inheritFrom" class="classattr">

#### odrl_inheritFrom: edmlib.edm.value_types.Ref 

<a class="headerlink" href="#CC_License.odrl_inheritFrom"></a>

<div class="docstring"><p>Mandate: 
mandatory</p>

<p>Cardinality: 
exactly_one</p>

<p>Value-Type:
Ref</p>

<p>Description: </p>

<p>ID of a base rights statement from which the described License is derived. This value 
must come for alist of statements controlled by Europeana.<odrl:inheritFrom rdf:resour
ce=“http://rightsstatements.org/vocab/NoC-­NC/1.0/”/></p>
</div> 

</div>
<div id="CC_License.cc_deprecatedOn" class="classattr">

#### cc_deprecatedOn: Any 

<a class="headerlink" href="#CC_License.cc_deprecatedOn"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Any</p>

<p>Description: </p>

<p>The date that the license expires, as it has been described, which implies among other
things the expiration of the restrictions specified by the license.<cc:deprecatedOn r
df:datatype=”http://www.w3.org/2001/XMLSchema#date”&gt;2029‐06-­01</cc:deprecatedOn> Note
this datatype is mandatory for cc:deprecatedOn.</p>
</div> 

</div>
<div id="CC_License.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#CC_License.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="SKOS_Concept">

###    class SKOS_Concept<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#SKOS_Concept"></a>

<div class="docstring"><p>optional-properties: SKOS_broader, SKOS_narrower, SKOS_related, SKOS_broadMatch, SKOS_narrowMatch, SKOS_relatedMatch, SKOS_exactMatch, SKOS_closeMatch, SKOS_note, SKOS_notation, SKOS_inScheme</p>

<p>recommended-properties: SKOS_prefLabel, SKOS_altLabel</p>
</div> 

<div id="SKOS_Concept.skos_prefLabel" class="classattr">

#### skos_prefLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#SKOS_Concept.skos_prefLabel"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>The preferred form of the name of the concept. Although the maximum number of occurren
ces is set at 1, it can be interpreted as 1 per language tag. At least one skos:prefLa
bel SHOULD be provided. Several prefLabels with languages tags are strongly recommende
d for language variants and translations.This is a recommended property for this class
.<skos:prefLabel xml:lang="fr">Buccin</skos:prefLabel><skos:prefLabel xml:lang="de">Bu
ccin</skos:prefLabel><skos:prefLabel xml:lang="nl">Buccin</skos:prefLabel>For recommen
dations on medata quality see Tier A-C requirements , more specifically Metadata Tier 
B and Metadata Tier C</p>
</div> 

</div>
<div id="SKOS_Concept.skos_altLabel" class="classattr">

#### skos_altLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#SKOS_Concept.skos_altLabel"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Alternative forms of the name of the concept. Recommended unless several prefLabel are
already given with different language tags (altLabel is not suitable for translations
of prefLabel).<skos:altLabel xml:lang="en">Buccin</skos:altLabel>This is a recommende
d property for this class.</p>
</div> 

</div>
<div id="SKOS_Concept.skos_broader" class="classattr">

#### skos_broader: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_broader"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of a broader concept in the same thesaurus or controlled vocabulary.<sk
os:broader rdf:resource=“<a href="http://www.mimo-db.eu/InstrumentsKeywords/4369_1">http://www.mimo-db.eu/InstrumentsKeywords/4369_1</a> ”/>For recom
mendations on medata quality see Tier A-C requirements , more specifically Metadata Ti
er B and Metadata Tier C</p>
</div> 

</div>
<div id="SKOS_Concept.skos_narrower" class="classattr">

#### skos_narrower: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_narrower"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of a narrower concept.<skos:narrower rdf:resource=“<a href="http://narrower.term">http://narrower.term</a>
/”/>For recommendations on medata quality see Tier A-C requirements , more specificall
y Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="SKOS_Concept.skos_related" class="classattr">

#### skos_related: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_related"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of a related concept<skos:related rdf:resource=“http://related.term/”/>
For recommendations on medata quality see Tier A-C requirements , more specifically Me
tadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="SKOS_Concept.skos_broadMatch" class="classattr">

#### skos_broadMatch: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_broadMatch"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of a broader, narrower or related matching concepts from other concept 
schemes.<skos:broadMatch rdf:resource=“http://broadMatch.term/”/><skos:narrowMatch rdf
:resource=“http://narrowMatch.term/”/><skos:relatedMatch rdf:resource=“<a href="http://relatedM">http://relatedM</a>
atch.term/”/></p>
</div> 

</div>
<div id="SKOS_Concept.skos_narrowMatch" class="classattr">

#### skos_narrowMatch: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_narrowMatch"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of a broader, narrower or related matching concepts from other concept 
schemes.<skos:broadMatch rdf:resource=“http://broadMatch.term/”/><skos:narrowMatch rdf
:resource=“http://narrowMatch.term/”/><skos:relatedMatch rdf:resource=“<a href="http://relatedM">http://relatedM</a>
atch.term/”/></p>
</div> 

</div>
<div id="SKOS_Concept.skos_relatedMatch" class="classattr">

#### skos_relatedMatch: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_relatedMatch"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of a broader, narrower or related matching concepts from other concept 
schemes.<skos:broadMatch rdf:resource=“http://broadMatch.term/”/><skos:narrowMatch rdf
:resource=“http://narrowMatch.term/”/><skos:relatedMatch rdf:resource=“<a href="http://relatedM">http://relatedM</a>
atch.term/”/></p>
</div> 

</div>
<div id="SKOS_Concept.skos_exactMatch" class="classattr">

#### skos_exactMatch: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_exactMatch"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of close or exactly matching concepts from other concept schemes.<skos:
exactMatch rdf:resource=“http://exactMatch.term/”/><skos:closeMatch rdf:resource=“http
://closeMatch.term/”/>For recommendations on medata quality see Tier A-C requirements 
, more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="SKOS_Concept.skos_closeMatch" class="classattr">

#### skos_closeMatch: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_closeMatch"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The identifier of close or exactly matching concepts from other concept schemes.<skos:
exactMatch rdf:resource=“http://exactMatch.term/”/><skos:closeMatch rdf:resource=“http
://closeMatch.term/”/>For recommendations on medata quality see Tier A-C requirements 
, more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="SKOS_Concept.skos_note" class="classattr">

#### skos_note: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#SKOS_Concept.skos_note"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Information relating to the concept.<skos:note>The buccin is a visually distinctive tr
ombone popularized in military bands in France between 1810–1845 which subsequently fa
ded into obscurity.</skos:note>For recommendations on medata quality see Tier A-C requ
irements, more specifically Metadata Tier B and Metadata Tier C.</p>
</div> 

</div>
<div id="SKOS_Concept.skos_notation" class="classattr">

#### skos_notation: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#SKOS_Concept.skos_notation"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>The notation in which the concept is represented. This may not be words in natural lan
guage for someknowledge organisation systems e.g. algebra<skos:notation rdf:datatype=“
http://www.w3.org/2001/XMLSchema#int”&gt;123</skos:notation></p>
</div> 

</div>
<div id="SKOS_Concept.skos_inScheme" class="classattr">

#### skos_inScheme: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SKOS_Concept.skos_inScheme"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The URI of a concept scheme</p>
</div> 

</div>
<div id="SKOS_Concept.validate_skos_pref_label" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_skos_pref_label(self) -&gt; Self  

<a class="headerlink" href="#SKOS_Concept.validate_skos_pref_label"></a>



</div>
<div id="SKOS_Concept.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#SKOS_Concept.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="EDM_Agent">

###    class EDM_Agent<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#EDM_Agent"></a>

<div class="docstring"><p>optional-properties: SKOS_note, DC_date, DC_identifier, DCTERMS_hasPart, DCTERMS_isPartOf, EDM_begin, EDM_end, EDM_hasMet, EDM_isRelatedTo, FOAF_name, RDAGR2_biographicalInformation, RDAGR2_dateOfEstablishment, RDAGR2_dateOfTermination, RDAGR2_gender, RDAGR2_placeOfBirth, RDAGR2_placeOfDeath, RDAGR2_professionOrOccupation, OWL_sameAs</p>

<p>recommended-properties: SKOS_prefLabel, SKOS_altLabel, RDAGR2_dateOfBirth, RDAGR2_dateOfDeath</p>
</div> 

<div id="EDM_Agent.skos_prefLabel" class="classattr">

#### skos_prefLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Agent.skos_prefLabel"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>The preferred form of the name of the agent. Although the maximum number of occurrence
s is set at 1, it can be interpreted as 1 per language tag. At least one skos:prefLabe
l SHOULD be provided. Several prefLabels with languages tags are strongly recommended 
for language variants and translations. This is a recommended property for this class.
<skos:prefLabel xml:lang=''fr''>Courtois neveu aîné</skos:prefLabel><skos:prefLabel xm
l:lang=''en''>Courtois’eldest nephew</skos:prefLabel> For recommendations on medata qu
ality see Tier A-C requirements , more specifically Metadata Tier B and Metadata Tier 
C</p>
</div> 

</div>
<div id="EDM_Agent.skos_altLabel" class="classattr">

#### skos_altLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Agent.skos_altLabel"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Alternative forms of the name of the agent. This is a recommended property for this cl
ass.<skos:altLabel xml:lang="en">Courtois</skos:altLabel><skos:altLabel xml:lang="fr">
Augte. Courtois aîné</skos:altLabel></p>
</div> 

</div>
<div id="EDM_Agent.skos_note" class="classattr">

#### skos_note: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Agent.skos_note"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>A note about the agent e.g. biographical notes.<skos:note> Courtois neveu aîné started
a company of the same name manufacturing brass instruments in Paris in 1803</skos:not
e></p>
</div> 

</div>
<div id="EDM_Agent.dc_date" class="classattr">

#### dc_date: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_Agent.dc_date"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>A significant date associated with the Agent. Europeana recommends date conforming to 
ISO 8601 starting with the year and with hyphens (YYYY-MM-DD).<dc:date>1803</dc:date/></p>
</div> 

</div>
<div id="EDM_Agent.dc_identifier" class="classattr">

#### dc_identifier: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Agent.dc_identifier"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>An identifier of the agent.<dc:identifier><a href="http://viaf.org/viaf/96994048">http://viaf.org/viaf/96994048</a>  </dc:identifi
er></p>
</div> 

</div>
<div id="EDM_Agent.dcterms_hasPart" class="classattr">

#### dcterms_hasPart: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Agent.dcterms_hasPart"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to an Agent that is part of the Agent being described (e.g. a part of a corp
oration).<dcterms:hasPart rdf:resource=“http://identifier/partOfCorporation/”&gt;</p>
</div> 

</div>
<div id="EDM_Agent.dcterms_isPartOf" class="classattr">

#### dcterms_isPartOf: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Agent.dcterms_isPartOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to an agent that the described agent is part of.<dcterms:isPartOf rdf:resour
ce=“http://identifier/parentCorporation/”&gt;</p>
</div> 

</div>
<div id="EDM_Agent.edm_begin" class="classattr">

#### edm_begin: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Agent.edm_begin"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The date the agent was born/established. Europeana recommends date conforming to ISO 8
601 starting with the year and with hyphens (YYYY-MM-DD).<edm:begin>1795</edm:begin>Ge
neric "begin" and "end" properties are being used to indicate start date and end date 
generically for edm:Agent and edm:TimeSpan. For edm:Agent this can be interpreted andb
irth and death dates.For recommendations on medata quality see Tier A-C requirements ,
more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_Agent.edm_end" class="classattr">

#### edm_end: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Agent.edm_end"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>Generic "begin" and "end" properties are being used to indicate start date and end dat
e generically for edm:Agent and edm:TimeSpan. For edm:Agent this can be interpreted an
dbirth and death dates.For recommendations on medata quality see Tier A-C requirements
, more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_Agent.edm_hasMet" class="classattr">

#### edm_hasMet: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Agent.edm_hasMet"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to another entity which the agent has “met” in a broad sense. For example a 
reference to a Place class<edm:hasMet rdf:resource=“http://sws.geonames.org/6620265/”&gt;</p>
</div> 

</div>
<div id="EDM_Agent.edm_isRelatedTo" class="classattr">

#### edm_isRelatedTo: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Agent.edm_isRelatedTo"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to other entities, particularly other agents, with whom the agent is related
in a generic sense.<edm:isRelatedTo rdf:resource=“http://identifier/relatedAgent/”&gt;</p>
</div> 

</div>
<div id="EDM_Agent.foaf_name" class="classattr">

#### foaf_name: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Agent.foaf_name"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>The name of the agent as a simple textual string.<foaf:name>Auguste Courtois</foaf:nam
e></p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_biographicalInformation" class="classattr">

#### rdagr2_biographicalInformation: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Agent.rdagr2_biographicalInformation"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Information pertaining to the life or history of the agent.<rdaGr2:biographicalInforma
tion>Courtois neveu aîné started a company of the same name manufacturing brass instru
ments in Paris in 1803</rdaGr2:biographicalInformation></p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_dateOfBirth" class="classattr">

#### rdagr2_dateOfBirth: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Agent.rdagr2_dateOfBirth"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The date the agent (person) was born. Europeana recommends date conforming to ISO 8601
starting with the year and with hyphens (YYYY-MM-DD). This is a recommended property 
for this class.<rdaGr2:dateOfBirth>1795</rdaGr2:dateOfBirth>dates.For recommendations 
on medata quality see Tier A-C requirements , more specifically Metadata Tier B and Me
tadata Tier C</p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_dateOfDeath" class="classattr">

#### rdagr2_dateOfDeath: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Agent.rdagr2_dateOfDeath"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The date the agent (person) died. Europeana recommends date conforming to ISO 8601 sta
rting with the year and with hyphens (YYYY‐MM-DD). This is a recommended property for 
this class.<rdaGr2:dateOfDeath>1895</rdaGr2:dateOfDeath>For recommendations on medata 
quality see Tier A-C requirements , more specifically Metadata Tier B and Metadata Tie
r C</p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_dateOfEstablishment" class="classattr">

#### rdagr2_dateOfEstablishment: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Agent.rdagr2_dateOfEstablishment"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The date on which the agent (corporate body) was established or founded.<rdaGr2:dateOf
Establishment>1795</rdaGr2:dateOfEstablishment></p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_dateOfTermination" class="classattr">

#### rdagr2_dateOfTermination: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Agent.rdagr2_dateOfTermination"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The date on which the agent (corporate body) was terminated or dissolved.<rdaGr2:dateO
fTermination>1895</rdaGr2:dateOfTermination></p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_gender" class="classattr">

#### rdagr2_gender: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Agent.rdagr2_gender"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The gender with which the agent identifies.&lt; rdaGr2:gender>Female</rdaGr2:gender></p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_placeOfBirth" class="classattr">

#### rdagr2_placeOfBirth: Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref, NoneType] 

<a class="headerlink" href="#EDM_Agent.rdagr2_placeOfBirth"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Union[Lit, Ref]]</p>

<p>Description: </p>

<p>The town, city, province, state, and/or country in which a person was born.<rdaGr2:pla
ceOfBirth>Lusaka, Northern Rhodesia</rdaGr2:placeOfBirth><rdaGr2:placeOfBirth rdf:reso
urce=”http://sws.geonames.org/909137/”/>For recommendations on medata quality see Tier
A-C requirements , more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_placeOfDeath" class="classattr">

#### rdagr2_placeOfDeath: Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref, NoneType] 

<a class="headerlink" href="#EDM_Agent.rdagr2_placeOfDeath"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Union[Lit, Ref]]</p>

<p>Description: </p>

<p>The town, city, province, state, and/or country in which a person died.<rdaGr2:placeOf
Death>London, United Kingdom</rdaGr2:placeOfDeath><rdaGr2:placeOfDeath rdf:resource=“h
ttp://sws.geonames.org/2635167/”/>For recommendations on medata quality see Tier A-C r
equirements , more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_Agent.rdagr2_professionOrOccupation" class="classattr">

#### rdagr2_professionOrOccupation: Union[List[Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], List[edmlib.edm.value_types.Ref], List[edmlib.edm.value_types.Lit], NoneType] 

<a class="headerlink" href="#EDM_Agent.rdagr2_professionOrOccupation"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[MixedValuesList]</p>

<p>Description: </p>

<p>The profession or occupation in which the agent works or has worked.<rdaGr2:profession
OrOccupation>Instrument Maker</rdaGr2:professionOrOccupation></p>
</div> 

</div>
<div id="EDM_Agent.owl_sameAs" class="classattr">

#### owl_sameAs: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Agent.owl_sameAs"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Another URI of the same agent.<owl:sameAs rdf:resource=“<a href="http://www.identifier/sameReso">http://www.identifier/sameReso</a>
urceElsewhere”/></p>
</div> 

</div>
<div id="EDM_Agent.validate_skos_pref_label" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_skos_pref_label(self) -&gt; Self  

<a class="headerlink" href="#EDM_Agent.validate_skos_pref_label"></a>



</div>
<div id="EDM_Agent.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#EDM_Agent.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="EDM_TimeSpan">

###    class EDM_TimeSpan<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#EDM_TimeSpan"></a>

<div class="docstring"><p>optional-properties: SKOS_altLabel, SKOS_note, DCTERMS_hasPart, DCTERMS_isPartOf, EDM_isNextInSequence, OWL_sameAs</p>

<p>recommended-properties: SKOS_prefLabel, EDM_begin, EDM_end</p>
</div> 

<div id="EDM_TimeSpan.skos_prefLabel" class="classattr">

#### skos_prefLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_TimeSpan.skos_prefLabel"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>The preferred form of the name of the timespan or period. Although the maximum number 
of occurrences is set at 1, it can be interpreted as 1 per language tag. At least one 
skos:prefLabel SHOULD be provided. Several prefLabels with languages tags are strongly
recommended for language variants andtranslations.<skos:prefLabel xml:lang=“en”&gt;Roman
Empire</skos:prefLabel>This is a recommended property for this class.</p>
</div> 

</div>
<div id="EDM_TimeSpan.skos_altLabel" class="classattr">

#### skos_altLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_TimeSpan.skos_altLabel"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Alternative forms of the name of the timespan or period. <skos:altLabel xml:lang=''fr'
'>Empire romain (27 avant J.-­‐C.-­‐476 après J.-­C.)</skos:altLabel &gt;</p>
</div> 

</div>
<div id="EDM_TimeSpan.skos_note" class="classattr">

#### skos_note: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_TimeSpan.skos_note"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Information relating to the timespan or period.<skos:note>The Roman Empire (Latin: Imp
erium Romanum) was the post-­Republican period of the ancient Roman civilization, char
acterised by an autocratic form of government and large territorial holdings around th
e Mediterranean in Europe, Africa, and Asia.</skos:note></p>
</div> 

</div>
<div id="EDM_TimeSpan.dcterms_hasPart" class="classattr">

#### dcterms_hasPart: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_TimeSpan.dcterms_hasPart"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to a timespan which is part of the described timespan.</p>
</div> 

</div>
<div id="EDM_TimeSpan.dcterms_isPartOf" class="classattr">

#### dcterms_isPartOf: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_TimeSpan.dcterms_isPartOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to a timespan of which the described timespan is a part.</p>
</div> 

</div>
<div id="EDM_TimeSpan.edm_begin" class="classattr">

#### edm_begin: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_TimeSpan.edm_begin"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The date the timespan started. Europeana recommends date conforming to ISO 8601 starti
ng with the year and with hyphens (YYYY-­MM-DD). Providing edm:begin in combination wi
th edm:end is recommended for this class.Example 1: <edm:begin>-0026</edm:begin>Exampl
e:2: <edm:begin>27 BC</edm:begin>Note: '27 BC', while allowed, does not follow the abo
ve recommendation.For recommendations on medata quality see Tier A-C requirements , mo
re specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_TimeSpan.edm_end" class="classattr">

#### edm_end: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_TimeSpan.edm_end"></a>

<div class="docstring"><p>Mandate: 
recommended</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The date the timespan finished. Europeana recommends date conforming to ISO 8601 start
ing with the year and with hyphens (YYYY‐MM-DD). Providing edm:end in combination with
edm:begin is recommended for this class.<edm:end>1770</edm:end>For recommendations on
medata quality see Tier A-C requirements , more specifically Metadata Tier B and Meta
data Tier C</p>
</div> 

</div>
<div id="EDM_TimeSpan.edm_isNextInSequence" class="classattr">

#### edm_isNextInSequence: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_TimeSpan.edm_isNextInSequence"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Can be used to represent a sequence of Time periods. Use this for objects that are par
t of a hierarchy or sequence to ensure correct display in the portal.<edm:isNextInSequ
ence rdf:resource=“http://semium.org/time/roman_republic”/> (The Roman Empire was prec
eded by the Roman Republic)</p>
</div> 

</div>
<div id="EDM_TimeSpan.owl_sameAs" class="classattr">

#### owl_sameAs: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_TimeSpan.owl_sameAs"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>The URI of a timespan<owl:sameAs rdf:resource=“http://semium.org/time/roman_empire”/></p>
</div> 

</div>
<div id="EDM_TimeSpan.validate_skos_pref_label" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_skos_pref_label(self) -&gt; Self  

<a class="headerlink" href="#EDM_TimeSpan.validate_skos_pref_label"></a>



</div>
<div id="EDM_TimeSpan.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#EDM_TimeSpan.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="EDM_Place">

###    class EDM_Place<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#EDM_Place"></a>

<div class="docstring"><p>optional-properties: WGS84_POS_lat, WGS84_POS_long, WGS84_POS_alt, SKOS_prefLabel, SKOS_altLabel, SKOS_note, DCTERMS_hasPart, DCTERMS_isPartOf, EDM_isNextInSequence, OWL_sameAs</p>
</div> 

<div id="EDM_Place.wgs84_pos_lat" class="classattr">

#### wgs84_pos_lat: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Place.wgs84_pos_lat"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The latitude of a spatial thing (decimal degrees). This is a recommended property for 
this class.<wgs84_pos:lat>51.5075</wgs84_pos:lat>For recommendations on medata quality
see Tier A-C requirements , more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_Place.wgs84_pos_long" class="classattr">

#### wgs84_pos_long: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Place.wgs84_pos_long"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The longitude of a spatial thing (decimal degrees). This is a recommended property for
this class.<wgs84_pos:long>-­‐0.1231</wgs84_pos:long>For recommendations on medata qu
ality see Tier A-C requirements, more specifically Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_Place.wgs84_pos_alt" class="classattr">

#### wgs84_pos_alt: Optional[edmlib.edm.value_types.Lit] 

<a class="headerlink" href="#EDM_Place.wgs84_pos_alt"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[Lit]</p>

<p>Description: </p>

<p>The altitude of a spatial thing (decimal metres above the reference)<wgs84_pos:alt>21&lt;
/wgs84_pos:alt></p>
</div> 

</div>
<div id="EDM_Place.skos_prefLabel" class="classattr">

#### skos_prefLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Place.skos_prefLabel"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_one</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>The preferred form of the name of the place. Although the maximum number of occurrence
s is set at 1, it can be interpreted as 1 per language tag. At least one skos:prefLabe
l SHOULD be provided. Several prefLabels with languages tags are strongly recommended 
for language variants and translations.<skos:prefLabel xml:lang="en">London</skos:pref
Label>For recommendations on medata quality see Tier A-C requirements , more specifica
lly Metadata Tier B and Metadata Tier C</p>
</div> 

</div>
<div id="EDM_Place.skos_altLabel" class="classattr">

#### skos_altLabel: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Place.skos_altLabel"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Alternative forms of the name of the place.<skos:altLabel xml:lang="en">Greater London
</skos:altLabel></p>
</div> 

</div>
<div id="EDM_Place.skos_note" class="classattr">

#### skos_note: Optional[List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#EDM_Place.skos_note"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Lit]]</p>

<p>Description: </p>

<p>Information relating to the place.<skos:note xml:lang="en">Pop. 21m</skos:note></p>
</div> 

</div>
<div id="EDM_Place.dcterms_hasPart" class="classattr">

#### dcterms_hasPart: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Place.dcterms_hasPart"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to a place that is part of the place being described.<dcterms:hasPart rdf:re
source=“http://sws.geonames.org/2643741/”/> (City of London)</p>
</div> 

</div>
<div id="EDM_Place.dcterms_isPartOf" class="classattr">

#### dcterms_isPartOf: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Place.dcterms_isPartOf"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Reference to a place that the described place is part of.<dcterms:isPartOf rdf:resourc
e=“http://sws.geonames.org/2635167/”/> (United Kingdom)</p>
</div> 

</div>
<div id="EDM_Place.edm_isNextInSequence" class="classattr">

#### edm_isNextInSequence: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Place.edm_isNextInSequence"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>Can be used to represent a sequence of Place entities over time e.g. the historical la
yers of the city of Troy. Use this for objects that are part of a hierarchy or sequenc
e to ensure correct display in the portal.</p>
</div> 

</div>
<div id="EDM_Place.owl_sameAs" class="classattr">

#### owl_sameAs: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#EDM_Place.owl_sameAs"></a>

<div class="docstring"><p>Mandate: 
optional</p>

<p>Cardinality: 
zero_to_many</p>

<p>Value-Type:
Optional[List[Ref]]</p>

<p>Description: </p>

<p>URI of a Place<owl:sameAs rdf:resource=“http://sws.geonames.org/2635167/”/>(London)</p>
</div> 

</div>
<div id="EDM_Place.validate_skos_pref_label" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_skos_pref_label(self) -&gt; Self  

<a class="headerlink" href="#EDM_Place.validate_skos_pref_label"></a>



</div>
<div id="EDM_Place.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#EDM_Place.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="SVCS_Service">

###    class SVCS_Service<wbr>(<span class="base">edmlib.edm.base.EDM_BaseClass</span>): 

<a class="headerlink" href="#SVCS_Service"></a>

<div class="docstring"><p>(Manually copied)</p>

<p>Optional-Properties:
dcterms_conformsTo, doap_implements</p>

<p>Mandatory-Properties: None
Recommended-Proeprties: None</p>

<p>Definition:
An established standard to which the web resource or service conforms.
W3C WCAG 2.0 (web content accessibility guidelines).
If the Service describes a IIIF resource, dcterms:conformsTo must be used
to describe the IIIF protocol the resource is conforming to.</p>

<p>Example:
<dcterms:conformsTo rdf:resource="http://iiif.io/api/image"/></p>
</div> 

<div id="SVCS_Service.dcterms_conformsTo" class="classattr">

#### dcterms_conformsTo: Optional[List[edmlib.edm.value_types.Ref]] 

<a class="headerlink" href="#SVCS_Service.dcterms_conformsTo"></a>

<div class="docstring"><p>Mandate: 
Optional</p>

<p>Definition: 
An established standard to which the web resource or service conforms. 
W3C WCAG 2.0 (web content accessibility guidelines). If the Service describes 
a IIIF resource, dcterms:conformsTo must be used to describe the IIIF protocol 
the resource is conforming to.</p>

<p>Example: 
<dcterms:conformsTo rdf:resource="http://iiif.io/api/image"/></p>
</div> 

</div>
<div id="SVCS_Service.doap_implements" class="classattr">

#### doap_implements: Optional[edmlib.edm.value_types.Ref] 

<a class="headerlink" href="#SVCS_Service.doap_implements"></a>

<div class="docstring"><p>Mandate: 
Optional</p>

<p>Definition: 
A specification that a project implements. Could be a standard, API or legally defined level of conformance. 
In IIIF doap:implements refers to the the protocol implemented in IIIF.</p>

<p>Example: 
<doap:implements rdf:resource="http://iiif.io/api/image/2/level1.json"/></p>
</div> 

</div>
<div id="SVCS_Service.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#SVCS_Service.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="MixedValuesList">

#### MixedValuesList = typing.Union[typing.List[typing.Union[edmlib.edm.value_types.Lit, edmlib.edm.value_types.Ref]], typing.List[edmlib.edm.value_types.Ref], typing.List[edmlib.edm.value_types.Lit]] 

<a class="headerlink" href="#MixedValuesList"></a>



</section>
<section id="EDM_Parser">

###    class EDM_Parser: 

<a class="headerlink" href="#EDM_Parser"></a>

<div class="docstring"><p>Parser for edm-xml records. Returns an edm_python.edm.EDM_Record object.</p>
</div> 

<div id="EDM_Parser.__init__" class="classattr">

####     EDM_Parser(graph: rdflib.graph.Graph)  

<a class="headerlink" href="#EDM_Parser.__init__"></a>



</div>
<div id="EDM_Parser.from_file" class="classattr">

####   @classmethod    def from_file(cls, path: str, format: str = &#39;xml&#39;) -&gt; Self  

<a class="headerlink" href="#EDM_Parser.from_file"></a>



</div>
<div id="EDM_Parser.from_string" class="classattr">

####   @classmethod    def from_string(cls, content: str, format: str = &#39;xml&#39;) -&gt; Self  

<a class="headerlink" href="#EDM_Parser.from_string"></a>



</div>
<div id="EDM_Parser.graph" class="classattr">

#### graph: rdflib.graph.Graph 

<a class="headerlink" href="#EDM_Parser.graph"></a>



</div>
<div id="EDM_Parser.get_single_ref" class="classattr">

####     def get_single_ref(self, obj_cls: object) -&gt; rdflib.term.URIRef  

<a class="headerlink" href="#EDM_Parser.get_single_ref"></a>

<div class="docstring"><p>Loooks up instances of a given obj_cls (a edm_python edm-class) and returns
a single IRI.
This method expects that the cardinality of the obj_cls is one per record.</p>
</div> 

</div>
<div id="EDM_Parser.get_many_ref" class="classattr">

####     def get_many_ref(self, obj_cls: object) -&gt; List[rdflib.term.URIRef]  

<a class="headerlink" href="#EDM_Parser.get_many_ref"></a>

<div class="docstring"><p>Loooks up instances of a given obj_cls (a edm_python edm-class) and returns
a list of instance-IRIs.
This method expects that the cardinality of the obj_cls is one or more.</p>
</div> 

</div>
<div id="EDM_Parser.get_triples" class="classattr">

####     def get_triples(self, ref: rdflib.term.URIRef)  

<a class="headerlink" href="#EDM_Parser.get_triples"></a>

<div class="docstring"><p>Return all predicate-object triples for a given URIRef within the instance`s-graph.</p>
</div> 

</div>
<div id="EDM_Parser.get_aggregation" class="classattr">

####     def get_aggregation(self)  

<a class="headerlink" href="#EDM_Parser.get_aggregation"></a>



</div>
<div id="EDM_Parser.get_webresources" class="classattr">

####     def get_webresources(self) -&gt; list[typing.Any]  

<a class="headerlink" href="#EDM_Parser.get_webresources"></a>



</div>
<div id="EDM_Parser.get_instance_triples" class="classattr">

####     def get_instance_triples(self, instance: rdflib.term.URIRef, cls_obj: object) -&gt; Dict[str, Any]  

<a class="headerlink" href="#EDM_Parser.get_instance_triples"></a>



</div>
<div id="EDM_Parser.parse_single_class" class="classattr">

####     def parse_single_class(self, cls_obj: object) -&gt; Any  

<a class="headerlink" href="#EDM_Parser.parse_single_class"></a>



</div>
<div id="EDM_Parser.parse_many_class" class="classattr">

####     def parse_many_class(self, cls_obj: Any) -&gt; List[Any]  

<a class="headerlink" href="#EDM_Parser.parse_many_class"></a>



</div>
<div id="EDM_Parser.parse" class="classattr">

####     def parse(self) -&gt; edmlib.edm.record.EDM_Record  

<a class="headerlink" href="#EDM_Parser.parse"></a>



</div>

---

</section>
<section id="Ref">

###    class Ref<wbr>(<span class="base">pydantic.main.BaseModel</span>): 

<a class="headerlink" href="#Ref"></a>

<div class="docstring"><p>About IRIs (from the rdflib.URIRef docstring):</p>

<p>RDF 1.1's IRI Section <a href="https://www.w3.org/TR/rdf11-concepts/#section-IRIs">https://www.w3.org/TR/rdf11-concepts/#section-IRIs</a>
An IRI (Internationalized Resource Identifier) within an RDF graph is a Unicode string that conforms to the syntax defined in RFC 3987.
IRIs in the RDF abstract syntax MUST be absolute, and MAY contain a fragment identifier.
IRIs are a generalization of URIs [RFC3986] that permits a wider range of Unicode characters.</p>
</div> 

<div id="Ref.value" class="classattr">

#### value: Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None)] 

<a class="headerlink" href="#Ref.value"></a>



</div>
<div id="Ref.is_ref" class="classattr">

#### is_ref: bool 

<a class="headerlink" href="#Ref.is_ref"></a>



</div>
<div id="Ref.validate_value_as_uri" class="classattr">

####   @field_validator(&#39;value&#39;)  @classmethod    def validate_value_as_uri(cls, value: str)  

<a class="headerlink" href="#Ref.validate_value_as_uri"></a>



</div>
<div id="Ref.to_rdflib" class="classattr">

####     def to_rdflib(self)  

<a class="headerlink" href="#Ref.to_rdflib"></a>

<div class="docstring"><p>Helper to convert this custom type to the rdflib equivalent
Used in the graph serialization of the EDM_Base-Class</p>
</div> 

</div>
<div id="Ref.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#Ref.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<section id="Lit">

###    class Lit<wbr>(<span class="base">pydantic.main.BaseModel</span>): 

<a class="headerlink" href="#Lit"></a>

<div class="docstring"><p>Overrides the RDFLib Literal with a custom class, so that it is serializable in pydantic model.
For the same reason, it uses the same attribute names.
Ignore the normalize attribute, it is just added for completeness.</p>
</div> 

<div id="Lit.value" class="classattr">

#### value: Annotated[str, StringConstraints(strip_whitespace=True, to_upper=None, to_lower=None, strict=None, min_length=1, max_length=None, pattern=None)] 

<a class="headerlink" href="#Lit.value"></a>



</div>
<div id="Lit.lang" class="classattr">

#### lang: Optional[str] 

<a class="headerlink" href="#Lit.lang"></a>



</div>
<div id="Lit.datatype" class="classattr">

#### datatype: Optional[str] 

<a class="headerlink" href="#Lit.datatype"></a>



</div>
<div id="Lit.normalize" class="classattr">

#### normalize: Optional[bool] 

<a class="headerlink" href="#Lit.normalize"></a>



</div>
<div id="Lit.validate_consistency" class="classattr">

####   @model_validator(mode=&#39;after&#39;)    def validate_consistency(self) -&gt; Self  

<a class="headerlink" href="#Lit.validate_consistency"></a>

<div class="docstring"><p>Checks that literal either has a lang_tag or a datatype, not both.</p>
</div> 

</div>
<div id="Lit.to_rdflib" class="classattr">

####     def to_rdflib(self)  

<a class="headerlink" href="#Lit.to_rdflib"></a>

<div class="docstring"><p>Helper to convert this custom type to the rdflib equivalent
Used in the graph serialization of the EDM_Base-Class</p>
</div> 

</div>
<div id="Lit.model_config" class="classattr">

#### model_config: ClassVar[pydantic.config.ConfigDict] = {} 

<a class="headerlink" href="#Lit.model_config"></a>

<div class="docstring"><p>Configuration for the model, should be a dictionary conforming to [<code>ConfigDict</code>][pydantic.config.ConfigDict].</p>
</div> 

</div>

---

</section>
<!--pdoc-end-->