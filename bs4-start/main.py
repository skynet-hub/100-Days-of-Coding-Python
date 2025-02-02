from bs4 import BeautifulSoup
import requests

# with open("./website.html") as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, 'html.parser') 

# all_anchor_tags = soup.find_all(name="a")

#What if I want to find all of the strings?

# for tag in all_anchor_tags:
#     print(tag.string, tag.get("href"))

#What if I wante to get hold of the link instead? Above just make use of the .get method and specify href   


#LEt us expand and get more tools for searching?
#Find method will find one thing, but then whe you do find you can use name, ids and class to narrow down and get the exact thing you are looking for
#e.g h1 with a id name

# heading = soup.find(name="h1", id="name")
# print(heading)

#Be careful with the use of the word class when you search as this is a reserved word in python

#Let us make an example on how to go about this...

# sub_heading = soup.find(name="h3", class_= "heading")

# print(sub_heading)

# #When we are dealing with beautiful soap we can make use of css selectors, and this is achoeved by using the select keyword
# #LEt us try this, select the first anchor tag, this is the only tag inside a paragraph

# first_anchor = soup.select_one(selector="p a")
# print(first_anchor)

# #To get hold of id just like in css make use of # and to make use of classes .

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_news = response.text

soup = BeautifulSoup(yc_news, 'html.parser')
articles = soup.findAll(name="a", class_="storylink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link= article.get("href")
    article_links.append(link)


article_up_vote = [score.getText() for score in soup.findAll(name="span", class_="score")]
final_up_votes = [int(score.split(" ")[0]) for score in article_up_vote]

# print(article_texts)
# print(article_links)
# print(final_up_votes)


index_of_biggest_upvote =final_up_votes.index(max(final_up_votes))
print(article_texts[index_of_biggest_upvote], article_links[index_of_biggest_upvote])
