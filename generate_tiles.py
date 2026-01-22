import os
from PIL import Image, ImageDraw, ImageFont

# Config
tile_size = 256  # standard tile size
zoom_levels = range(0, 5)  # generate zoom levels 0 to 4
output_dir = "tiles"

# Optional: load a font if you want
try:
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = None  # will use default font

for z in zoom_levels:
    num_tiles = 2 ** z
    for x in range(num_tiles):
        for y in range(num_tiles):
            # Create grey image
            img = Image.new("RGB", (tile_size, tile_size), color=(200, 200, 200))
            draw = ImageDraw.Draw(img)
            
            # Prepare the text
            text = f"{z}/{x}/{y}"

            # Get bounding box of the text
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            text_x = (tile_size - text_width) / 2
            text_y = (tile_size - text_height) / 2

            # Draw the text
            draw.text((text_x, text_y), text, fill=(50, 50, 50), font=font)

            
            # Create output folder
            tile_path = os.path.join(output_dir, str(z), str(x))
            os.makedirs(tile_path, exist_ok=True)
            
            # Save tile
            img.save(os.path.join(tile_path, f"{y}.png"))

print("Tiles generated successfully!")
