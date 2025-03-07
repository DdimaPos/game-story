label scene_13:
    scene mc_car_noon with fade
    play music "car_engine.mp3" fadein 1.0
    show mc_sprite smoking at left
    # SPRITE need a sprite how pa holds a map(could be just a paper that looks like a map)RT
    show pa_sprite at right:
        ypos 1200
        xzoom -1.0
    pa "We’ve checked every pizza place in the city"
    pa "Nothing matches the description"
    mc "It doesn’t make sense" 
    mc "There’s no way we missed it"
    pa "Unless it’s not on the map.{w=0.2} Or…{w=0.2} it doesn’t exist."
    mc "Either way, we’re running out of ti..."
    # SOUND of sirens
    play sound "police_sirens.mp3" loop
    pause 1.0 
    show pa_sprite angry with dissolve
    pa "You’ve got to be kidding me"
    mc "Let's go"

    stop music fadeout 1
    stop sound
    jump scene_14
  