import miney 
mt = miney.Minetest()

pos = mt.player.MineyPlayer.position
print(pos)

pos['x'] += 1

for i in range(5):
    mt.node.set(pos, "default:dirt")
    pos['x'] += 1

mt.player.MineyPlayer.position = {"x":pos['x']-1, "y":pos['y'],"z":pos['z']+1}
