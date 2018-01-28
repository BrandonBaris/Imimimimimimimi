label gauntlet_start:
  scene church with fade
  play music "assets/bgm/fightagainst.mp3" fadeout 1.0 fadein 1.0

  p0 "If I recall the dragon's lair is located past this forest."
  b0 "Hey! Listen!  The forest is teeming with traps and dangerous creatures that call it home."
  with flash
  p0 "Let's go!"

  #CLIFF
  n0 "You start off on a steep cliff towering over a lush forest and river."
  menu:
    "Jump towards trees":
      p0 "Here goes!"
      b0 "Fly like me!"
      n0 "You jump off the cliff looking for a soft place to land in the trees."
      p0 "OH SHIIIIIIIIIII----------!! OOF!"
      n0 "*TWACK*"
      with vpunch
      n0 "You hit a branch jutting out from the cliff face and spiral out of control landing head first into the ground."
      jump reset
    "Jump towards river":
      p0 "Here goes!"
      b0 "Fly like me!"
      n0 "You jump off the cliff heading towards the river."
      n0 "*SMACK*"
      with hpunch
      p0 "ARGHHH!"
      n0 "Hitting the water at your falling speed makes your body crumple as if you hitted solid concrete."
      jump reset
    "Climb":
      "You climb down safely."
      p0 "Whew, that was a lot higher than I thought!"

  #RIVER
  n0 "A rapid river stands in your way as you look for a way across it.  You notice a fallen tree that forms a makeshift bridge over the river."
  b0 "Look at all those rocks being carried away by the river!"
  menu:
    "Swim across the river":
      n0 "The current quickly overpowers you as your helpless body batters against the rocks."
      b0 "Haha, you look like one of those rocks!"
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
  b0 "I haven't seen that before."
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
  b0 "Uh oh. Not sure if you avoid this one!"
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
      b0 "Nice shot!"
    "Run away!":
      n0 "You attempt to run away as it tackles you and bites into your neck"
      p0 "Gyaaaa-"
      jump reset

  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  #PLACEHOLDER
  return
