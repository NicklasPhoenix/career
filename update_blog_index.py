import os
import glob
import re
from datetime import datetime

def extract_article_info(file_path):
    """Extract title, date, and description from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "Article Title"
        
        # Clean up title (remove any HTML tags and extra text)
        title = re.sub(r'<[^>]+>', '', title)
        title = re.sub(r':\s*Complete Guide.*$', '', title)
        title = title.strip()
        
        # Extract meta description
        desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content, re.IGNORECASE)
        description = desc_match.group(1).strip() if desc_match else "Career advice and insights for your professional journey."
        
        # Extract date from filename or meta tag
        filename = os.path.basename(file_path)
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
        if date_match:
            date_str = date_match.group(1)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%B %d, %Y")
        else:
            formatted_date = "January 25, 2025"
        
        # Calculate reading time estimate
        word_count = len(re.findall(r'\w+', content))
        reading_time = max(5, min(20, word_count // 200))  # 200 words per minute
        
        return {
            'title': title,
            'description': description,
            'date': formatted_date,
            'reading_time': reading_time,
            'filename': filename
        }
    except Exception as e:
        print(f"⚠️  Error reading {file_path}: {e}")
        return None

def update_blog_index():
    """Update blog/index.html with current articles"""
    
    # Find all blog articles (exclude index.html)
    blog_files = glob.glob("blog/*.html")
    articles = []
    
    for file_path in blog_files:
        if "index.html" not in file_path:
            article_info = extract_article_info(file_path)
            if article_info:
                articles.append(article_info)
    
    # Sort articles by filename (newest first)
    articles.sort(key=lambda x: x['filename'], reverse=True)
    
    # Split articles into featured (first 3) and latest (rest)
    featured_articles = articles[:3]
    latest_articles = articles[3:]
    
    # Generate blog index HTML
    blog_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - Career Advice and Insights | Career Analyzer</title>
    <meta name="description" content="Discover career change tips, industry insights, and professional development advice. Expert guidance for career transitions and growth.">
    <link rel="stylesheet" href="/career/css/styles.css">
</head>
<body>
    <div class="container">
        <header>
            <nav class="main-nav">
                <a href="/career/">Career Analyzer Tool</a>
                <a href="/career/blog/">Career Advice Blog</a>
                <a href="/career/guides/">Free Career Guides</a>
                <a href="/career/tools/">Career Tools</a>
            </nav>
        </header>
        
        <main>
            <article>
                <h1 class="page-title">Career Advice Blog</h1>
                
                <div class="article-meta">
                    <span>Expert insights and practical tips for career development and transitions</span>
                </div>'''
    
    # Add featured articles section
    if featured_articles:
        blog_html += '''
                
                <section class="content-section">
                    <h2>Featured Articles</h2>
                    <div class="blog-post-list">'''
        
        for article in featured_articles:
            url_path = f"/career/blog/{article['filename']}"
            blog_html += f'''
                        <article class="blog-post">
                            <h3><a href="{url_path}">{article['title']}</a></h3>
                            <div class="article-meta">
                                <time datetime="{datetime.now().strftime('%Y-%m-%d')}">{article['date']}</time>
                                <span>{article['reading_time']} min read</span>
                            </div>
                            <p>{article['description'][:200]}{'...' if len(article['description']) > 200 else ''}</p>
                        </article>'''
        
        blog_html += '''
                    </div>'''
    
    # Add latest articles section
    if latest_articles:
        blog_html += '''
                    
                    <h2>Latest Articles</h2>
                    <div class="blog-post-list">'''
        
        for article in latest_articles:
            url_path = f"/career/blog/{article['filename']}"
            blog_html += f'''
                        <article class="blog-post">
                            <h3><a href="{url_path}">{article['title']}</a></h3>
                            <div class="article-meta">
                                <time datetime="{datetime.now().strftime('%Y-%m-%d')}">{article['date']}</time>
                                <span>{article['reading_time']} min read</span>
                            </div>
                            <p>{article['description'][:200]}{'...' if len(article['description']) > 200 else ''}</p>
                        </article>'''
        
        blog_html += '''
                    </div>'''
    
    # Close main content and add footer
    blog_html += '''
                </section>
            </article>
        </main>
        
        <footer>
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Career Resources</h4>
                    <ul>
                        <li><a href="/career/blog/">Career Change Blog</a></li>
                        <li><a href="/career/guides/">Industry Guides</a></li>
                        <li><a href="/career/tools/">Free Tools</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Popular Articles</h4>
                    <ul>'''
    
    # Add top 3 articles to footer
    for i, article in enumerate(featured_articles[:3]):
        url_path = f"/career/blog/{article['filename']}"
        blog_html += f'''
                        <li><a href="{url_path}">{article['title']}</a></li>'''
    
    blog_html += '''
                    </ul>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>'''
    
    # Write the updated blog index
    os.makedirs("blog", exist_ok=True)
    with open("blog/index.html", "w", encoding="utf-8") as f:
        f.write(blog_html)
    
    print(f"✅ Updated blog/index.html with {len(articles)} articles")
    print(f"📊 Featured: {len(featured_articles)}, Latest: {len(latest_articles)}")
    
    return len(articles)

if __name__ == "__main__":
    article_count = update_blog_index()
    print(f"📝 Total blog articles: {article_count}")