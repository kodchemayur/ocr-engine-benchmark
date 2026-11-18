# 🔍 OCR Engine Benchmark: PyTesseract vs EasyOCR vs IBM Docling

This repository contains the benchmarking script featured in the **"Which OCR is best for messy documents?"** video. 

We test three popular OCR engines against a messy, low-quality Walgreens receipt to see which one can successfully extract the total amount (`$29.53`).

### 🏆 The Contenders
1. **PyTesseract:** The classic, legacy OCR engine. Fast, but fragile.
2. **EasyOCR:** The modern standard using deep learning vision.
3. **IBM Docling:** The next-gen Document AI. Slow, but highly accurate for complex layouts and RAG pipelines.

---

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/ocr-engine-benchmark.git](https://github.com/YOUR_USERNAME/ocr-engine-benchmark.git)
cd ocr-engine-benchmark

**2. Install Python dependencies:**
```bash
pip install -r requirements.txt

**3. Install Tesseract OS Engine:Note: PyTesseract requires the actual Tesseract software installed on your machine.**

Windows: Download the installer from UB-Mannheim (The script assumes it's installed at C:\Program Files\Tesseract-OCR\tesseract.exe).

Mac: brew install tesseract

Linux (Ubuntu): sudo apt install tesseract-ocr

**🚀 How to Run the Benchmark**
Simply run the Python script. It will automatically download the sample receipt image and run all three engines back-to-back.

Bash
python ocr.py

**📊 The Takeaway for AI Builders**
Fast doesn't mean good. If you are building a Retrieval-Augmented Generation (RAG) pipeline, passing fast but hallucinated OCR data into your LLM will poison your context window. A slower, layout-aware engine like Docling ensures your agent actually gets the right numbers.


### 4. Next Steps to Push
1. Create the repo on GitHub (e.g., `ocr-engine-benchmark`).
2. Add your `ocr.py`, `requirements.txt`, and `README.md` to the folder.
3. Commit and push:
   ```bash
   git add .
   git commit -m "Initial commit: OCR benchmark script"
   git push origin main