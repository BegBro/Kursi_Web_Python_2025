"""
cards = {5, 7, 'туз','валет','дама','король'}
print(cards)
cards_2 = cards.copy()
cards_2.discard('туз')
cards_buf = cards_2 & cards
while cards_buf:
    print(cards_buf.pop())
"""

"""
cards ={3, 7, 'T','D','V','K'}
ace = {'T'}

result = cards - ace
print(result)
"""

"""
t_is = False
cards = {5, 7, 'туз','валет','дама','король'}
print(cards)
while cards:
    card = cards.pop()
    if card == 'туз':
        cards.add(card)
        t_is = True
    else:
        print(cards)
    if t_is and len(cards) == 1:
        break
"""