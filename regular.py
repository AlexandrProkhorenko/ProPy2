import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  clean_list = []
  for elem in contacts_list:
    filter_list = list(filter(None,elem))
    clean_list.append(filter_list)
  clean_list[-2].append(clean_list[-1][1])
  del clean_list[-1]

  data = clean_list[1][0].split()
  new_list = data + clean_list[1]
  del new_list[3]
  clean_list[1].extend(new_list)
  while len(clean_list[1]) >= 8:
    del clean_list[1][0]
  new_list.clear()
  data.clear()

  data = clean_list[2][0].split()
  new_list = data + clean_list[2]
  del new_list[3], new_list[4]
  new_list.insert(4,clean_list[4][4])
  new_list.insert(5, clean_list[2][2])
  clean_list[2].extend(new_list)
  while len(clean_list[2]) >= 7:
    del clean_list[2][0]
  del clean_list[4]
  new_list.clear()
  data.clear()


  data = clean_list[3]
  new_list = data[1].split()
  name = new_list[0]
  fathestvo = new_list[1]
  clean_list[3].insert(1,name)
  clean_list[3].insert(2, fathestvo)
  del clean_list[3][3]


  data = clean_list[4][0].split()
  new_list = data + clean_list[4]
  del new_list[3]
  clean_list[4].extend(new_list)
  while len(clean_list[4]) >= 7:
    del clean_list[4][0]
  new_list.clear()
  data.clear()

  data = clean_list[5][0].split()
  new_list = data + clean_list[5]
  del new_list[3]
  clean_list[5].extend(new_list)
  while len(clean_list[5]) >= 7:
    del clean_list[5][0]
  new_list.clear()
  data.clear()

  data = clean_list[6][0].split()
  new_list = data + clean_list[6]
  del new_list[3]
  clean_list[6].extend(new_list)
  while len(clean_list[6]) >= 7:
    del clean_list[6][0]
  new_list.clear()
  data.clear()


  def number(pattern, subst, list):
    x = 0
    for i in list:
      y = 0
      for n in i:
        list[x][y] = re.sub(pattern, subst, n)
        y = y + 1
      x = x + 1
number(r"(\+7|8)\s*?\(?(\d{3})\)?\-?\s?(\d{3})\-?(\d{2})\-?(\d{2})", r"+7(\2)\3-\4-\5", clean_list)
number(r"\(?\доб.\s+(\d+)\)?", r"доб.\1", clean_list)
for i in clean_list:
  print(i)

  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(clean_list)


























































































  # print(convertList_list[11:28])






























  # first_line = contacts_list[0]
  # second_line = contacts_list[1]
  # second_line = list(filter(None, second_line))





























