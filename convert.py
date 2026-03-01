import argparse
from pathlib import Path
import pypandoc

# Import our dictionary of styles from the profiles.py file
from profiles import cv_profiles

def generate_cv(input_filename, output_filename, profile_name):
    """
    Converts a Markdown CV from an input folder to a PDF in an output folder.
    """
    # 1. Setup our directory paths
    input_dir = Path("input")
    output_dir = Path("output")
    
    # Create the output directory if it does not already exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Construct the full file paths
    # pathlib uses the '/' operator to safely join folders and filenames
    input_filepath = input_dir / input_filename
    output_filepath = output_dir / output_filename
    
    # 3. Check if the input file actually exists before trying to convert
    if not input_filepath.is_file():
        print(f"Error: Could not find '{input_filepath}'.")
        print("Please ensure you have created an 'input' folder and placed your Markdown file inside it.")
        return

    # 4. Validate the chosen styling profile
    if profile_name not in cv_profiles:
        print(f"Warning: Profile '{profile_name}' not found. Defaulting to 'modern'.")
        profile_name = "modern"
    
    extra_args = cv_profiles[profile_name]
    
    print(f"Reading from: {input_filepath}")
    print(f"Generating CV using the '{profile_name}' profile...")
    
    try:
        # 5. Convert the document using Pandoc
        # Note: pypandoc expects strings, so we convert the Path objects to strings using str()
        pypandoc.convert_file(
            str(input_filepath), 
            'pdf', 
            outputfile=str(output_filepath),
            extra_args=extra_args
        )
        print(f"Success! Your CV is ready at: {output_filepath}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Tip: Ensure your Markdown syntax is correct and MiKTeX packages are installed.")

# 6. Command-line argument setup
if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Convert Markdown CV to PDF.")
    
    # Define the arguments the user can provide
    parser.add_argument('-i', '--input', type=str, default='my_cv.md', help="Name of the input Markdown file.")
    parser.add_argument('-o', '--output', type=str, default='my_cv.pdf', help="Name of the output PDF file.")
    parser.add_argument('-p', '--profile', type=str, default='modern', help="Styling profile to use (e.g., 'modern' or 'classic').")
    
    # Parse the arguments from the terminal
    args = parser.parse_args()
    
    # Run the function with the provided arguments
    generate_cv(args.input, args.output, args.profile)