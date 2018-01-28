label start:
    scene bg forest with fade

    N0 "System initialized..."
    N0 "5"
    N0 "4"
    N0 "3"
    N0 "2"
    N0 "1"
    N0 "Complete"

    python:
        P0 = renpy.input("Enter your name.")
        P0 = P0.strip()

        if not P0:
            P0 = "Blue"

    "Player name accepted."
    "Welcome [P0]."
    "Starting up world..."

    scene bg forest temple with fade
    P0 "Where am I?"
    L0 "It's about time you synced up! Wake up!"
    P0 "Is that you Lily?"
    "My colleague Lily relentlessly jabs me in the side as I groggily wake up after syncing up into the game."

    L0 "Wake up! We got a lot of testing to do on this run!"
    P0 "I'm up! I'm up!"
    "For being in a virtual world, the pain from her sharp jabs still feels so real."
    R0 "I see sleeping beauty finally synced up."
    "My other colleague, Ryder, chimes in from the global communications channel."
    L0 "First on the list is testing the newly implemented battle system."

    # CONTINUE INTRO HERE

    N0 "System restarting..."
    N0 "5"
    N0 "4"
    N0 "3"
    N0 "2"
    N0 "1"
    N0 "Complete"

    H0 "Welcome back [P0]"
    P0 "Huh."
    H0 "Your memories may be a bit fuzzy as there were errors when resetting to this game state."
    P0 "Memory loss in a game?  That's a serious bug!"
    H0 "There have been difficulties after you encountered a critical bug failure and you are trapped in this game."
    P0 "Where's Lily and Ryder? I can't contact them."
    H0 "They are working to debugging the game so they can rescue you from this virtual prison."
    P0 "What are you?"
    H0 "I am a game entity created by Lily to help in debugging.  You can call me Hana. Nice to meet you!"
    H0 "I have been dispatched because the bugs have been making it unable to use regular communications."
    P0 "So what am I supposed to do? Just sit here?"
    H0 "They need help to trace where the errors are coming from and the best way to help them do that is by playing the game like normal."
    H0 "Should any irregularities go out of control, I will reset you to this saved state to prevent your body from being harmed from the consequences."
    P0 "Alright... Looks like I need to beat this game then and that means defeating that dragon."
    H0 "That's the spirit."

    jump act01_start
    return
