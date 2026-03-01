"""
This file stores our different styling profiles for the CV.
Each profile is a list of arguments passed to Pandoc and LaTeX.
"""

# 1. Define a sleek, modern profile with sans-serif fonts and blue links
modern_profile = [
    '--pdf-engine=xelatex',
    '-V', 'geometry:margin=1in',
    '-V', 'mainfont=Arial',      # Changes the main text to a clean sans-serif font
    '-V', 'colorlinks=true',     # Enables colored links instead of boxes
    '-V', 'linkcolor=blue',      # Sets hyperlinks to blue
    '-V', 'urlcolor=blue'        # Sets URLs to blue
]

# 2. Define a traditional, classic profile
classic_profile = [
    '--pdf-engine=xelatex',
    '-V', 'geometry:margin=1.2in', # Slightly wider margins
    '-V', 'colorlinks=true',
    '-V', 'linkcolor=darkgray'     # A subtle, professional link color
]

# 3. Export them in a dictionary for easy access
cv_profiles = {
    'modern': modern_profile,
    'classic': classic_profile
}