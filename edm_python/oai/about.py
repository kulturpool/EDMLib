from pydantic import BaseModel
from edm_python.oai.provenance import Provenance


class OaiAbout(BaseModel):
    description: str
    provenance: Provenance
