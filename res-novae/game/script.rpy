# @author Divya Polson
init:
    $ count = 100
    $ budget = 5000
    # define growth rate
    $ a = 0 #num of scenes
    $ scenes = ["virus", "volcano", "pollution", "breed", "research", "famine"]
    $ renpy.random.shuffle(scenes)
    $ current_img = "creature.png"

label randomize:
    python:
        if scenes and a < 7:
            a += 1
            renpy.jump(scenes.pop(0))
        else:
            renpy.jump("final")

label traits:
    show screen creature
    show screen count
    show screen money
    "{b}%(species_name)s{/b}: %(species)s creature that is %(diet)s."
    return

#definitions
label genetic_diversity:
    "{b}Genetic Diversity{/b}: The total number of genetic characteristics in the genetic makeup of a species. Genetic diversity serves as a way for populations to adapt to changing environments. "
    return
label keystone_species:
    "{b}Keystone Species{/b}: A species that plays a critical role in maintaining the structure of an ecological community, affecting many other organisms in an ecosystem."
    return
label immunity:
    "{b}Immunity{/b}: An organism's ability to resist a particular infection or toxin by the action of specific antibodies or sensitized white blood cells."
    return
label carbon_footprint:
    "{b}Carbon Footprint{/b}: The total emissions caused by an individual, organization, or product, expressed as carbon dioxide equivalent."
    return
label foraging:
    "{b}Foraging{/b}: Searching for wild food resources. It affects an animal's fitness because it plays an important role in an animal's ability to survive and reproduce."
    return
label mutation:
    "{b}Mutation{/b}: Departure from the parent type in one or more heritable characteristics, caused by a change in a gene or a chromosome."
    return

screen creature:
    add current_img xpos 0.81 ypos 0.03
screen count:
     add "count.png" xpos 0.81 ypos 0.33
     text "{a=traits}[count] [species_name]{/a}" xpos 0.9 ypos 0.34 xalign 0.5
     zorder 5
screen money:
     add "budget.png" xpos 0.81 ypos 0.4
     text "[budget] coins" xpos 0.9 ypos 0.41 xalign 0.5
screen environments:
    imagebutton idle "images/forest_preview.png" hover "forest_hover" xpos 0.04 ypos 0.2 action Function(renpy.jump, label="forest")
    text "Temperate forest" xpos 0.16 ypos 0.59 xalign 0.5
    imagebutton idle "images/desert_preview.png" hover "desert_hover.png" xpos 0.27 ypos 0.2 action Function(renpy.jump, label="desert")
    text "Coastal Desert" xpos 0.39 ypos 0.59 xalign 0.5
    imagebutton idle "images/tundra_preview.png" hover "tundra_hover" xpos 0.5 ypos 0.2 action Function(renpy.jump, label="tundra")
    text "Tundra" xpos 0.62 ypos 0.59 xalign 0.5
    imagebutton idle "images/rainforest_preview.png" hover "rainforest_hover" xpos 0.73 ypos 0.2 action Function(renpy.jump, label="rainforest")
    text "Tropical rainforest" xpos 0.85 ypos 0.59 xalign 0.5
    zorder 100
screen mutations:
    imagebutton idle "images/wings.png" hover "wings.png" xpos 0.2 ypos 0.3 action Function(renpy.jump, label="breed_wings")
    imagebutton idle "images/tail.png" hover "tail.png" xpos 0.4 ypos 0.3 action Function(renpy.jump, label="breed_tail")
    imagebutton idle "images/fangs.png" hover "fangs.png" xpos 0.6 ypos 0.3 action Function(renpy.jump, label="breed_fangs")
    zorder 100

label start:

    scene lab
    with fade

    play music "BrightEyes.mp3" fadeout 1.0 fadein 1.0

    "Welcome! You're a scientist working for Res Novae Labs, a forward-thinking biology lab specializing in genetic engineering."

    "Your newest project involves populating a new planet, Luna. To start, you've grown an experimental species."

    $ generate_species = renpy.random.randint(1,3)
    $ generate_diet = renpy.random.randint(1,3)
    if generate_diet == 1:
        $ diet = "herbivorous"
    elif generate_diet == 2:
        $ diet = "omnivorous"
    else:
        $ diet = "carnivorous"

    if generate_species == 1:
        show screen creature
        "Your species is a land creature. It is %(diet)s."
        $ species = "land"

    elif generate_species == 2:
        show screen creature
        "Your species is a water creature. It is %(diet)s."
        $ species = "water"

    else:
        show screen creature
        "Your species is an air creature. It is %(diet)s."
        $ species = "air"


    $ species_name = renpy.input("What would you like to name your new species?")

    if species_name == "":
        $ species_name ="bebops"

    show screen count

    "Great name! You'll begin with %(count)s organisms."

    "You'll face some obstacles, so use your skills to make good decisions for the survival of your %(species_name)s."

    show screen money

    "To start, you have a budget of %(budget)s coins. You can use coins to breed organisms, conduct research,
    and more."

    "Spend them wisely!"

    "First order of business: your species needs somewhere to live.
    Try to pick somewhere that best fits the traits of your species."

    scene env

    hide screen creature
    hide screen count
    hide screen money

    show screen environments
    with dissolve

    "Where would you like to place your %(species_name)s?"

label tundra:

    hide screen environments
    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    $ location = "tundra"
    scene tundra
    with fade
    show screen count
    show screen money
    stop music
    show screen creature

    if species == "land":
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    elif species == "water":
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    else:
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    jump randomize

label rainforest:

    hide screen environments
    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    $ location = "rainforest"
    scene rainforest
    with fade
    show screen count
    show screen money
    stop music
    show screen creature

    if species == "land":
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    elif species == "water":
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    else:
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    jump randomize

label desert:

    hide screen environments
    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    $ location = "desert"
    scene desert
    with fade
    show screen count
    show screen money
    stop music
    play music "BumblyMarch.mp3" fadeout 1.0 fadein 1.0
    show screen creature

    if species == "land":
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    elif species == "water":
        $ count += int(count + (count * 0.20))
        "u have %(species)s. U DEAD ALREADY."
    else:
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    jump randomize

label forest:

    hide screen environments
    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    $ location = "forest"
    scene forest
    with fade
    show screen count
    show screen money
    stop music
    show screen creature

    if species == "land":
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    elif species == "water":
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    else:
        $ count += int(count + (count * 0.20))
        "u have %(species)s."
    jump randomize

label virus:

    hide screen mutations
    $ count = int(count - (count * 0.40))

    if count <= 0:
      jump dead
    else:
        pass

    play music "NAIS.mp3" fadeout 1.0 fadein 1.0
    scene virus
    "Looks like there's a new virus you've never seen before..."

    "It seems to be spreading fast. Unfortunately, it's quickly wiping out your population."

    "What would you like to do?"

    menu:

        "Research the virus ($1000).":
            $ renpy.notify('- 1000 coins')
            jump virus_research
        "Migrate species. ($500)":
            $ renpy.notify('- 500 coins')
            jump migrate
        "Do nothing.":
            pass

    $ count = int(count - (count * 0.10))

    "Interesting...not as many organisms are dying..."

    "A few of your %(species_name)s seem to have built up a resistance to the virus."

    "By not intervening, you have allowed your species to gradually grow {a=immunity}immune{/a} to the disease."

    jump randomize

label virus_research:

    scene research

    $ virus_result = renpy.random.randint(1,10)
    if virus_result > 2:

        "Congratulations, your research team developed a cure!"

        $ count = int(count + (count * 0.15))

        "The affected organisms slowly begin to regain their health."
        jump randomize

    else:
        "Unfortunately, your research didn't result in a cure."

        $ count = int(count - (count * 0.10))

        "Although a few have built up {a=immunity}immunity{/a}, many continue to suffer from the effects of the virus."
        jump randomize

label volcano:

    $ renpy.notify('- ' + str(int(count * 0.10)))
    $ count = int(count - (count * 0.10))
    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    stop music
    scene volcano

    "Bad news! A volcano erupted a short distance away from your ecosystem."

    "Your species is suffering respiratory issues from the ashes."

    "What would you like to do?"

    menu:
        "Send out a medical rescue team. ($700).":
            $ budget -= 700
            jump volcano_rescue
        "Migrate species. ($500).":
            jump migrate
        "Do nothing.":
            pass

    $ count = int(count - (count * 0.15))

    "Your species suffers temporarily, but manages to make it through the next few months."

    jump randomize

label volcano_rescue:

    $ renpy.notify('- $700')
    #$ renpy.notify('- ' + str(int(count * 0.05)))
    $ count = int(count - (count * 0.05))

    "Good work! The medical rescue team heals some of the injured and minimizes losses."
    jump randomize

label pollution:

    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    $ count = int(count - (count * 0.12))

    scene pollution
    play music "Hitman.mp3" fadeout 1.0 fadein 1.0
    $ current_img = "creature_sad.png"
    show screen creature
    show screen count

    "Your lab is producing some pollution..."

    "The air is full of smog and the lab's waste is polluting your species' water source."

    "What would you like to do?"

    menu:
        "Invest in more eco-friendly facilities ($1500).":

            $ budget -= 1500
            $ renpy.notify('- 1500 coins')
            $ count = int(count + (count * 0.28))
            "The renovations are a success and your collective {a=carbon_footprint}carbon footprint{/a} is lower than ever."
            #$ renpy.notify('+ ' + str(int(count * 0.28)))
            jump randomize

        "Organize a cleanup effort ($100).":

            $ budget -= 100
            $ renpy.notify('- 100 coins')
            $ count = int(count - (count * 0.08))
            "The cleanup event helped clear up some of the pollution, but wasn't a permanent solution."
            jump randomize

        "Do nothing.":
            #$ renpy.notify('- ' + str(int(count * 0.17)))
            $ count = int(count - (count * 0.17))
            "Because of the lack of action, the %(species_name)s continue to suffer from the toxic fumes."
            jump randomize

label migrate:

    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    scene migration
    play music "BumblyMarch.mp3" fadeout 1.0 fadein 1.0

    $ budget -= 500
    "Migration can be a good way to increase the {a=genetic_diversity}genetic diversity{/a} within a species."

    "Be aware that migration comes at a cost—not everyone will survive the long treks."

    $ current_img = "creature_sad.png"
    show screen creature
    hide screen count
    hide screen money

    show screen environments
    with dissolve

    "Where would you like to move?"

label breed:

    if count <= 0:
      jump dead
    else:
        pass

    scene breeding

    "It's mating season!"

    "You've noticed that three new {a=mutation}mutated{/a} organisms have popped up within your species."

    "Some mutations can have negative effects, and can be dangerous for the survival of the species."

    "Others can help increase the diversity of the gene pool and help evolve beneficial traits."

    "You can choose whether or not you want to breed these mutations or let them die out naturally."

    show screen mutations
    with dissolve

    $ count = int(count + (count * 0.40))

    "Which mutation would you like to breed?"

label breed_wings:

    hide screen mutations
    $ current_img = "wings.png"
    "You chose to breed wings! This can be a useful trait that helps with {a=foraging}foraging{/a} and migration. But be warned, it takes a lot of energy to breed this trait."
    jump randomize

label breed_fangs:

    hide screen mutations
    $ current_img = "fangs.png"
    "You chose to breed fangs! This can an especially beneficial trait for carnivorous creatures, helping them more easily dig into their prey."
    jump randomize

label breed_tail:

    hide screen mutations
    $ current_img = "tail.png"
    "You chose to breed a tail! This trait is particularly beneficial for species living in forests, as it helps with balance and movement, and can even act as another arm."
    jump randomize

label famine:

    hide screen mutations
    scene famine
    $ current_img = "creature_sad.png"
    show screen creature
    show screen count

    if count <= 0:
      jump dead
    else:
        pass

    "It looks like your species has been hit by a terrible famine..."

    "A {a=keystone_species}keystone species{/a} in your ecosystem, the Glorps, has dwindled in size and disrupted the food chain."

    "Your species is quickly running out of food and approaching starvation."

    "What would you like to do?"

    menu:

        "Research a possible new source of food ($800).":
            $ budget -= 800
            $ renpy.notify('- 800 coins')
            jump famine_research
        "Migrate ($500).":
            jump migrate
        "Wait it out.":
            "A new vegetation begins growing in the environment, eventually returning balance to the ecosystem."
            $ renpy.notify('- ' + str(int(count * 0.50)))
            $ count = int(count - (count * 0.50))
            "Your species has survived the famine, but just barely."
            jump randomize

label famine_research:

    scene research

    $ famine_result = renpy.random.randint(1,10)
    if famine_result >3:

        "Congratulations! Your research was a success."

        "Your research team discovered a new fauna that could restore the balance of the ecosystem."

        $ count = int(count + (count * 0.10))
        $ renpy.notify('+ ' + str(int(count * 0.10)))

        "Your species is slowly beginning to regain its strength following the famine."

        jump randomize

    else:

        "Unfortunately, your research yielded no results."

        "Luckily for you, a new vegetation begins growing in the environment, eventually returning balance to the ecosystem."
        $ renpy.notify('- ' + str(int(count * 0.50)))
        $ count = int(count - (count * 0.50))

        "Your species has survived the famine, but just barely."

        jump randomize


label research:

    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    scene research
    play music "Arcadia.mp3" fadeout 1.0 fadein 1.0

    "You and your fellow Res Novae scientists spent the last several months collecting samples and running tests."

    "Recently, you stumbled across something interesting."

    "You've discovered a new plant specimen with unknown properties."

    "What would you like to do?"

    menu:

        "Research and test the specimen. ($450)":
            jump research_result
        "Do nothing.":
            pass

    "Little did you know, the plant was extremely poisonous and instantly fatal to your species."

    $ count = int(count - (count * 0.30))

    jump randomize

label research_result:

    $ research_result = renpy.random.randint(1,10)

    if research_result > 3:

        $ count = int(count + (count * 0.30))

        "Great work! You discovered that this new specimen has incredible healing powers for your species."

        "You"

        jump randomize

    else:

        $ count = int(count - (count * 0.05))

        "Unfortunately, you discover that the plant is extremely poisonous and instantly fatal to your species."

        "The good news is your research helped your team develop an antidote to counteract the effects."

        jump randomize

label final:

    hide screen mutations
    if count <= 0:
      jump dead
    else:
        pass

    scene end
    play music "BrightEyes.mp3" fadeout 1.0 fadein 1.0

    "Looks like you've made it to the end."

    "Here are your stats so far: you've grown your %(species_name)s to %(count)s, and you have $%(budget)s left."

    if count > 100:
        "Great work!"
    else:
        "Your %(species_name)s survived, but you didn't successfully grow your species. Better luck next time!"
    return

label dead:

    scene end

    "Unfortunately, it looks like your species has died out."

    "Better luck next time!"

    return
