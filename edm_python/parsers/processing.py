from io import BytesIO
from typing import Any, List, Tuple

from lxml import etree  # type: ignore
from lxml.etree import _Element  # type: ignore pylint: disable=no-name-in-module
from rdflib import Graph
from sickle import Sickle  # type: ignore
from sickle.models import Record  # type: ignore

from ..edm import EDM_Record
from ..parsers import EDM_Parser

endpoint_url = "http://sammlungenonline.albertina.at:16015/oai/"
sickle = Sickle(endpoint_url)


ns = {
    "ore": "http://www.openarchives.org/ore/terms/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}


def fix_rdf_about(xml: _Element):
    """
    Fixes the specific error that ore:Aggregation elements have rdf:resource instead of rdf:about as attribs.
    """
    el = xml.xpath(".//ore:Aggregation[@rdf:resource]", namespaces=ns)  # type: ignore
    val = el[0].xpath("./@rdf:resource", namespaces=ns)[0]
    el[0].attrib.pop("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
    el[0].attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"] = val

    return xml


def fix_whitespaces(xml: _Element):
    """
    Fixes trailing whitespaces in some URIRefs in the edm XML files.
    """
    els = xml.xpath(".//*[contains(@rdf:resource | @rdf:about, ' ')]", namespaces=ns)  # type: ignore
    for el in els:
        for k, v in el.attrib.items():
            if v.endswith(" "):
                el.attrib[k] = v.rstrip()
    return xml


def record_to_graph(rec: Record) -> Graph:
    """
    Helper that accepts a sickle.Record object and returns an rdflib.Graph.
    """
    rdf: Any = rec.xml.xpath(  # type: ignore
        ".//rdf:RDF", namespaces={"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"}
    )[0]
    res = fix_rdf_about(rdf)
    res = fix_whitespaces(res)
    return Graph().parse(BytesIO(etree.tostring(res)), format="xml")  # type: ignore


def compare(count: int = 1) -> List[Tuple[Graph, EDM_Record, Record]]:
    """
    Creates a tuple per record, containing:
    - the graph object pre-processing
    - the processed edm_record
    and the input sickle.Record.
    """
    res: List[Tuple[Graph, EDM_Record, Record]] = []
    idx = 0
    rec: Any
    for rec in sickle.ListRecords(metadataPrefix="oai_dc"):  # type: ignore
        g: Graph = record_to_graph(rec)

        if idx == count:
            break
        if idx % 100 == 0:
            print(f"{idx}/{count}")
        try:
            res.append((g, process(g), rec))
            idx += 1
        except Exception as e:
            print(e)
            idx += 1
            continue

    return res


def run_processing(count: int = 10000) -> List[EDM_Record]:
    res: List[EDM_Record] = []
    idx = 0
    rec: Any
    for rec in sickle.ListRecords(metadataPrefix="oai_dc"):  # type: ignore
        g: Graph = record_to_graph(rec)

        idx += 1
        if idx == count:
            break
        if idx % 100 == 0:
            print(f"{idx}/{count}")
        try:
            res.append(process(g))
        except Exception as e:
            print(e)
            continue

    return res


def process(g: Graph) -> EDM_Record:
    parser = EDM_Parser(g)
    return parser.parse()
