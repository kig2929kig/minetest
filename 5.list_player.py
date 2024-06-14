import miney

# 실행 중인 Minetest와 miney 연결
# miney Minetest에서 python 프로그래밍을 위한 API
mt = miney.Minetest()


# 모든 플레이어 목록을 출력

print(list(mt.player))


