from typing import List, Any, Iterable
from pathlib import Path
import os
from collections import defaultdict
import pandas as pd
from jinja2 import FileSystemLoader, Environment
from .fetch_types import EDM_Type, Cardinality, Valuetype, PropertyStruct
from .service_property_structs import has_service, is_referenced_by

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent

TABLE_BASE_DIR = BASE_DIR / "fetch" / "data" / "new_tables"
LATEST_TABLE_DIR = TABLE_BASE_DIR / sorted(os.listdir(TABLE_BASE_DIR), reverse=True)[0]
OUTPUT_BASE_DIR = BASE_DIR / "MODULE_TEST" / "classes"
OUTPUT_CONTEXT_CLASS_PATH = OUTPUT_BASE_DIR / "context.py"
OUTPUT_CORE_CLASS_PATH = OUTPUT_BASE_DIR / "core.py"
OUTPUT_INIT_PATH = OUTPUT_BASE_DIR / "__init__.py"

for dirpath in [
    OUTPUT_BASE_DIR,
]:
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

edm_type_map: dict[EDM_Type, str] = {
    EDM_Type.PROPERTY: "edm_property.jinja",
    EDM_Type.CORE: "edm_class.jinja",
    EDM_Type.CONTEXT: "edm_class.jinja",
}


def parse_property(p: str) -> Iterable[str]:
    """
    TODO: add docstring.
    TODO: fix type hints
    """

    if len(p.split(":")) > 2:
        res: List[str] | List[List[str]] = []
        # handle the special case of the skos_Concept table which contains multiple properties in one cell. Split those out
        assert p.startswith("skos")
        temp = p.replace("skos:", "/skos:").lstrip("/")
        props = temp.split("/")
        for el in props:
            res.append(el.split(":"))  # type: ignore
        return tuple(res)

    else:
        return p.split(":")


# TODO: this might be a method of VALUETYPE itself, or?
def parse_value_type(vt: Valuetype):
    """
    TODO: add docstring.
    """
    if "string" in vt:
        return Valuetype.STRING
    if "literal" in vt:
        if "ref" in vt:
            return Valuetype.LITERAL_OR_REF
        return Valuetype.LITERAL
    if "ref" in vt:
        return Valuetype.REF
    if "loating" in vt:
        return Valuetype.FLOATING_POINT

    # raise ValueError(f"ValueType did not match any expected types.")


# TODO: this might be a method of CARDINALITY itself, or?
def parse_cardinality(c: Cardinality):
    """
    TODO: add docstring.
    """

    temp = c.strip()
    start = temp[0]
    end = temp[-1]
    match (start, end):
        case ("0", "1"):
            return Cardinality.ZERO_TO_ONE
        case ("0", "n"):
            return Cardinality.ZERO_TO_MANY
        case ("1", "1"):
            return Cardinality.EXACTLY_ONE
        case _:
            raise ValueError(f"Unknown Cardinality: {c}.")


def list_all_value_types(tables_dict: dict[str, pd.DataFrame]):
    """
    TODO: add docstring.
    """

    # helper to check all values of the column value types
    vts: set[str] = set()
    vt: Any
    for _, table in tables_dict.items():
        for vt in table[table.columns[2]]:
            vts.add(vt)
    return vts


def list_all_cardinality_variants(tables_dict: dict[str, pd.DataFrame]):
    # helper to check all value of the column value types
    cards: set[str] = set()
    for _, table in tables_dict.items():
        card: Any
        for card in table[table.columns[3]]:
            cards.add(card)
    return cards


def process_class_name(cls_name):  # type: ignore
    ns, name = cls_name.split("_")  # type: ignore
    return "_".join([ns.upper(), name])  # type: ignore


def prepare():
    """
    TODO: add docstring.
    """
    # TODO: include versioning here once implemented
    table_names = [el for el in os.listdir(LATEST_TABLE_DIR) if el.endswith("xlsx")]
    tables: dict[str, pd.DataFrame] = {name.rstrip(".xlsx"): pd.read_excel(LATEST_TABLE_DIR / name) for name in table_names}  # type: ignore
    tables = {name: df.drop(columns=[df.columns[0]]) for name, df in tables.items()}  # type: ignore
    core_names = ["ore_Aggregation", "edm_ProvidedCHO", "edm_WebResource"]
    core = {process_class_name(k): tables[k] for k in core_names}
    context = {
        process_class_name(k): tables[k] for k in tables.keys() if k not in core_names
    }

    return {"core": core, "context": context, "tables": tables}


def render_with_jinja(
    edm_type: EDM_Type,
    data: defaultdict[str, List[PropertyStruct]] | List[PropertyStruct],
) -> str:
    """
    TODO: add docstring.
    """
    template_loader = FileSystemLoader(
        searchpath=BASE_DIR / "fetch" / "jinja_templates"
    )
    template_env = Environment(loader=template_loader)
    template = template_env.get_template(edm_type_map[edm_type])
    res = template.render(data=data)
    return res


def render_init_with_jinja(classlist: List[str]) -> str:
    """
    TODO: add docstring.
    """
    template_loader = FileSystemLoader(
        searchpath=BASE_DIR / "fetch" / "jinja_templates"
    )
    template_env = Environment(loader=template_loader)
    template = template_env.get_template("class_init.jinja")
    res = template.render(classlist=classlist)
    return res


def make_prop_dict(
    table_dict: dict[str, pd.DataFrame]
) -> defaultdict[str, List[PropertyStruct]]:
    """
    Creates a dictionary with all properties associated with the given class.
    """
    prop_dict: defaultdict[str, List[PropertyStruct]] = defaultdict(list)
    for name, df in table_dict.items():
        tup: Any
        for tup in df.itertuples():  # type: ignore
            prop = parse_property(tup[1])
            vt = parse_value_type(tup[3])
            cardinality = parse_cardinality(tup[4])
            mandate = tup[5]
            description = tup[2]

            if type(prop) == tuple:
                # process the special case where the prop name field contains several properties with the same description, cardinality, etc.
                for p in prop:  # type: ignore
                    prop_dict[name].append(PropertyStruct(name, p[0], p[1], vt, cardinality, mandate, description, cardinality.is_optional))  # type: ignore
            else:
                # handle the default case
                prop_dict[name].append(PropertyStruct(name, prop[0], prop[1], vt, cardinality, mandate, description, cardinality.is_optional))  # type: ignore
    # print(prop_dict)
    return prop_dict


def process(edm_type: EDM_Type, table_dict: dict[str, pd.DataFrame]):
    """
    TODO: add docstring.
    """
    prop_dict = make_prop_dict(table_dict)
    if edm_type == EDM_Type.CORE:
        prop_dict["EDM_WebResource"] += [has_service, is_referenced_by]
    result = render_with_jinja(edm_type, prop_dict)
    return result


def create_python_classes():
    """
    TODO: add docsting.
    """
    data = prepare()
    context = data["context"]
    core = data["core"]
    # properties: List[PropertyStruct] = [
    #     item for el in make_prop_dict(data["tables"]).values() for item in el
    # ]
    core_template = process(EDM_Type.CORE, core)
    context_template = process(EDM_Type.CONTEXT, context)
    classlist = list(context.keys()) + list(core.keys())
    init_template = render_init_with_jinja(classlist)

    for file_path, temp in [
        (OUTPUT_CORE_CLASS_PATH, core_template),
        (OUTPUT_CONTEXT_CLASS_PATH, context_template),
        (OUTPUT_INIT_PATH, init_template),
    ]:
        with open(file_path, "w", encoding="UTF-8") as file:
            file.write(temp)

    # sorted_properties: dict[str, List[PropertyStruct]] = {  # type: ignore
    #     "mandatory": list(filter(lambda x: x.mandate == Mandate.MANDATORY, properties)),
    #     "recommended": list(
    #         filter(lambda x: x.mandate == Mandate.RECOMMENDED, properties)
    #     ),
    #     "optional": list(filter(lambda x: x.mandate == Mandate.OPTIONAL, properties)),
    # }


if __name__ == "__main__":
    create_python_classes()
