from PIL import Image, ImageDraw, ImageFont

# --- Canvas Setup ---
width, height = 800, 600
poster = Image.new("RGB", (width, height), "navy")
draw = ImageDraw.Draw(poster)

# --- Fonts ---
try:
    font_title = ImageFont.truetype("arialbd.ttf", 64)
    font_text = ImageFont.truetype("arial.ttf", 36)
except:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

# --- Helper: Centered Text Function ---
def draw_centered_text(draw, text, font, y, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, y), text, font=font, fill=fill)

# --- Team Name (Centered) ---
draw_centered_text(draw, "BSCS 4 WARRIORS", font_title, 50, "gold")

# --- Slogan (Centered) ---
draw_centered_text(draw, "\"Unite. Fight. Win.\"", font_text, 130, "white")

# --- WARRIOR EMBLEM (Shield + Sword) ---
# Shield base (polygon)
shield_top = 240
shield_center_x = width // 2
shield_width = 120
shield_height = 170

shield_points = [
    (shield_center_x - shield_width // 2, shield_top),  # Top left
    (shield_center_x + shield_width // 2, shield_top),  # Top right
    (shield_center_x + shield_width // 2 - 10, shield_top + 70),
    (shield_center_x, shield_top + shield_height),       # Bottom point
    (shield_center_x - shield_width // 2 + 10, shield_top + 70)
]
draw.polygon(shield_points, fill="gold", outline="white")

# Sword (centered inside shield)
sword_x = shield_center_x
sword_top = shield_top + 20
sword_bottom = shield_top + 120

# Sword blade
draw.line([(sword_x, sword_top), (sword_x, sword_bottom)], fill="white", width=4)

# Crossguard
draw.line([(sword_x - 12, sword_top + 20), (sword_x + 12, sword_top + 20)], fill="white", width=3)

# Handle
draw.rectangle([sword_x - 2, sword_bottom, sword_x + 2, sword_bottom + 20], fill="white")

# Shield inner border (optional)
inner_offset = 5
inner_points = [(x + (inner_offset if x < shield_center_x else -inner_offset), y + inner_offset)
                for (x, y) in shield_points]
draw.line(inner_points + [inner_points[0]], fill="white", width=1)

# --- Border ---
border_color = "white"
border_thickness = 10
draw.rectangle(
    [border_thickness//2, border_thickness//2, width - border_thickness//2, height - border_thickness//2],
    outline=border_color,
    width=border_thickness
)

# --- Save and Show Output ---
poster.save("bscs4_team_spirit_poster.png")
poster.show()
