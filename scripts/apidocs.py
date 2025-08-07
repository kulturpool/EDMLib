import sys
import re
from pathlib import Path
from pdoc.__main__ import cli
from pdoc.render import env
import shutil

import re
from typing import Set, Optional


def generate_id(text: str, existing_ids: Optional[Set[str]] = None) -> str:
    """
    Generate a unique ID from text following GitHub-style anchor rules.

    Args:
        text: Input text to convert to ID
        existing_ids: Set of already used IDs to ensure uniqueness

    Returns:
        String ID conforming to the specified rules
    """
    if existing_ids is None:
        existing_ids = set()

    # Convert to lowercase
    result = text.lower()

    # Remove all non-word characters (keep letters, numbers, spaces, hyphens)
    result = re.sub(r"[^\w\s-]", "", result)

    # Convert spaces to hyphens
    result = re.sub(r"\s+", "-", result)

    # Convert multiple hyphens to single hyphen
    result = re.sub(r"-+", "-", result)

    # Remove leading/trailing hyphens
    result = result.strip("-")

    # Handle empty result
    if not result:
        result = "section"

    # Ensure uniqueness by appending incrementing number if needed
    base_id = result
    counter = 1

    while result in existing_ids:
        result = f"{base_id}-{counter}"
        counter += 1

    # Add to existing_ids set if provided
    existing_ids.add(result)

    return result


def format_id(input: str):
    return generate_id(input)


def main():
    try:
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        docs_dir = project_root / "docs"
        edm_html_path = docs_dir / "edmlib.html"

        env.filters.update({"format_id": format_id})

        cli(
            [
                "-o",
                "docs",
                "-d",
                "markdown",
                "-t",
                "./scripts",
                # "--no-include-undocumented",
                "--no-show-source",
                "edmlib",
            ]
        )

        if edm_html_path.exists():
            # Remove leading whitespace from each line in the file because
            # README.md expects no leading whitespace
            lines = edm_html_path.read_text().splitlines()
            processed_lines = [line.lstrip() for line in lines]
            processed_lines = [
                re.sub(
                    r"^<indent (\d+)>",
                    lambda m: "".join([" " for e in range(int(m.group(1)))]),
                    line,
                )
                for line in processed_lines
            ]

            edm_html_path.write_text("\n".join(processed_lines))
        else:
            raise Exception(f"File not found: {edm_html_path}")

        readme_path = project_root / "README.md"
        full_api_docs = edm_html_path.read_text()

        if readme_path.exists():
            content = readme_path.read_text()

            api_marker = "<!--pdoc-start-->"
            if api_marker in content:
                # Replace existing API docs
                parts = content.split(api_marker, 1)
                new_content = parts[0].rstrip() + full_api_docs
            else:
                # Append API docs
                new_content = content.rstrip() + "\n\n" + full_api_docs

            # Write updated README
            readme_path.write_text(new_content)

            # Cleanup generated docs
            shutil.rmtree(docs_dir)
        else:
            raise Exception("README.md not found.")

        print(f"✅ Updated README.md with API documentation.")
    except Exception as e:
        print(f"❌ Error generating API documentation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
