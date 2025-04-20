# PIAIC Student ID Card Generator (Command-Line)

## Project Description

This Python script generates a downloadable PDF of a PIAIC Student ID card based on user input provided via the command line. The generated card aims to match the design specifications provided for the PIAIC class task, including layout, student details, profile photo, and specific design elements.

This project utilizes the `reportlab` library for PDF creation and the `Pillow` library for image processing.

## Features

*   **PDF Generation:** Creates a high-resolution PDF document (A4 size) with the ID card centered.
*   **Accurate Layout:** Follows the specified layout for heading, student details, profile photo, colored rectangles, and signature section.
*   **Command-Line Interface:** Prompts the user to enter all required student information.
*   **Profile Photo:** Accepts a user-provided profile photo (JPG or PNG format) and embeds it onto the card with a border.
*   **Customization:**
    *   Allows users to specify custom colors (using Hex codes) for the 'Q1' and 'CAE' rectangles (defaults to Red and Purple).
    *   Supports an optional semi-transparent watermark using a user-provided PIAIC logo image.
*   **Font Handling:** Attempts to use the Arial font and gracefully falls back to the built-in Helvetica font if Arial is not found.
*   **Validation:** Includes basic validation for user inputs (non-empty fields) and image files (existence, readability, format).
*   **Output:** Saves the generated ID card as `PIAIC_Student_ID_Card.pdf` in a user-specified directory and attempts to open it automatically.

## Requirements

*   Python 3.8 or higher
*   `reportlab` library
*   `Pillow` library

## Installation

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

## Usage

1.  **Run the script:**
    Execute the script from your terminal:
    ```bash
    python main.py
    ```
2.  **Follow the prompts:**
    The script will ask you to enter the following information:
    *   Student Details (Name, Roll Number, Distance Learning status, City, Center, Campus, Days/Time, Batch)
    *   The full path to the profile photo file (e.g., `C:\Users\YourName\Pictures\profile.jpg` or `/home/user/images/photo.png`).
    *   The full path to the directory where you want to save the generated PDF (e.g., `C:\Users\YourName\Documents` or `/home/user/output`).
    *   *(Optional)* Hex color code for the 'Q1' rectangle (e.g., `#FF0000`). Press Enter to use the default Red.
    *   *(Optional)* Hex color code for the 'CAE' rectangle (e.g., `#800080`). Press Enter to use the default Purple.
    *   *(Optional)* The full path to a logo image file (e.g., `piaic_logo.png`) to be used as a watermark. Press Enter to skip the watermark.

3.  **Retrieve the PDF:**
    If successful, the script will create the `PIAIC_Student_ID_Card.pdf` file in the output directory you specified. It will also attempt to open the file automatically using your system's default PDF viewer.

## Error Handling

The script includes basic error handling for common issues:
*   File not found errors for the profile photo, optional logo, or output directory.
*   Errors related to invalid, corrupted, or unsupported image file formats.
*   Notifications if invalid Hex color codes are entered (defaults will be used).

Error messages will be printed to the console to guide the user.

---

*This project was created as part of a PIAIC class assignment.*
