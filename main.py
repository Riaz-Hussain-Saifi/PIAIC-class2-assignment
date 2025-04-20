# --- Prerequisites ---
# Make sure you have ReportLab and Pillow installed:
# pip install reportlab Pillow
# -------------------

import io
import os # Needed for checking file existence
from PIL import Image as PILImage # Pillow is used by ReportLab's ImageReader

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm # Millimeters for easier dimensioning
from reportlab.lib.pagesizes import A4 # We'll define a custom size based on mm
from reportlab.lib.colors import black, white, red, purple, cyan, HexColor
from reportlab.lib.utils import ImageReader
from reportlab.lib.enums import TA_CENTER, TA_RIGHT # For text alignment

# --- 1. Function to Get User Input ---
def get_student_info():
    """Prompts the user for student details."""
    print("--- Please Enter Student Details ---")
    details = {
        "student_name": input("Name: "),
        "roll_number": input("Roll Number (e.g., PIAIC123456): "),
        "distance_learning": input("Distance Learning (Yes/No): "),
        "city": input("City: "),
        "center": input("Center (e.g., Sindh Boy Scouts Association): "),
        "campus": input("Campus (e.g., Main Campus): "),
        "days_time": input("Days/Time (e.g., Saturday - 02:00 PM to 06:00 PM): "),
        "batch": input("Batch (e.g., Batch 71): "),
        "quarter": input("Quarter Label (e.g., Q1): "), # For the red label
        "track": input("Track Label (e.g., CAE, AI): "), # For the purple label
        "image_path": input("Full path to student's photo (e.g., C:\\path\\to\\photo.jpg): "),
        "output_filename": input("Enter desired output PDF filename (e.g., piaic_card.pdf): ")
    }
    # Ensure output filename ends with .pdf
    if not details["output_filename"].lower().endswith(".pdf"):
        details["output_filename"] += ".pdf"
        print(f"   (Adjusted filename to: {details['output_filename']})")

    print("------------------------------------\n")
    return details

# --- 2. Function to Generate the ID Card PDF ---
def generate_id_card(details):
    """Generates the PIAIC ID Card PDF based on provided details."""

    # --- Card Dimensions and Styling ---
    card_width = 140 * mm
    card_height = 90 * mm
    margin = 4 * mm # Border margin

    # Font settings (Using standard Helvetica)
    font_normal = "Helvetica"
    font_bold = "Helvetica-Bold"
    font_size_heading = 16
    font_size_info_label = 9.5 # Font size for labels like "Name:"
    font_size_info_value = 9.5 # Font size for values like "Muhammad Ali"
    font_size_label_footer = 9 # Font size for Q1/CAE labels
    font_size_signature = 8

    # Photo dimensions and position (tuned to look like typical ID cards)
    photo_width = 30 * mm
    photo_height = 38 * mm
    photo_margin_top = 7 * mm # Distance from top border edge
    photo_margin_right = 7 * mm # Distance from right border edge

    # Colors (Using standard names, can be replaced with HexColor for exact shades)
    # piaic_red = HexColor("#E31E24") # Example Red if needed
    # piaic_purple = HexColor("#662D91") # Example Purple if needed
    # piaic_cyan = HexColor("#00AEEF") # Example Cyan if needed
    piaic_red = red
    piaic_purple = purple
    piaic_cyan = cyan

    # --- PDF Generation ---
    try:
        c = canvas.Canvas(details["output_filename"], pagesize=(card_width, card_height))

        # --- Optional: Background Logo/Watermark ---
        # Uncomment and adjust if you have a watermark image file
        # try:
        #     watermark_path = 'piaic_logo_watermark.png' # Place this file in the same directory
        #     if os.path.exists(watermark_path):
        #         watermark = ImageReader(watermark_path)
        #         # Center the watermark roughly
        #         wm_width = card_width * 0.4
        #         wm_height = card_height * 0.4 # Adjust size as needed
        #         wm_x = (card_width - wm_width) / 2
        #         wm_y = (card_height - wm_height) / 3 # Position lower part of card
        #         c.saveState()
        #         c.setFillAlpha(0.1) # Make it very transparent
        #         c.drawImage(watermark, wm_x, wm_y, width=wm_width, height=wm_height, preserveAspectRatio=True, mask='auto')
        #         c.restoreState()
        # except Exception as e:
        #     print(f"⚠️ Warning: Could not add watermark - {e}")
        # -------------------------------------------

        # --- Card Background and Border ---
        c.setFillColor(white)
        c.rect(0, 0, card_width, card_height, fill=1) # White background
        c.setStrokeColor(black)
        c.setLineWidth(1) # Standard line width for border
        # Draw border slightly inside the page edges
        c.rect(margin, margin, card_width - 2 * margin, card_height - 2 * margin, stroke=1, fill=0)

        # --- Top Section: Heading ---
        c.setFont(font_bold, font_size_heading)
        c.setFillColor(black)
        # Position heading centered horizontally, vertically below top margin
        heading_y = card_height - margin - 8*mm # Adjust vertical position
        c.drawCentredString(card_width / 2, heading_y, "ID CARD")

        # --- Top Section: Student Photo ---
        image_path = details["image_path"]
        # Calculate photo position (top-right corner, respecting margins)
        photo_x = card_width - margin - photo_margin_right - photo_width
        photo_y = card_height - margin - photo_margin_top - photo_height

        if not os.path.exists(image_path):
            print(f"⚠️ Error: Image file not found at '{image_path}'. Drawing placeholder.")
            # Draw a placeholder box if image fails
            c.setStrokeColor(black)
            c.setLineWidth(0.5)
            c.rect(photo_x, photo_y, photo_width, photo_height, stroke=1, fill=0)
            c.setFont(font_normal, 8)
            c.setFillColor(black)
            c.drawCentredString(photo_x + photo_width/2, photo_y + photo_height/2, "Photo Missing")
        else:
            try:
                student_photo = ImageReader(image_path)
                # Draw the image, preserving aspect ratio, anchored to center of the box
                c.drawImage(student_photo, photo_x, photo_y, width=photo_width, height=photo_height, preserveAspectRatio=True, mask='auto', anchor='c')
                # Draw a thin border around the photo
                c.setStrokeColor(black)
                c.setLineWidth(0.5)
                c.rect(photo_x, photo_y, photo_width, photo_height, stroke=1, fill=0)
            except Exception as e:
                print(f"⚠️ Error processing image: {e}. Drawing placeholder.")
                # Draw a placeholder box if image processing fails
                c.setStrokeColor(black)
                c.setLineWidth(0.5)
                c.rect(photo_x, photo_y, photo_width, photo_height, stroke=1, fill=0)
                c.setFont(font_normal, 8)
                c.setFillColor(black)
                c.drawCentredString(photo_x + photo_width/2, photo_y + photo_height/2, "Photo Error")


        # --- Student Information (Left Side) ---
        c.setFillColor(black)
        text_x_label = margin + 6 * mm # X position for labels (e.g., "Name:")
        text_x_value = text_x_label + 30 * mm # X position for values (e.g., "Student Name") - Adjust indent as needed
        # Start Y position below the heading, leaving space
        text_y = heading_y - 8 * mm
        line_height = 4.5 * mm # Vertical spacing between lines - adjust for visual fit

        info_lines = [
            ("Name", details["student_name"]),
            ("Roll Number", details["roll_number"]),
            ("Distance Learning", details["distance_learning"]),
            ("City", details["city"]),
            ("Center", details["center"]),
            ("Campus", details["campus"]),
            ("Days/Time", details["days_time"]),
            ("Batch", details["batch"]),
        ]

        for label, value in info_lines:
            # Draw label (bold)
            c.setFont(font_bold, font_size_info_label)
            c.drawString(text_x_label, text_y, f"{label}:")
            # Draw value (normal)
            c.setFont(font_normal, font_size_info_value)
            c.drawString(text_x_value, text_y, value)
            text_y -= line_height # Move down for the next line

        # --- Colored Footer Labels (Bottom-Left) ---
        label_height = 5 * mm
        label_width = 12 * mm
        label_spacing = 1.5 * mm # Space between the two labels
        label_y = margin + 6 * mm # Position from bottom margin
        label_x_start = margin + 6 * mm # Position from left margin

        # Quarter Label (Red)
        c.setFillColor(piaic_red)
        c.rect(label_x_start, label_y, label_width, label_height, stroke=0, fill=1)
        c.setFont(font_bold, font_size_label_footer)
        c.setFillColor(white)
        # Center text vertically within the label rectangle
        c.drawCentredString(label_x_start + label_width / 2, label_y + (label_height - font_size_label_footer)/2 + 0.5*mm, details["quarter"])

        # Track Label (Purple) - Positioned next to Quarter
        label_x_track = label_x_start + label_width + label_spacing
        c.setFillColor(piaic_purple)
        c.rect(label_x_track, label_y, label_width, label_height, stroke=0, fill=1)
        c.setFont(font_bold, font_size_label_footer)
        c.setFillColor(white)
        # Center text vertically
        c.drawCentredString(label_x_track + label_width / 2, label_y + (label_height - font_size_label_footer)/2 + 0.5*mm, details["track"])

        # --- Authorized Signature Line (Bottom-Right) ---
        # Align signature line vertically slightly above the colored labels
        sig_line_y = label_y + label_height + 1 * mm
        # Define horizontal position and length for the signature line
        sig_line_start_x = card_width * 0.58 # Start further right
        sig_line_end_x = card_width - margin - 6 * mm # End near right margin
        c.setStrokeColor(black)
        c.setLineWidth(0.5)
        c.line(sig_line_start_x, sig_line_y, sig_line_end_x, sig_line_y)

        # Signature Text ("Authorized Signature")
        c.setFont(font_normal, font_size_signature)
        c.setFillColor(piaic_cyan) # Use the defined cyan color
        sig_text_y = sig_line_y - 3 * mm # Position text below the line
        # Center the text horizontally under the line
        sig_text_center_x = (sig_line_start_x + sig_line_end_x) / 2
        c.drawCentredString(sig_text_center_x, sig_text_y, "Authorized Signature")

        # --- Save the PDF ---
        c.save()
        print(f"\n✅ Successfully generated ID card: '{details['output_filename']}'")
        print(f"   The file has been saved in the current directory.")

    except Exception as e:
        print(f"\n❌ An error occurred during PDF generation: {e}")
        import traceback
        traceback.print_exc() # Print detailed error traceback

# --- 3. Main Execution Block ---
if __name__ == "__main__":
    print("===================================")
    print("  PIAIC ID Card Generator Script ")
    print("===================================\n")

    # Get student details from user
    student_details = get_student_info()

    # Generate the ID card
    generate_id_card(student_details)

    print("\n--- Script Finished ---")
