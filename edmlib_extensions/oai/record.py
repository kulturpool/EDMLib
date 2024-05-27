from pydantic import BaseModel
from edmlib.oai.header import OaiHeader
from edmlib.oai.about import OaiAbout
from edmlib.edm import EDM_Record


class OaiRecord(BaseModel):
    header: OaiHeader
    metadata: EDM_Record
    about: OaiAbout
