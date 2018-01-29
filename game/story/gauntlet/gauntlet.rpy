label gauntlet_start:
  scene bg forest with fade
  show bluebird at top
  play music "assets/bgm/fightagainst.mp3" fadeout 1.0 fadein 1.0

  p0 "If I recall the dragon's lair is located past this forest."
  b0 "Hey! Listen!  The forest is teeming with traps and dangerous creatures that call it home. Imimimimimimimi!"
  with flash
  p0 "Let's go!"

  #CLIFF
  n0 "You start off on a steep cliff towering over a lush forest and river."
  menu:
    "Jump towards trees":
      p0 "Here goes!"
      b0 "Fly like me! Imimimimimimimi!"
      n0 "You jump off the cliff looking for a soft place to land in the trees."
      p0 "OH SHIIIIIIIIIII----------!! OOF!"
      n0 "*TWACK*"
      with vpunch
      n0 "You hit a branch jutting out from the cliff face and spiral out of control landing head first into the ground."
      jump reset
    "Jump towards river":
      p0 "Here goes!"
      b0 "Fly like me! Imimimimimimimi!"
      n0 "You jump off the cliff heading towards the river."
      n0 "*SMACK*"
      with hpunch
      p0 "ARGHHH!"
      n0 "Hitting the water at your falling speed makes your body crumple as if you hitted solid concrete."
      jump reset
    "Climb down":
      "You climb down safely."
      p0 "Whew, that was a lot higher than I thought!"

  #RIVER
  n0 "A rapid river stands in your way as you look for a way across it.  You notice a fallen tree that forms a makeshift bridge over the river."
  b0 "Look at all those rocks being carried away by the river! Imimimimimimimi!"
  menu:
    "Swim across the river":
      n0 "The current quickly overpowers you as your helpless body batters against the rocks."
      b0 "Haha, you look like one of those rocks!  Imimimimimimimi!"
      jump reset
    "Cross using the tree bridge":
      n0 "You quickly scamper across the tree bridge before you lose your balance."
      p0 "Whew!"

  #MATH
  n0 "You are greeted on the other side by a ferocious math problen!"
  n0 "What is the answer for 1 + 1?"
  menu:
    "1":
      n0 "You die immediately from your incorrect answer."
      jump reset
    "2":
      n0 "The number grunts acknowledgingly and lets you pass."
    "3":
      n0 "You die immediately from your incorrect answer."
      jump reset
    "H":
      n0 "You die immediately from your incorrect answer."
      jump reset
    "Dog":
      n0 "You die immediately from your incorrect answer."
      jump reset

  #TIDEPOD
  n0 "A wild tidepod appears right before you on the ground."
  b0 "I haven't seen that before.  Imimimimimimimi!"
  menu:
    "Pick it up and eat it":
      p0 "This looks edible..."
      n0 "You gag as your stomach feels queasy from eating the tidepod."
      p0 "HURK..."
      n0 "You foam at the mouth as the poison slowly seeps thru your system."
      jump reset
    "Ignore it":
      n0 "You quickly walk past it."

  #WOLF
  n0 "A wild wolf stops you in your tracks as it eyes you maliciously."
  b0 "Uh oh. Not sure if you avoid this one! Imimimimimimimi!"
  menu:
    "Punch it":
      n0 "You attempt to punch it as it drags you down and bites into your neck"
      p0 "Gyaaaa-"
      jump reset
    "Howl at it":
      n0 "You attempt to howl at it to confuse it."
      p0 "AWOOOOOOOOO!"
      n0 "It howls back at you."
      n0 "Moments later more wolves appear and surround you for an easy meal."
      jump reset
    "Cast magic missile":
      p0 "MAGIC MISSILE!"
      n0 "The spell flies and obliterates the wolf."
      n0 "BAM!"
      with hpunch
      p0 "YES!"
      b0 "Nice shot! Imimimimimimimi!"
    "Run away!":
      n0 "You attempt to run away as it tackles you and bites into your neck"
      p0 "Gyaaaa-"
      jump reset

  #DROPBEAR
  n0 "Looking up you see a dropbear menacingly looking at you."
  b0 "Careful! Imimimimimimimi!"
  menu:
    "Cast magic missile":
      p0 "Take this!"
      with flash
      "Dropbear" "SKREEEE!"
      n0 "Drop bear pieces rain down."
    "Ignore it":
      n0 "You try to ignore it, but it jumps on you and eviscerates your face"
      with vpunch
      p0 "GYAAA!"
      jump reset

  #FLYING_UNDERWEAR
  n0 "A piece of underwear floats around in the air."
  b0 "How did that get here? Imimimimimimimi!"
  menu:
    "Inspect it":
      n0 "You get closer to inspect it."
      p0 "It looks like a..."
      n0 "Before you can finish your sentence, the mimic underwear wraps around your head and starts strangling you."
      p0 "MmMmmph!!!"
      jump reset
    "Dodge it":
      n0 "You circle around it."

  #BANANA_PEEL
  b0 "Watch out! A banana peel! Imimimimimimimi!"
  p0 "It can't be that bad."
  menu:
    "Kick it":
      n0 "You kick the banana peel away into the bushes."
    "Ignore it":
      n0 "You ignore the banana peel and walk past it."
      n0 "The trap activates and the {b}HOMING{/b} banana peel slips right under your feet."
      p0 "Whaaa-"
      n0 "You slip violently and crack your head open."
      jump reset

  #GAZEBO_OF_DOOM
  b0 "What's that? Imimimimimimimi!"
  n0 "A gazebo stands out in the open in the middle of nowhere."
  p0 "That's odd..."
  menu:
    "Cast magic missile":
      n0 "You cast magic missile at the gazebo."
      n0 "ROAAAAAAAAAAAR"
      p0 "Wha-WHAT?!"
      n0 "The gazebo roars to life and eats you."
      jump reset
    "Take a short rest":
      p0 "I guess it's important to rest when I get the chance."
      n0 "You take a seat inside the gazebo."
      n0 "ROAAAAAAAAAAAR"
      p0 "Wha-WHAT?!"
      n0 "The gazebo roars to life and eats you."
      jump reset
    "Ignore it":
      n0 "You quickly walk past it without a thought."

  #CLOWN
  n0 "A sad clown jumps out from the trees."
  p0 "Uwaa!"
  b0 "Why was he there?! Imimimimimimimi!"
  menu:
    "Punch it":
      n0 "*THWACK*"
      n0 "The clown gets angry and rips you into two."
      jump reset
    "Laugh at it":
      n0 "You laugh at it for some reason."
      n0 "The sad clown smiles and walks away while waving his hand."

  #TREASURE_CHEST
  p0 "Hey, there's a chest here."
  menu:
    "Open it":
      n0 "You approach the chest and it roars as it turns out to be a mimic!"
      "Mimic" "GAOOOOOO!"
      n0 "The mimic chomps off half of your body as you scream in horror"
      p0 "KYaaaaaaaa!"
      jump reset
    "Ignore it":
      n0 "Despite the temptation, you ignore it and continue on."

  #POTION
  n0 "Your foot taps on a potion lying on the ground."
  b0 "Maybe it'll do something if you drink it! Imimimimimimimi!"
  menu:
    "Drink it quickly":
      n0 "You pick it up and drink it"
      p0 "AGHHH!"
      n0 "The potion works quickly as you turn into a cat."
      with flash
      p0 "Meowwww."
      b0 "It did do something! Imimimimimimimi!"
      jump reset
    "Examine it":
      n0 "You notice the label and read it"
      p0 "Cat transformation potion."
      b0 "It does do something! Imimimimimimimi!"
      p0 "No thank you."
      n0 "You continue on your journey."

  #KNIFE
  n0 "Your feet snags onto something and a sparkle catches the side of your eye."
  b0 "Dodge! Imimimimimimimi!"
  menu:
    "Jump to the side":
      p0 "AHH!"
      with vpunch
    "Duck down":
      p0 "AHH!"
      with vpunch
    "Jump up":
      p0 "AHH!"
      n0 "A knife comes flying out out of nowhere and pierces your heart."
      p0 "Ughhh..."
      n0 "You crash down as the world fades around you."
      jump reset

  n0 "A knife flies past you as it hits a tree."
  p0 "Whew..."

  #MIME
  n0 "You encounter a vicious mime."
  b0 "They like to copycat stuff! Imimimimimimimi!"
  menu:
    "Cast magic missile":
      n0 "You start to cast magic missile at it as the mime copies you."
      n0 "Unfortunately the mime is better than you and its spell is mcuh stronger than yours."
      n0 "Your pitiful missile is overpowered as your body shatters in pieces from the missile's impact."
      "Mime" "..."
      jump reset
    "Run away":
      n0 "You make a run for it and the mime also retreats."

  #BOMB
  n0 "A lit bomb is thrown right next to you."
  p0 "AHH!"
  menu: 
    "Kick it away":
      n0 "With amazing speed you kick the bomb and it flies into a hole."
      n0 "{b}BOOOOOOOM!{/b}"
      b0 "That was some quick thinking! Imimimimimimimi!"
    "Pick it up":
      n0 "You pick it up and it blows up in your face immediately!"
      n0 "{b}BOOOOOOOM!{/b}"
      jump reset

  #CAT
  b0 "Look at that cute cat! Imimimimimimimi!"
  "Cat" "Meow."
  menu:
    "Pet cat":
      n0 "You pet the cat."
      p0 "Nice kitty."
      "Cat" "Purr..."
    "Ignore cat":
      n0 "The cat ignores you as well."

  #DRUNK
  n0 "A seemingly harmless drunk hobbles on the side of the road."
  menu:
    "Take their keys":
      n0 "You mob the drunk and take their keys."
      p0 "No drinking and driving!"
      n0 "The man passes out on the side as you continue onward."
    "Ingore it":
      n0 "You ignore the drunk as you continue onward."
      n0 "Moments later you hear the screech of tires as you watch an out of control car collide into you."
      n0 "Your mangled body flies into the air."
      jump reset

  jump dragon_start
  return
