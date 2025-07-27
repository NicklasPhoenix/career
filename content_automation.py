#!/usr/bin/env python3
"""
Content Automation Script
Generates new blog posts, updates blog index, and updates sitemap
"""

import os
import sys
from datetime import datetime
from generate_content import create_blog_post
from update_blog_index import update_blog_index
from update_sitemap import update_sitemap

def main():
    """Main automation function"""
    print("🚀 Starting content automation...")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Step 1: Generate new blog post
        print("\n📝 Step 1: Generating new blog post...")
        post_info = create_blog_post()
        print(f"✅ Created: {post_info['title']}")
        
        # Step 2: Update blog index
        print("\n📋 Step 2: Updating blog index...")
        article_count = update_blog_index()
        print(f"✅ Blog index updated with {article_count} articles")
        
        # Step 3: Update sitemap
        print("\n🗺️  Step 3: Updating sitemap...")
        url_count = update_sitemap()
        print(f"✅ Sitemap updated with {url_count} URLs")
        
        # Step 4: Summary
        print(f"\n🎉 Content automation completed successfully!")
        print(f"📊 Summary:")
        print(f"   • New article: {post_info['filename']}")
        print(f"   • Topic: {post_info['topic']}")
        print(f"   • Total articles: {article_count}")
        print(f"   • Total sitemap URLs: {url_count}")
        
        return {
            'success': True,
            'new_post': post_info,
            'total_articles': article_count,
            'total_urls': url_count
        }
        
    except Exception as e:
        print(f"❌ Error during content automation: {e}")
        return {
            'success': False,
            'error': str(e)
        }

if __name__ == "__main__":
    result = main()
    
    # Exit with appropriate code
    sys.exit(0 if result['success'] else 1)