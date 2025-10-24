# 🌱 Seed Card Generator

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Generate **print-ready seed cards** from a CSV file of seed information. Each card includes icons, seed details, and optional notes, exported into a Word document with multiple cards per page.

---

## Features

- Print-ready **3 × 4.5 cm** seed cards at **300 DPI**.  
- Supports icons for **Position, Sow, Germination, Spacing, Height, Water, and Note**.  
- Automatically wraps text to fit the card.  
- Dynamic title sizing for long seed names.  
- Export 25 cards per page into a Word document.  
- Borders are fully visible on all sides.  

---

## Requirements

- Python 3.8+  
- Install dependencies:

```bash
pip install pillow python-docx

seeds.csv file with required columns.
icons/ folder containing the necessary icons.

Usage

Ensure seeds.csv and the icons/ folder are in the project directory.
Run the script with a seed name:

```bash
python seed_card_generator.py "Bottle Gourd"

If no seed name is provided, it defaults to "Bottle Gourd".
Output Word document:
BOTTLE_GOURD_cards.docx

File Structure

seed-card-generator/
│
├── seed_card_generator.py      # Main script
├── seeds.csv                   # CSV data file
├── icons/                      # Folder containing icons
└── README.md                   # Project documentation

Notes
Page margins in the Word document are 0.5 cm for 25 cards per page.
Missing icons will not stop card generation.
Adjust font size or line height in seed_card_generator.py if text overlaps.
Ensure CSV values are properly formatted to avoid overlapping text.

License
MIT License. You can freely modify, use, and distribute this project.


