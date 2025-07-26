"""
Connects with ConvertKit, Mailchimp, or SendGrid
Automatically sends email sequences to captured leads
"""

EMAIL_SEQUENCE = [
    {
        'day': 0,
        'subject': 'Your Career Analysis Results',
        'template': 'welcome_email.html'
    },
    {
        'day': 3,
        'subject': '5 Mistakes People Make When Changing Careers',
        'template': 'mistakes_email.html'
    },
    {
        'day': 7,
        'subject': 'Limited Time: Full Career Roadmap 50% Off',
        'template': 'sale_email.html'
    }
]