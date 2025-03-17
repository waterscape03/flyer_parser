# Flyer Parser

A Python tool to scrape and parse brochures from the Prospektmaschine website.

## Overview

This project scrapes brochure information from the Prospektmaschine website, including titles, thumbnails, shop names, and validity dates. The parsed data is saved in a structured JSON format.

## Features

- Fetch brochures from [Prospektmaschine](https://www.prospektmaschine.de/hypermarkte/)
- Extract brochure details (title, thumbnail URL, shop name, validity dates)
- Save data in JSON format

## Requirements

- Python 3.6+
- Required packages:
  - requests>=2.31.0
  - beautifulsoup4>=4.12.2

## Installation

1. Clone this repository: 

```bash
git clone https://github.com/waterscape03/flyer_parser.git
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```
## Usage

Run the scraper with:

```bash
python main.py
```