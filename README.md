# Markdown CV to PDF Converter

A lightweight, Python-based command-line tool that converts Markdown resumes into professionally styled, mathematically typeset PDFs.

This project uses **Pandoc** and **LaTeX** (via MiKTeX) to prioritize pristine typography and readable formatting, allowing developers to write their CV in simple Markdown while generating a beautiful, modular PDF output.

## Features

* **Separation of Concerns:** Write content in Markdown (`input/`) and output compiled PDFs (`output/`).
* **Modular Styling:** Easily swap between different layout and font profiles (e.g., 'modern' vs. 'classic') using a dedicated `profiles.py` configuration file.
* **Command-Line Interface:** Quickly generate different versions of your CV using built-in terminal arguments.

## Prerequisites

Because this tool relies on professional typesetting engines, you must install the following system-level software before running the Python script:

1. **Python 3.x:** Installed on your system.
2. **Pandoc:** Download and install the core engine from the [Pandoc website](https://pandoc.org/installing.html).
3. **MiKTeX (Windows):** Download and install [MiKTeX](https://miktex.org/download).
   * **Important Configuration:** You *must* add the MiKTeX `x64` binary folder to your Windows Environment Variables `PATH`.
   * Example path: `C:\Users\<YourUsername>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`

## Installation

1. Clone or download this repository.
2. Open your terminal in the project directory.
3. Set up a virtual environment (PowerShell):

```powershell

   python -m venv venv

```

4. Activate the Python virtual environment:

```powershell

   .\venv\Scripts\Activate.ps1

```

5. Install the required Python packages using the included requirements file:

```bash

   pip install -r requirements.txt

```

## Project Structure

* `convert.py`: The main execution script containing the CLI logic and folder management.
* `profiles.py`: A configuration dictionary storing Pandoc/LaTeX arguments for different visual styles.
* `requirements.txt`: Python package dependencies.
* `input/`: Place your source `.md` files here.
* `output/`: The script will automatically generate your compiled `.pdf` files here.

## Usage

First, place your Markdown CV inside the `input` folder (e.g., `input/my_cv.md`).

Open your terminal and run the script.

**Option 1: Run with default settings**
This will look for `my_cv.md`, apply the `modern` styling profile, and output `my_cv.pdf`.

```bash

python convert.py

```

**Option 2: Run with custom arguments**
You can specify the input file, output file, and styling profile using terminal flags:

```bash

python convert.py --input my_cv.md --output tech_resume.pdf --profile classic

```

### Available Arguments

* `-i`, `--input`: The name of your source file in the input folder (Default: `my_cv.md`).
* `-o`, `--output`: The desired name of your compiled PDF (Default: `my_cv.pdf`).
* `-p`, `--profile`: The styling profile to use from `profiles.py` (Default: `modern`).
