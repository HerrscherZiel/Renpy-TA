# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
# define mc = Character("Mc", image="mc") 
define mc = Character("You", image="mc")


#stats
default hunger = 50
default energy = 50
default vit = 50
default health = round((hunger+energy+vit) / 3)

default Knowledge = 1
default Practice = 1
default Cappability = 1
default Education = Knowledge+Practice+Cappability /3

default Friend = 1
default Community = 1
default Relations = 1
default Social = Friend+Community+Relations /3

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg lime

    show screen game_stats

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hello this is just placeholder text for testing purpose only."

    e "My name is E, im a default character in this game engine, how about you?"

    e "What is your name?"

    python:
        name = renpy.input("What's your name?")

        name = name.strip()

    mc normal2 "Hi hello, my name is [name]"

    mc normal2 "Nice to meet you E"

    e "Nice to meet you too, ah by the way i have a question for you"

    mc "What's it?"

    e "Between Kaga and Alvea, who would you choose?"

    mc "{i} Hmm who should i choose... {/i}"

    mc " I choose"

    menu:

        "Show Alvea":
            jump alvea

        "Show Kaga":
            jump kaga

    # This ends the game.

    return

label alvea:

    show cg_alvea with dissolve

    e "This is Alvea"

    e "Alvea is just a character that you drew few months back then."

    hide cg_alvea with dissolve

    show e

    e "Anyaway after this i will show you what is parameter looks like"

    mc normal2 " Wow im thrilled for sure."

    e "Button on the top right corner is a button to see all your stats throughthout the game"

    e "Try to click it [name], you can go back with return arrow if you're in stats screen"

    e "How was it?"

    mc "Sound convenient."

    e "Then answer this question, see if it affect your stast"

    e "What would you choose ?"

    menu:

        "Eat":
            call choose_eat

        "Sleep":
            $ energy += 30
            $ hunger -= 20
    
    e "Now see your stats again quick"

    e "How's your stat now?"

    e "See the difference?"

    mc "Yeah my stats are changed"

    e "See.. anyway come with me please [name]"

    mc "Where?"

    e "Just follow me!"

    mc "Aye aye maam"

    jump test_hunger

    return

label kaga:

    show cg_kaga with dissolve

    $ persistent.kaga_unlocked = True


    e "This is Kaga"

    return

label choose_eat:
    $ energy += 15
    $ hunger += 25
    $ health = round((hunger+energy+vit) / 3)

    "You got your lunch!"
    "Stats affected"
    return

label test_hunger:

    if hunger >= 50:
        e "your'e already eat don't you?"
        
        mc "Hehe i just want to eat again"
    
    elif hunger <= 50:
        e "Are you have your lunch yet?"

        mc "No, haven't get my lunch yet."

        e "Then go order something here."
