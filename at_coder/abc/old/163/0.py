import collections
def find_pairs(values, target):
  # dic = {}
  # for value in values:
  #   dic[value] = True
  dic = collections.Counter(values)

  for value in values:
    compliment = target - value
    if dic.get(compliment):
      if target == compliment and dic[compliment] > 1:
        return (value, compliment)
      return (value, compliment)

# print(find_pairs([14,13,6,7,8,10,1,2],3))
# print(find_pairs([2,2],4))

# edge case
print(find_pairs([-1,3], 2))
print(find_pairs([], 1))

# 1. ask quesitons before coding
# 2. how well they can code
# 3. edge cases in test
#     - duplicates staying 
#     - both inputs going to be valid