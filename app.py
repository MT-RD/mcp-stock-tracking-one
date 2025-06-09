"""
MCP Stock Tracking App - Gradio Frontend
"""

import gradio as gr

def create_interface():
    """Create a simple Gradio interface"""
    with gr.Blocks(title="MCP Stock Tracker") as app:
        gr.Markdown("# 📈 MCP Stock Tracking App")
        gr.Markdown("Welcome to the stock tracking application!")
        
        with gr.Row():
            gr.Textbox(label="Stock Symbol", placeholder="Enter a stock symbol (e.g., AAPL)")
            gr.Button("Search", variant="primary")
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch()
