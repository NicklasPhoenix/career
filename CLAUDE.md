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
# Generate new blog content
python generate_content.py

# Post to Reddit (requires API credentials)
python reddit_autoposter.py

# Post to Twitter/X (requires API credentials)
python twitter_autoposter.py

# Send automated emails (requires email service setup)
python email_automation.py
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
- **`generate_content.py`**: AI-powered blog post generation
- **`reddit_autoposter.py`**: Automated Reddit posting with rate limiting
- **`twitter_autoposter.py`**: Twitter/X automation for content promotion
- **`quora_responder.py`**: Quora answer automation (Selenium-based)
- **`email_automation.py`**: Email sequence automation

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

## GitHub Pages Configuration

### URL Structure
All internal links use `/career/` prefix for proper GitHub Pages routing:
- Main tool: `/career/`
- Blog: `/career/blog/`
- Guides: `/career/guides/`
- Tools: `/career/tools/`

### Deployment Notes
- Static site automatically deploys on push to main branch
- CSS and JS paths use relative links with `/career/` prefix
- No build process required - pure HTML/CSS/JS

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