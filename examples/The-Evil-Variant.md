The evilvariant mode of SLEX tries to turn the game into the [[Evil Variant]] - that is, it implements some of the most evil patch ideas from the IRC, and some player-hostile features from other NetHack variants. Sometimes those are specifically made even worse than they are in their respective original variants.

It can be activated by adding the following line to the configuration file:

<code>OPTIONS=hybridevilvariant</code>

Here's a list of changes that are enabled by picking the evilvariant (hybrid) race (probably incomplete):

* Free action and discount action can't be active at the same time. If the player has free action, they cannot have discount action.
* Certain materials, including silver and dragonhide, are susceptible to (more) forms of erosion.
* Item destruction (fire, cold, shock, and the side effect of fire that causes armor worn by the player to gradually burn) is much harsher.
* Lighting a cursed light source causes the player to burn their finger and take a little bit of damage.
* Rubbing an object now requires the player character to have hands.
* Cheating at Sokoban increases divine anger by one every time the player does it.
* The mysterious force is back, and worse than ever - it may instantly bump the player back all the way to the Vibrating Square level no matter how far they've already ascended.
* Cannibalism increases divine anger by one every time the player commits it.
* Ragnarok can instakill the player and their pets.
* Eating slimy, oily, wobbly, jelly etc. corpses will give temporary slippery hands.
* Even if a corpse eaten by the player is tainted, it will take the full time to eat it and the player can't forcibly interrupt it (from [[Grunthack]]).
* Engraving is impossible while the player is held by a monster.
* The first instance of "Elbereth" in a string the player is trying to engrave will always misengrave, so you need to either write "Elbe" then "reth" or "ElberethElbereth", and both of these will require two turns to complete before you can have a fully working engraving.
* The player doesn't gain alignment for killing monsters (from [[Nethack Fourk]]).
* Being engulfed by a monster often afflicts the player with the confusion status effect in addition to whatever the engulfing attack normally does.
* All Z-class monsters possess an additional sickness-inducing melee attack, and all M-class monsters possess an additional itemcursing melee attack.
* If a monster steals items from the player, there is no message indicating what the stolen item actually is.
* The "erase all data" artifact scroll will delete the player's data even if a monster reads it.
* Wands of slow monster zapped by monsters will afflict the player with long-lasting inertia (from [[FIQhack]]).
* If a monster zaps an elemental attack wand or plays an elemental damage horn, the player's items will be destroyed by the element in question, even if the actual beam didn't hit or was reflected. This is done to simulate the [[Wands Balance Patch|Wand Destruction Patch]].
* Armor pieces with magical properties won't display that they have such properties unless they are identified.
* If the player opens a cursed bag of holding, they aren't told what items have vanished, there's just a generic "Stuff has vanished" message.
* Gods are harder to mollify the angrier they are, i.e. the level that a sacrifice must have to have any chance of mollifying the gods is higher.
* All temple priests are [[elder priest]]s.
* Player characters whose intelligence is below 8 may screw up when reading a scroll and get the confused effect.
* The game says "Palim-Palim" and "Buh-Bye" instead of "Hello" and "Goodbye".
* If the player is level-drained and thereby loses proficiency in a skill, the skill point is not refunded but instead becomes lost forever.
* Players that are being strangled, polymorphed into a silent monster, lack a head, or are in a form that makes buzzing, burbling or gurgling sounds, are unable to cast spells.
* Level teleporters blind the player when triggered.
* Zapping teleport at monsters on no-teleport levels has no effect.
* If the player falls asleep, they crash into the floor and take damage.
* Chest and door traps are much nastier, causing a variety of detrimental effects when triggered.
* If the player's hands are unusable due to cursed items, zapping wands is not possible.
* A player who self-zaps a wand of make invisible only becomes invisible for a few turns.
* Inspired by Grunthack, player characters with low dexterity will fumble intermittently.
* Certain evil traps are more common.
* Engraving with a wand can cause it to break if the player's strength is at least 18. With higher strength it becomes more likely for this to happen.
* Being a barbarian or having at least 15 constitution can cause potions to not work when quaffed, with a 20% chance.
* Trying to melee a leprechaun and having it dodge causes a few turns of paralysis.
* Random bad effects have 100 times the usual chance of rolling data delete.
* When sacrificing, the burst of flame or flash of light can now negatively affect the player.
* The BOFH in the Mainframe has data delete attacks.
* Being disintegrated will still disintegrate the player's armor pieces even if the player is resistant.
