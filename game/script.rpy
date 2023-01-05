# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# label splashscreen:
#     call screen confirm(message="Proceed to play the game?", yes_action=Return(), no_action=Quit(confirm=False))
#     return

define r = Character("Rissa", image="r")
# define mc = Character("Mc", image="mc") 
define mc = Character("You", image="mc")
define w1 = Character("Warga")
define pa = Character("Pad Andy")


#stats
default hunger = 50
default energy = 50
default vit = 50
default health = round((hunger+energy+vit) / 3)

default knowledge = 1
default practice = 1
default application = 1
default academic = round((knowledge+practice+application) / 3)

default friend = 1
default community = 1
default public = 1
default social = round((friend+community+public) /3)

default rissa_fond = 0

#days
default day = 1

#time
#1 = morning, #2 = noon/evening, #3 = night
default timephase = 1

#place

#keys
default prologue = True
default prologueCount = 1
default firstMart = True
default firstKos = True
default firstKampung = True
default firstKampus = True
default placeKeys = 1

#sub keys
default rotiAwal = False

default maps = False


# The game starts here.



label start:
    $ my_task.addTask(task_eat_your_first_food)
    $ my_task.addTask(task_choose_best_girl)
    $ my_task.addTask(task_dont_be_greedy)
    $ my_task.addTask(task_survive_too_long)

    # show screen tasks_screen
    # These display lines of dialogue.

    scene bg black
    with Dissolve(2.0)

    pause 2.0

    "....................."

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

    pause 2.5

    hide day1 pro with dissolve

    show day1 street:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 2.5

    # hide day1 pro 
    # with dissolve

    scene bg streets with dissolve

    play music "audio/bgm/Aerosol of my Love.mp3" loop volume 0.1

    "Setelah keluar dari ruang kelas, mahasiswa baru menyebar ke berbagai arah sesuai dengan kepentingan masing-masing."
    
    "Terlihat ada yang mengumpul dengan mahasiswa baru lainnya, ada yang berfoto-foto dengan teman satu kelas orientasi, ada yang dijemput oleh orang tua mereka, ada yang berjalan keluar dari kampus, dan ada juga yang berjalan ke arah parkiran."

    "Dari banyak mahasiswa baru yang berjalan menuju parkiran motor, di antaranya terdapat seorang mahasiswa laki-laki yang mengenakan jaket bewarna X."

    "Mahasiswa itu berjalan sendirian tidak seperti kebanyakan mahasiswa lain yang bersenda gurau dengan teman di sebelah mereka." 
    
    show mc normal jacket:
        xalign 0.2 yalign -0.3
    with dissolve
    
    mc "Akhirnya selesai juga, capek juga seminggu ini orientasinya."

    mc  "Tapi seru juga sih, dapet pengalaman baru, ga sabar nanti kuliahnya kaya apa."

    mc  "Mampir beli minum dulu gak ya? Tapi gak tau dimana minimarket sekitar sini..."

    "Halooo… Permisi!!"

    "{i}Tak sadar, tiba-tiba ada seorang perempuan yang berdiri di depanku{/i}"

    show r normal2:
        xalign 0.0 yalign 1.0
        linear 0.8 xalign 0.9
    with dissolve

    mc  "Ohh.. maaf-maaf ada apa ya?"

    r   "Tidak apa-apa kok, cuma mau manggil saja, kamu tadi tiba-tiba berhenti tepat di depanku."

    mc  "Maaf-maaf hehehe…."

    r   "Oh iya, aku Rissa, aku mahasiswa baru juga, dari Vokasi jurusan TRPL."

    r   "Kamu juga mahasiswa baru juga kan?"

    "Game ini memiliki fitur {b}pengambilan keputusan{/b} sesuai pilihan pemain."

    "Dalam pengambilan keputusan, pilihan yang diambil oleh pemain akan {b}mempengaruhi alur{/b} dari game atau {i}{b}Choices matter.{/b}{/i}"

    "Pilihan yang diambil dapat mempengaruhi game baik secara langsung maupun tidak langsung."

    "Jadi pastikan dulu pilihanmu sebelum memilih."

    "Perempuan yang memperkenalkan dirinya dengan nama {i}Rissa{/i} tiba-tiba menyulurkan tangannya ke arahmu."

    "Kamu memilih untuk..."

    menu:

        "Bersalaman":

            $ rissa_fond += 15
            
            "Kamu ikut menyulurkan tanganmu dan bersalaman dengan perempuan yang ada di depanmu."

        "Abaikan":

            "Kamu mengabaikan tangannya."

    python:
        name = renpy.input("Masukan namamu!")

        name = name.strip()

    mc  "Iya aku mahasiswa baru juga, aku {i}{b}[name]{/b}{/i}, kebetulan aku juga dari TRPL, salam kenal."

    r   "Wah teman satu angkatan kita ternyata hehehe. Oh ya kenapa tadi tiba-tiba berhenti mendadak? Ada yang jatuh kah?"

    mc  "Oh tidak, tadi cuma kepikiran mau mampir ke minimarket, tapi aku belum tau minimarket yang dekat disini dimana."

    r   "Owhh… kalau gitu ikut aja aku, lumayan deket kok dari sini, tidak perlu pakai motor juga."

    mc  "Kamu sudah jalan-jalan daerah sekitar ya? Kok sudah tau daerah dekat sini."

    r   "Hahaha… tidak kok, kebetulan rumahku dekat daerah sini saja, jadi ya tahu daerah sini."

    mc  "Pantas saja sudah tau."

    r   "Kalau kamu dari mana [name]?"

    mc  "Aku dari luar kota, baru 3 hari sebelum orientasi aku datang kesini."

    mc  "Oh ya, tidak apa kamu mengantarku ke minimarket?"

    r   "Aku juga mau beli sesuatu kok, jadi santai aja."

    mc  "Oke kalau begitu."

    "Vivy berjalan dan melambaikan tangannya kepadamu, menyuruhmu untuk mengikutinya."

    "Kamu berjalan di belakang Vivy, kamu mengikutinya ke arah minimarket"

    "Dalam game ini, terdapat {b}menu map{/b}, dimana pemain dapat {b}memilih kegiatan{/b} apa yang selanjutnya akan dilakukan, bedasarkan lokasi yang dipilih di map."

    "Pemain dapat memilih kegiatan dengan cara {b}memilih icon{/b} yang ada di map." 

    "Pemain akan berpindah ke lokasi yang dituju, dan melakukan kegiatan sesuai icon yang dipilih."

    "Setiap memilih suatu kegiatan pada map, maka {b}waktu akan berganti{/b} menjadi fase waktu berikutnya." 
    
    "Pada game ini terdapat 3 jenis waktu, yaitu {b}Pagi -> Siang/Sore -> Malam.{/b}"

    "Setelah melakukan aktivitas pada {b}Malam hari{/b}, maka {b}hari akan berubah.{/b}"

    "Hari, Waktu, dan Tempat dapat dilihat pada bagian {b}kiri atas layar{/b}."

    show screen days_screen

    "Game ini akan berjalan selama {b}30 hari{/b}." 

    "Setelah hari ke 30 selesai, pemain akan mendapatkan ending dari game ini."

    "Untuk berpindah ke minimarket, pilih icon minimarket kemudian klik kiri pada icon."

    jump first_map

    return

label first_map:

    scene bg black
    with fade

    pause 2.0
    
    "Untuk memilih kegiatan yang akan dilakukan selanjutnya, kamu dapat mengarahkan pointer ke arah icon yang ada pada {b}Map{/b}."

    "Untuk sekarang pilihlah Icon Minimart, kemudian tekan klik kiri."

    hide screen days_screen

    call screen mapUI
    # ($day, $timephase)

    return

label day2:

    $ day += 1

    scene bg black
    with Dissolve(2.0)

    pause 2.0

    show day2 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 3.0

    hide day2 pro with dissolve

    show day2 kosmorn:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 3.0

    scene bg kosmorn with dissolve

    show screen stats_screen with dissolve

    #alarm sound

    "Kringgggg"

    "Kringgg"

    "Kringgg"

    "Alarmmu berbunyi beberapa kali sebelum kamu bangun dan mematikannya."

    "Dengan mata yang masih sipit, kamu meraba-raba di sekeliling tempat tidurmu."

    "Menggenggam ponsel, kamu melihat banyak notifikasi dari grup chat LANEmu. Kamu mengabaikannya dan matamu fokus untuk mencari waktu yang sudah menunjukan pukul 5 pagi."

    "Melihat sinar matahari yang sudah masuk melalui jendela kamarmu, kamu bangun dan merapikan tempat tidurmu."

    "Setelah selesai merapikan tempat tidur, kemudian kamu berjalan ke arah kamar mandi untuk membasuh mukamu."

    mc normal2"Uahhhh….. Masih ngantuk…"

    mc "{i}tapi disini pagi hari begini tidak dingin tapi malah keringatan begini ya?!{/i}"

    "Sesampainya di kamar mandi kamu langsung membasuh muka dan menggosok gigimu."

    mc "Enggak enak sekali bangun bangun muka berminyak seperti ini."

    # Sfx grumbling

    "Grugggg"

    mc "…. Laparr…."

    "{b}!Stats drop tutorial{/b}!"

    "Beberapa stats yang dimiliki {b}dapat berkurang{/b}."

    "Penyebab berkurangnya stats yang ada dapat dikarenakan oleh {b}pemilihan pilihan{/b} maupun berkurang {b}secara otomatis{/b}."

    "Pemilihan pilihan seperti kegiatan {i}olahraga{/i} dapat mengurangi tingkat {b}energimu{/b} namun menambah tingkat {b}fit{/b}mu."

    "Sementara stats dapat berkurang secara otomatis jika hari berganti, stats yang dapat berkurang secara otomatis adalah main {b}stats kesehatan{/b}."

    mc "aku masih punya makanan sisa tidak ya?"

    "Kamu mencari makanan yang ada di kamar kosmu."

    if rotiAwal == True:
        
        mc "Oh iyaa, kemarin aku masih menyimpan roti, lumayanlah buat sarapan."

        "Kamu mengambil roti yang kamu beli di Minimart kemarin dan langsung memakannya."

        "{b}!Stats berubah!{/b}"

    else:
        mc "Yahhh tidak ada apa-apa, roti yang kubeli kemarin juga langsung aku makan."

        mc "Apa boleh buat, sekalian nanti siang sajalah makannya."

    "Kemudian kamu mengingat terdapat banyak notifikasi dari grup chat LANE ketika bangun tadi."

    "Merebahkan tubuhmu di kasur, kamu mengambil ponselmu dan mulai men scroll chat-chat yang ada di grup."

    show phone chat:
        yalign 0.5 
    with moveinbottom

    "Seperti grup chat pada umumnya, terdapat beberapa orang yang selalu muncul dan memulai chat."

    "Kemudian anggota grup lainnya mulai muncul membalas dengan chat maupun hanya dengan sticker."

    "Scroll-scroll-scroll"

    "Kamu mulai membaca chat dengan timestamp pagi hari ini."

    "Beberapa chat masih berisi candaan antar anggota grup, namun pada beberapa chat terakhir terdapat chat dengan text bold yang dikirimkan oleh Rosianne."

    mc "{i}Untuk mahasiswa dengan DPA Pak Andy, diharapkan dapat hadir di kampus siang ini untuk melakukan bimbingan bersama{/b}."

    "Kemudian kamu membaca chat balasan yang ada di bawah chat tersebut."

    "{i}DPA itu apa guyss?{i}"

    "{i}Maaf, cara cek punya DPA siapa dimana ya{/i}??"

    "{i}DPAku Pak Andy juga nihh, jadinya jam berapa itu siangnya?{/i}"

    "Pertanyaan yang ada tersebut dijawab oleh pengirim pesan tersebut sekaligus."

    "{i}DPA itu Dosen Pembimbing Akademik, intinya yang intinya ya yang bimbing kegiatan akademik kamu selama berkuliah. Kalau mau konsultasi, bimbingan, maupun tanya yang lain baiknya sama DPA kamu{/i}."

    "{i}Kalau mau cek siapa DPA kamu, bisa lihat di website akademik kita {b}Simaster{/b}. Di simasternya nanti pilih menu {b}Akademik kemahasiswaan{/b} => {b}Akademik{/b} => {b}Diskusi DPA{/b}.{/i}."

    mc "{i}Ohh begitu ya cara lihatnya, aku coba dulu lah{/i}."

    hide phone chat with fade
    
    show simaster with fade

    mc "Terus menu akademik kemahasiswaan, akademik, terus diskusi DPA."

    show menuSimaster with dissolve

    mc "Ohhh ternyata DPAku juga Pak Andy."

    show DPA with dissolve

    "Setelah mengecek siapa DPAmu di Simaster, kamu melanjutkan scrolling chat di grupmu."

    "Untuk jam berapanya masih kutanyakan ya teman-temann."

    "{i}Okee Annee{/i}."

    "Chat selanjutnya masih dilanjutkan dengan candaan oleh beberapa tokoh yang ada di grup."

    mc "{i}hmmm sepertinya si Rosianne ini bakal jadi tokoh ketua kelas di angkatan deh{/i}."

    "Scroll-scroll-scroll"

    "{i}Oh ini teman-teman Pak Andy sudah bales chatku!{/i}"

    "{i}Jam berapa tuh Anne?{/i}"

    "{i}Iya jam berapa?{/i}"

    "{i}Kalau yang bukan Pak Andy kita kapan gengs?{/i}"

    mc "{i}Ohh ternyata tidak semua Pak Andy ya?{/i}"

    "{i}Kata Pak Andy nanti siang antara jam 12 sampai jam 1 nih, di Lab TRPL katanya{/i}."

    "{i}Waduh dimana itu..{/i}"

    "{i}Iya dimana itu?{/i}"

    "Chat yang di grup masih bermunculan satu persatu, namun kamu mengabaikannya."

    "Kamu melirik melihat jam yang ada di ponselmu."

    "07.30 adalah waktu yang ditunjukan."

    mc "{i}masih nanti siang yaa, mau apa dulu ya pagi ini?{/i}"

    "Melihat waktu yang masih pagi, dan bimbingan akan diadakan di siang hari kamu memutuskan untuk mengisi waktu pagimu."

    "Kamu memutuskan untuk…."

    hide screen stats_screen

    call screen mapUI

    return

label nothing:

    scene bg black

    "nothing here, you're wrong"


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
