from pydantic import BaseModel


class OaiHeader(BaseModel):
    identifier: str  # should be our URIRef
    datestamp: str  # should be already formatted utc YYYY-MM-DD datestring with or without timezone
