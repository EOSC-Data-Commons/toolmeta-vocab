# toolmeta-vocab

A project to host Turtle (`.ttl`) RDF vocabularies for describing computational tools in the
[European Open Science Cloud (EOSC)](https://eosc.eu/) ecosystem, published via
[GitHub Pages](https://eosc-data-commons.github.io/toolmeta-vocab/).

## Vocabularies

| Vocabulary | Namespace | Download |
|---|---|---|
| ToolMeta Core | `https://eosc-data-commons.github.io/toolmeta-vocab/` | [toolmeta.ttl](vocab/toolmeta.ttl) |

## Repository layout

```
vocab/          # Turtle vocabulary source files
docs/           # Static site assets (HTML landing page)
.github/
  workflows/
    pages.yml   # GitHub Actions workflow – validates TTL and deploys to GitHub Pages
```

## Adding a new vocabulary

1. Place your `.ttl` file inside `vocab/`.
2. Add a card for it in `docs/index.html`.
3. Open a pull request — the CI workflow will validate the Turtle syntax automatically.

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

## Publishing

Pushes to `main` trigger the [pages.yml](.github/workflows/pages.yml) GitHub Actions
workflow, which:

1. Validates all `vocab/*.ttl` files with `rdflib`.
2. Copies the vocabulary files and HTML landing page into a build artefact.
3. Deploys the artefact to [GitHub Pages](https://eosc-data-commons.github.io/toolmeta-vocab/).

> **Note:** Before the first deployment, enable GitHub Pages in the repository settings
> (**Settings → Pages → Source → GitHub Actions**).

## License

[Apache 2.0](LICENSE)