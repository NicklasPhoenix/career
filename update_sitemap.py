import os
from datetime import datetime
import glob

def update_sitemap():
    """Update sitemap.xml with all current pages"""
    
    base_url = "https://nicklasphoenix.github.io/career"
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Start sitemap XML
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'''
    
    # Define main pages with their priorities
    main_pages = [
        {"url": "/", "priority": "1.0", "changefreq": "weekly"},
        {"url": "/blog/", "priority": "0.9", "changefreq": "daily"},
        {"url": "/guides/", "priority": "0.8", "changefreq": "weekly"}, 
        {"url": "/tools/", "priority": "0.8", "changefreq": "monthly"}
    ]
    
    # Add main pages
    for page in main_pages:
        sitemap_content += f'''
  <url>
    <loc>{base_url}{page["url"]}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>{page["changefreq"]}</changefreq>
    <priority>{page["priority"]}</priority>
  </url>'''
    
    # Find all HTML files in subdirectories
    html_files = []
    
    # Blog articles
    blog_files = glob.glob("blog/*.html")
    for file in blog_files:
        if "index.html" not in file:
            html_files.append({
                "path": file,
                "priority": "0.7",
                "changefreq": "monthly"
            })
    
    # Guide pages
    guide_files = glob.glob("guides/*.html")
    for file in guide_files:
        if "index.html" not in file:
            html_files.append({
                "path": file,
                "priority": "0.7",
                "changefreq": "monthly"
            })
    
    # Tool pages
    tool_files = glob.glob("tools/*.html")
    for file in tool_files:
        if "index.html" not in file:
            html_files.append({
                "path": file,
                "priority": "0.6",
                "changefreq": "monthly"
            })
    
    # Sort files by modification time (newest first)
    html_files.sort(key=lambda x: os.path.getmtime(x["path"]), reverse=True)
    
    # Add individual pages to sitemap
    for file_info in html_files:
        file_path = file_info["path"]
        url_path = "/" + file_path.replace("\\", "/")
        
        # Get file modification date
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        mod_date = mod_time.strftime("%Y-%m-%d")
        
        sitemap_content += f'''
  <url>
    <loc>{base_url}{url_path}</loc>
    <lastmod>{mod_date}</lastmod>
    <changefreq>{file_info["changefreq"]}</changefreq>
    <priority>{file_info["priority"]}</priority>
  </url>'''
    
    # Close sitemap XML
    sitemap_content += '''
</urlset>'''
    
    # Write sitemap file
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    
    print(f"✅ Updated sitemap.xml with {len(html_files) + len(main_pages)} URLs")
    print(f"📅 Last modified: {current_date}")
    
    return len(html_files) + len(main_pages)

if __name__ == "__main__":
    url_count = update_sitemap()
    print(f"🔗 Total URLs in sitemap: {url_count}")