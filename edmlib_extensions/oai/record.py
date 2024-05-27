from pydantic import BaseModel
from edm_python.oai.header import OaiHeader
from edm_python.oai.about import OaiAbout
from edm_python.edm import EDM_Record


class OaiRecord(BaseModel):
    header: OaiHeader
    metadata: EDM_Record
    about: OaiAbout
