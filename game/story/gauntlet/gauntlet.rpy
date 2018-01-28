label gauntlet_start:
  scene church with fade
  P0 "If I recall the dragon's lair is located past this forest."
  H0 "Careful.  The forest is teeming with traps and dangerous beastmen that call it home."

  N0 "You start off on a steep cliff towering over a lush forest."

  #CLIFF
  menu:
    "Jump":
      P0 "Here goes!"
      N0 "[P0] jumps off the cliff looking for a soft place to land on."
      P0 "OH SHIIIIIIIIIII----------!! OOF!"
      N0 "*TWACK*"
      N0 "[P0] hits a branch jutting out from the cliff face and spirals out of control landing head first into the ground and dying immediately."
      jump reset
    "Climb":
      "[P0] climbs down safely."
      P0 "Whew, that was a lot higher than I thought!"

  #RIVER
  menu:
    "Swim":
      "DIE"
    "Cross":
      "DIE"

  #WILDBOAR
  #WOLF
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
