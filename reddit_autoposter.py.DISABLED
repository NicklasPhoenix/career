import praw
import random
import os
import time

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_CLIENT_SECRET'],
    username=os.environ['REDDIT_USERNAME'],
    password=os.environ['REDDIT_PASSWORD'],
    user_agent='CareerToolBot/1.0'
)

# Subreddits to post in
SUBREDDITS = [
    'careerguidance',
    'careeradvice',
    'findapath',
    'ITCareerQuestions',
    'cscareerquestions',
    'jobs',
    'GetEmployed'
]

# Post templates that don't look spammy
POST_TEMPLATES = [
    {
        'title': "Made a free tool to help figure out career transitions - would love feedback",
        'text': "Hey everyone, I've been working on a career analyzer tool that matches your skills with potential careers. It's completely free and gives you 3 detailed matches.\n\nI built it because I went through a career change myself and wished something like this existed.\n\nWould love any feedback on how to improve it: [link]\n\nHope it helps someone!"
    },
    {
        'title': "Free career matching tool I built (no ads, no signup)",
        'text': "Hi all, I created a simple tool that analyzes your skills and suggests matching careers with salary info and transition steps.\n\nNo email required, no ads, just trying to help people who are stuck like I was.\n\nCheck it out if you're considering a career change: [link]"
    },
    {
        'title': "Built something to help with career changes - thoughts?",
        'text': "After helping a few friends figure out career transitions, I turned my process into a free online tool.\n\nIt asks about your skills/interests and shows careers that match, with real salary data and how to transition.\n\nWould appreciate any feedback: [link]"
    }
]

def post_to_reddit():
    # Choose random subreddit and template
    subreddit_name = random.choice(SUBREDDITS)
    template = random.choice(POST_TEMPLATES)
    
    # Replace [link] with your actual URL
    url = "https://nicklasphoenix.github.io/career"
    title = template['title']
    text = template['text'].replace('[link]', url)
    
    try:
        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title=title, selftext=text)
        print(f"Posted to r/{subreddit_name}: {submission.url}")
        
        # Wait a bit to seem human
        time.sleep(random.randint(60, 300))
        
        # Add a helpful comment to your own post
        helpful_comments = [
            "Feel free to ask if you have any questions about the tool or career transitions in general!",
            "Happy to help if anyone needs advice on their specific situation.",
            "Let me know if you'd like me to add any specific careers to the analyzer!"
        ]
        submission.reply(random.choice(helpful_comments))
        
    except Exception as e:
        print(f"Error posting to {subreddit_name}: {e}")

if __name__ == "__main__":
    post_to_reddit()