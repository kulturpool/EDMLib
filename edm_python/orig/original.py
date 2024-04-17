from pydantic import BaseModel
from edm_python.oai.header import OaiHeader
from edm_python.oai.provenance import Provenance
from enum import StrEnum
import subprocess
import os


class OriginalType(StrEnum):
    lido_xml = "lido_xml"
    edm_xml = "edm_xml"
    mets_xml = "mets_xml"
    mods_xml = "mods_xml"
    mets_mods_xml = "mets_mods_xml"
    edm_python_json = "json"
    kpool_framed_json_ld = "kpool_framed_json_ld"
    rdf_ttl = "ttl"
    rdf_xml = "rdf/xml"
    jsonld = "json-ld"

    @classmethod
    def list(cls):
        return [el.value for el in cls]


class OriginalRecord(BaseModel):
    header: OaiHeader
    provenance: Provenance
    record: str
    record_type: OriginalType


if __name__ == "__main__":
    print("testing original type list")
    print(OriginalType.list())
    print("testing commit hash")

    def get_commit_hash():
        git_hash = (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode("ascii")
            .strip()
        )
        return git_hash

    print(get_commit_hash())

    def get_repo_name():
        return os.path.basename(
            subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
            .decode("ascii")
            .strip()
        )

    def has_uncomitted_changes():
        git_status: str = (
            subprocess.check_output(["git", "status"]).decode("ascii").strip()
        )
        return (
            "Changes not staged for commit" in git_status
            or "Untracked files" in git_status
            or "Changes to be committed" in git_status
        )

    def get_current_branch():
        branch_name: str = (
            subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            .decode("ascii")
            .strip()
        )
        return branch_name

    print("uncommited_changes", has_uncomitted_changes())
    print("repo-name: ", get_repo_name())
    print("branch-name: ", get_current_branch())
    # TODO: if running in production (without a git repo), we need to put this info in an env var or something and read it from there!
