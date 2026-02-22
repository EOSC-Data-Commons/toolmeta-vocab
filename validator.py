from rdflib import Graph
from pyshacl import validate


def validate_toolmeta(data_file: str, shapes_file: str):
    data_graph = Graph()
    data_graph.parse(data_file, format="json-ld")

    data_graph.parse("vocab/toolmeta.ttl", format="turtle")

    shapes_graph = Graph()
    shapes_graph.parse(shapes_file, format="turtle")

    conforms, report_graph, report_text = validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        inference="rdfs",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
    )

    print(report_text)

    if not conforms:
        raise Exception("❌ SHACL validation failed")
    else:
        print("✅ SHACL validation successful")


if __name__ == "__main__":
    validate_toolmeta("examples/a_galaxy_workflow.json", "vocab/toolmeta-shapes.ttl")
