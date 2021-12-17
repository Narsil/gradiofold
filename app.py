import gradio as gr
from pathlib import Path
import tempfile


def molstar(output_name):
    structure_url = (
        f"https://nodata.dev/gradiofold/predictions/{output_name}/prediction.pdb"
    )
    return f'<iframe style="height: 50rem; width:100%" src="https://nodata.dev/gradiofold/molstar.html?structure-url={structure_url}"/>'


def main(dropdown):
    filename = PRECALCULATED_MOLECULES[dropdown]
    return molstar(filename)


PRECALCULATED_MOLECULES = {"Covid spike": "ncov-s"}


file_input = gr.inputs.File(
    file_count="single",
    type="file",
    label="Send a Fasta file representing the protein",
    optional=False,
)
dropdown_input = gr.inputs.Dropdown(
    list(PRECALCULATED_MOLECULES.keys()) + ["custom fasta file"]
)
inputs = [dropdown_input]
iface = gr.Interface(fn=main, inputs=inputs, outputs="html")
if __name__ == "__main__":
    iface.launch()
