This page is supposed to be a rudimentary version history of [[Slash'EM Extended]]. Unfortunately there is no exact date/version number associated with most of these features; the ones at the top of this list are from recent versions, while the ones at the bottom have been there for a long time already. This list also isn't complete. You should refer to history2.txt in the repo instead.

* Angering a god will summon hostile Kops and Sephiroth, and there's also a higher chance of receiving a smite.
* Neutral god minions have been beefed up; they were too weak.
* Eating a nymph conveys a 10% chance of a charisma boost (similar to mind flayers increasing intelligence when eaten).
* Added a "withering" effect that can damage the player's items even if they are damageproof or outright immune to damage. The player can be subjected to this by enemy spellcasters, coming into contact with lethe waters, or enemies with the new AD_WTHR attack.
* Incorporated the "detect foot" spell from SporkHack, and actually made it into something useful. Yes, Demogorgon isn't immune to its effect.
* Golden and stone dragons can leave scales, which can be made into dragon scale mail. The golden scales grant sickness resistance while stone scales (obviously) give petrification resistance.
* Half physical/spell damage only works 50% of the time, so it's more like "25% resistance to physical/spell damage". The Hand of Vecna now only gives its powerful effects when wielded.
* Throwing the potion of amnesia at Medusa, Croesus, a rider or a quest nemesis actually has an effect other than just generating a funny message. For example, throwing it at Death will level-drain him. Also, thrown potions and eggs of all kinds are much more likely to hit a monster.
* Abusing attributes is more likely to result in a reduction if the attribute in question is higher (it used to be the other way round).
* Luckstones only give +1 luck if noncursed and +2 if blessed; they can stack, but the maximum luck bonus is still +3.
* A player leaving bones will have all contents of their containers removed to ensure that the bones pile's finder is less likely to receive tons of powerful items.
* The alignment quest keys can no longer be used as unbreakable keys to open any random lock; they only fit in their respective artifact doors in Vlad's tower.
* Enemies using wands will be more dangerous later in the game. There is also more randomness in the amount of charges a wand has upon being generated, and sometimes wands will have been recharged already.
* Gems thrown to unicorns give a smaller luck boost.
* Rings can be enchanted past +7. They're still very likely to explode, but they don't always do so.
* Objects in a bones pile are much less likely to keep their blessed status if they were blessed to begin with.
* Bones file ghosts are more similar to DCSS ghosts - read: they will usually be hostile versions of the previous player character, able to use most of the items in the bones pile.
* If a monster grows up, the player will get a notification message.
* The experience table has been redone; the first level up comes at 20 XP, and the gap between level ups has been fixed too.
* Touching a cockatrice egg with an exposed body part will slowly turn the player to stone.
* Room generation in standard rooms-and-corridors levels has been enhanced to allow special features in special rooms. For example, there may be traps in a shop, or a fountain in a vault. Rooms may also be overgrown with trees, or have some pools, iron bars etc. Also implemented the Sporkhack code that randomly replaces walls with iron bars.
* Mimics can take on more types of appearance, including water, lava, thrones, altars, fountains etc.
* Iron balls and chains always use the flail skill, even if the player isn't a Convict.
* The ruffled shirt and victorian underwear can lifesave a player if cursed. Nobles and the planned Activistor role can choose to curse them on purpose.
* Added scrolls of healing and standard id. The player starts with some of these.
* Elbereth squares have a small chance to affect @ and A, as long as they aren't unique monsters.
* Added the traproom and poolroom special room types from Sporkhack, and a new grueroom that automatically gets dark when the player enters for the first time.
* Added a wand of summon undead. Monsters may use this to fill the level with undead monsters.
* Added a scroll of lockout that can turn dug-out corridors back into walls. They can also be used by monsters.
* All monsters can use musable items like wands of death and potions of gain level. Yes, this includes killer bees, newts and lichens. Fear the LWTWOD - lichen with a wand of death! :D
* Breath weapons appear as a random type if the player is hallucinating.
* Added a solar beam type of ray that can be used by spellcasting/breathing monsters with AD_LITE.
* A player character named "Gehenna" (without quotes) cannot pray, and certain other mechanisms are changed to behave like the player is in the Gehennom, even if they are not.
* All concealed monsters get an item to hide under, even if they are spawned after a level has already been created. For example, if an enemy priest casts sticks to snakes.
* A player character named "IWBTG" (without quotes) will die as soon as they take damage. They can use the #jump command and will get a funny message if that lands on a square containing any kind of sword.
* Added new monster types with new glyphs: nemese, archfiend, grue, rub monster and wall monster.
* Added a wand of charging that works similarly to an uncursed scroll. It can only be recharged once though.
* There's an AD_NGRA attack type for monsters that removes Elbereth engravings from underneath the player.
* Enhancing a spellcasting skill to Skilled or Expert will increase the player's mana regeneration rate.
* The player's health regeneration will go up if the riding skill is enhanced to Skilled or Expert.
* Added ADOM tension rooms that are filled with monsters of one randomly determined type.
* A "permanent" Elbereth square is no longer truly permanent; there is a very small chance for it to be eroded.
* The artifact naming bug/exploit has been removed.
* The player is more likely to move in the intended direction while confused/stunned.
* An exploding bag of holding scatters its contents rather than simply deleting all of it (from Unnethack).
* Eating a banana cures hallucination, melons cure confusion, pears cure stun, and asian pears cure both confusion and stun.
* Some throwing weapons that weren't stackable (knives for example) can now be stacked, and some that couldn't be multishot can now.
* Engulfing monsters have a chance to miss the player.
* Every item that gets generated may be cursed, blessed and/or have a random enchantment. This includes horns obtained from killing a unicorn, for example; they used to be uncursed +0 every time.
* Newt corpses can give a boost to maximum mana even if the player's current mana isn't full.
* Monsters have a higher chance to hit the player with thrown weapons and missiles fired from a launcher.
* More variation for random monster spawns; their minimum level is always 1, even at sanctum depth, and their maximum level will rarely be higher than the actual level difficulty.
* The player may name their character "lostsoul" (without the quotes) to start at Medusa depth on the upstairs.
* Any water tile that gets generated on loading a level has a small chance to inhabit a random sea monster.
* Eels and other sea monsters can spawn randomly and don't lose health while on dry land. This ability doesn't extend to players polymorphed into one, though.
* Monsters growing on old corpses can also be puddings, blobs and jellies now.
* Resistances are really resistances instead of immunities, at least for the player; in most cases there is still a slight chance for the player to take damage from something they are resistant to. Reflection also has a small chance to fail.
* The wand of digging does less damage to monsters that engulf the player. No longer can Jubilex be killed in a single hit.
* Monsters have an increased chance of suffering system shock when stepping on a polymorph trap. There is also a small chance that the trap is removed.
* Unicorn horns need to be enchanted to +15 in order to get their maximum chance of working; every point of enchantment up to +15 makes it work a little better. They still can't reliably enchanted beyond +7 though, so the player has to get very lucky and randomly find a higher enchanted one or hope the enchant weapon scroll doesn't destroy it.
* Dropping stuff on an altar may cause it to vanish. The same is true if the player otherwise interacts with an altar very often; this has been done to reduce the ability to do altar-farming.
* Purple worms are much less likely to instakill other monsters.
* Added the Noble and Pirate roles (thanks Chris for making them).
* Implemented many of the Lethe patch's special levels. They can appear in the Gehennom, and obviously have lethe waters.
* There are shambling horrors (from Spork/Unnethack) that get randomly generated attributes at the start of the game.
* Item-stealing monsters are more likely to succeed if the player character is of the other gender.
* Applying a polearm carries a small chance to break it. If the polearm is an artifact, chances of breakage are greatly reduced.
* The ability to endlessly farm items with fishing poles has been removed.
* Restful sleep goes off less frequently.
* Cockatrices no longer instantly petrify the player on touch. The same is true for Medusa's gaze attack.
* Sacrificing is less likely to grant gifts or other good things.
* The Book of the Dead can be read while blind.
* Eating a tainted corpse can give intrinsics and other benefits associated with it, in addition to the usual food poisoning.
* Special levels (including Minetown, Sokoban, the demon lairs etc.) have a chance to not be present in a given game. "Important" ones (Minetown definitely is one of those) are very likely to get generated though.
* Invoking an artifact yields a much longer timeout.
* Gremlins can steal intrinsics whenever they want; it doesn't have to be night. Also made sure other monsters with AD_CURS can steal intrinsics, too.
* Lycanthropy is less annoying: the player will auto-polymorph a lot less often. Unfortunately the lycanthrope race still sucks.
* More characters will receive gauntlet-like messages when low on food or about to die.
* Many instadeaths are a lot less likely and/or toned down. This is valid for poison attacks/spikes, wand/touch/finger/whatever of death, drowning attacks, disintegration etc. The player might actually survive without poison/magic resistance.
* A --More-- prompt will often appear if the player tried to do an action that usually prompts for a direction, if for whatever reason the player doesn't actually get to choose one. Example: use "o" to open a door, usually you expect to choose a direction - how many times did you bump into the door after getting told that your polymorph form doesn't have hands? In my case the answer is TOO MANY TIMES!!! It is my mission to eradicate all those interface screws off the face of the Dungeons of Doom, as harsh as that may sound. If you still find an action that usually gives a direction but doesn't give a --More-- prompt if it fails, please by all means tell me what it is so I can fix it!
* Tins created by the player can have szechuan, sauteed etc. food in them (used to always be homemade or rotten).
* Alignment penalties for doing things like attacking fleeing monsters as a Knight have been increased.

There are many more features that make Slash'EM Extended unique, though; probably too many to list them all... Refer to the main [[Slash'EM Extended]] page to see an overview of the important ones. --[[User:Bluescreenofdeath|Bluescreenofdeath]] ([[User talk:Bluescreenofdeath|talk]]) 09:46, 6 June 2014 (UTC)
