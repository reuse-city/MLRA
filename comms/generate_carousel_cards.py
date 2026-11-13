#!/usr/bin/env python3
"""
Generate a 5-card carousel set (1080x1350, 4:5 portrait) for Instagram.
Inviting participation to the Material Literacy & Resource Assessment (MLRA)
project co-design and the 18 November 2026 Info Session.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, 'assets')
OUT_DIR = os.path.join(SCRIPT_DIR, 'instagram-cards')
os.makedirs(OUT_DIR, exist_ok=True)

# Brand colors
C_MAGENTA = (229, 0, 80)
C_DARK_MAGENTA = (184, 0, 63)
C_LIGHT_MAGENTA = (255, 240, 246)
C_HSS_GREEN = (105, 151, 31)
C_DARK = (24, 24, 28)
C_WHITE = (255, 255, 255)
C_BG = (247, 248, 250)
C_CARD_BORDER = (226, 230, 238)
C_MUTED_TEXT = (90, 95, 105)
C_SUBTLE = (140, 145, 158)

FONT_BOLD_PATH = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FONT_REG_PATH = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FONT_ITALIC_PATH = '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'

def get_font(size, bold=False, italic=False):
    path = FONT_BOLD_PATH if bold else (FONT_ITALIC_PATH if italic else FONT_REG_PATH)
    return ImageFont.truetype(path, size)

# Load assets
gig_logo = Image.open(f'{ASSETS_DIR}/gig_logo.png').convert('RGBA')
hss_logo = Image.open(f'{ASSETS_DIR}/hss_logo_de.png').convert('RGBA')
hss_fp_logo = Image.open(f'{ASSETS_DIR}/hss_foerderprogramm.png').convert('RGBA')
reuse_logo = Image.open(f'{ASSETS_DIR}/reuse_city_logo.png').convert('RGBA')
qr_code = Image.open(f'{ASSETS_DIR}/qr_code.png').convert('RGBA')
knolling_img = Image.open(f'{ASSETS_DIR}/camera_knolling.png').convert('RGBA')
workshop_img = Image.open(f'{ASSETS_DIR}/maker_workshop.png').convert('RGBA')

def draw_rounded_card(draw, rect, radius=24, fill=C_WHITE, outline=C_CARD_BORDER, width=2):
    draw.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=width)

def draw_pill(draw, xy, text, font, fill=C_LIGHT_MAGENTA, text_color=C_MAGENTA, pad_x=22, pad_y=9):
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    w = tw + pad_x * 2
    h = th + pad_y * 2
    x0, y0 = xy[0] - w//2, xy[1] - h//2
    draw.rounded_rectangle((x0, y0, x0 + w, y0 + h), radius=h//2, fill=fill)
    draw.text((x0 + pad_x - bbox[0], y0 + pad_y - bbox[1]), text, font=font, fill=text_color)
    return x0, y0, w, h

def draw_header_bar(img, draw, card_idx, total_cards=5):
    # Header background
    draw.rectangle([0, 0, W, 130], fill=C_WHITE)
    draw.line([(0, 130), (W, 130)], fill=(230, 233, 240), width=2)

    # GIG Logo left
    gh = 62
    gw = int(gig_logo.width * (gh / gig_logo.height))
    gl = gig_logo.resize((gw, gh), Image.Resampling.LANCZOS)
    img.alpha_composite(gl, (55, (130 - gh) // 2 + 2))

    # HSS Logo right
    hh = 66
    hw = int(hss_logo.width * (hh / hss_logo.height))
    hl = hss_logo.resize((hw, hh), Image.Resampling.LANCZOS)
    img.alpha_composite(hl, (W - 55 - hw, (130 - hh) // 2 + 2))

    # Card indicator pill at top right of content or subtle dots
    draw.text((W // 2, 70), f"{card_idx} / {total_cards}", font=get_font(20, bold=True), fill=C_SUBTLE, anchor="mm")

def draw_footer_bar(draw, text="Swipe to learn more  ->"):
    draw.rectangle([0, H - 70, W, H], fill=C_WHITE)
    draw.line([(0, H - 70), (W, H - 70)], fill=(230, 233, 240), width=2)
    draw.text((W // 2, H - 35), text, font=get_font(20, bold=True), fill=C_MAGENTA, anchor="mm")

# -------------------------------------------------------------------------
# CARD 1: COVER / HOOK
# -------------------------------------------------------------------------
def render_card_1():
    img = Image.new('RGBA', (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header_bar(img, draw, 1)

    # Hero circular photo (camera knolling)
    circle_diam = 530
    mask = Image.new('L', (circle_diam, circle_diam), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, circle_diam, circle_diam), fill=255)

    kw, kh = knolling_img.size
    cw, ch = int(circle_diam * 1.35), int(circle_diam * 1.35)
    crop = knolling_img.crop(((kw - cw)//2, (kh - ch)//2, (kw + cw)//2, (kh + ch)//2))
    crop = crop.resize((circle_diam, circle_diam), Image.Resampling.LANCZOS)

    circle_card = Image.new('RGBA', (circle_diam, circle_diam), (0,0,0,0))
    circle_card.paste(crop, (0, 0), mask)

    cx, cy = W // 2, 440
    ring_r = circle_diam // 2 + 10
    draw.ellipse([cx - ring_r, cy - ring_r, cx + ring_r, cy + ring_r], outline=C_MAGENTA, width=8)
    img.alpha_composite(circle_card, (cx - circle_diam//2, cy - circle_diam//2))

    # Bottom Content Card
    card_rect = [55, 740, W - 55, 1240]
    draw_rounded_card(draw, card_rect, radius=28, fill=C_WHITE, outline=C_CARD_BORDER, width=2)

    draw_pill(draw, (W // 2, 795), "OPEN CALL FOR CO-DESIGNERS", get_font(22, bold=True), fill=C_LIGHT_MAGENTA, text_color=C_MAGENTA, pad_x=24, pad_y=10)

    draw.text((W // 2, 865), "CALLING ALL MAKERS,", font=get_font(40, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 920), "REPAIRERS & EDUCATORS!", font=get_font(40, bold=True), fill=C_MAGENTA, anchor="mm")

    draw.text((W // 2, 995), "Have experiential knowledge in repair cafés,", font=get_font(26, bold=False), fill=C_MUTED_TEXT, anchor="mm")
    draw.text((W // 2, 1035), "makerspaces, and local material circularity?", font=get_font(26, bold=False), fill=C_MUTED_TEXT, anchor="mm")

    draw.line([(100, 1080), (W - 100, 1080)], fill=(235, 238, 245), width=2)

    draw.text((W // 2, 1125), "Help us turn repair expertise into open learning.", font=get_font(28, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 1165), "Building on the Circular Material Valuer findings.", font=get_font(24, italic=True), fill=C_MUTED_TEXT, anchor="mm")

    draw_footer_bar(draw, "Swipe to discover the project  ->")
    return img

# -------------------------------------------------------------------------
# CARD 2: THE PROJECT & PLATFORM
# -------------------------------------------------------------------------
def render_card_2():
    img = Image.new('RGBA', (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header_bar(img, draw, 2)

    draw_pill(draw, (W // 2, 175), "NEW GIG PROJECT • 2026–2027", get_font(22, bold=True), fill=C_LIGHT_MAGENTA, text_color=C_MAGENTA, pad_x=24, pad_y=10)

    draw.text((W // 2, 240), "Material Literacy &", font=get_font(46, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 295), "Resource Assessment", font=get_font(46, bold=True), fill=C_MAGENTA, anchor="mm")
    draw.text((W // 2, 350), "( MLRA )", font=get_font(32, bold=True), fill=C_HSS_GREEN, anchor="mm")

    # Photo Card (workshop photo)
    pw, ph = W - 110, 390
    w_img = workshop_img.resize((pw, int(workshop_img.height * (pw / workshop_img.width))), Image.Resampling.LANCZOS)
    w_crop = w_img.crop((0, (w_img.height - ph)//2, pw, (w_img.height + ph)//2))
    mask_card = Image.new('L', (pw, ph), 0)
    ImageDraw.Draw(mask_card).rounded_rectangle((0, 0, pw, ph), radius=24, fill=255)
    img.paste(w_crop, (55, 395), mask_card)

    # Narrative Card
    card2_rect = [55, 810, W - 55, 1240]
    draw_rounded_card(draw, card2_rect, radius=28, fill=C_WHITE, outline=C_CARD_BORDER, width=2)

    draw_pill(draw, (W // 2, 860), "GLOBAL INNOVATION ACADEMY", get_font(22, bold=True), fill=C_LIGHT_MAGENTA, text_color=C_MAGENTA, pad_x=22, pad_y=8)
    draw.text((W // 2, 915), "A Permanent, Community-Owned MOOC", font=get_font(32, bold=True), fill=C_DARK, anchor="mm")

    lines = [
        "Too often, valuable open knowledge and curricula disappear",
        "when temporary project grants and commercial platforms expire.",
        "",
        "MLRA translates hands-on workshop expertise into open, self-paced",
        "learning pathways hosted permanently on the community-owned GIA."
    ]
    y_d = 970
    for line in lines:
        if line:
            draw.text((W // 2, y_d), line, font=get_font(24, bold=False), fill=C_MUTED_TEXT, anchor="mm")
        y_d += 32

    draw.line([(100, 1135), (W - 100, 1135)], fill=(235, 238, 245), width=2)

    # Funder note & emblem
    draw.text((100, 1180), "Supported by Hans Sauer Stiftung", font=get_font(22, bold=True), fill=C_HSS_GREEN)
    draw.text((100, 1210), "Förderprogramm 'Citizen Science... und dann? 2026–2027'", font=get_font(19, italic=True), fill=C_MUTED_TEXT)

    fpw = 170
    fph = int(hss_fp_logo.height * (fpw / hss_fp_logo.width))
    fpl = hss_fp_logo.resize((fpw, fph), Image.Resampling.LANCZOS)
    img.alpha_composite(fpl, (W - 80 - fpw, 1150))

    draw_footer_bar(draw, "Swipe to see the 3 co-design tracks  ->")
    return img

# -------------------------------------------------------------------------
# CARD 3: WHAT WE ARE CO-DESIGNING
# -------------------------------------------------------------------------
def render_card_3():
    img = Image.new('RGBA', (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header_bar(img, draw, 3)

    draw_pill(draw, (W // 2, 175), "PARTICIPATORY TRACKS", get_font(22, bold=True), fill=C_LIGHT_MAGENTA, text_color=C_MAGENTA, pad_x=24, pad_y=10)

    draw.text((W // 2, 235), "What We Are Co-Designing", font=get_font(44, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 285), "Collaborative modules for open workshops:", font=get_font(26, bold=False), fill=C_MUTED_TEXT, anchor="mm")

    pillars = [
        ("1", "Material Identification", "Low-tech testing protocols and visual guides for plastics, metals, and textiles in community spaces.", C_MAGENTA),
        ("2", "Condition & Repair Triage", "Diagnostic rubrics to assess repair viability, component harvesting, and local material value.", C_HSS_GREEN),
        ("3", "Open Commons (OER)", "Self-paced, multilingual learning paths published under CC BY-SA 4.0 on the Global Innovation Academy.", (58, 120, 130))
    ]

    y_top = 340
    for num, title, desc, accent_color in pillars:
        card_box = [55, y_top, W - 55, y_top + 235]
        draw_rounded_card(draw, card_box, radius=24, fill=C_WHITE, outline=C_CARD_BORDER, width=2)
        draw.rounded_rectangle([55, y_top, 67, y_top + 235], radius=4, fill=accent_color)

        badge_r = 24
        bx, by = 115, y_top + 48
        draw.ellipse([bx - badge_r, by - badge_r, bx + badge_r, by + badge_r], fill=accent_color)
        draw.text((bx, by), num, font=get_font(24, bold=True), fill=C_WHITE, anchor="mm")

        draw.text((155, y_top + 33), title, font=get_font(30, bold=True), fill=C_DARK)

        words = desc.split()
        line1 = " ".join(words[:8])
        line2 = " ".join(words[8:])
        draw.text((105, y_top + 100), line1, font=get_font(24, bold=False), fill=C_MUTED_TEXT)
        draw.text((105, y_top + 138), line2, font=get_font(24, bold=False), fill=C_MUTED_TEXT)

        draw.text((105, y_top + 192), "[+] Community Review & Pilot Validation", font=get_font(20, bold=True), fill=accent_color)
        y_top += 260

    draw.text((W // 2, 1160), "Are you a fixer, educator, or maker?", font=get_font(28, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 1200), "Your experience is central to shaping this course.", font=get_font(25, italic=True), fill=C_MAGENTA, anchor="mm")

    draw_footer_bar(draw, "Swipe for the Info Session date  ->")
    return img

# -------------------------------------------------------------------------
# CARD 4: THE FIRST INFO SESSION
# -------------------------------------------------------------------------
def render_card_4():
    img = Image.new('RGBA', (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header_bar(img, draw, 4)

    draw_pill(draw, (W // 2, 175), "SAVE THE DATE", get_font(22, bold=True), fill=C_LIGHT_MAGENTA, text_color=C_MAGENTA, pad_x=24, pad_y=10)

    draw.text((W // 2, 235), "First Open Info Session", font=get_font(44, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 285), "Learn about the project & how to take part", font=get_font(26, bold=False), fill=C_MUTED_TEXT, anchor="mm")

    # Calendar Card
    card_box = [55, 335, W - 55, 1240]
    draw_rounded_card(draw, card_box, radius=28, fill=C_WHITE, outline=C_CARD_BORDER, width=2)

    # Header on card
    draw.rounded_rectangle([55, 335, W - 55, 435], radius=28, fill=C_MAGENTA)
    draw.rectangle([55, 395, W - 55, 435], fill=C_MAGENTA)
    draw.text((W // 2, 385), "ONLINE INFO SESSION", font=get_font(28, bold=True), fill=C_WHITE, anchor="mm")

    draw.text((W // 2, 495), "Wednesday", font=get_font(30, bold=False), fill=C_MUTED_TEXT, anchor="mm")
    draw.text((W // 2, 550), "18 November 2026", font=get_font(46, bold=True), fill=C_DARK, anchor="mm")

    # Time pill
    time_rect = [95, 605, W - 95, 715]
    draw.rounded_rectangle(time_rect, radius=18, fill=(245, 247, 250), outline=(215, 220, 230), width=2)
    draw.text((W // 2, 642), "14:00 – 15:30 CET", font=get_font(32, bold=True), fill=C_MAGENTA, anchor="mm")
    draw.text((W // 2, 682), "13:00 – 14:30 UTC   •   10:00 – 11:30 BRT", font=get_font(23, bold=False), fill=C_MUTED_TEXT, anchor="mm")

    draw.text((W // 2, 755), "Live on Zoom  •  Free & Open for All", font=get_font(26, bold=True), fill=C_HSS_GREEN, anchor="mm")

    draw.line([(100, 795), (W - 100, 795)], fill=(235, 238, 245), width=2)

    draw.text((100, 830), "Session Agenda:", font=get_font(25, bold=True), fill=C_DARK)
    agenda = [
        "• Welcome & Project Introduction (MLRA)",
        "• The Global Innovation Academy Platform Roadmap",
        "• Findings from the Circular Material Valuer Curriculum",
        "• Participatory Working Group & Community Compensation",
        "• Project Timeline, Next Steps & Open Q&A"
    ]
    y_ag = 875
    for itm in agenda:
        draw.text((100, y_ag), itm, font=get_font(23, bold=False), fill=C_MUTED_TEXT)
        y_ag += 40

    draw.line([(100, 1090), (W - 100, 1090)], fill=(235, 238, 245), width=2)
    draw.text((W // 2, 1130), "Hosted by Felipe Schmidt Fonseca & Sandra Mamitzsch (GIG)", font=get_font(22, italic=True), fill=C_MUTED_TEXT, anchor="mm")

    draw_pill(draw, (W // 2, 1195), "SCAN QR OR CLICK BIO TO RSVP  ->", get_font(23, bold=True), fill=C_MAGENTA, text_color=C_WHITE, pad_x=24, pad_y=10)

    draw_footer_bar(draw, "Swipe to register & view partners  ->")
    return img

# -------------------------------------------------------------------------
# CARD 5: CALL TO ACTION & ALL LOGOS
# -------------------------------------------------------------------------
def render_card_5():
    img = Image.new('RGBA', (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header_bar(img, draw, 5)

    draw_pill(draw, (W // 2, 175), "GET INVOLVED NOW", get_font(22, bold=True), fill=C_LIGHT_MAGENTA, text_color=C_MAGENTA, pad_x=24, pad_y=10)

    draw.text((W // 2, 235), "Join the Co-Design!", font=get_font(46, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 285), "Fill out the quick participation form:", font=get_font(25, bold=False), fill=C_MUTED_TEXT, anchor="mm")

    # QR Card
    qr_box = [180, 330, W - 180, 870]
    draw_rounded_card(draw, qr_box, radius=28, fill=C_WHITE, outline=C_MAGENTA, width=3)

    qr_size = 350
    qr_res = qr_code.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    img.alpha_composite(qr_res, ((W - qr_size)//2, 360))

    draw.text((W // 2, 740), "SCAN WITH YOUR CAMERA", font=get_font(26, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 785), "or click the link in bio", font=get_font(24, bold=False), fill=C_MAGENTA, anchor="mm")
    draw.text((W // 2, 830), "cloud.globalinnovationgathering.org", font=get_font(20, italic=True), fill=C_MUTED_TEXT, anchor="mm")

    draw.text((W // 2, 915), "Can't make it to the 18 Nov session?", font=get_font(25, bold=True), fill=C_DARK, anchor="mm")
    draw.text((W // 2, 950), "Fill the form anyway to stay connected for future co-design sprints!", font=get_font(21, bold=False), fill=C_MUTED_TEXT, anchor="mm")

    # Project Partners & Supporters Bar
    footer_rect = [55, 995, W - 55, 1240]
    draw_rounded_card(draw, footer_rect, radius=24, fill=C_WHITE, outline=C_CARD_BORDER, width=2)
    draw.text((W // 2, 1025), "PROJECT PARTNERS & SUPPORTERS", font=get_font(18, bold=True), fill=C_SUBTLE, anchor="mm")

    # Row 1: GIG left, HSS right
    gh = 55
    gw = int(gig_logo.width * (gh / gig_logo.height))
    gl = gig_logo.resize((gw, gh), Image.Resampling.LANCZOS)
    img.alpha_composite(gl, (120, 1055))

    hh = 60
    hw = int(hss_logo.width * (hh / hss_logo.height))
    hl = hss_logo.resize((hw, hh), Image.Resampling.LANCZOS)
    img.alpha_composite(hl, (W - 120 - hw, 1050))

    # Row 2: Reuse City left, Funding Program right
    rh = 55
    rw = int(reuse_logo.width * (rh / reuse_logo.height))
    rl = reuse_logo.resize((rw, rh), Image.Resampling.LANCZOS)
    img.alpha_composite(rl, (120 + (gw - rw)//2, 1125))

    fph = 60
    fpw = int(hss_fp_logo.width * (fph / hss_fp_logo.height))
    fpl = hss_fp_logo.resize((fpw, fph), Image.Resampling.LANCZOS)
    img.alpha_composite(fpl, (W - 120 - hw + (hw - fpw)//2, 1120))

    draw.text((W // 2, 1210), "Global Innovation Academy  •  Inclusive Circularity Series", font=get_font(19, bold=True), fill=C_MUTED_TEXT, anchor="mm")

    draw_footer_bar(draw, "Tap link in bio to participate")
    return img

def main():
    cards = [
        ("card_1_cover.png", render_card_1),
        ("card_2_project.png", render_card_2),
        ("card_3_tracks.png", render_card_3),
        ("card_4_info_session.png", render_card_4),
        ("card_5_rsvp_logos.png", render_card_5)
    ]

    for filename, renderer in cards:
        path = f"{OUT_DIR}/{filename}"
        img = renderer()
        img.save(path, quality=95)
        print(f"Generated: {path}")

if __name__ == '__main__':
    main()
