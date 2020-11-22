from stackapi import StackAPI
'''
SITE = StackAPI('stackoverflow')
comments = SITE.fetch('comments')
print(comments)'''
SITE = StackAPI("stackoverflow")
SITE.max_pages=2
SITE.page_size=100
questions = SITE.fetch('questions', min=10, sort='votes')
for quest in questions['items']:
    if 'title' not in quest:
        continue
    quest_id = quest['question_id']
    title = quest['title']
    tags = []
    if 'tags' in quest:
      tags = quest['tags']
    #body = quest['body']
    body = ""
    if 'body' in quest:
      body = quest['body']

      questions = SITE.fetch('questions', id=[quest_id],min=10, sort='votes')
      print(title)
