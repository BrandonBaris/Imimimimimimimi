label start:
    scene bg bgblack with dissolve
    play music "assets/bgm/newday.mp3" fadeout 1.0 fadein 1.0
    n0 "System initialized..."
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
    with longfade

    python:
        p0 = renpy.input("Enter your name.")
        p0 = p0.strip()

        if not p0:
            p0 = "Ash"

    n0 "Player name accepted."
    n0 "Welcome [p0]."
    n0 "Starting up world..."

    scene bg temple with fade
    p0 "Where am I?"
    l0 "It's about time you synced up! Wake up!"
    with hpunch
    p0 "Is that you Lily?"
    "Your colleague Lily relentlessly jabs you in the side as you groggily wake up after syncing up into the game."
    l0 "Wake up! We have a lot of testing to do on this run!"
    with hpunch
    p0 "I'm up! I'm up!"
    "For being in a virtual world, the pain from her sharp jabs still feels so real."
    r0 "I see sleeping beauty finally synced up."
    "Your other colleague, Ryder, chimes in from the global communications channel."
    l0 "First on the list is testing the upgraded battle system."
    r0 "I'll spawn a random monster for you two to fight.  Make sure to get used your virtual bodies."
    "You all belong to a company developing a virtual dive system that allows a user to experience a total gaming experience that uses all senses of the body."
    "It uses techniques that sends signals to the brain directly to simulate senses we would feel in the normal world."
    "The technology is new, but it shows promise as the results have been stellar.  Never have you experienced another reality that felt so real."
    l0 "Can't wait to try out this magic system and blow up some enemies!"
    "Lily readies her staff in anticipation.  Being a genius programmer, she was recently chosen to be part of the dive team to adapt to changes on the fly."
    r0 "Hold on.  The spawning is taking some time..."
    "Ryder today is serving as the game master to watch over today's testing.  He is one of your most trusted friends in the company."
    "You wait for him to spawn the monster as you fiddle around with your equipment.  Being part of the main testing team have the most experience when it came to virtual diving."
    r0 "There we go! Here comes the monster. Get ready!"
    "Ryder notifies you two as the monster begins to form in front of you."
    l0 "That... that's a pretty huge form than usual don't you think?"
    p0 "You're right..."
    "The monster form appearing is not the usual size you have tested with."
    "It continues to grow in height to a two story building and scales start to appear on its surface."
    p0 "It's a dragon!  That's the toughest monster we created in the game!  There's no way we can clear that by ourselves!"
    play music "assets/bgm/primal.mp3" fadeout 1.0 fadein 1.0
    l0 "What?!"
    p0 "Run away!"
    "You signal to Lily to retreat before the monster completes spawning."
    r0 "Whoa! Whoa whoa whoa!  That wasn't supposed to be part of the random spawn list."
    "Ryder realizes what's going on and frantically starts trying to cancel the spawning."
    r0 "It's not letting me!"
    d0 "ROARRR!!"
    with vpunch
    "The dragon completes its spawning and immediately starts to aggressively attack any players like it was designed to do."
    p0 "Crap!  Hide Lily!  Let's hope it will wonder off"
    "You run behind a tree to take cover"
    l0 "Ack!"
    "Lily trips as she attempts to find a place to hide."
    with hpunch
    d0 "RAAAAAAAAAAA!"
    with hpunch
    "The dragon spots her and starts running closer."
    l0 "KYAAA!"
    "Lily screams as she attempts to try and cast a spell, but is too late as the dragon is already next to her."
    d0 "RARGHHHHH!"
    l0 "URK!!"
    "With a swift motion of its neck, the dragon impales Lily with the horn on top of its head."
    p0 "NO!"
    with flash
    r0 "Something weird is happening!  Failures are happening all over the system!"
    p0 "LILY!"
    "You scream as you run out and launch spells at the dragon to make it let go of Lily."
    r0 "[p0]! Disengage and log out immediately! The game is too unstable to continue."
    p0 "AHHHHH!"
    "Ryder's words are too late as the dragon engulfs you in flames and the world around you drowns into a blazing inferno..."
    with fade
    n0 ". {w} . {w} ."

    stop music fadeout 1.0

    n1 "{color=#f20}YOU DIED{/color}"
    with hpunch
    scene bg lilywhite01 with flash
    scene bg bgblack with fade
    n0 "Restarting game..."
    play music "assets/bgm/longway.mp3" fadeout 1.0 fadein 1.0
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
    
    jump reset_start

label reset_start:
    scene bg temple with longfade
    show bluebird at top
    with dissolve
    b0 "Imimimimimimimi!"
    b0 "Welcome back [p0]"
    p0 "Huh."
    b0 "Your memories may be a bit fuzzy as there were errors when resetting to this game state.  Imimimimimimimi!"
    p0 "Memory loss in a game?  That's a serious bug!"
    b0 "There have been difficulties after you encountered a critical bug failure and you have been trapped in this game.  Imimimimimimimi!"
    p0 "Where's Lily and Ryder? I can't contact them."
    b0 "They are working to debugging the game so they can rescue you from this virtual prison.  Imimimimimimimi!"
    p0 "What are you?"
    b0 "I am a game entity created by Lily to help in debugging.  You can call me Hana. Nice to meet you! Imimimimimimimi!"
    b0 "I have been dispatched because the bugs have been making it unable to use regular communications.  Imimimimimimimi!"
    p0 "Do you always need to sing that annoying sound?"
    b0 "I'm sorry. That's just part of my programming! Imimimimimimimi!"
    p0 "So what am I supposed to do? Just sit here?"
    b0 "They need help to trace where the errors are coming from and the best way to help them do that is by playing the game like normal.  Imimimimimimimi!"
    b0 "Should any irregularities go out of control, I will reset you to this saved state to prevent your body from being harmed from the consequences."
    p0 "Alright... Looks like I need to beat this game then and that means defeating that dragon."
    b0 "That's the spirit. Imimimimimimimi!"

    # jump finale
    # jump dragon_start
    jump gauntlet_start
    return
