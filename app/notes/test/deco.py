#encoding:utf-8

def pairwise(iterable):
  itnext = iter(iterable).__next__
  while True:
    yield itnext(), {itnext(): itnext(), itnext():itnext()}

def dictFromSequence(keyAndValues):
  return dict(pairwise(keyAndValues))

a = ['A', 'count', 10, 'price', 100, 'B', 'count', 20, 'price', 200]

shopping_cart = dictFromSequence(a)
print(shopping_cart)
print(type(shopping_cart))