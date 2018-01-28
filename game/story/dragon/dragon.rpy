label dragon_start:
  scene bg church with fade
  play music "assets/bgm/primal.mp3" fadeout 1.0 fadein 1.0
  n0 "Finally you arrive at the lair of the dragon as the dragon rises up from its lethargy as it notices your presence."
  p0 "Here goes nothing..."
  n0 "The dragon roars as it pulls back its head with flames bellowing as it prepares for a breath attack."
  with vpunch
  b0 "Watch out!"

  menu:
    "Dodge roll to the side":
      n0 "You jumps to the side, but the gap closed is nowhere enough to dodge the immense fireball the dragon breathes out."
      with hpunch
      p0 "ARHGHHH!"
      with hpunch
      jump reset
    "Dodge behind a huge rock":
      n0 "You jump behind a huge rock as the torrent of fire surges and blasts against the rock's protective cover."
      with hpunch
    "Throw the peace sign":
      n0 "You make your hand into a peace sign trying to bring a peaceful resolution."
      with flash
      n0 "The dragon quickly has a very peaceful dinner with your roasted remains."
      jump reset
    "Curse at it":
      n0 "Summoning all your might, you unlease verbal abuse at the dragon."
      p0 "!@#&&&#!@@&!&!#&! Fight me you ****** dragon!"
      n0 "The fire blast promptly roasts you."
      with flash
      p0 "ARHGHGHHHHHH!"
      jump reset

  d0 "GROARRRR!!"
  n0 "The dragon roars as it jumps into the air searching for you."
  b0 "You need to do something to ground it!"

  menu:
    "Cast magic missile at the dragon":
      n0 "You aim for the dragon and launches a magic missile at the dragon!"
      d0 "GRAAAAAAA!"
      with hpunch
      n0 "The spell lands cleanly, but it seems too weak to have any effect on the dragon."
      with flash
      n0 "The dragon retaliates by launching a salvo of fireballs that rain from above."
      with flash
      p0 "AGHHHH"
      with hpunch
      n0 "With no cover to to shield from above, You burns in the raining inferno."
      jump reset
    "Cast magic missile at the spiky ceiling":
      n0 "You cast magic missile at the spiky ceiling."
      with flash
      n0 "BOOM!"
      with vpunch
      n0 "The spell explodes as large rock debris rain down from the ceiling and impales the dragon's wings."
      d0 "GRAARRRRR"
      n0 "The dragon growls in pain as the weight of the rocks sends it careening to the ground."
      with vpunch
    "Cast magic shield":
      n0 "You set up a magic shield as the dragon launches a fireball salvo from above."
      n0 "The fireballs rain down as it hammers against the magic shield"
      with flash
      with vpunch
      p0 "Ughh.  I can't hold out much longer...."
      p0 "AHHHHHH!"
      with flash
      n0 "The fireballs quickly overwhelm the shield and incinerate You."
      jump reset

  n0 "The beast winces as it is pummeled by the huge rocks."

  menu:
    "Cast magic missile at it":
      n0 "The missile hits the dragon in its weakened state and it reels in pain screeching loudly"
      with flash
      d0 "REEEEEEEEE!"
      with hpunch
      n0 "Unfortunately rocks are falling all over the place and one squishes you."
      with vpunch
      jump reset
    "Talk smack":
      n0 "You gloat at the dragon from your ingenius move that took it down."
      p0 "Haha! Stupid! Stupid!"
      n0 "Too bad rocks are still falling and one turns you into a pancake."
      with vpunch
      jump reset
    "Run up to it and hit it with your sword":
      p0 "Now is my chance!"
      n0 "You make a dash with your sword out to the dragon."
      n0 "In its pain, the dragon lashes out at you with its claw in desperation and gashes your stomach open."
      with vpunch
      p0 "Ughhhhh"
      n0 "You fall down in pain as your guts spill on the floor...{w} then a rock falls on you."
      with vpunch
      jump reset
    "Run away":
      n0 "You run away from the dragon as you attempt to dodge the rocks that are still raining down from the ceiling."
      p0 "Gyaaaaaa!"
      n0 "A small crevice on the ground is nearby and you jump in to hopefully avoid being hit."

  n0 "The barrage of rocks quiet down as you peek out from your hiding spot."
  n0 "The dragon grunts as it is pinned down by the heavy debris."
  p0 "now is my chance!"
  
  menu:
    "Cast magic missile at it":
      n0 "The missile hits the dragon in its weakened state and it reels in pain screeching loudly"
      with flash
      d0 "REEEEEEEEE!"
      with hpunch
      n0 "It's super effective!"
    "Run up to it and hit it with your sword":
      p0 "Take this dragon!"
      n0 "You make a dash with your sword out to the dragon."
      n0 "In its pain, the dragon lashes out at you with its claw in desperation and gashes your stomach open."
      with vpunch
      p0 "Ughhhhh"
      n0 "You fall down in pain as your guts spill on the floor."
    "Gloat at it":
      p0 "Hahahaha! Stupid dragon! You're not all that great!"
      d0 "Grrr..."
      n0 "The dragon sneers at you in anger and musters its strength to spit at a fireball."
      p0 "AHHH!"
      n0 "It catches you off guard and sears the flesh off you instantly as you scream in pain and collapse on the ground on fire."
      with flash
      d0 "Get rekt."
      jump reset

  n0 "The dragon slumps to the ground from the spell."
  n0 "Its breath is labored as it lays on the ground vulnerable."

  menu:
    "Run up to it and stab it with your sword":
      p0 "Time for the deathblow! RAAH!!"
      n0 "You run with sword thru the dragon's chest into its heart"
      d0 "Gyaaaaooo--"
      n0 "The dragon lets out a rumbling sound as it is finally defeated."
    "Laugh at it":
      p0 "AHAHAHAHAHA!"
      n0 "You laugh in triumph."
      p0 "AHAHAHAHAHA!"
      n0 "Amazed at your incredible feat you laugh for an unusual amount of time."
      n0 "Mustering the last of its strength, the dragon spits are a fireball into your open, laughing mouth."
      n0 "It sears your internal organs in a flash and you collapse to the ground in pain as you die a horrible death."
      with hpunch
      jump reset

  n0 "The dust settles as you stare dragon's lifeless body making sure it is finally dead."
  p0 "Wooooooooo! I finally defeated the dragon!"
  p0 "Now I can finally see if I can get out of here!"
  n0 "Your surroundings fade away as you are returned to the loading lobby of the game."
  jump finale

return