import os
import json
import random
from datetime import datetime
import re

# Career-related topics that get traffic
TOPICS = [
    "career change at {age}",
    "highest paying {industry} jobs {year}",
    "how to become a {job_title} with no experience",
    "remote {job_type} jobs that pay well",
    "{skill} jobs for beginners",
    "career transition from {old_job} to {new_job}",
    "best certifications for {career}",
    "day in the life of a {job_title}",
    "{city} tech job market {year}",
    "skills needed for {job_title} in {year}",
    "salary guide for {job_title} in {year}",
    "work life balance in {industry}",
    "entry level {industry} jobs",
    "freelance {job_type} opportunities",
    "women in {industry} careers"
]

VARIABLES = {
    "age": ["25", "30", "35", "40", "45", "50"],
    "industry": ["tech", "healthcare", "finance", "marketing", "sales", "education", "consulting"],
    "year": ["2025", "2026"],
    "job_title": ["data analyst", "UX designer", "project manager", "software developer", "marketing coordinator", "financial advisor", "nurse practitioner"],
    "job_type": ["coding", "design", "management", "analyst", "writing", "consulting"],
    "skill": ["Python", "Excel", "SQL", "JavaScript", "Figma", "Tableau", "PowerBI"],
    "old_job": ["teacher", "accountant", "retail manager", "nurse", "customer service", "sales associate"],
    "new_job": ["programmer", "data analyst", "UX designer", "product manager", "digital marketer"],
    "career": ["IT", "data science", "cybersecurity", "cloud computing", "digital marketing", "project management"],
    "city": ["Austin", "Seattle", "Denver", "Miami", "Chicago", "Boston", "San Diego"]
}

def generate_topic():
    template = random.choice(TOPICS)
    for var, values in VARIABLES.items():
        if f"{{{var}}}" in template:
            template = template.replace(f"{{{var}}}", random.choice(values))
    return template

def create_slug(topic):
    """Create URL-friendly slug from topic"""
    slug = topic.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')

def generate_article_content(topic):
    """Generate realistic article content based on topic"""
    
    # Extract key elements from topic
    words = topic.split()
    main_keyword = topic
    
    # Generate realistic content sections
    sections = []
    
    if "career change" in topic:
        sections = [
            "Why Consider This Career Change",
            "Skills You Need to Develop", 
            "Step-by-Step Transition Plan",
            "Salary Expectations and Growth",
            "Common Challenges and Solutions"
        ]
    elif "remote" in topic:
        sections = [
            "Top Remote Job Opportunities",
            "Skills Required for Remote Work",
            "How to Find Remote Positions",
            "Remote Work Best Practices",
            "Salary and Benefits Overview"
        ]
    elif "highest paying" in topic:
        sections = [
            "Industry Salary Overview",
            "Top-Paying Positions",
            "Required Qualifications",
            "Career Progression Paths",
            "How to Negotiate Your Salary"
        ]
    else:
        sections = [
            "Getting Started in This Field",
            "Essential Skills and Qualifications",
            "Job Market Analysis",
            "Career Development Tips",
            "Future Outlook and Trends"
        ]
    
    # Generate FAQ questions
    faq_questions = [
        f"What qualifications do I need for {topic}?",
        f"How long does it take to transition to {topic}?",
        f"What is the average salary for {topic}?"
    ]
    
    return sections, faq_questions

def create_full_html_article(topic, sections, faq_questions):
    """Create complete HTML article"""
    
    title = topic.title()
    slug = create_slug(topic)
    date = datetime.now().strftime("%Y-%m-%d")
    
    # Calculate reading time (rough estimate)
    reading_time = random.randint(8, 15)
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Essential SEO Meta Tags -->
    <title>{title}: Complete Guide | Career Analyzer</title>
    <meta name="description" content="Discover everything you need to know about {topic}. Complete guide with actionable steps, salary information, and career transition tips.">
    <meta name="keywords" content="{topic}, career guide, {', '.join(topic.split()[:3])}">
    <link rel="canonical" href="https://nicklasphoenix.github.io/career/blog/{date}-{slug}.html">
    
    <!-- Open Graph for Social Sharing -->
    <meta property="og:title" content="{title}: Complete Guide">
    <meta property="og:description" content="Discover everything you need to know about {topic}. Complete guide with actionable steps and career transition tips.">
    <meta property="og:image" content="https://yourusername.github.io/images/{slug}.jpg">
    <meta property="og:url" content="https://nicklasphoenix.github.io/career/blog/{date}-{slug}.html">
    
    <!-- Schema Markup for Rich Snippets -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}: Complete Guide",
      "datePublished": "{date}",
      "dateModified": "{date}",
      "author": {{
        "@type": "Person",
        "name": "Career Expert",
        "url": "https://nicklasphoenix.github.io/career/about"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Career Analyzer",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://nicklasphoenix.github.io/career/logo.png"
        }}
      }},
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "https://nicklasphoenix.github.io/career/blog/{date}-{slug}.html"
      }}
    }}
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="/career/favicon.svg">
    
    <link rel="stylesheet" href="/career/css/styles.css">
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYK51P2BNR"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());

        gtag('config', 'G-MYK51P2BNR');
    </script>
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
                <!-- H1 with Primary Keyword -->
                <h1>{title}: Complete Guide</h1>
                
                <!-- Author and Date -->
                <div class="article-meta">
                    <span>By Career Expert</span>
                    <time datetime="{date}">{datetime.now().strftime("%B %d, %Y")}</time>
                    <span>{reading_time} min read</span>
                </div>
                
                <!-- Table of Contents -->
                <nav class="toc">
                    <h2>What You'll Learn:</h2>
                    <ul>'''

    # Add TOC links
    for i, section in enumerate(sections):
        section_id = create_slug(section)
        html_content += f'\n                        <li><a href="#{section_id}">{section}</a></li>'

    html_content += '''
                    </ul>
                </nav>
                
                <!-- Introduction -->
                <section id="intro">
                    <p>The field of ''' + topic + ''' has seen tremendous growth in recent years. Whether you're considering a career change or just starting your professional journey, understanding the landscape of ''' + topic + ''' is crucial for making informed decisions about your future.</p>
                    
                    <p>In this comprehensive guide, we'll explore everything you need to know about ''' + topic + ''', including the skills required, salary expectations, and step-by-step guidance for getting started in this field.</p>
                    
                    <!-- Early CTA -->
                    <div class="cta-box">
                        <h3>Not Sure Which Career Path Is Right for You?</h3>
                        <p>Take our free career analyzer to discover careers that match your skills and interests</p>
                        <a href="/career/" class="cta-button">Start Free Career Analysis →</a>
                    </div>
                </section>'''

    # Add main content sections
    for i, section in enumerate(sections):
        section_id = create_slug(section)
        html_content += f'''
                
                <!-- {section} -->
                <section id="{section_id}">
                    <h2>{section}</h2>
                    <p>When it comes to {topic}, {section.lower()} is a critical aspect that can determine your success in this field. Let's explore the key considerations and actionable steps you can take.</p>
                    
                    <p>Industry experts recommend focusing on these essential elements:</p>
                    <ul>
                        <li>Developing relevant skills that employers value most</li>
                        <li>Understanding market demands and salary expectations</li>
                        <li>Building a strong professional network in the field</li>
                        <li>Creating a strategic career development plan</li>
                    </ul>
                    
                    <p>By focusing on these areas, you'll be well-positioned to succeed in {topic} and build a rewarding career that aligns with your goals and interests.</p>
                </section>'''

    # Add FAQ section
    html_content += '''
                
                <!-- FAQ Section -->
                <section class="faq" itemscope itemtype="https://schema.org/FAQPage">
                    <h2>Frequently Asked Questions</h2>'''

    for i, question in enumerate(faq_questions):
        answer_id = f"answer-{i+1}"
        html_content += f'''
                    
                    <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                        <h3 itemprop="name">{question}</h3>
                        <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                            <p itemprop="text">The requirements and timeline for {topic} can vary depending on your background and goals. Generally, most professionals find success by focusing on skill development, networking, and gaining relevant experience in the field.</p>
                        </div>
                    </div>'''

    html_content += '''
                </section>
                
                <!-- Final CTA -->
                <section class="final-cta">
                    <h2>Ready to Explore Your Career Options?</h2>
                    <p>Get personalized career recommendations based on your unique skills and interests.</p>
                    <a href="/career/" class="cta-button">Take the Free Career Assessment</a>
                </section>
            </article>
            
            <!-- Sidebar -->
            <aside>
                <!-- Related Articles -->
                <section class="related">
                    <h3>Related Articles</h3>
                    <ul>
                        <li><a href="/career/blog/career-change-at-30.html">Career Change at 30: Complete Guide</a></li>
                        <li><a href="/career/blog/tech-career-transition-guide.html">Tech Career Transition Guide</a></li>
                        <li><a href="/career/blog/highest-paying-remote-careers.html">Highest Paying Remote Careers</a></li>
                    </ul>
                </section>
                
                <!-- Tool Promotion -->
                <section class="tool-promo">
                    <h3>Free Career Tools</h3>
                    <p>Explore our free tools to help plan your career transition</p>
                    <a href="/career/tools/" class="sidebar-cta">Browse Tools</a>
                </section>
            </aside>
        </main>
        
        <!-- Footer -->
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
                    <ul>
                        <li><a href="/career/blog/career-change-at-30.html">Career Change at 30</a></li>
                        <li><a href="/career/blog/tech-career-transition-guide.html">Tech Career Transition</a></li>
                        <li><a href="/career/blog/best-remote-jobs-2025.html">Best Remote Jobs 2025</a></li>
                    </ul>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>'''

    return html_content

def create_blog_post():
    """Generate and save a new blog post"""
    topic = generate_topic()
    sections, faq_questions = generate_article_content(topic)
    
    slug = create_slug(topic)
    date = datetime.now().strftime("%Y-%m-%d")
    
    # Create filename
    filename = f"blog/{date}-{slug}.html"
    
    # Generate full HTML content
    html_content = create_full_html_article(topic, sections, faq_questions)
    
    # Save the article
    os.makedirs("blog", exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Created new blog post: {filename}")
    print(f"📝 Topic: {topic.title()}")
    
    return {
        'filename': filename,
        'topic': topic,
        'title': topic.title(),
        'date': date,
        'slug': slug
    }

if __name__ == "__main__":
    result = create_blog_post()
    print(f"📁 Generated: {result['filename']}")