a = 5
b = 5

class teaser():
  a = 2
  b = 2
  def __init__(self):
    print(f"Enter Initializing...\n\tself.a->{self.a}\n\tself.b->{self.b}")
    self.a = 4
    self.b = 2
    print(f"After Initializing...\n\tself.a->{self.a}\n\tself.b->{self.b}")
    print(f"But but:\n\t'a' = {a}\n\t'b' = {b}")
    print("Exit Initializing")
  def __str__(self):
    print(f"Entering __str__ method...\n\tself.a->{self.a}\n\tself.b->{self.b}")
    self.a = 3
    self.b = 2
    print(f"After __str__ method...\n\tself.a->{self.a}\n\tself.b->{self.b}")
    print(f"But but:\n\tself.a({self.a}) == a({a})? {self.a == a}")
    print(f"But but:\n\tself.b({self.b}) == b({b})? {self.b == b}")
    return f'Returning: a({a}) + b({b}) = {str(a+b)}'
    
number = teaser()
print(number)