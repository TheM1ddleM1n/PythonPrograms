import os
from anthropic import Anthropic
from github import Github

def get_claude_response(message):
    """Get response from Claude"""
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": message
        }]
    )
    
    return response.content[0].text

def main():
    # Initialize GitHub client
    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
    issue_number = int(os.environ["ISSUE_NUMBER"])
    issue = repo.get_issue(issue_number)
    
    event_name = os.environ["EVENT_NAME"]
    
    # Determine what to respond to
    if event_name == "issues":
        # New issue or edited issue
        issue_title = os.environ["ISSUE_TITLE"]
        issue_body = os.environ.get("ISSUE_BODY", "")
        
        # Skip if issue already has comments from the bot
        comments = issue.get_comments()
        bot_name = "github-actions[bot]"
        if any(comment.user.login == bot_name for comment in comments):
            print("Bot already responded to this issue")
            return
        
        message = f"Issue: {issue_title}\n\n{issue_body}"
        
    elif event_name == "issue_comment":
        # Someone commented on the issue
        comment_body = os.environ.get("COMMENT_BODY", "")
        
        # Skip if it's the bot's own comment
        if not comment_body or comment_body.startswith("🤖"):
            print("Skipping bot's own comment")
            return
        
        message = comment_body
    else:
        print(f"Unhandled event: {event_name}")
        return
    
    print(f"Asking Claude: {message[:100]}...")
    
    # Get Claude's response
    try:
        claude_response = get_claude_response(message)
        
        # Post as comment
        bot_comment = f"🤖 **Claude's Response:**\n\n{claude_response}"
        issue.create_comment(bot_comment)
        
        print("Successfully posted Claude's response!")
        
    except Exception as e:
        print(f"Error: {e}")
        issue.create_comment(f"⚠️ Sorry, I encountered an error: {str(e)}")

if __name__ == "__main__":
    main()
