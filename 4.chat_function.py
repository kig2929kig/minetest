import miney

# 실행 중인 Minetest와 miney 연결
# miney Minetest에서 python 프로그래밍을 위한 API
mt = miney.Minetest()


# 채팅 기능
mt.chat.send_to_all("Hello~ Minetest")


print(list(mt.player))
