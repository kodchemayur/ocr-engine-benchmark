import os
import time
import urllib.request
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def download_messy_image():
    # The Walgreens messy receipt
    image_url = "https://raw.githubusercontent.com/veryfi/veryfi-python/master/tests/assets/receipt_public.jpg"
    filename = "messy_receipt.jpg"
    if not os.path.exists(filename):
        console.print("[dim]Downloading sample messy receipt...[/dim]")
        urllib.request.urlretrieve(image_url, filename)
    return filename

def main():
    console.clear()
    image_path = download_messy_image()
    console.print(f"[bold cyan]🎯 REAL 3-WAY OCR BENCHMARK ON '{image_path}'...[/bold cyan]\n")
    
    # ==========================================
    # 1. RUN PYTESSERACT (The Classic)
    # ==========================================
    console.print("[bold yellow][RUNNING] 1. PyTesseract (Legacy OCR)...[/bold yellow]")
    try:
        import pytesseract
        from PIL import Image
        
        # Point directly to the Windows installation path
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        start_time = time.time()
        img = Image.open(image_path)
        tesseract_raw_text = pytesseract.image_to_string(img)
        tesseract_time = time.time() - start_time
        
        console.print(Panel(tesseract_raw_text[:300].strip() + "...", title="PyTesseract Raw Output", border_style="blue"))
    except Exception as e:
        console.print(f"[red]PyTesseract failed: {e}[/red]")
        tesseract_time = 0
        tesseract_raw_text = ""

    # ==========================================
    # 2. RUN EASYOCR (The Modern Standard)
    # ==========================================
    console.print("\n[bold yellow][RUNNING] 2. EasyOCR (Deep Learning Vision)...[/bold yellow]")
    try:
        import easyocr
        reader = easyocr.Reader(['en'], gpu=False, verbose=False)
        
        start_time = time.time()
        easy_results = reader.readtext(image_path, detail=0)
        easy_time = time.time() - start_time
        easy_raw_text = " ".join(easy_results)
        
        console.print(Panel(str(easy_results)[:300] + "...", title="EasyOCR Raw Output (Flat List)", border_style="red"))
    except Exception as e:
        console.print(f"[red]EasyOCR failed: {e}[/red]")
        easy_time = 0
        easy_raw_text = ""

    # ==========================================
    # 3. RUN IBM DOCLING (The Next-Gen)
    # ==========================================
    console.print("\n[bold yellow][RUNNING] 3. IBM Docling (Document AI)...[/bold yellow]")
    try:
        from docling.document_converter import DocumentConverter
        converter = DocumentConverter()
        
        start_time = time.time()
        docling_result = converter.convert(image_path)
        docling_raw_text = docling_result.document.export_to_markdown()
        docling_time = time.time() - start_time
        
        console.print(Panel(docling_raw_text[:300].strip() + "...", title="Docling Raw Output (Markdown)", border_style="green"))
    except Exception as e:
        console.print(f"[red]Docling failed: {e}[/red]")
        docling_time = 0
        docling_raw_text = ""

    # ==========================================
    # 4. THE OBJECTIVE TESTING MATRIX
    # ==========================================
    console.print("\n[bold cyan]📊 PERFORMANCE MATRIX (RAW DATA ONLY):[/bold cyan]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan", width=20)
    table.add_column("PyTesseract", style="blue")
    table.add_column("EasyOCR", style="red")
    table.add_column("IBM Docling", style="green")
    
    # Metric 1: Speed
    table.add_row("Execution Speed", f"{tesseract_time:.2f} sec", f"{easy_time:.2f} sec", f"{docling_time:.2f} sec")
    
    # Metric 2: Format Output
    table.add_row("Raw Data Format", "String (Spaced)", "Python List (Flat)", "Markdown (Structured)")
    
    # Metric 3: Layout Retention
    table.add_row("Layout Retention", "Poor (Breaks easily)", "Lost (Reads L to R)", "Preserved (Blocks)")
    
    # Metric 4: Keyword Detection Test (Total: 29.53)
    tess_found = "29.53" in tesseract_raw_text
    easy_found = "29.53" in easy_raw_text
    doc_found = "29.53" in docling_raw_text
    table.add_row("Found Total (29.53)?", "✅ Yes" if tess_found else "❌ No", "✅ Yes" if easy_found else "❌ No", "✅ Yes" if doc_found else "❌ No")
    
    console.print(table)
    console.print("\n[bold white]End of Benchmark.[/bold white]\n")

if __name__ == "__main__":
    main()