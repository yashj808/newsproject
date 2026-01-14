from django.shortcuts import render
from newsapi import NewsApiClient
from django.utils import timezone
from datetime import datetime, timedelta

def indec(request):
    source = request.GET.get('source', 'techcrunch')
    newsapi = NewsApiClient(api_key='YOUR_API_KEY')
    
    # Calculate the time 4 hours ago and format it
    four_hours_ago = (timezone.now() - timedelta(hours=4)).strftime('%Y-%m-%dT%H:%M:%S')
    
    all_articles = newsapi.get_everything(sources=source,
                                          language='en',
                                          from_param=four_hours_ago,
                                          sort_by='publishedAt')

    l = all_articles['articles']
    fallback_message = None

    if not l:
        top_headlines = newsapi.get_top_headlines(country="us", language='en')
        l = top_headlines['articles']
        fallback_message = f"No news from {source.replace('-', ' ').title()} in the last 4 hours. Showing top US headlines instead."

    desc = []
    news = []
    img = []
    pub_since = []
    urls = []

    for f in l:
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        urls.append(f['url'])
        
        # Parse the date string
        pub_date = datetime.fromisoformat(f['publishedAt'].replace('Z', '+00:00'))
        
        # Calculate time since publication
        time_diff = timezone.now() - pub_date
        
        # Format the time difference
        if time_diff.days > 0:
            pub_since.append(f"{time_diff.days} days ago")
        elif (time_diff.seconds // 3600) > 0:
            pub_since.append(f"{time_diff.seconds // 3600} hours ago")
        elif (time_diff.seconds // 60) > 0:
            pub_since.append(f"{time_diff.seconds // 60} minutes ago")
        else:
            pub_since.append("Just now")

    mylist = zip(news, desc, img, pub_since, urls)

    return render(request, 'index.html', context={"mylist": mylist, "source": source, "fallback_message": fallback_message})