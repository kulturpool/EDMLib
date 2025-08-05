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