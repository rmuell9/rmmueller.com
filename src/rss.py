import os
import datetime
import conversion
from xml.etree.ElementTree import Element, SubElement, tostring

def generate_rss_feed(content_dir, dest_path, site_url, site_title, 
                     site_description):
    
    # Create RSS root
    rss_root = Element("rss", version="2.0")
    channel = SubElement(rss_root, "channel")
    
    # Channel info
    SubElement(channel, "title").text = site_title
    SubElement(channel, "link").text = site_url
    SubElement(channel, "description").text = site_description
    SubElement(channel, "language").text = "en-us"
    
    # Collect all markdown files with metadata
    posts = []
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    
                    title = conversion.extract_title(content)
                    # Get file modification time as pub date
                    mtime = os.path.getmtime(file_path)
                    pub_date = datetime.datetime.fromtimestamp(mtime)
                    
                    # Create URL from file path
                    rel_path = os.path.relpath(file_path, content_dir)
                    url_path = rel_path[:-3] + '.html'  # .md -> .html
                    url = f"{site_url}/{url_path}".replace('\\', '/')
                    
                    posts.append({
                        'title': title,
                        'url': url,
                        'pub_date': pub_date,
                        'content': content
                    })
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    # Sort by publication date (newest first)
    posts.sort(key=lambda x: x['pub_date'], reverse=True)
    
    # Add items to RSS
    for post in posts[:20]:  # Limit to 20 most recent
        item = SubElement(channel, "item")
        SubElement(item, "title").text = post['title']
        SubElement(item, "link").text = post['url']
        SubElement(item, "pubDate").text = post['pub_date'].strftime(
            '%a, %d %b %Y %H:%M:%S GMT')
        
        # Extract first paragraph as description
        lines = post['content'].split('\n')
        description = ""
        for line in lines[1:]:  # Skip title line
            line = line.strip()
            if line and not line.startswith('#'):
                description = line[:200] + "..." if len(line) > 200 else line
                break
        
        SubElement(item, "description").text = description or post['title']
        SubElement(item, "guid").text = post['url']
    
    # Write RSS file
    rss_string = tostring(rss_root, encoding='unicode')
    with open(dest_path, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(rss_string)
