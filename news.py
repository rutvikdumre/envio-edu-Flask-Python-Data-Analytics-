from newsapi import NewsApiClient

def getNews():
    # Init
    newsapi = NewsApiClient(api_key='b35acb4a95cd4864afcc5acd082c1220')
    # /v2/top-headlines
    top_headlines = newsapi.get_everything(q='Climate',language='en')
    l=[]
    for i in top_headlines['articles']:
        l+=[i]
    ctr=0
    titles=[]
    content=[]
    url=[]
    image=[]
    time=[]
    for i in l:
        if(ctr>10):
            break
        else:
            ctr+=1
            titles+=[i['title']]
            content+=[i['description']]
            url+=[i['url']]
            image+=[i['urlToImage']]
            time+=[i['publishedAt']]
    return titles,content,url,image,time
