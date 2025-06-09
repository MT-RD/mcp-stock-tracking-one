"""
MCP Stock Tracking App - Gradio Frontend
"""

import gradio as gr

def search_stock(symbol):
    """Simple placeholder function for stock search"""
    if not symbol.strip():
        return "⚠️ Please enter a stock symbol!"
    
    return f"🔍 Searching for {symbol.upper()}...\n\n✨ Coming soon! MCP server connection will be added in the next update.\n\n📊 Features being developed:\n• Real-time stock prices\n• Investment analysis\n• Smart recommendations\n• Portfolio tracking"

def create_interface():
    """Create a simple Gradio interface"""
    with gr.Blocks(title="MCP Stock Tracker") as app:
        gr.Markdown("# 📈 MCP Stock Tracking App")
        gr.Markdown("Welcome to the stock tracking application!")
        
        with gr.Row():
            symbol_input = gr.Textbox(label="Stock Symbol", placeholder="Enter a stock symbol (e.g., AAPL)")
            search_btn = gr.Button("Search", variant="primary")
        
        # Output area for search results
        result_output = gr.Textbox(
            label="Search Results", 
            lines=6,
            interactive=False,
            placeholder="Enter a stock symbol and click Search to see results..."
        )
        
        # Connect button click to handler function
        search_btn.click(
            fn=search_stock,
            inputs=symbol_input,
            outputs=result_output
        )
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch()
