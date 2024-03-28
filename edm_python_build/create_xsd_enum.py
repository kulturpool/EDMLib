from pathlib import Path
from rdflib import XSD
from jinja2 import FileSystemLoader, Environment


def render_enum():
    template_loader = FileSystemLoader(
        searchpath=Path("../jinja_templates/dataclasses/")
    )
    template_env = Environment(loader=template_loader)
    template = template_env.get_template("xsd_enum.jinja")
    res = template.render(data=[{"full": el.toPython(), "label": el.toPython().split("#")[1]} for el in dir(XSD)])  # type: ignore
    return res


def create_xsd_enum():
    template_string = render_enum()
    with open(
        Path().absolute().parent / "use" / "dataclasses" / "xsd_enum.py",
        "w",
        encoding="UTF-8",
    ) as file:
        file.write(template_string)


if __name__ == "__main__":
    create_xsd_enum()
