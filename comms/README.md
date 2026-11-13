# Communications & Outreach Assets

This directory contains social media campaigns, visual assets, and recruitment copy for the **Material Literacy & Resource Assessment (MLRA)** project.

---

## 📸 Instagram Carousel Card Set (4:5 Portrait)

A 5-card carousel optimized for Instagram feed posts (1080 × 1350 px, 4:5 portrait ratio) inviting makers, repairers, and educators to join the participatory co-design working group and attend the upcoming Info Session.

The generated cards are stored in [`instagram-cards/`](instagram-cards/):

| Card | File | Description |
| :--- | :--- | :--- |
| **01** | [`card_1_cover.png`](instagram-cards/card_1_cover.png) | **Cover:** High-impact callout to makers, repairers & educators featuring circular knolling photography. |
| **02** | [`card_2_project.png`](instagram-cards/card_2_project.png) | **Project:** Introduction to MLRA and the permanent community-owned MOOC on the Global Innovation Academy (GIA), supported by Hans Sauer Stiftung. |
| **03** | [`card_3_tracks.png`](instagram-cards/card_3_tracks.png) | **Co-Design Tracks:** (1) Material Identification, (2) Condition & Repair Triage, (3) Open Commons (OER). |
| **04** | [`card_4_info_session.png`](instagram-cards/card_4_info_session.png) | **Info Session:** Date (**18 Nov 2026**), multi-timezone pill (14:00 CET / 13:00 UTC / 10:00 BRT), Zoom meeting details, and agenda. |
| **05** | [`card_5_rsvp_logos.png`](instagram-cards/card_5_rsvp_logos.png) | **Call to Action & Logos:** High-resolution Dino QR code linking to the participation form, plus full partner/funder logo bar (GIG, Hans Sauer Stiftung, Reuse City, GIA). |

### 📝 Ready-to-Post Caption
* **Post Copy & Hashtags:** [`instagram_post_caption.md`](instagram_post_caption.md)

### 🎨 How to Regenerate the Cards
The cards are generated programmatically using Python and Pillow to ensure pixel-perfect brand alignment:

```bash
# Requires Pillow and Liberation Sans fonts
python3 comms/generate_carousel_cards.py
```

---

## 📂 Directory Contents

* **[`assets/`](assets/):** Source vector logos, brand marks, and high-resolution photography:
  * GIG logo (`gig_logo.png`)
  * Hans Sauer Stiftung logo (`hss_logo_de.png`, `hss_logo_en.png`)
  * HSS Förderprogramm 2026–2027 badge (`hss_foerderprogramm.png`)
  * Reuse City logo (`reuse_city_logo.png`)
  * Camera knolling teardown photo (`camera_knolling.png`)
  * Maker workshop photo (`maker_workshop.png`)
  * GIG cloud participation form QR code (`qr_code.png`)
* **[`external-recruitment/`](external-recruitment/):** Working group participant recruitment outreach copy.
* **[`generate_carousel_cards.py`](generate_carousel_cards.py):** Standalone Python generator script.
* **[`instagram-cards/`](instagram-cards/):** Rendered 1080×1350 PNG cards ready for upload.
