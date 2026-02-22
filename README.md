# toolmeta-vocab

A project to host Turtle (`.ttl`) RDF vocabularies for describing tools in the
[European Open Science Cloud (EOSC)](https://eosc.eu/horizon-europe-projects/eosc-data-commons) ecosystem, published via
[GitHub Pages](https://eosc-data-commons.github.io/toolmeta-vocab/).

## Vocabularies

| Vocabulary    | Namespace                                             | Download                           |
| ------------- | ----------------------------------------------------- | ---------------------------------- |
| ToolMeta Core | `https://eosc-data-commons.github.io/toolmeta-vocab/` | [toolmeta.ttl](vocab/toolmeta.ttl) |

## Local validation

```bash
pip install rdflib
python -c "
from rdflib import Graph
g = Graph()
g.parse('vocab/toolmeta.ttl', format='turtle')
print(len(g), 'triples loaded successfully')
"
```
