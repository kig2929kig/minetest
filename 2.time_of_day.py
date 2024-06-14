import miney

# 실행 중인 Minetest와 miney 연결
# miney Minetest에서 python 프로그래밍을 위한 API
mt = miney.Minetest()


# Minetest 게임 내의 현재 시간을 나타냄
# 0.0 ~ 1.0 사이의 값
# 0.0은 자정(00:00)
# 1.0은 다음 날 자정(24:00)
# 0.5는 정오(12:00)
mt.time_of_day = 0.5
