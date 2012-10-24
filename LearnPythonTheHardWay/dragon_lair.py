import random
from sys import exit

player_max_health = 100
player_health = player_max_health	
equiped_weapon = "Short Sword"
equiped_armor = "Leather Armor"
inventory = ["Potion"]

def str():
	wep_str = weapon_stats(equiped_weapon)[0]
	arm_str = armor_stats(equiped_armor)[0]
	return wep_str + arm_str

def dex():
	wep_dex = weapon_stats(equiped_weapon)[1]
	arm_dex = armor_stats(equiped_armor)[1]
	return wep_dex + arm_dex
	
def intel():
	wep_int = weapon_stats(equiped_weapon)[2]
	arm_int = armor_stats(equiped_armor)[2]
	return wep_int + arm_int

def armor_stats(armor):
	if armor == "Leather Armor":
		str = 10
		dex = 40
		intel = 2
		dmg_red = 15
	
	elif armor == "No Armor":
		str = 0
		dex = 0
		intel = 2
		dmg_red = 0
	
	elif armor == "Plate Armor":
		str = 30
		dex = 40
		intel = 2
		dmg_red = 70
	
	else:
		print "armor not recognised"
	
	return [str,dex,intel,dmg_red]
	
def weapon_stats(weapon):
	if weapon == "Short Sword":
		str = 10
		dex = 2
		intel = 1
		dmg = random.randint(10,20)
		dmg_txt = "10 - 20"
		dmg_type = "Normal"
		
	elif weapon == "Fists":
		str = 0
		dex = 0
		intel = 0
		dmg = random.randint(1,5)
		dmg_txt = "1 - 5"
		dmg_type = "Normal"
	
	elif weapon == "Cold Poker":
		str = 20
		dex = 50
		intel = 1
		dmg = random.randint(25,45)
		dmg_txt = "25 - 45"
		dmg_type = "Ice"
	
	else:
		print "weapon not recognised"
	
	return [str,dex,intel,dmg,dmg_type,dmg_txt]
	
def weapon_damage(target):
	hit = int(random.randint(0,100) + (dex()*0.5))
	if hit >= monster_stats(target)[2]:
		if weapon_stats(equiped_weapon)[4] == monster_stats(target)[4]:
			damage = 2*(int(weapon_stats(equiped_weapon)[3] * (1+(float(str())/100))))
		else:
			damage = int(weapon_stats(equiped_weapon)[3] * (1+(float(str())/100)))
		return ["You deal %d damage to the %s" % (damage,target),damage]
	else:
		damage = 0
		return ["You MISS the %s" % target,damage]
		
def monster_stats(monster):
	if monster == "Target Dummy":
		hp = 20
		dmg = random.randint(1,5)
		to_hit_monster = 50
		monster_hit_chance = 20
		monster_weakness = "Normal"
		
	elif monster == "Troll":
		hp = 80
		dmg = random.randint(5,15)
		to_hit_monster = 50
		monster_hit_chance = 20
		monster_weakness = "Ice"
	
	elif monster == "Ogre":
		hp = 160
		dmg = random.randint(70,100)
		to_hit_monster = 25
		monster_hit_chance = 40
		monster_weakness = "None"
	
	elif monster == "boss_left":
		hp = 250
		dmg = random.randint(60,120)
		to_hit_monster = 25
		monster_hit_chance = 40
		monster_weakness = "Ice"
	
	elif monster == "boss_right":
		hp = 250
		dmg = random.randint(70,100)
		to_hit_monster = 25
		monster_hit_chance = 40
		monster_weakness = "None"
	
	elif monster == "boss_head":
		hp = 20
		dmg = random.randint(70,100)
		to_hit_monster = 25
		monster_hit_chance = 40
		monster_weakness = "None"
		
	else:
		print "monster not recognised"
		
	return [hp,dmg,to_hit_monster,monster_hit_chance,monster_weakness]

def monster_damage(monster):
	hit = random.randint(0,100)
	if hit >= monster_stats(monster)[3]:
		damage = int(monster_stats(monster)[1] * (float((100 - armor_stats(equiped_armor)[3]))/100))
		return ["The %s deals %d damage to you" % (monster,damage),damage]
	else:	
		return ["The %s MISSES you" % monster,0]
		
def heal():
	global player_health
	if "Potion" in inventory:
		player_health = player_max_health
		print "You drink a Potion and heal yourself to full health"
		inventory.remove("Potion")
		print "You have %d/%d health left" % (player_health,player_max_health)
		print "You have %d Potions left" % inventory.count("Potion")
	else:
		print "You check your bags but discover that you do not have any Potions"
	
def stats():
	print "%d/%d Health" % (player_health,player_max_health)
	print "Weapon: %s" % equiped_weapon
	print "Weapon DMG: %s" % weapon_stats(equiped_weapon)[5]
	print "Armor: %s" % equiped_armor
	print "DMG Reduction: %s%%" % armor_stats(equiped_armor)[3]
	print "Str: %d" % str()
	print "Dex: %d" % dex()
	print "Int: %d" % intel()
	print "Inventory: %s" % inventory
	print "\n"
	
def combat(monster):
	monster_health = monster_stats(monster)[0]
	global player_health
	print "\n"
	print "You stand face to face against the %s and ready your %s" % (monster, equiped_weapon)
	combat_loop = 1
	while combat_loop == 1:
		print "The %s stands before you." % monster
		print "You can attack, heal or view your stats."
		action = raw_input("> ")
		print "\n"
		
		if "attack" in action:
			player_dmg = weapon_damage(monster)
			print "You attack the %s with your %s" % (monster,equiped_weapon)
			print player_dmg[0]
			monster_health = monster_health - player_dmg[1]
			print "The %s has %d/%d health left" % (monster,monster_health,monster_stats(monster)[0])
			print "\n"
			
		elif "heal" in action:
			heal()
		
		elif "stats" in action:
			stats()
		
		else:
			print "You fumble around unsuccessfully trying to %s " % action
		
		if monster_health <= 0:
			print "You have killed the %s" % monster
			combat_loop = 0
			
		elif monster_health > 0 and (("attack" in action) or ("heal" in action)) :
			monster_dmg = monster_damage(monster)
			print "The %s attacks you!" % monster
			print monster_dmg[0]
			player_health = player_health - monster_dmg[1]
			print "You have %d/%d health left" % (player_health,player_max_health)
			print "\n"
			
			if player_health <= 0:
				print "The %s has defeated you." % monster
				print "\n"
				game_over()
			else:
				combat_loop = 1
		else:
			combat_loop = 1

def game_over():
	print "You fall to the ground and feel the world around you go dark."
	print "With your death, the dragon continued to harass the villagers feasting on thier"
	print "livestock and generally making a big mess of things."
	print "\n"
	print " _____________"
	print "|             |"
	print "| *GAME OVER* |"
	print "|_____________|"
	exit(0)

def boss_fight():
	print "As you walk into the large chamber, the enourmous crimson Dragon turns to face you."
	print "The Dragon's right side appears to be made of tough stone while it's left side appears"
	print "to be made of pure flame. You know that the weakest point of any foe is it's face"
	print "but the Dragon's head towers above you, how are you going to reach it's face?"
	print "Before you can plan your attack, the Dragon charges at you!" 
	print "\n"
	raw_input("Press ENTER to continue")
	
	boss_left_health = monster_stats("boss_left")[0]
	boss_right_health = monster_stats("boss_right")[0]
	boss_head_health = monster_stats("boss_head")[0]
	boss_head_lowered = 0
	global player_health
	
	boss_fight = 1
	while boss_fight == 1:
		print "You can heal, view stats or attack the Dragon's left, right or head."
		print "What do you do?"
		print "\n"
		action = raw_input("> ")
		print "\n"
		
		if ("head" in action) and boss_head_lowered == 1:
			print "With the Dragon's head now in your reach, you stab the Dragon in the face!"
			player_damage = weapon_damage("boss_head")[1]
			boss_head_health = boss_head_health - player_damage
			
			if player_damage <= 0:
				print "You MISS your attack!"
				print "The Dragon's left foot has %d/%d health left" % (boss_left_health,monster_stats("boss_left")[0])
				print "\n"				
			else:		
				print "You deal %s damage to the Dragon's face" % player_damage
				print "The Dragon's face has %d/%d health left" % (boss_head_health,monster_stats("boss_head")[0])
				print "\n"
			
			if boss_head_health <= 0:
				print "The Dragon's head crashes to the ground, you manage to roll out of the way"
				print "to avoid being crushed. With one last roar the Dragon opens it's mouth to"
				print "melt you with it's flaming breathe. Anticipating this, you dodge to the left"
				print "and with a booming voice you yell 'HADOUKEN!!' as you fire your own fireball"
				print "at the dragon. The fireball hits the dragon in the face killing it instantly." 
				print "\n"
				raw_input("Press ENTER to continue")
				boss_fight = 0
			else:
				boss_fight = 1
		
		elif ("head" in action) and boss_head_lowered == 0:
			print "You try to attack the Dragon in the face but it's too high!"
			print "You need to lower it's head by attacking it's feet first!"
			print "\n"
		
		elif "left" in action:
			print "You attack the Dragon's left foot! your %s is SUPER EFFECTIVE" % equiped_weapon
			player_damage = weapon_damage("boss_left")[1]
			boss_left_health = boss_left_health - player_damage
			
			if player_damage <= 0:
				print "You MISS your attack!"
				print "The Dragon's left foot has %d/%d health left" % (boss_left_health,monster_stats("boss_left")[0])
				print "\n"
			else:
				print "You deal %s damage to the Dragon's left foot" % player_damage
				print "The Dragon's left foot has %d/%d health left" % (boss_left_health,monster_stats("boss_left")[0])
				print "\n"			
			if boss_left_health <= 0:
				print "You have destroyed the Dragon's left foot! Unable to support the weight,"
				print "The Dragon LOWERS it's HEAD!!"
				print "\n"	
				boss_head_lowered = 1
			else:
				boss_head_lowered = 0
		
		elif "right" in action:
			print "You attack the Dragon's right foot"
			player_damage = weapon_damage("boss_right")[1]
			boss_right_health = boss_right_health - player_damage
			
			if player_damage <= 0:
				print "You MISS your attack!"
				print "The Dragon's left foot has %d/%d health left" % (boss_left_health,monster_stats("boss_left")[0])
				print "\n"					
			else:	
				print "You deal %s damage to the Dragon's right foot" % player_damage
				print "The Dragon's right foot has %d/%d health left" % (boss_right_health,monster_stats("boss_right")[0])
				print "\n"	
				
			if boss_right_health <= 0:
				print "You have destroyed the Dragon's right foot! Unable to support the weight,"
				print "The Dragon LOWERS it's HEAD!!"
				print "\n"	
				boss_head_lowered = 1
			else:
				boss_head_lowered = 0
					
		elif "stats" in action:
			stats()
		
		elif "heal" in action:
			heal()
		
		else:
			print "You try to %s but the Dragon whips you with it's tail and says NO!" % action
			
		if boss_head_health > 0 and not("stats" in action):
			print "The Dragon attacks you!"
			dragon_damage = monster_damage("boss_left")[1]
			player_health = player_health - dragon_damage
			
			if dragon_damage <= 0:
				print "You dodge the Dragon's attack!"
				print "You have %d/%d health left." % (player_health,player_max_health)
				print "\n"	
			
			else:
				print "The Dragon deals %s damage to you!" % dragon_damage
				print "You have %d/%d health left." % (player_health,player_max_health)
				print "\n"	
				
			if player_health <= 0:
				game_over()
			else:
				boss_fight = 1
		
		elif boss_head_health > 0 and ("stats" in action):
			boss_fight = 1
		
		else:
			boss_fight = 0
	
loop = 1
troll_alive = 1
ogre_alive = 1
print "\n"	
print "Armed with your trusty 'Short Sword', some rudementary 'Leather Armor'"
print "and a single Health Potion."
while loop == 1:
	print """
You stand before a large door, a sign hanging above the door convienatly 
tells you that this door leads into the: 
			 ___________________
			|                   |
			| * DARGON'S LAIR * |
			|___________________|

The villagers have all be complaining about this dragon and commissioned
you to kill it for them. 

To your left there is a path that leads into a forrest, the villagers told
you that a Troll lives in those woods and wears heavy plate armor.

To the right there is another path that leads into a rocky quarry, the 
villagers also told you that an enourmous Ogre lives there and wields
the a legendary frost sword "Cold Poker".
"""
	print "What would you like to do?\n"
	action = raw_input("> ")
	if (("left" in action) or ("forrest" in action)) and troll_alive == 1:
		print "You set off into the spooky forrest, the villagers didn't tell you it was going to be spooky."
		print "As you contemplate increasing your fee due to unforseen spookyness, a six foot tall, green skinned"
		print "Troll looking monster falls from the trees above and lands in front of you. This is probably the Troll"
		print "the villagers were talking about. Upon closer inspection, you see that the Troll is wearing fashionable"
		print "Plate Armor, with this is mind you decide that you deserve this armor more than the troll."
		print "\n"
		print "What are you going to do?"
		action = raw_input("> ")
		print "You try to %s but the Troll slaps you in the face and says 'You no take keystone'" % action
		print "oh well, looks like you will have to fight the Troll"
		combat("Troll")
		print "The Troll's lifeless body lays on the ground in front of you. Like a thug, you take the poor Troll's" 
		print "glorious Plate Armor and wear it. To your surprise you find pockets in your new armor and inside you find"
		print "the a Health Potion and the 'Left Keystone'."
		equiped_armor = "Plate Armor"
		inventory.append("Left Keystone")
		inventory.append("Potion")
		troll_alive = 0
		print "\n"
		print "Having successfully murdered a poor, innocent Troll you head back to the Dragon's Lair entrance."
		print "\n"
		raw_input("Press ENTER to continue")
		
	elif (("left" in action) or ("forrest" in action)) and troll_alive == 0:
		print "You have already killed that poor troll and stole all of his stuff, there is nothing left to do in the forrest"
		print "\n"
		raw_input("Press ENTER to continue")
		
	elif (("right" in action) or ("quarry" in action)) and ogre_alive == 1:
		print "You head down the path into a quarry, where you eventually the ENOURMOUS Ogre sitting in a river stream."
		print "Upon closer inspection you see the slight glimmer of the Right Keystone hanging from a necklace around"
		print "the Ogre's neck. Upon even closer inspection you see that the Ogre carries the lagendary frost sword"
		print "The Cold Poker. Upon even closer inspection still you realise the Ogre isn't sitting in the stream, it's squatting"
		print "down trying to clear its bowls from the mornings breakfast. The Ogre looks up at you surprised! in an instant,"
		print "The ogre pulls it's pants up and begins to charge at you."
		print "\n"
		raw_input("Press ENTER to continue")
		combat("Ogre")
		print "To your relief, the massive ogre finaly falls to the ground with loud a crash."
		print "A small health potion rolls out of the Ogre's torn pants, you pick up the potion"
		print "and put it in your pack. You take the Right Keystone from the Ogre's necklace and"
		print "pick up the legendary 'Cold Poker' before heading back to the Dragon's Lair entrance." 
		print "\n"
		ogre_alive = 0
		equiped_weapon = "Cold Poker"
		inventory.append("Right Keystone")
		inventory.append("Potion")
		raw_input("Press ENTER to continue")
		
	elif (("right" in action) or ("quarry" in action)) and ogre_alive == 0:
		print "The mighty Ogre has already been slain, the memory of that glorious victory still rings in your mind."
		print "\n"
		raw_input("Press ENTER to continue")
		
	elif "door" in action:
		print "at the center of the large door, there are two empty slots"
		print "above the two slots there is a sign that says 'insert keystones here'"
		print "\n"
		
		if ("Left Keystone" in inventory) and ("Right Keystone" in inventory):
			print "You place both Keystones into the slots."
			print "You hear a mechanism click and the Door opens, you enter the Dragon's Lair."
			print "\n"
			raw_input("Press ENTER to continue")
			inventory.remove("Left Keystone")
			inventory.remove("Right Keystone")
			boss_fight()
			loop = 0
			
		elif ("Left Keystone" in inventory) and not ("Right Keystone" in inventory):
			print "You place the 'Left Keystone' in one of the slots but nothing happens"
			print "Looks like you will need the Right Keystone too."
			print "\n"
			raw_input("Press ENTER key continue")
			
		elif ("Right Keystone" in inventory) and not ("Left Keystone" in inventory):
			print "You place the 'Right Keystone' in one of the slots but nothing happens"
			print "Looks like you will need the Left Keystone too."
			print "\n"
			raw_input("Press ENTER key continue")
			
		else:
			print "You push on the door but it won't budge, did you just ignore the"
			print "'insert keystones here' sign?"
			print "\n"
			raw_input("Press ENTER key continue")
			
	elif "stats" in action:
		stats()
	
	else:
		print "You attempt to %s but find that it is not helpful." % action 
		print "That dragon is'nt going to kill itself! hurry up and get killing!"
		print "\n"
		raw_input("Press ENTER key continue")
	
print "You head back to the village carrying the massive head of the Dragon on your"
print "back. As you walk off into the sunset you think about the great triumphs you"
print "had accomplished today but soon realise that your accomplishments today are"
print "nothing compared to what you will accomplish at the tavern tonight!!"
print "\n"
print " _____________________________________"
print "|                                     |"
print "|         Congratulations!            |" 
print "| Thank you for playing Dragon's Lair |"
print "|  (badly) Written by Nicholas Chai   |"
print "|_____________________________________|"
exit(0)