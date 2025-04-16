import requests

# Replace with your Facebook Page ID
PAGE_ID = "YOUR_FACEBOOK_PAGE_ID"
# Replace with your valid Facebook Access Token
ACCESS_TOKEN = "YOUR_FACEBOOK_ACCESS_TOKEN"
# Specify the Graph API version you want to use (e.g., v19.0)
GRAPH_API_VERSION = "v19.0"

def fetch_public_posts(page_id, access_token, api_version):
    """Fetches public posts from a Facebook page."""
    base_url = f"https://graph.facebook.com/{api_version}/{page_id}/posts"
    params = {
        "access_token": access_token,
        "fields": "id,message,created_time,permalink_url", # Specify the fields you want
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raise an exception for bad status codes
        data = response.json()

        if "data" in data:
            posts = data["data"]
            print(f"Public posts from Facebook Page (ID: {page_id}):")
            for post in posts:
                print(f"  Post ID: {post.get('id')}")
                if "message" in post:
                    print(f"  Message: {post['message']}")
                print(f"  Created Time: {post.get('created_time')}")
                print(f"  Permalink URL: {post.get('permalink_url')}")
                print("-" * 20)
            if "paging" in data and "next" in data["paging"]:
                next_page_url = data["paging"]["next"]
                print(f"Next page: {next_page_url}")
                # You can implement logic here to fetch subsequent pages if needed
        else:
            print("No public posts found or an error occurred.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
    except KeyError:
        print("Error parsing the API response.")

if __name__ == "__main__":
    fetch_public_posts(PAGE_ID, ACCESS_TOKEN, GRAPH_API_VERSION)
