# from ..edm.rdflib_extensions import Literal, StrLiteral, FloatLiteral, URIRef
from rdflib import Literal, URIRef
from typing import Any, Union
from enum import StrEnum
from dataclasses import dataclass


class Mandate(StrEnum):
    """
    Encapsulates value options for a propertie`s or classe`s Mandate, i.e.
    if a record MUST, SHOULD or CAN hold the designated class or property.
    """

    MANDATORY = "mandatory"
    RECOMMENDED = "recommended"
    OPTIONAL = "optional"


# NOTE: shared
class Cardinality(StrEnum):
    """
    Encapsulates the cardinality options of a Property. I.e. how often it
    must or can appear within a class.
    """

    ZERO_TO_ONE = "zero_to_one"
    ZERO_TO_MANY = "zero_to_many"
    EXACTLY_ONE = "exactly_one"

    @property
    def is_optional(self):
        return self.value.startswith("zero")


# NOTE: processing only
class Valuetype(StrEnum):
    """
    Encapsulates the allowed types of a resource's value as given by the europeana Mapping Guidelines

    :type StrEnum: Standard-Library StrEnum
    """

    LITERAL = "literal"
    LITERAL_OR_REF = "literal_or_ref"
    REF = "ref"
    STRING = (
        "string"  # Note that strings in RDF are also Literals (of xsd datatype string)
    )
    FLOATING_POINT = "floating_point"  # Note that floats in RDF are also Literals (of xsd datatype float)

    def as_type(self, as_string: bool = False) -> Any:
        """
        Convert the instance to a python datatype or a string representation of the python datatype.
        The string representation is used to create type annotations in jinja-templates.
        """
    

        match self:
            case Valuetype.LITERAL:
                return Literal if not as_string else "Literal"
            case Valuetype.LITERAL_OR_REF:
                return (
                    Union[Literal, URIRef]
                    if not as_string
                    else "Union[Literal, URIRef]"
                )
            case Valuetype.REF:
                return URIRef if not as_string else "URIRef"
            case Valuetype.STRING:
                return Literal if not as_string else "Literal"
            case Valuetype.FLOATING_POINT:
                return Literal if not as_string else "Literal"

    @property
    def to_template(self) -> Any:
        """
        Return the python datatype as a string.
        Coded as a property to be convertable inside a jinja or django template.
        """
        return self.as_type(as_string=True)


# NOTE: processing only
@dataclass
class PropertyStruct:
    """
    Represents a property as a python datastructure during processing.
    Splits all needed information into separate attributes.
    This is only used during processing, it should not be used when implementing a mapping or "Anbindung"
    """

    parent_class: str
    namespace: str
    label: str
    value_type: Valuetype
    cardinality: Cardinality
    mandate: Mandate
    description: str
    optional: bool = False

    @property
    def to_template_parent_class(self):
        """
        Shorthand to add the parent_class attribute to a jinja or django template.
        """
        if ":" in self.parent_class:
            sep = ":"
        elif "_" in self.parent_class:
            sep = "_"
        else:
            sep = None

        if sep:
            ns, cls = self.parent_class.split(sep)
            return f"{ns.upper()}_{cls}"
        else:
            print(self.parent_class)
            return self.parent_class

    @property
    def to_template_namespace(self):
        """
        Shorthand to add the namespace attribute to a jinja or django template.
        """
        return self.namespace.upper()

    @property
    def to_template_label(self):
        """
        Shorthand to add the label attribute to a jinja or django template.
        """
        return self.label

    @property
    def to_template_type(self):
        """
        Shorthand to add the type attribute to a jinja or django template.
        """
        value_type = self.value_type.to_template

        match self.cardinality:
            case Cardinality.ZERO_TO_ONE:
                return f"Optional[{value_type}]"
            case Cardinality.ZERO_TO_MANY:
                if self.value_type == Valuetype.LITERAL_OR_REF:
                    return "Optional[MixedValuesList]"
                else:
                    return f"Optional[List[{value_type}]]"
            case Cardinality.EXACTLY_ONE:
                return f"{value_type}"

    @property
    def to_template_description(self):
        """
        Shorthand to add the description attribute to a jinja or django template.
        """
        return "\n\t".join(
            self.description[i : i + 86] for i in range(0, len(self.description), 86)
        )

    @property
    def to_template_cardinality(self):
        """
        Shorthand to add the cardinality attribute to a jinja or django template.
        """
        return f"CARDINALITY.{self.cardinality.upper()}"

    @property
    def to_template_Mandate(self):
        """
        Shorthand to add the Mandate attribute to a jinja or djanog template.
        """
        return f"Mandate.{self.mandate.upper()}"


# NOTE: processing only
class EDM_Type(StrEnum):
    """
    Enum that differentiates between a Property, Core-Class and Context-Class as denoted by the
    edm mapping guidelines.
    Only used during processing of the datamodel, not intended for using the datamodel.
    """

    PROPERTY = "property"
    CORE = "core"
    CONTEXT = "context"


