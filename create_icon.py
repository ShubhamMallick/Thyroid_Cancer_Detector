"""
Script to create a simple thyroid icon for the application
"""
from PIL import Image, ImageDraw
import os

def create_thyroid_icon():
    # Create a 256x256 image with transparent background
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Define colors
    thyroid_color = (70, 130, 180)  # Steel blue
    outline_color = (25, 25, 112)   # Midnight blue
    
    # Draw thyroid shape (butterfly-like shape)
    center_x, center_y = size // 2, size // 2
    
    # Left lobe
    left_lobe = [
        (center_x - 80, center_y - 40),
        (center_x - 100, center_y - 20),
        (center_x - 110, center_y + 20),
        (center_x - 90, center_y + 60),
        (center_x - 60, center_y + 70),
        (center_x - 30, center_y + 50),
        (center_x - 20, center_y + 20),
        (center_x - 30, center_y - 20)
    ]
    
    # Right lobe
    right_lobe = [
        (center_x + 80, center_y - 40),
        (center_x + 100, center_y - 20),
        (center_x + 110, center_y + 20),
        (center_x + 90, center_y + 60),
        (center_x + 60, center_y + 70),
        (center_x + 30, center_y + 50),
        (center_x + 20, center_y + 20),
        (center_x + 30, center_y - 20)
    ]
    
    # Draw the lobes
    draw.polygon(left_lobe, fill=thyroid_color, outline=outline_color, width=3)
    draw.polygon(right_lobe, fill=thyroid_color, outline=outline_color, width=3)
    
    # Draw connecting isthmus
    isthmus = [
        (center_x - 20, center_y + 20),
        (center_x + 20, center_y + 20),
        (center_x + 25, center_y + 35),
        (center_x - 25, center_y + 35)
    ]
    draw.polygon(isthmus, fill=thyroid_color, outline=outline_color, width=2)
    
    # Add medical cross symbol
    cross_size = 30
    cross_thickness = 8
    cross_x, cross_y = center_x, center_y - 80
    
    # Vertical line of cross
    draw.rectangle([
        cross_x - cross_thickness//2, cross_y - cross_size//2,
        cross_x + cross_thickness//2, cross_y + cross_size//2
    ], fill=(220, 20, 60))  # Crimson
    
    # Horizontal line of cross
    draw.rectangle([
        cross_x - cross_size//2, cross_y - cross_thickness//2,
        cross_x + cross_size//2, cross_y + cross_thickness//2
    ], fill=(220, 20, 60))  # Crimson
    
    # Save in multiple sizes
    sizes = [16, 32, 48, 64, 128, 256]
    for s in sizes:
        resized = img.resize((s, s), Image.Resampling.LANCZOS)
        resized.save(f'thyroid_icon_{s}.png')
    
    # Save as ICO file for Windows
    img.save('thyroid_icon.ico', format='ICO', sizes=[(16,16), (32,32), (48,48), (64,64)])
    print("Icon files created successfully!")

if __name__ == "__main__":
    create_thyroid_icon()
