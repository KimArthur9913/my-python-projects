import random

# 1. Настройка
suits = ['♤', '♡', '♢', '♧']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

deck = [f"{r}{s}" for s in suits for r in ranks]
random.shuffle(deck)

player_hand = [deck.pop() for _ in range(6)]
bot_hand = [deck.pop() for _ in range(6)]
trump_card = deck[0]
trump_suit = trump_card[-1]

def can_beat(card_to_beat, attack_card, trump):
    suit_b, rank_b = card_to_beat[-1], card_to_beat[:-1]
    suit_a, rank_a = attack_card[-1], attack_card[:-1]
    if suit_a == suit_b: return values[rank_a] > values[rank_b]
    if suit_a == trump and suit_b != trump: return True
    return False

def card_strength(c):
    return values[c[:-1]] + (100 if c[-1] == trump_suit else 0)

# Кто ходит первым (у кого меньше козырь - для простоты начнем с игрока)
player_turn = True 

# ОСНОВНОЙ ЦИКЛ
while len(player_hand) > 0 and len(bot_hand) > 0:
    table = [] # Карты на столе в этом кону
    print(f"\n{'='*20}\nКОЗЫРЬ: {trump_card} | В колоде: {len(deck)}")
    
    if player_turn:
        print("ТВОЙ ХОД! Твои карты:")
        for i, c in enumerate(player_hand, 1): print(f"{i}.{c}", end=" ")
        
        choice = int(input("\nВыбери карту для атаки: ")) - 1
        attack_card = player_hand.pop(choice)
        table.append(attack_card)
        
        while True: # Цикл подкидывания
            print(f"На столе: {table}")
            # Бот пытается отбиться
            to_beat = table[-1]
            possible = [c for c in bot_hand if can_beat(to_beat, c, trump_suit)]
            
            if possible:
                bot_card = min(possible, key=card_strength)
                print(f"Бот отбился: {bot_card}")
                bot_hand.remove(bot_card)
                table.append(bot_card)
                
                # Игрок может подкинуть
                ranks_on_table = [c[:-1] for c in table]
                can_add = [c for c in player_hand if c[:-1] in ranks_on_table]
                
                if can_add:
                    print("Можно подкинуть:")
                    for i, c in enumerate(player_hand, 1): print(f"{i}.{c}", end=" ")
                    add_choice = input("\nНомер карты чтобы подкинуть или '0' для БИТА: ")
                    if add_choice == '0': break
                    table.append(player_hand.pop(int(add_choice)-1))
                else:
                    print("Нечего подкинуть.")
                    break
            else:
                print("Бот берет карты!")
                bot_hand.extend(table)
                player_turn = True # Игрок снова ходит
                table = []
                break
        if table: player_turn = False # Если была бита, ход переходит к боту
            
    else:
        # ХОД БОТА
        bot_card = min(bot_hand, key=card_strength)
        bot_hand.remove(bot_card)
        table.append(bot_card)
        print(f"Бот ходит: {bot_card}")
        
        while True:
            print(f"Твои карты: {[f'{i+1}.{c}' for i,c in enumerate(player_hand)]}")
            your_move = input("Выбери карту чтобы отбиться или '0' чтобы ВЗЯТЬ: ")
            
            if your_move == '0':
                player_hand.extend(table)
                player_turn = False # Бот снова ходит
                table = []
                break
            else:
                def_card = player_hand.pop(int(your_move)-1)
                if can_beat(table[-1], def_card, trump_suit):
                    table.append(def_card)
                    # Бот пытается подкинуть
                    ranks_on_table = [c[:-1] for c in table]
                    bot_can_add = [c for c in bot_hand if c[:-1] in ranks_on_table and c[-1] != trump_suit]
                    if bot_can_add:
                        add_c = min(bot_can_add, key=card_strength)
                        bot_hand.remove(add_c)
                        table.append(add_c)
                        print(f"Бот подкинул: {add_c}")
                    else:
                        print("Бот: Бита!")
                        player_turn = True
                        break
                else:
                    print("Так нельзя бить! Карта вернулась в руку.")
                    player_hand.append(def_card)

    # Добор карт
    while len(player_hand) < 6 and len(deck) > 0: player_hand.append(deck.pop())
    while len(bot_hand) < 6 and len(deck) > 0: bot_hand.append(deck.pop())

print("ИГРА ОКОНЧЕНА!")