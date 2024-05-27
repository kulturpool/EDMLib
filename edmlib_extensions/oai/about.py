from pydantic import BaseModel
from edmlib.oai.provenance import Provenance


class OaiAbout(BaseModel):
    description: str
    provenance: Provenance
