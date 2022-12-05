# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# label splashscreen:
#     call screen confirm(message="Proceed to play the game?", yes_action=Return(), no_action=Quit(confirm=False))
#     return

define v = Character("Vivy")
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

default vivy_fond = 0

#days
default day = 1

#time
#0 = morning, #1 = noon/evening, #2 = night
default timephase = 1

#place

#keys
default firstMart = True

default place_list = ["campus", "street", "minimart", "dorm"]

# The game starts here.

label start:
    $ my_task.addTask(task_eat_your_first_food)
    $ my_task.addTask(task_choose_best_girl)
    $ my_task.addTask(task_dont_be_greedy)
    $ my_task.addTask(task_survive_too_long)

    # show screen tasks_screen

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    scene bg black
    with Dissolve(2.0)

    pause 2.0

    "..........."

    "......"

    "Hari telah menunjukan pukul 4, menandakan program orientasi mahasiswa baru di univ X telah usai."
    
    "Berhamburan keluar dari ruang kelas dengan berbagai atribut orientasi yang mereka bawa."

    "Bermacam-macam ekspresi terlihat dari raut muka mahasiswa baru yang sedang berhamburan keluar."

    "Meski terdapat berbagai macam ekspresi yang terlihat, namun pada umumnya para mahasiswa baru merasakan hal yang sama, yaitu senang dan tidak sabar."

    "Senang karena mereka baru saja menyelesaikan langkah pertama dalam kehidupan kuliah mereka."

    "Dan tak sabar untuk menjalani kehidupan baru mereka sebagai seorang mahasiswa. Teman baru, mata kuliah, lingkungan baru, dan berbagai hal yang belum pernah mereka rasakan sebelumnya."

    window hide

    show day1 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 1.5

    hide day1 pro with dissolve

    show day1 street:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 1.5

    # hide day1 pro 
    # with dissolve

    scene bg street with dissolve

    "Setelah keluar dari ruang kelas, mahasiswa baru menyebar ke berbagai arah sesuai dengan kepentingan masing-masing."
    
    "Terlihat ada yang mengumpul dengan mahasiswa baru lainnya, ada yang berfoto-foto dengan teman satu kelas orientasi, ada yang dijemput oleh orang tua mereka, ada yang berjalan keluar dari kampus, dan ada juga yang berjalan ke arah parkiran."

    "Dari banyak mahasiswa baru yang berjalan menuju parkiran motor, di antaranya terdapat seorang mahasiswa laki-laki yang mengenakan jaket bewarna X."

    "Mahasiswa itu berjalan sendirian tidak seperti kebanyakan mahasiswa lain yang bersenda gurau dengan teman di sebelah mereka." 
    
    mc normal2  "Akhirnya selesai juga, capek juga seminggu ini orientasinya."

    mc  "Tapi seru juga sih, dapet pengalaman baru, ga sabar nanti kuliahnya kaya apa."

    mc  "Mampir beli minum dulu gak ya? Tapi gak tau dimana minimarket sekitar sini..."

    v   "Halooo… Permisi!!"

    "{i}Tak sadar, tiba-tiba ada seorang perempuan yang berdiri di depanku{/i}"

    show v normal:
        xalign 0.0 yalign 0.0
        linear 0.8 xalign 0.9

    mc  "Ohh.. maaf-maaf ada apa ya?"

    v   "Tidak apa-apa kok, cuma mau manggil saja, kamu tadi diam tiba-tiba pas di depanku."

    mc  "Maaf-maaf hehehe…."

    v   "Oh iya, aku Vivy, aku mahasiswa baru juga, dari Vokasi jurusan TRPL."

    v   "Kamu juga mahasiswa baru juga kan?"

    "Game ini memiliki fitur {b}pengambilan keputusan{/b} sesuai pilihan pemain."

    "Dalam pengambilan keputusan, pilihan yang diambil oleh pemain akan {b}mempengaruhi alur{/b} dari game atau {i}{b}Choices matter.{/b}{/i}"

    "Pilihan yang diambil dapat mempengaruhi game baik secara langsung maupun tidak langsung."

    "Jadi pastikan dulu pilihanmu sebelum memilih."

    "Perempuan yang memperkenalkan dirinya dengan nama {i}Vivy{/i} tiba-tiba menyulurkan tangannya ke arahmu."

    "Kamu memilih untuk..."

    menu:

        "Bersalaman":

            $ vivy_fond += 15
            
            "Kamu ikut menyulurkan tanganmu dan bersalaman dengan perempuan yang ada di depanmu."

        "Abaikan":

            "Kamu mengabaikan tangannya."

    python:
        name = renpy.input("Masukan namamu!")

        name = name.strip()

    mc  "Iya aku mahasiswa baru juga, aku {i}{b}[name]{/b}{/i}, kebetulan aku juga dari TRPL, salam kenal."

    v   "Wah teman satu angkatan kita ternyata hehehe. Oh ya kenapa tadi tiba-tiba berhenti mendadak? Ada yang jatuh kah?"

    mc  "Oh tidak, tadi cuma kepikiran mau mampir ke minimarket, tapi aku belum tau minimarket yang dekat disini dimana."

    v   "Owhh… kalau gitu ikut aja aku, lumayan deket kok dari sini, tidak perlu pakai motor juga."

    mc  "Kamu sudah jalan-jalan daerah sekitar ya? Kok sudah tau daerah dekat sini."

    v   "Hahaha… tidak kok, kebetulan rumahku dekat daerah sini saja, jadi ya tahu daerah sini."

    mc  "Pantas saja sudah tau."

    v   "Kalau kamu dari mana [name]?"

    mc  "Aku dari luar kota, baru 3 hari sebelum orientasi aku datang kesini."

    mc  "Oh ya, tidak apa kamu mengantarku ke minimarket?"

    v   "Aku juga mau beli sesuatu kok, jadi santai aja."

    mc  "Oke kalau begitu."

    "Vivy berjalan dan melambaikan tangannya kepadamu, menyuruhmu untuk mengikutinya."

    "Kamu berjalan di belakang Vivy, kamu mengikutinya ke arah minimarket"

    "Dalam game ini, terdapat {b}menu map{/b}, dimana pemain dapat {b}memilih kegiatan{/b} apa yang selanjutnya akan dilakukan, bedasarkan lokasi yang dipilih di map."

    "Pemain dapat memilih kegiatan dengan cara {b}memilih icon{/b} yang ada di map." 

    "Pemain akan berpindah ke lokasi yang dituju, dan melakukan kegiatan sesuai icon yang dipilih."

    "Setiap memilih suatu kegiatan pada map, maka {b}waktu akan berganti{/b} menjadi fase waktu berikutnya." 
    
    "Pada game ini terdapat 3 jenis waktu, yaitu {b}Pagi -> Siang/Sore -> Malam.{/b}"

    "Setelah melakukan aktivitas pada {b}Malam hari{/b}, maka {b}hari akan berubah.{/b}"

    "Game ini akan berjalan selama {b}30 hari{/b}." 

    "Setelah hari ke 30 selesai, pemain akan mendapatkan ending dari game ini."

    "Hari, Waktu, dan Tempat dapat dilihat pada bagian {b}kiri atas layar{/b}."

    show screen days_screen

    jump first_map

    # This ends the game.

    return

label nothing:

    scene bg black

    "nothing here, you're wrong"

# label alvea:

#     show cg_alvea with dissolve

#     e "This is Alvea"

#     e "Alvea is just a character that you drew few months back then."

#     hide cg_alvea with dissolve

#     show eileen happy

#     e "Anyaway after this i will show you what is parameter looks like"

#     mc normal2 " Wow im thrilled for sure."

#     e "Button on the top right corner is a button to see all your stats throughthout the game"

#     e "Try to click it [name], you can go back with return arrow if you're in stats screen"

#     e "How was it?"

#     mc "Sound convenient."

#     e "Then answer this question, see if it affect your stast"

#     e "What would you choose ?"

#     menu:

#         "Eat":
#             call choose_eat

#         "Sleep":
#             $ energy += 30
#             $ hunger -= 20
#             $ health = round((hunger+energy+vit) / 3)
    
#     e "Now see your stats again quick"

#     e "How's your stat now?"

#     e "See the difference?"

#     mc "Yeah my stats are changed"

#     e "See.. anyway come with me please [name]"

#     mc "Where?"

#     e "Just follow me!"

#     mc "Aye aye maam"

#     jump test_hunger

#     return

# label kaga:

#     show cg_kaga with dissolve

#     $ persistent.kaga_unlocked = True


#     e "This is Kaga, one of many ship waifus from Kantai Collection franchises"

#     mc "Whoaa"

#     e "You're the one who drew it by the way."

#     mc "Really??"

#     hide cg_kaga with dissolve

#     show eileen happy

#     e "Yeahh, anywayy, try to add days to see if the days counter is working."

#     e "The days counter are in the top left corner by the way."

#     mc "Okeyy maam!"

#     menu:

#         "Add day":
#             $day += 1

#     e "Looks the day's now changed."

#     mc "Yeah i see it too."

#     e "This game has 30 days in total, so you must choose your option carefully not to drop out the univ you know."

#     mc "I see... Eileen do you know where the closest minimart here?"

#     mc "I'm kinda new in this town so i don't know any shop around here."

#     e "Sure, i'll lead you the way."

#     e "Minimart huhh... ah here i have a map, why don't you click it so you know where the minimart location ?"

#     e "If you clicked it i'll guide you there."

#     mc "Aight, just click it right?"

#     e "Yeah."

#     hide eileen happy with dissolve

#     call maps

#     return

# label choose_eat:
#     $ energy += 15
#     $ hunger += 25
#     $ health = round((hunger+energy+vit) / 3)

#     "You got your lunch!"
#     "Stats affected"
#     return

# label test_hunger:

#     if hunger >= 50:
#         e "your'e already eat don't you?"
        
#         mc "Hehe i just want to eat again"
    
#     elif hunger <= 50:
#         e "Are you have your lunch yet?"

#         mc "No, haven't get my lunch yet."

#         e "Then go order something here."
    
#     return

# label maps:

#     call screen mapUI

#     "Click the Map button"

#     return

# label minimart:

#     show bg grey

#     "This is minimart"

#     e "Welcome to the Minimart"

#     mc "WHoaa"

#     jump endd

#     return

# label endd:

#     show bg lime

#     e "This is it, Thank You"

#     return