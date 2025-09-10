from edmlib import EDM_Parser
from edmlib.edm.classes.core import EDM_ProvidedCHO
from pathlib import Path


def test_parser_owl_sameas():
    with open(Path(__file__).parent / "minimal-edm-with-owlsameas.xml", "r") as file:
        parser = EDM_Parser.from_string(file.read(), format="xml")
        record = parser.parse()
        cho: EDM_ProvidedCHO = record.provided_cho

        # Only accept 'owl_sameAs' as the correct attribute name as file
        sameas = cho.owl_sameAs
        assert (
            sameas is not None
        ), "owl:sameAs property not parsed (expected attribute 'owl_sameAs')"

        # Require a list of two values
        assert isinstance(
            sameas, list
        ), f"owl_sameAs should be a list, got {type(sameas)}"
        assert len(sameas) == 2, f"Expected 2 owl:sameAs, got {len(sameas)}"

        uris = {ref.value for ref in sameas}
        assert "http://example.org/other/1" in uris, "Missing first owl:sameAs URI"
        assert "http://example.org/other/2" in uris, "Missing second owl:sameAs URI"
