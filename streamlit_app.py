# # import streamlit as st

# # st.title("🎈 My new app")
# # st.write(
# #     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# # )

# import streamlit as st

# def home():
#     st.title("Welcome to My Portfolio")
#     st.write("Quick intro here...")
#     # Add more content...

# def about():
#     st.title("About Me")
#     st.write("Your bio, skills, and portfolio here...")

# def blogs():
#     st.title("My Blogs")
#     st.write("Browse my blog posts below...")
#     # Code to fetch and display Medium blogs here...

# # Navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "About", "Blogs"])

# if page == "Home":
#     home()
# elif page == "About":
#     about()
# elif page == "Blogs":
#     blogs()


import streamlit as st
import feedparser

# Define functions for each page
def home():
    st.title("Welcome to My Portfolio")
    st.write("Quick intro here...")
    # Add more content, e.g., summary of projects

def about():
    st.title("About Me")
    st.write("This is the about section where you can share your bio, skills, experience, etc.")
    # Add sections for skills, experience, etc.

def fetch_medium_posts():
    # Fetch Medium posts using your Medium feed URL
    feed_url = "https://medium.com/feed/@your_medium_username"
    feed = feedparser.parse(feed_url)
    return feed.entries

def blogs():
    st.title("My Blogs")
    # posts = fetch_medium_posts()
    # for post in posts:
    #     st.write(f"### [{post.title}]({post.link})")
    #     st.write(post.published)
    #     st.write(post.summary[:150] + "...")  # Show a snippet of the summary
    #     st.write("---")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Page", ["Home", "About", "Blogs"])

# Page logic
if page == "Home":
    home()
elif page == "About":
    about()
elif page == "Blogs":
    blogs()
