import miney

mt = miney.Minetest()

mt.time_of_day = 0.5

pos = mt.player.MineyPlayer.position

print(pos['x']) # 앞 뒤 
print(pos['y']) # 공중
print(pos['z']) # 좌 우



#mt.player.MineyPlayer.position = {"x":pos['x']+100, "y":pos['y']+100,"z":pos['z']+100}
mt.player.MineyPlayer.position = {"x":pos['x']-1, "y":pos['y'],"z":pos['z']}
