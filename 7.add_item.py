import miney

# 실행 중인 Minetest와 miney 연결
# miney Minetest에서 python 프로그래밍을 위한 API
mt = miney.Minetest()


# fly 권한 부여 - K 키를 누르면 fly 모두가 부여
# 스페이스바를 누르면 상승하고, Shift키를 누르면 하강

mt.player.MineyPlayer.fly = True

# player의 이동 속도와 함께 설정하면
mt.player.MineyPlayer.speed = 5
