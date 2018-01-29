label reset:
  scene bg bgblack with fade
  play music "assets/bgm/longway.mp3" fadeout 1.0 fadein 1.0
  n1 "{color=#f20}YOU DIED{/color}"
  with dissolve
  n0 "Restarting game..."
  with fade
  n1 "5"
  with flash
  n1 "4"
  with flash
  n1 "3"
  with flash
  n1 "2"
  with flash
  n1 "1"
  with flash
  n1 "Complete"
  # jump dragon_start
  # jump gauntlet_start
  jump reset_start

label finale:
  scene bg bgblack with fade
  python:
    p0 = renpy.input("Enter your name.")
    p0 = p0.strip()

    if not p0:
      p0 = "Ash"

  play music "assets/bgm/longway.mp3" fadeout 1.0 fadein 1.0
  n0 "*BEEP BEEP*"
  with flash
  b0 "You have a call!"
  p0 "Ah! It's from Ryder."
  r0 "[p0]? [p0]!"
  p0 "I'm here! I'm glad to hear from you!"
  r0 "[p0]! Are you alright?"
  p0 "I just barely made it.  I heard about my situation.  What's the progress on that?"
  r0 "Listen to me carefully [p0].  It's about Lily."
  p0 "Huh? Isn't she supposed to be helping you?  She even made this assistant to help me thru the game."
  r0 "No [p0].{w} Lily's...{w} dead."
  p0 "Wha..."
  r0 "Something...{w} something wrong happened with her dive unit.{w}  Maybe some bad calibration or something that we're still investigating, but that huge critical failure caused a sensory overload that her body could not handle."
  p0 "She died..."
  r0 "That's not all of it..."
  r0 "Her mind is still connected into the game.  The shock of her body dying has made her go insane."
  p0 "Wait... what?!"
  scene bg lilywhite01 with vpunch
  scene bg bgblack with fade
  r0 "She's haunting you [p0].  She does not want to be alone so she has been corrupting the game's code to keep you inside and has been blocking attempts at communications."
  r0 "We tracked your progress and managed to find a window where we can hack into and contact you [p0]."
  p0 "What do I do?!"
  scene bg lilywhite02 with flash
  scene bg bgblack with fade
  r0 "Hang in there! We'll try to find a way to rescue you. Stay aware and watch out for her!"
  n0 "*bzzkt*"
  with vpunch
  scene bg lilyblack01 with flash
  scene bg bgblack with fade
  p0 "It's getting hard to breath..."
  n0 "...Imimi..."
  r0 "...what's that? I can't hear *bzkkk*{w} ...hear you...{w} some kind of interference..."
  scene bg lilyblack02 with flash
  scene bg bgblack with fade
  p0 "Urkkk.."
  with hpunch
  r0 "No wa--!"
  with flash
  n0 "Imimimmimi..."
  with hpunch
  n0 "Only an eerie sound fills your hearing."
  n0 "A sound you have noticed was buzzing all this time."
  with flash
  n0 "...Imimimimimimimi..."
  scene bg lilyblack03 with fade
  scene bg bgblack with fade
  n1 "{color=#f20}YOU DIED{/color}"
  with fade
  n0 "Restarting game..."
  with fade
  n0 "5"
  with fade
  n0 "4"
  with fade
  n0 "3"
  with fade
  n0 "2"
  with fade
  n0 "1"
  with fade
  scene bg endsplash with longfade
  n0 "THE END"
return
