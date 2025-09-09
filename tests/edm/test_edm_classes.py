import pytest
from tests.fixtures.record import cho_id_missmatch, xml_with_lang_in_edm_type
from pydantic import ValidationError

from edmlib import (
    EDM_Record,
    EDM_Agent,
    EDM_Place,
    EDM_TimeSpan,
    EDM_WebResource,
    ORE_Aggregation,
    SKOS_Concept,
    EDM_Parser,
    Ref,
    Lit,
)


def test_validation_cho_and_aggregation_id(cho_id_missmatch) -> None:
    with pytest.raises(ValidationError):
        EDM_Record(**cho_id_missmatch)


def test_replacing_local_uris() -> None:
    pass


@pytest.mark.parametrize("model", (SKOS_Concept, EDM_Agent, EDM_Place, EDM_TimeSpan))
def test_validation_skos_pref_label(model) -> None:
    with pytest.raises(ValidationError):
        model(
            id=Ref(value="https://example.com/fake_concept"),
            skos_prefLabel=[
                Lit(value="name", lang="de"),
                Lit(value="no-name", lang="de"),
                Lit(value="nombre", lang="es"),
            ],
        )


@pytest.mark.parametrize("model", (SKOS_Concept, EDM_Agent, EDM_Place, EDM_TimeSpan))
def test_validation_skos_pref_label_single_lang_tag_in_List_ok(model) -> None:
    concept = model(
        id=Ref(value="https://example.com/fake_concept"),
        skos_prefLabel=[
            Lit(value="name", lang="de"),
        ],
    )
    assert concept


@pytest.mark.parametrize("model", (SKOS_Concept, EDM_Agent, EDM_Place, EDM_TimeSpan))
def test_validation_skos_pref_label_without_lang_tag_ok(model) -> None:
    concept = model(
        id=Ref(value="https://example.com/fake_concept"),
        skos_prefLabel=[
            Lit(value="name", lang=None),
        ],
    )
    pref_label = concept.skos_prefLabel
    assert pref_label and len(pref_label) == 1
    assert pref_label[0].value == "name"


@pytest.mark.parametrize("model", (SKOS_Concept, EDM_Agent))
def test_validation_skos_pref_label_multi_none_lang_tags_fail(model) -> None:
    with pytest.raises(ValidationError):
        model(
            id=Ref(value="https://example.com/fake_concept"),
            skos_prefLabel=[
                Lit(value="Name", lang=None),
                Lit(value="name", lang=None),
                Lit(value="nombre", lang="de"),
            ],
        )


@pytest.mark.parametrize("model", (SKOS_Concept, EDM_Agent, EDM_Place, EDM_TimeSpan))
def test_validation_skos_pref_label_single_missing_tag_raises(model) -> None:
    with pytest.raises(ValidationError):
        model(
            id=Ref(value="https://example.com/fake_concept"),
            skos_prefLabel=[
                Lit(value="Name", lang=None),
                Lit(value="name", lang="fr"),
                Lit(value="nombre", lang="de"),
            ],
        )


@pytest.mark.parametrize("model", (SKOS_Concept, EDM_Agent, EDM_Place, EDM_TimeSpan))
def test_validation_multi_pref_label_with_distinct_lang_tag_ok(model) -> None:
    concept = model(
        id=Ref(value="https://example.com/fake_concept"),
        skos_prefLabel=[
            Lit(value="Name", lang="de"),
            Lit(value="name", lang="en"),
            Lit(value="nombre", lang="es"),
        ],
    )
    assert concept
    pref_label = concept.skos_prefLabel
    assert pref_label and len(pref_label) == 3


def test_validation_edm_type_with_lang_raises(xml_with_lang_in_edm_type) -> None:
    with pytest.raises(ValidationError):
        parser = EDM_Parser.from_string(content=xml_with_lang_in_edm_type, format="xml")
        parser.parse()


def test_rightsstatements_normalization():
    aggregation = ORE_Aggregation(
        id=Ref(value="https://example.com/aggregation"),
        edm_aggregatedCHO=Ref(value="https://example.com/aggregation"),
        edm_dataProvider=Lit(value="Data Provider"),
        edm_isShownBy=Ref(value="https://example.com/isShownBy"),
        edm_isShownAt=Ref(value="https://example.com/isShownAt"),
        edm_provider=Lit(value="Provider"),
        edm_rights=Ref(value="https://rightsstatements.org/page/NoC-NC/1.0/"),
    )

    assert (
        aggregation.edm_rights.value == "http://rightsstatements.org/vocab/NoC-NC/1.0/"
    )

    ressource = EDM_WebResource(
        id=Ref(value="https://example.com/webresource"),
        edm_rights=Ref(value="https://rightsstatements.org/page/NoC-NC/1.0/"),
    )

    assert (
        ressource.edm_rights
        and ressource.edm_rights.value
        == "http://rightsstatements.org/vocab/NoC-NC/1.0/"
    )
