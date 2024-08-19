#Python
# Define a function to share fitness progress on social media
import requests

def shareProgress(progress) {
  url = 'https://api.twitter.com/1.1/statuses/update.json'
  headers = {
    'Authorization': 'Bearer YOUR_TWITTER_TOKEN',
    'Content-Type': 'application/json'
  }
  data = {
    'status': `Just reached a new fitness milestone! ${progress}`
  }
  response = requests.post(url, headers=headers, json=data)
  if response.status_code == 200:
    print('Progress shared successfully!')
  else:
    print('Error sharing progress:', response.text)
}

# Example usage:
progress = 'Completed a 5K run!'
shareProgress(progress)