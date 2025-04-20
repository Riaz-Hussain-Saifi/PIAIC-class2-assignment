# PIAIC Student ID Card Generator (Command-Line & Google Colab)

## Project Description

This project provides tools to generate a downloadable PDF of a PIAIC Student ID card based on user input. The generated card aims to match the design specifications provided for the PIAIC class task, including layout, student details, profile photo, and specific design elements.

Two versions are available:

1.  **Python Script (Command-Line):** A script you run locally on your computer. It utilizes the `reportlab` library for PDF creation and the `Pillow` library for image processing.
2.  **Google Colab Notebook:** An online version that runs in your browser, requiring no local installation.

## Features (Applies to both versions unless noted)

*   **PDF Generation:** Creates a high-resolution PDF document (specific card size, often placed on A4 for local script) with the ID card layout.
*   **Accurate Layout:** Follows the specified layout for heading, student details, profile photo, colored rectangles, and signature section.
*   **User Input:** Prompts the user to enter all required student information.
*   **Profile Photo:** Accepts a user-provided profile photo (JPG or PNG format) and embeds it onto the card with a border.
*   **Customization (Local Script):**
    *   Allows users to specify custom colors (using Hex codes) for the 'Q1' and 'CAE' rectangles (defaults to Red and Purple).
    *   Supports an optional semi-transparent watermark using a user-provided PIAIC logo image.
*   **Font Handling (Local Script):** Attempts to use the Arial font and gracefully falls back to the built-in Helvetica font if Arial is not found.
*   **Validation:** Includes basic validation for user inputs and image files.
*   **Output:** Saves the generated ID card as a PDF file. The local script saves to a specified directory and attempts to open it; the Colab version makes it available for download.

## Requirements (Local Script Version)

*   Python 3.8 or higher
*   `reportlab` library
*   `Pillow` library
*(These are **not** required if using the Google Colab version)*

## Installation (Local Script Version)

*(Skip this section if using the Google Colab version)*

1.  **Clone the repository or download the script:**
    Make sure you have the `main.py` file.
2.  **Navigate to the project directory:**
    Open your terminal or command prompt and change the directory to where you saved the script.
    ```bash
    cd path/to/your/project/folder
    ```
3.  **Install required libraries:**
    ```bash
    pip install reportlab Pillow
    ```

## Usage (Local Script)

1.  **Run the script:**
    Execute the script from your terminal:
    ```bash
    python main.py
    ```
2.  **Follow the prompts:**
    The script will ask you to enter the following information:
    *   Student Details (Name, Roll Number, Distance Learning status, City, Center, Campus, Days/Time, Batch, Quarter Label, Track Label)
    *   The full path to the profile photo file (e.g., `C:\Users\YourName\Pictures\profile.jpg` or `/home/user/images/photo.png`).
    *   The desired output PDF filename (e.g., `my_card.pdf`).
    *   *(Optional - Local Script Specific)* Hex color code for the 'Q1' rectangle. Press Enter for default.
    *   *(Optional - Local Script Specific)* Hex color code for the 'CAE' rectangle. Press Enter for default.
    *   *(Optional - Local Script Specific)* The full path to a logo image file for a watermark. Press Enter to skip.

3.  **Retrieve the PDF:**
    If successful, the script will create the specified PDF file in the same directory where the script is run (or a specified output directory if modified). It might attempt to open the file automatically.

## Google Colab Version (Alternative)

For users who prefer not to set up a local Python environment or want a simpler web-based experience, a Google Colab notebook version of this generator is available:

[➡️ **Link to PIAIC ID Card Generator on Google Colab**](https://colab.research.google.com/drive/1l89etSMNsVeg4quoWK3U89SzpQvD995r?authuser=0#scrollTo=POY8h2jOoiCd)

**Benefits:**

*   No local Python or library installation required.
*   Runs directly in your web browser (requires a Google account).
*   Easier file handling (upload prompts within the notebook).

**Usage (Colab):**

1.  Click the link above to open the notebook in Google Colab.
2.  Read the instructions provided within the notebook cells.
3.  Run the code cells sequentially by clicking the 'Play' button next to each cell.
4.  You will be prompted to enter student details directly in the notebook's input fields.
5.  You will be prompted to upload your profile photo (and optional logo if supported by that version) using Colab's file upload interface.
6.  After execution, the generated PDF file will be available for download from the Colab environment (check the notebook's output or file browser panel).

## Error Handling (Local Script)

The local script includes basic error handling for common issues:
*   File not found errors for the profile photo, optional logo.
*   Errors related to invalid, corrupted, or unsupported image file formats.
*   Notifications if invalid Hex color codes are entered (defaults will be used).

Error messages will be printed to the console to guide the user. (The Colab version will display errors within the notebook interface).

---

*This project was created as part of a PIAIC class assignment.*
