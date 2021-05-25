import random
import colorama
from colorama import Fore

colorama.init()
print(Fore.RED)
print("==================================")
print(Fore.WHITE)
print("Lisans başarıyla oluşturuldu.")
print(Fore.WHITE)

def LisansOlusturucu():
    lisans = ["Lisans: IShv46ySDy","Lisans: M3jOxt8gI7","Lisans: ByGy7IKjxX","Lisans: 612bh6LYLX","Lisans: mQ6ocanvpq"]
    lisans2 = ["qGg4X02z3S2kHcv", "zLQoFDxt9reGCH7", "4iVYjbdYhJlhyT9", "q5roEE90wnlrRr4", "mz6h3rDWASEai9y", "px8PIkcApGa0SZE", "wQvb5Aw8Tgx1SEm8""px8PIkcApG84a0SZE", "wQvb5Alkow8Tx1SEm8"]
    return "{}-{}".format(random.choice(lisans), random.choice(lisans2))

for i in range(1):
    print(LisansOlusturucu())

print(Fore.RED)
print("==================================")
