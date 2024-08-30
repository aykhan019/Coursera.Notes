from notion_client import Client
from notion_exporter import NotionExporter
import os
import re

# Initialize Notion client and exporter using token from environment variables
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
notion = Client(auth=NOTION_TOKEN)

def sanitize_name(name):
    """
    Sanitize file and directory names to be filesystem-friendly.
    
    Parameters:
        name (str): The name to sanitize.
    
    Returns:
        str: The sanitized name.
    """
    return re.sub(r'[<>:"/\\|?*]', ' -', name)

def parse_metadata(content):
    """
    Parse metadata from the content and extract title and body content.
    
    Parameters:
        content (str): The content to parse.
    
    Returns:
        tuple: A tuple containing the title and body content.
    """
    parts = content.split('---')
    if len(parts) < 3:
        return "Untitled", ''  # Handle cases without metadata
    
    metadata = parts[1]
    page_content = parts[2]

    # Extract title from metadata
    match = re.search(r'title:\s*(.+)', metadata)
    title = match.group(1).strip() if match else "Untitled"

    return title, page_content

def get_subpage_ids(id):
    """
    Retrieve IDs of child pages from a given page ID.
    
    Parameters:
        id (str): The page ID.
    
    Returns:
        list: A list of child page IDs.
    """
    try:
        children = notion.blocks.children.list(block_id=id)
        subpage_ids = [child['id'] for child in children['results'] if child['type'] == 'child_page']
        return subpage_ids
    except Exception:
        return []

def build_page_hierarchy(page_ids):
    """
    Build a hierarchy of pages with their child IDs.
    
    Parameters:
        page_ids (list): A list of page IDs.
    
    Returns:
        dict: A dictionary mapping page IDs to lists of child page IDs.
    """
    hierarchy_dict = {}
    for page_id in page_ids:
        child_ids = get_subpage_ids(page_id)
        hierarchy_dict[page_id] = child_ids
    return hierarchy_dict

def save_page_to_file(page_title, page_content, parent_dir):
    """
    Save page content to a Markdown file.
    
    Parameters:
        page_title (str): The title of the page.
        page_content (str): The content of the page.
        parent_dir (str): The directory to save the file in.
    """
    file_name = sanitize_name(f"{page_title}.md")
    file_path = os.path.join(parent_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(page_content)

TOP_PAGE_ID = os.getenv('TOP_PAGE_ID')
exporter = NotionExporter(notion_token=NOTION_TOKEN, export_child_pages=True, extract_page_metadata=True)
exported_data = exporter.export_pages([TOP_PAGE_ID])
hierarchy_dict = build_page_hierarchy(exported_data)

def save_hierarchy_to_folder(page_id, parent_dir):
    """
    Save the page and its child pages to a directory structure.
    
    Parameters:
        page_id (str): The ID of the page to save.
        parent_dir (str): The parent directory to save the page in.
    """
    page_title, page_content = parse_metadata(exported_data.get(page_id, ""))
    os.makedirs(parent_dir, exist_ok=True)
    save_page_to_file(page_title, page_content, parent_dir)

    children_ids = hierarchy_dict.get(page_id, [])
    for child_id in children_ids:
        child_title, child_page_content = parse_metadata(exported_data.get(child_id, ""))
        child_folder = os.path.join(parent_dir, sanitize_name(child_title))
        save_hierarchy_to_folder(child_id, child_folder)

def main():
    root_folder = r'data'
    save_hierarchy_to_folder(TOP_PAGE_ID, root_folder)

if __name__ == "__main__":
    main()
