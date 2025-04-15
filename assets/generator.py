from PIL import Image
import os

# Define paths
base_card_path = 'static/BaseCard.png'
colors_dir = 'static/colors/'
numbers_dir = 'static/numbers/'
output_dir = 'generated/'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load base card
base_card = Image.open(base_card_path).convert("RGBA")

# Process all color/number combinations
for color_file in os.listdir(colors_dir):
    color_path = os.path.join(colors_dir, color_file)
    color = Image.open(color_path).convert("RGBA")
    
    for number_file in os.listdir(numbers_dir):
        number_path = os.path.join(numbers_dir, number_file)
        number = Image.open(number_path).convert("RGBA")
        
        # Create composite image
        composite = base_card.copy()
        composite.paste(color, (0, 0), color)  # Paste color with transparency
        composite.paste(number, (0, 0), number)  # Paste number with transparency
        
        # Save result
        output_name = f"card_{color_file.split('.')[0]}_{number_file}"
        composite.save(os.path.join(output_dir, output_name))
