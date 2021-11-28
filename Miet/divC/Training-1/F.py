# -*- coding: utf-8 -*-
# @Author: kostya
# @Date:   2021-11-14 00:49:14
# @Last Modified by:   kostya
# @Last Modified time: 2021-11-14 17:06:54

def get_max_score(d):
  ans = None
  for i in d:
    if ans is None or d[i] > d[ans]:
      ans = i
  return ans


n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in a:
  d[i] = d.get(i, 0) + 1
a = set(a)
score = dict()
true_score = dict()
for i in a:
  score[i] = d[i] * i - d.get(i + 1, 0) * (i + 1) - d.get(i - 1, 0) * (i - 1)
  true_score[i] = d[i] * i
ans = 0
while len(score) > 0:
  max_score = get_max_score(score)
  ans += true_score[max_score]
  if max_score - 2 in score:
    score[max_score - 2] += true_score.get(max_score - 1, 0)
  if max_score + 2 in score:
    score[max_score + 2] += true_score.get(max_score + 1, 0)
  del score[max_score]
  if max_score - 1 in score:
    del score[max_score - 1]
  if max_score + 1 in score:
    del score[max_score + 1]
  del true_score[max_score]
  if max_score - 1 in true_score:
    del true_score[max_score - 1]
  if max_score + 1 in true_score:
    del true_score[max_score + 1]
print(ans)
