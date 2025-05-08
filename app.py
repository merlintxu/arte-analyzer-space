import gradio as gr
from utils.drive_utils import authenticate_and_select_folder
from utils.analysis_pipeline import analyze_image_folder
from utils.openai_generation import generate_framed_images
import json
import os

DATA_FOLDER = "data/original"
RESULTS_FOLDER = "data/results"
METADATA_FILE = "metadata_store.json"

def run_pipeline():
    if not os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'w') as f:
            json.dump({}, f)

    results = analyze_image_folder(DATA_FOLDER, METADATA_FILE)
    generate_framed_images(results, RESULTS_FOLDER)
    return "✅ Análisis completado y marcos generados."

with gr.Blocks() as demo:
    gr.Markdown("# 🎨 Analizador de Arte con IA")
    select_button = gr.Button("1️⃣ Autenticarse y seleccionar carpeta en Drive")
    analyze_button = gr.Button("2️⃣ Analizar imágenes y generar marcos")
    output_text = gr.Textbox(label="Estado")

    select_button.click(fn=authenticate_and_select_folder, outputs=[])
    analyze_button.click(fn=run_pipeline, outputs=output_text)

demo.launch()
