import pypandoc

# 1. Define your input and output file paths
input_md = 'my_cv.md'
output_pdf = 'my_cv.pdf'

try:
    # 2. Convert using Pandoc, specifying a LaTeX engine (like xelatex or pdflatex)
    # extra_args allows us to pass specific layout options to the LaTeX engine
    pypandoc.convert_file(
        input_md, 
        'pdf', 
        outputfile=output_pdf,
        extra_args=['--pdf-engine=xelatex', '-V', 'geometry:margin=1in']
    )
    print("LaTeX CV successfully generated!")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Ensure Pandoc and MiKTeX are installed and added to your Windows PATH.")