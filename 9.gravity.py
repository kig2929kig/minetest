import miney

def set_hp(event):
    mt.player["MineyPlayer"].hp = 2*10
    print("seting hp")

mt = miney.Minetest()

mt.on_event('hp', set_hp)
