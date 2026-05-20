import random

player = {
    "name": "dksh",
    "hp": 100,
    "max-hp": 100,
    "atk": 15,
    "gold": 0,
    "potion": 2,
}

def create_monster() : 
    monsters = [
        {
            "name": "피카츄",
            "hp": 35,
            "atk": 55,
            "gold": 10,
        },
        {
            "name": "이상해꽃",
            "hp": 80,
            "atk": 82,
            "gold": 30,
        },
        {
            "name": "리자몽",
            "hp": 78,
            "atk": 84,
            "gold": 50,
        },
    ]

    return random.choice(monsters).copy()

def battle() : 
    monster = create_monster()
    print(f"\n** {monster['name']} 등장!")

    while monster['hp'] > 0 and player['hp'] > 0 : 
        print(f"\n[플레이어 HP]: {player['hp']} / 몬스터 HP: {monster['hp']}")
        action = int(input("동작 선택: 1. 공격 / 2. 포션 사용"))

        if action == 1 : 
            dmg = random.randint(player['atk'] - 3, player['atk'] + 3)
            monster['hp'] -= dmg
            print(f"** {monster['name']}에게 {dmg} 데미지!")
        
        elif action == 2 : 
            if player['potion'] > 0 : 
                heal = random.randint(20, 35)
                player['hp'] = min(player['max-hp'], player['hp'] + heal)
                player['potion'] -= 1
                print(f"** HP {heal} 회복!")
            
            else : 
                print("포션이 없다!")
                # 포션이 없네 ,,?
        
        else : 
            print("잘못된 입력!")
            # 잘못된 입력인데요 ?

        if monster['hp'] > 0 : 
            mdmg = random.randint(monster['atk'] - 2, monster['atk'] + 2)
            player['hp'] -= mdmg
            print(f"** {monster['name']}의 공격! {mdmg} 데미지!")
        
    if player['hp'] > 0 : 
        reward = monster['gold']
        player['gold'] += reward
        print(f"\n** 승리! {reward} 골드 획득!")
    
    else : 
        print("\n** 패배... 게임 오버")
        # 전투에서 패배햇어 .. 다시 도전해볼까 ?
    
def shop() : 
    print("\n** 상점")
    # 상점이에요 !
    print("1. 포션 구매 (10 골드)")
    print("2. 공격력 강화 (30 골드)")
    print("3. 나가기")
    # 상점에서 나갈래 ,,

    choice = int(input("선택: "))
    # 머를 선택할거야 ? : 

    if choice == 1 : 
        if player['gold'] >= 10 : 
            player['gold'] -= 10
            player['potion'] += 1
            print("* 포션 + 1")
            # 포션 한개가 추가됫어 !
        
        else : 
            print("골드 부족")
            # 골드가 부족한데 ?
        
    elif choice == 2 : 
        if player['gold'] >= 30 : 
            player['gold'] -= 30
            player['atk'] += 10
            print("* 공격력 + 10")
            # 공격력 10이 추가됫어 !
        
        else : 
            print("골드 부족")
        
while True : 
    if player['hp'] <= 0 : 
        print("게임 종료")
        # 게임이 끝낫어 ;ㅁ;
        return
    
    print("\n============================")
    print(f"HP: {player['hp']} | ATK: {player['atk']} | GOLD: {player['gold']} | POTION: {player['potion']}")
    print("\n============================")
    print("1. 사냥")
    # 사냥하러 가볼래 ?
    print("2. 상점")
    # 상점에 쳐들어가자 !
    print("3. 종료")
    # 왜 종료해 ?
    # 종료할게 !

    cmd = int(input("선택: "))
    # 어떤걸 선택할래 ? : 

    if cmd == 1 : 
        battle()
        
    elif cmd == 2 : 
        shop()
    
    elif cmd == 3 : 
        print("게임 종료")
        # 게임 종료를 눌럿어 ㅜㅅㅜ
        break
    
    else : 
        print("잘못된 입력")
        # 잘못된 입력이라니까여 ?