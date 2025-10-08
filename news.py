# import streamlit as st
# import requests
# st.title("PERSONALIZED NEWS AGGREGATOR")
# st.write("Get the latest news ")
# category = st.sidebar.selectbox(
#     "Choose a news category",
#     ["general","technology","business","entertainment","sports"]
# )
# keyword = st.sidebar.text_input("Enter a keyword(it is optional)")

# def fetch_news(category, keyword=None):
#     return[
#         {"title":"Sample headline 1","description":"This is the sample article"},
#          {"title":"Sample headline 2","description":"This is the another example "},
#     ]
#     if st.button("Show news"):
#         st.subheader(f"Top {category.capitalize()} News")
#         articles = fetch_news(category,keyword)
#         for article in articles:
#            st.markdown(f"#{article['title']}")
#            st.write(article['description'])
#            st.markdown('---')

# import requests

# # ✅ Replace this with your actual API key from https://newsapi.org/
# API_KEY = "your_news_api_key_here"

# def fetch_news(category=None, keyword=None):
#     """
#     Fetch news articles from NewsAPI based on category or keyword.
#     Returns a list of dictionaries containing title, description, and URL.
#     """
#     base_url = "https://newsapi.org/v2/top-headlines"
#     params = {
#         "apiKey": API_KEY,
#         "country": "in",  # Get Indian news
#     }

#     if category:
#         params["category"] = category.lower()
#     if keyword:
#         params["q"] = keyword

#     try:
#         response = requests.get(base_url, params=params)
#         data = response.json()

#         # ✅ Return top 5 articles in clean format
#         if data["status"] == "ok":
#             articles = []
#             for article in data["articles"][:5]:
#                 articles.append({
#                     "title": article["title"],
#                     "description": article["description"],
#                     "url": article["url"]
#                 })
#             return articles
#         else:
#             print("Error from API:", data.get("message", "Unknown error"))
#             return []
#     except Exception as e:
#         print("Error fetching news:", e)
#         return []