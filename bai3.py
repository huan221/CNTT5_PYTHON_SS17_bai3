import itertools
teams_list = []


def input_team(teams):
    print("--- NHẬP DANH SÁCH ---")
    teams_inp = input("Nhập các đội (cách nhau bởi dấu phẩy): ")
    list_team = teams_inp.split(",")
    list_team = [team.strip().upper() for team in list_team if team != '']

    teams.extend(list_team)
    
    print(f"Đã ghi nhận {len(list_team)} đội: {list_team}")


def create_games(teams):
    list_game = list(itertools.combinations(teams, 2))
    return list_game
    

def create_id_games(teams):
    list_game = create_games(teams)
    for index, game in enumerate(list_game, start=1):
        print(f"{f'Trận {index} ({game[0]} vs {game[1]})':<25} -> ID: M{index:02d}-{game[0][0:3]:X<3}-{game[1][0:3]:X<3}")
        


def main():
    while True:
        choice = input("""
============= ESPORTS MATCHMAKER =============
1. Nhập danh sách Đội tuyển
2. Tạo lịch thi đấu (Combinations)
3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)
4. Đóng hệ thống
==============================================
Chọn chức năng (1-4): """)
        
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Vui lòng nhập số nguyên 1-4")
            continue
    
        match choice:
            case 1:
                input_team(teams_list)
                
            case 2:
                list_game = create_games(teams_list)
                for index, game in enumerate(list_game, start=1):
                    print(f"{index}. {game[0]} vs {game[1]}")
                print(f"Tổng số trận đấu: {len(list_game)} trận.")
                
            case 3:
                create_id_games(teams_list)
                
            case 4:
                print("Thoát chương trình.")
                break
        
            case _:
                print("Lỗi cú pháp")
                
main()            
                
        