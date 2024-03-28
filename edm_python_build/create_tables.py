from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import pandas as pd
from datetime import datetime
from pathlib import Path
import os

wrappers = [
    (
        "edm:ProvidedCHO",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2106294284/edm+ProvidedCHO",
    ),
    (
        "ore:Aggregation",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2106032160/ore+Aggregation",
    ),
    (
        "edm:WebResource",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2106392591/edm+WebResource",
    ),
    (
        "edm:Agent",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2106195985/edm+Agent",
    ),
    (
        "edm:Place",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2105901079/edm+Place",
    ),
    (
        "edm:TimeSpan",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2106261527/edm+TimeSpan",
    ),
    (
        "skos:Concept",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2106032167/skos+Concept",
    ),
    (
        "cc:License",
        "https://europeana.atlassian.net/wiki/spaces/EF/pages/2291138591/cc+License",
    ),
]

SERVICE_URL = "https://europeana.atlassian.net/wiki/spaces/EF/pages/2189262924/IIIF+EDM+classes+and+properties"

# mandate of resources is color coded within the an elements data-text-cusom-color attribute. These are the mappings:
color_attr = "data-text-custom-color"
colors = {"#bf2600": "recommended", "#0747a6": "mandatory"}


def get_color_attr(el):  # type: ignore
    """
    Map the color coding within the html to the mandate attribute.
    If no color code given, the mandate defaults to optional (this is not a fallback but the intended encoding by europeana).
    """
    if el.span:  # type: ignore
        if color_attr in el.span.attrs.keys():  # type: ignore
            color = el.span.attrs[color_attr]  # type: ignore
            res = colors[color]  # type: ignore
        else:
            res = "optional"
    else:
        res = "optional"
    return res


def get_table_from_url(url: str, table_index: int = 0):
    req = Request(url)
    html_page = urlopen(req).read()
    soup = bs(html_page, "html.parser")
    tables = soup.find_all("table")
    rows = tables[table_index].find_all("tr")
    headers = rows[0]
    elements = rows[1:]
    df = pd.DataFrame(
        [[element.text for element in row] for row in elements],
        columns=[header.text for header in headers],
    )
    prop_els = [[x for x in el][0] for el in elements]
    df["Normative"] = [get_color_attr(x) for x in prop_els]

    return df

def update_tables():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M")
    output_dir = Path(__file__).absolute() / "data" / "new_tables" / f"{timestamp}"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    tables: dict[str, pd.DataFrame] = {}
    for wrap in wrappers:
        name, url = wrap
        table_index = 0

        if name == "edm:Agent":
            # TODO: implement a check that this assumption holds, otherwise throw an error to update the code if this assumption changes in the future.
            # the edm:Agent page contains 3 tables, of which we want to extract only the third
            table_index = 2

        tables.update({name: get_table_from_url(url, table_index)})

    for name, table in tables.items():
        table.to_excel(output_dir / f"{name.replace(':', '_')}.xlsx", engine="openpyxl")  # type: ignore


if __name__ == "__main__":
    update_tables()
