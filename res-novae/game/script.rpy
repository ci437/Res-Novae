# @author Divya Polson

init:
    $ count = 100
    $ energy = 70
    $ budget = 5000
    $ a = 0 #num of scenes
    $ scenes = ["virus", "volcano", "hitman", "breed", "research"]
    $ renpy.random.shuffle(scenes)

label randomize:
    python:
        if scenes and a < 6:
            a += 1
            renpy.jump(scenes.pop(0))
        else:
            renpy.jump("final")

label start:

    scene lab
    with fade

    play music "BrightEyes.mp3" fadeout 1.0 fadein 1.0

    "Welcome! You're a scientist working for Res Novae Labs, a forward-thinking biology lab specializing in genetic engineering."

    "Your newest project involves populating a new planet, Luna. To start, you've grown an experimental species."

    $ generate_species = renpy.random.randint(1,3)

    if generate_species == 1:
        "Your species is a land creature."
        $ species = "land"
    elif generate_species == 2:
        "Your species is a water creature."
        $ species = "water"
    else:
        "Your species is an air creature."
        $ species = "air"

    $ species_name = renpy.input("What would you like to name your new species?")

    if species_name == "":
        $ species_name ="bebops"

    "Great name! You'll begin with %(count)s organisms."

    "You'll face some obstacles, so use your skills to make good decisions for the survival of your %(species_name)s."

    "To start, you have a budget of %(budget)s coins. You can use coins to breed organisms, conduct research,
    and more."

    "Spend them wisely!"

    "First order of business: your species needs somewhere to live.
    Try to pick somewhere that best fits the traits of your species."

    "Where would you like to place your %(species_name)s?"

    menu:

        "The tundra.":
            jump tundra
        "The desert.":
            jump desert
        "The forest.":
            jump forest

label tundra:

    scene tundra
    stop music

    if species == "land":
        $ count += 1
        "u have %(species)s."
    elif species == "water":
        $ count += 90
        "u have %(species)s."
    else:
        $ count = 8
        "u have %(species)s."
    jump randomize

label desert:

    scene desert
    with fade
    stop music
    play music "BumblyMarch.mp3" fadeout 1.0 fadein 1.0

    if species == "land":
        $ count += 1
        "u have %(species)s."
    elif species == "water":
        $ count += 90
        "u have %(species)s. U DEAD ALREADY."
    else:
        $ count = 8
        "u have %(species)s."
    jump randomize

label forest:

    scene forest
    stop music

    if species == "land":
        $ count += 1
        "u have %(species)s."
    elif species == "water":
        $ count += 90
        "u have %(species)s."
    else:
        $ count = 8
        "u have %(species)s."
    jump randomize

label virus:

    play music "NAIS.mp3" fadeout 1.0 fadein 1.0
    scene virus
    "Looks like there's a new virus you've never seen before..."

    "It seems to be spreading fast. Unfortunately, it's wiped out half of your population."

    "What would you like to do?"

    menu:

        "Research the virus ($1000).":
            jump randomize
        "Migrate species. ($500)":
            jump migrate
        "Do nothing.":
            jump randomize

label volcano:

    stop music
    scene volcano

    "Bad luck! A volcano erupted only 12 miles away from your ecosystem."

    "50 die from the eruption, and 150 are injured. Many more are suffering respiratory issues from the ashes."

    "What would you like to do?"

    menu:
        "Heal the injured ($300).":
            jump randomize
        "Migrate species. ($500).":
            jump migrate
        "Do nothing.":
            jump randomize

label hitman:

    scene lab
    play music "Hitman.mp3" fadeout 1.0 fadein 1.0

    "A new predator has moved in."

    "They're vicious, killing off a great chunk of your population."

    "What would you like to do?"

    menu:
        "Heal the injured ($300).":
            jump randomize
        "Migrate species. ($500).":
            jump migrate
        "Do nothing.":
            jump randomize

label migrate:

    scene lab
    play music "BumblyMarch.mp3" fadeout 1.0 fadein 1.0

    $ budget -= 500
    "Migration is BLAH BLAH. Facts"

    "Be aware that migration comes at a cost--not everyone will survive the long treks."

    "Where would you like to move?"

    menu:

        "The tundra.":
            jump tundra
        "The desert.":
            jump desert
        "The forest.":
            jump forest

label breed:

    scene breed

    "Three new mutations have popped up."

    "Some mutations can have negative effects, and can be dangerous for the survival of the species."

    "Others can help increase the diversity of the gene pool and help evolve the species for the better."

    "You can choose whether or not you want to breed these mutations or let them die out naturally."

    "What would you like to do?"

    menu:

        "Breed Mutation A.":
            jump randomize
        "Breed Mutation B.":
            jump randomize
        "None":
            jump randomize

label research:

    scene lab
    play music "Arcadia.mp3" fadeout 1.0 fadein 1.0

    "Ayyy resarch is cool."

    "You and your fellow Res Novae scientists spent the last several months collecting samples and running tests."

    "Congratulations, you made a new discovery!"

    jump randomize

label final:

    scene lab
    play music "BrightEyes.mp3" fadeout 1.0 fadein 1.0

    "Looks like we've made it to the end."

    "Here are your stats so far: you've grown your %(species_name)s to %(count)s, and you have $%(budget)s left."

    "Great work!"

    return
