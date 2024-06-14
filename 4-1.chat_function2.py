import miney

# 실행 중인 Minetest와 miney 연결
# miney Minetest에서 python 프로그래밍을 위한 API
mt = miney.Minetest()


# 채팅 기능
def start_chat():
    player = "kig2929kig"

    while True :
        msg = input("채팅(종료: q or Q) => ")
        if msg in ['q', 'Q'] :
            break
        mt.chat.send_to_all(player + ":" + msg)

# 메뉴

def menu() :
    print("****************\n")
    print("* 1 : 채팅     *\n")
    print("* 0 : 종료     *\n")
    print("****************\n")

    menu_number = input("메뉴 선택 : ")
    return int(menu_number)

while True :
    select = menu()
    if select == 1:
        start_chat()
    elif select == 0:
        break

