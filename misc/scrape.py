import os
import requests
from bs4 import BeautifulSoup

# Define the base directory for downloads
BASE_DIR = "Downloaded_PDFs"

# Flag to control dry run vs actual download
DRY_RUN = False  # Set to False to download actual PDFs

# Ensure the base directory exists
os.makedirs(BASE_DIR, exist_ok=True)

def process_file(url, save_path):
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        if DRY_RUN:
            # Create dummy file
            with open(save_path, 'wb') as f:
                f.write(b'%PDF-1.4\n%dummy pdf file\n')
            print(f"Created dummy file at: {save_path}")
        else:
            # Download the actual PDF file
            response = requests.get(url)
            response.raise_for_status()
            
            # Save the PDF file
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {save_path}")
            
    except Exception as e:
        print(f"Failed to {'create dummy file' if DRY_RUN else 'download'} at {save_path}: {e}")

def process_mpt_section(mpt_title, grid_container):
    # Process each class card in this MPT section
    for class_card in grid_container.find_all('div', class_=['acecard', 'acecard_special']):
        # Get class name
        class_heading = class_card.find('h2')
        if not class_heading:
            continue
        class_name = class_heading.text.strip()

        # Process each link in the card
        for link in class_card.find_all('a'):
            url = link['href']
            category = link['class'][-1].replace('-', '_').title()
            
            # Extract filename from URL
            filename = url.split('/')[-1]
            
            # Create directory structure
            file_dir = os.path.join(BASE_DIR, mpt_title, class_name, category)
            file_path = os.path.join(file_dir, filename)
            
            # Process the file (dummy or actual download)
            process_file(url, file_path)
            print(f"Processing: {mpt_title} -> {class_name} -> {category} -> {filename}")

def process_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all MPT sections
    mpt_titles = soup.find_all('h1', class_='text-center')
    
    for mpt_title in mpt_titles:
        current_mpt = mpt_title.text.strip()
        
        # Find the next grid-container after this title
        grid_container = mpt_title.find_next('div', class_='grid-container')
        
        if grid_container:
            process_mpt_section(current_mpt, grid_container)
        else:
            print(f"Warning: No grid container found for {current_mpt}")

# Read the HTML file
with open('input.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Print mode information
print(f"Running in {'DRY RUN' if DRY_RUN else 'DOWNLOAD'} mode")

# Process the HTML
process_html(html_content)
