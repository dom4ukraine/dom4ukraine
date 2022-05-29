#!/usr/bin/python
import praw
import pdb
import re
import os

#                                 this is my test comment replier that tracks comments

# Create the Reddit instance
reddit = praw.Reddit('bot4ukraine')


# Have we run this code before? If not, create an empty list
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# If we have run the code before, load the list of comment we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))


subreddit = reddit.subreddit('dom4ukraine')
for comment in subreddit.comments():
    print(comment.body)

    # If we haven't replied to this comment before
    if comment.id not in comments_replied_to:

        # Do a case insensitive search
        if re.search("slava ukrayini", comment.body, re.IGNORECASE):
            # Reply to the comment
            comment.reply("heroyam slava")
            print("bot4ukraine replying to : ", comment.body)

            # Store the current id into our list
            comments_replied_to.append(comment.id)

# Write our updated list back to the file
with open("comments_replied_to.txt", "w") as f:
    for post_id in comments_replied_to:
        f.write(post_id + "\n")
