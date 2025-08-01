# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a career guidance website built as a static HTML site designed for GitHub Pages deployment. The main feature is a career path analyzer tool that helps users discover careers matching their skills, interests, and salary goals. The project includes content generation automation and social media posting capabilities.

## Common Development Commands

### Deployment
```bash
# Deploy to GitHub Pages (automatic on push to main)
git add .
git commit -m "Update career site content"
git push origin main

# Site will be available at: https://[username].github.io/career/
```

### Content Generation (Python Automation)
```bash
# Full content automation workflow (generates post, updates index, updates sitemap)
python content_automation.py

# Individual commands
python generate_content.py          # Generate new blog content
python update_blog_index.py         # Update blog/index.html with new articles
python update_sitemap.py            # Refresh sitemap.xml with all pages

# Social media automation (requires API credentials)
python twitter_autoposter.py        # Post to Twitter/X
python email_automation.py          # Send automated emails

# Note: Reddit and Quora automation are disabled (.DISABLED files)
```

### Development Server
```bash
# Serve locally for testing (Python)
python -m http.server 8000
# Then visit: http://localhost:8000

# Alternative with Node.js
npx serve .
```

## Project Architecture

### Core Website Structure
- **`index.html`**: Main career analyzer tool with interactive quiz
- **`css/styles.css`**: Unified CSS framework with modern design system
- **`blog/`**: SEO-optimized career advice articles
- **`guides/`**: Detailed career transition guides  
- **`tools/`**: Additional career tools (resume scorer, salary calculator, etc.)
- **`templates/`**: Reusable HTML templates

### Content Management
- **`project.md`**: Comprehensive SEO and monetization strategy guide
- **`socialautomation.md`**: Complete automation setup instructions
- **`sitemap.xml`**: Search engine sitemap
- **`robots.txt`**: SEO crawler directives

### Automation Scripts
- **`content_automation.py`**: Master automation script (generates content + updates indexes)
- **`generate_content.py`**: AI-powered blog post generation
- **`update_blog_index.py`**: Maintains blog/index.html with latest articles
- **`update_sitemap.py`**: Automatically updates sitemap.xml with all site pages
- **`twitter_autoposter.py`**: Twitter/X automation for content promotion
- **`email_automation.py`**: Email sequence automation
- **`reddit_autoposter.py.DISABLED`**: Reddit posting (disabled)
- **`quora_responder.py.DISABLED`**: Quora automation (disabled)

## Key Design Patterns

### Career Matching Algorithm
The main tool uses a weighted scoring system:
- Skills matching: 40% weight
- Interest alignment: 30% weight  
- Salary compatibility: 20% weight
- Work environment fit: 10% weight

Career data is stored in a JavaScript object with properties for skills, interests, salary ranges, growth projections, and transition timelines.

### Monetization Strategy
- Free: Top 3 career matches shown
- Premium ($9.99): Full 10+ matches with detailed roadmaps
- Uses A/B testing for price optimization
- Payment integration ready for Stripe/PayPal/Gumroad

### SEO Architecture
- Semantic HTML structure with proper heading hierarchy
- Schema.org markup for rich snippets
- Open Graph tags for social sharing
- Canonical URLs with `/career/` prefix for GitHub Pages
- Internal linking strategy between blog, guides, and tools

### CSS Architecture Pattern
**CRITICAL**: All subpages (blog, guides, tools) must use the container wrapper:
```html
<body>
    <div class="container">
        <!-- All page content goes here -->
    </div>
</body>
```
The `.container` class provides essential centering and padding:
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
}
```

## Content Generation Strategy

### Automated Topics
The content generator creates articles around high-traffic keywords:
- "career change at [age]"
- "highest paying [industry] jobs [year]"
- "how to become a [job_title] with no experience"
- "remote [job_type] jobs that pay well"

### SEO Requirements
- 1500+ word articles with H2 structure
- FAQ sections targeting featured snippets
- Internal CTAs to the main career tool
- Meta descriptions under 160 characters

## Social Media Automation

### Reddit Strategy
- Target subreddits: r/careerguidance, r/careeradvice, r/findapath
- Post templates that provide value before mentioning the tool
- Rate limiting and human-like behavior patterns
- Automatic follow-up comments

### Twitter/X Posting
- Variety of tweet templates with career statistics
- Hashtag rotation for different career topics
- Scheduled posting during peak engagement times

## Deployment Configuration

### Vercel Deployment (Current)
All paths configured for root domain deployment:
- CSS: `/css/styles.css`
- Favicon: `/favicon.svg`, `/favicon.ico`
- Internal links: `/`, `/blog/`, `/guides/`, `/tools/`
- Static assets served from root

### GitHub Pages (Alternative)
For GitHub Pages deployment, paths need `/career/` prefix:
- CSS: `/career/css/styles.css`
- Internal links: `/career/`, `/career/blog/`, etc.
- Use find/replace to switch deployment targets

### Deployment Notes
- Static site - no build process required
- Pure HTML/CSS/JS architecture
- Automatic deployment on push to main (Vercel)

## Analytics and Tracking

### Google Analytics Events
- Quiz completion tracking
- Conversion tracking for premium upgrades
- Social sharing events
- Page view and engagement metrics

### A/B Testing
- Dynamic price testing ($9.99, $14.99, $19.99)
- CTA button text variations
- Feature list optimization

## API Integrations Required

### Content Generation
- OpenAI API for article generation
- Alternative: Claude API, Groq, or other LLM services

### Social Media
- Reddit API (PRAW library)
- Twitter API v2
- Quora (Selenium automation)

### Email Marketing
- ConvertKit, Mailchimp, or SendGrid integration
- Automated email sequences for lead nurturing

### Payment Processing
- Stripe Payment Links
- PayPal.Me integration
- Gumroad for simple setup
- Buy Me a Coffee for quick start

## Security and Rate Limiting

### API Credentials
Store sensitive keys in GitHub Secrets:
- `OPENAI_API_KEY`
- `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET`
- `TWITTER_API_KEY` / `TWITTER_API_SECRET`
- Email service API keys

### Rate Limiting
- Reddit: Max 1 post per subreddit per week
- Twitter: Respect API rate limits
- Content generation: Batch processing to avoid API limits

## Performance Considerations

### Static Site Optimization
- CSS variables for consistent theming
- Minimal JavaScript dependencies
- Optimized images and assets
- Fast loading animations and transitions

### Career Database
- Client-side career matching for instant results
- No external API calls for core functionality
- Expandable career data structure

## Scaling Strategy

### Traffic Growth
- Month 1: 1,000+ visitors from organic content
- Month 3: 10,000+ visitors with consistent posting
- Month 6: 50,000+ visitors with SEO momentum

### Revenue Projections
- Month 1: $50-100 (building traffic)
- Month 3: $500-1,500 (compound growth)
- Month 6: $2,000+ (established authority)

## Development Workflow

### Content Updates
1. Create new HTML files in appropriate directories
2. Update internal navigation links
3. Add to sitemap.xml
4. Deploy via git push

### Tool Enhancements
1. Modify career database in index.html
2. Update matching algorithm if needed
3. Test locally before deployment
4. Monitor analytics for usage patterns

### Automation Setup
1. Configure GitHub Secrets for API keys
2. Enable GitHub Actions workflows
3. Test automation scripts locally first
4. Monitor posting frequency to avoid rate limits