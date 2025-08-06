import sys
import re
from pathlib import Path
from pdoc.__main__ import cli
import shutil


def main():
    try:
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        docs_dir = project_root / "docs"
        edm_html_path = docs_dir / "edmlib.html"

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
