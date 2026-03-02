from edmlib.edm.value_types import Ref
from enum import Enum


# Controlled vocabulary: Usage Area (edm:intendedUsage)
class UsageArea(Enum):
    KNOWLEDGE = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Knowledge")
    RESEARCH = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Research")
    EDUCATION = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Education")
    INFOTAINMENT = Ref(
        value="http://data.europeana.eu/vocabulary/usageArea/Infotainment"
    )
    TOURISM = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Tourism")
    GAMING = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Gaming")
    EXHIBITION = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Exhibition")
    CREATIVITY = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Creativity")
    DESIGN = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Design")
    ART = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Art")
    CURATION = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Curation")
    MAINTENANCE = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Maintenance")
    RESTORATION = Ref(value="http://data.europeana.eu/vocabulary/usageArea/Restoration")
    DOCUMENTATION = Ref(
        value="http://data.europeana.eu/vocabulary/usageArea/Documentation"
    )


# Controlled vocabulary: Relation to the physical reaRefy (schema:digitalSourceType)
class DigitalSourceType(Enum):
    DIGITAL_CAPTURE = Ref(
        value="https://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture"
    )
    DATA_DRIVEN_MEDIA = Ref(
        value="https://cv.iptc.org/newscodes/digitalsourcetype/dataDrivenMedia"
    )
    DIGITAL_CREATION = Ref(
        value="https://cv.iptc.org/newscodes/digitalsourcetype/digitalCreation"
    )


# Controlled vocabulary: Type of 3D model (dc:type)
class ModelType(Enum):
    MESH = Ref(value="http://data.europeana.eu/vocabulary/modelType/3DMesh")
    POINT_CLOUD = Ref(
        value="http://data.europeana.eu/vocabulary/modelType/3DPointCloud"
    )
    BIM = Ref(value="http://data.europeana.eu/vocabulary/modelType/BIM")
    PARAMETRIC_MODEL = Ref(
        value="http://data.europeana.eu/vocabulary/modelType/parametricModel"
    )
