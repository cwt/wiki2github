This is for the SLASH'EM Extended rcfile, in case players want to change what the dungeon looks like. First, this line is required:

<pre>OPTIONS=IBMgraphics</pre>

'''The following applies to version 2.0.5 and later - for older versions please scroll down'''

Then, the following part '''MUST be put at the end of your rcfile''' or it will not work correctly. The last line makes solid rock be displayed as the # glyph:

 DUNGEON = 032 179 196 218 191 192 217 197 193 194 \
            180 195 035 035 035 250 254 254 043 043 \
            241 241 035 035 250 250 177 177 060 062 \
            060 062 095 124 092 244 244 244 247 250 \
            247 250 250 035 035 096 096 035 247 035 \
            247 247 247 247 247 244 244 092 092 124 \
            124 250 250 250 250 250 250 250 096 250 \
            096 096 124 124 035

If you want to get rid of the # glyph for solid rock, use the following one instead (remember to put it at the end of your rcfile or it might not work right):

 DUNGEON = 032 179 196 218 191 192 217 197 193 194 \
            180 195 035 035 035 250 254 254 043 043 \
            241 241 035 035 250 250 177 177 060 062 \
            060 062 095 124 092 244 244 244 247 250 \
            247 250 250 035 035 096 096 032 247 035 \
            247 247 247 247 247 244 244 092 092 124 \
            124 250 250 250 250 250 250 250 096 250 \
            096 096 124 124 035

Symbol explanation for customization follows below.

<pre>
unexplored area = 032 (blank space)
vertical wall, horizontal wall = 179, 196
four types of corners = 218, 191, 192, 217
crosswall = 197
four more types of wall, ending with "trwall" = 193, 194, 180, 195
rock wall, grave wall, tunnel wall = 035 (hash)
doorway = 250 (dot)
open door x2 = 254 (filled square)
closed door x2 = 043 (plus, same as spellbook symbol)
iron bars and tree = 241 (plus-minus)
farmland and mountain = 035 (hash)
floor and dark part of a room = 250
dark corridor and lit corridor = 177
staircase up and down = 060 and 062 (smaller than and greater than)
ladder up and down = 060 and 062
altar = 095 (underscore)
grave = 124 (pipe)
throne = 092 (backslash)
sink, toilet, fountain = 244 (pilcrow)
water = 247, ice = 250, lava = 247
lowered drawbridges x2 (vertical and horizontal) = 250
raised drawbridges x2 (vertical and horizontal) = 035
air and cloud = 096 (apostrophe)
solid rock = 035 (CHANGE THIS TO 032 TO DISABLE)
underwater glyph = 247
water tunnel = 035
crystal water, moorland, urine lake, shifting sand, styx river = 247
well, poisoned well = 244
wagon, burning wagon = 092
wooden table, straw mattress = 124
snow, ash, sand, paved floor, highway, grass, nether mist = 250
stalactite = 096
cryptfloor = 250
bubbles, rain cloud = 096
pentagram, carved bed = 124
grayout glyph = 035
</pre>

For versions older than 2.0.5, use this instead:

 DUNGEON = 032 179 196 218 191 192 217 197 193 194 \
            180 195 250 254 254 043 043 035 035 250 \
            250 177 177 060 062 060 062 095 124 092 \
            244 244 244 247 250 247 250 250 035 035 \
            096 096 035 247 035

If you want to get rid of the # glyph for solid rock, use the following one instead (remember to put it at the end of your rcfile or it might not work right):

 DUNGEON = 032 179 196 218 191 192 217 197 193 194 \
            180 195 250 254 254 043 043 035 035 250 \
            250 177 177 060 062 060 062 095 124 092 \
            244 244 244 247 250 247 250 250 035 035 \
            096 096 032 247 035
