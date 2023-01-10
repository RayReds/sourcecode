def author_rankings(thread_list):
  # TODO: Determine (author, upvotes, ranking) over all threads.
  dc = thread_list
  li = []
  dic = {}
  for i in dc:
      for post in i['posts']:
          if post['author'] in dic:
              dic[post['author']] += post['upvotes']
          else:
              dic[post['author']] = post['upvotes']
  for k, v in dic.items():
      upvt = v
      stat = None
      if upvt == 0:
          stat = 'Insignificantly Evil'
      elif upvt < 20:
          stat = 'Cautiously Evil'
      elif upvt < 100:
          stat = 'Justifiably Evil'
      elif upvt < 500:
          stat = 'Wickedly Evil'
      else:
          stat = 'Diabolically Evil'
      li.append((k, v, stat))
  extra = []
  li.sort(key=lambda x: x[1], reverse=True)
  for i in li:
      if extra == []:
          extra.append([i])
      elif extra[-1][0][1] == i[1]:
          extra[-1].append(i)
      else:
          extra.append([i])
  li = []
  for i in extra:
      i.sort(key = lambda x:x[0])
      for a in i:
          li.append(a)
  return li


if __name__ == '__main__':
  # Example calls to your function.
  print(author_rankings([
    {
        'title': 'Invade Manhatten, anyone?',
        'tags': ['world-domination', 'hangout'],
        'posts': [
            {
                'author': 'Mr. Sinister',
                'content': "I'm thinking 9 pm?",
                'upvotes': 2,
            },
            {
                'author': 'Mystique',
                'content': "Sounds fun!",
                'upvotes': 0,
            },
            {
                'author': 'Magneto',
                'content': "I'm in!",
                'upvotes': 0,
            },
        ],
    }
  ]))
