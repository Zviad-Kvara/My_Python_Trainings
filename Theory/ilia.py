# გავაკეთე ნაბიჯ ნაბიჯ, მარა გავიაროთ იქნებ კიდევ 
# არის რამე მარტივი მიდგომა. თუ შესაძლებელია დავწეროთ
# თასკი, რომელიც ამოიხსნება ამ კოდით 

def outer_func(x):
    y = 4
    return lambda z: x+y+z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

