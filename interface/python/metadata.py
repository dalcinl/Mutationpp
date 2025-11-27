import pathlib

rootdir = pathlib.Path(__file__).parent.parent.parent
rooturl = "https://github.com/mutationpp/Mutationpp/"


def get_readme(settings=None):  # noqa: ARG001
    baseurl = pathlib.PurePosixPath(rooturl) / "blob" / "HEAD"
    readme = (rootdir / "README.md").read_text()
    text = f'<base href="{baseurl}/">\n\n{readme}'
    return {"text": text, "content-type": "text/markdown"}


def dynamic_metadata(field, settings=None):
    getter = globals()["get_" + field.replace("-", "_")]
    return getter(settings)


if __name__ == "__main__":
    print(dynamic_metadata(__import__("sys").argv[1]))
