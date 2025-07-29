# Text to Vector Project

This repository contains several Python scripts for working with text-to-vector models, generating diagrams from text, and visualizing data. The project leverages Hugging Face Transformers, Sentence Transformers, and other popular Python libraries.

## Contents

- `try.py`: Uses a language model to generate Mermaid flowcharts from a given process description and saves the Mermaid code to a file.
- `try2.py`: Similar to `try.py`, but with more advanced extraction and the ability to render Mermaid diagrams to PNG using the Mermaid CLI. Includes functions for both generating and rendering diagrams.
- `verify.py`: Verifies that key dependencies (PyTorch, Transformers, Sentence Transformers, Pandas, Matplotlib) are installed and working. Also demonstrates basic usage of these libraries.

## Requirements

- Python 3.8+
- [transformers](https://huggingface.co/docs/transformers/index)
- [torch](https://pytorch.org/)
- [sentence-transformers](https://www.sbert.net/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [mermaid-cli](https://github.com/mermaid-js/mermaid-cli) (for rendering diagrams to PNG, used in `try2.py`)

You can install the Python dependencies with:

```bash
pip install torch transformers sentence-transformers pandas matplotlib
```

To install Mermaid CLI (for diagram rendering):

```bash
npm install -g @mermaid-js/mermaid-cli
```

## Usage

### Generate a Mermaid Diagram from Text

Run `try.py` to generate a Mermaid diagram from a hardcoded process description:

```bash
python try.py
```

This will create a `diagram.mmd` file with the Mermaid DSL.

### Advanced Diagram Generation and Rendering

Run `try2.py` to generate a Mermaid diagram from a custom process and render it to PNG:

```bash
python try2.py
```

This will create files like `weather_agent.mmd` and `weather_agent.png`.

You can modify the script to generate diagrams for other processes by changing the `generate_mermaid` function call.

### Verify Environment

Run `verify.py` to check that all dependencies are installed and working:

```bash
python verify.py
```

## License

This project is provided for educational and demonstration purposes.
