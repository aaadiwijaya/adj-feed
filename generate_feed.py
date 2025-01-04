from feedgen.feed import FeedGenerator
import os

# Create the feed generator
fg = FeedGenerator()
fg.id('https://<username>.github.io/my-feed')
fg.title('My GitHub Feed')
fg.author({'name': 'Your Name', 'email': 'your-email@example.com'})
fg.link(href='https://<username>.github.io/my-feed', rel='self')
fg.language('en')

# Add feed entries (replace this with your actual feed content)
entry = fg.add_entry()
entry.id('https://<username>.github.io/my-feed/posts/post1')
entry.title('First Post')
entry.link(href='https://<username>.github.io/my-feed/posts/post1')
entry.description('This is the description of the first post')

# Write the feed to an XML file
fg.rss_file('feed.xml')

# Move the feed.xml to the docs/ directory if using GitHub Pages with docs/ folder
if not os.path.exists('docs'):
    os.makedirs('docs')
os.rename('feed.xml', 'docs/feed.xml')
