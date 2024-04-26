
define audio.mainmenu = "audio/bgm/Aerosol of my Love.mp3"
define audio.library = "audio/bgm/study-in-a-minor-113931.mp3"
define audio.minimart = "audio/bgm/smooth-sexy-rampb-coffee-music-155218.mp3"
define audio.kos = "audio/bgm/separation-185196.mp3"
define audio.kampung = "audio/bgm/our-summer-in-provence-176854.mp3"
define audio.kota = "audio/bgm/Aerosol of my Love.mp3"
define audio.kampus = "audio/bgm/lofi-study-112191.mp3"

# on "show" action If(renpy.music.is_playing(), true=None, false=pop_songs.RandomPlay())

screen bgm_screen:

    $ renpy.music.stop('music',2)

    if placeKeys == 1:
        $ renpy.music.play('audio/bgm/lofi-study-112191.mp3', 'music', True, 31, False)
    elif placeKeys == 2:
        $ renpy.music.play('audio/bgm/smooth-sexy-rampb-coffee-music-155218.mp3', 'music', True, 1, False)
    elif placeKeys == 3:
        $ renpy.music.play('audio/bgm/separation-185196.mp3', 'music', True, 1, False, 2)
    elif placeKeys == 4:
        $ renpy.music.play('audio/bgm/our-summer-in-provence-176854.mp3', 'music', True, 1, False)
    elif placeKeys == 5:
        $ renpy.music.play('audio/bgm/our-summer-in-provence-176854.mp3', 'music', True, 1, False)
    elif placeKeys == 6:
        $ renpy.music.play('audio/bgm/study-in-a-minor-113931.mp3', 'music', True, 1, False)
    elif placeKeys == 7:
        $ renpy.music.play('audio/bgm/Aerosol of my Love.mp3', 'music', True, 1, False)
    elif placeKeys == 8:
        $ renpy.music.play('audio/bgm/lofi-study-112191.mp3', 'music', True, 1, False)
    elif placeKeys == 9:
        $ renpy.music.play('audio/bgm/lofi-study-112191.mp3', 'music', True, 1, False)
    else:
        pass
    