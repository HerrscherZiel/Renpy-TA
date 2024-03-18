﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# label splashscreen:
#     call screen confirm(message="Proceed to play the game?", yes_action=Return(), no_action=Quit(confirm=False))
#     return

define r = Character("Rissa", image="r")
define j = Character("TriJe", image="t")
define mc = Character("You", image="mc")
define w = Character("Warga", image="w")
define pa = Character("Pak Andy", image="pa")
define bn = Character("Bu Nira", image="bn")
define aa1 = Character("Aa'", image="anonM")
define kev = Character("Kevin", image="kev")
define t = Character("Teman", image="t")
define k = Character("Kating", image="t")
define stall = Character("Kak Stand", image="anonM")
define siapa = "Suara"

#nvl
define n = nvl_narrator


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

#status
default obesseCount = 0
default obesse = False

default thinCount = 0
default thin = False

default healthyCount = 0
default healthy = False

default sickCount = 0
default sick = False

default fitCount = 0
default fitt = False

default weakCount = 0
default weak = False

#friends
default rissa_fond = 0
default trije_fond = 0
default kevin_fond = 0

#days
default day = 1
default k_days = 1

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
default capa = '1'
default note = ""

default maps = False
default hima = False
default hima_intro = False


# The game starts here.


label start:
    # $ my_task.addTask(task_eat_your_first_food)
    # $ my_task.addTask(task_choose_best_girl)
    # $ my_task.addTask(task_dont_be_greedy)
    # $ my_task.addTask(task_survive_too_long)

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

    siapa "Halooo… Permisi!!"

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

    call screen tutorial_choices1 with dissolve

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

    "Rissa berjalan dan melambaikan tangannya kepadamu, menyuruhmu untuk mengikutinya."

    "Kamu berjalan di belakang Rissa, kamu mengikutinya ke arah minimarket"

    "Dalam game ini, terdapat {b}menu MAP{/b}, dimana pemain dapat {b}memilih kegiatan{/b} apa yang selanjutnya akan dilakukan, bedasarkan lokasi yang dipilih di map."

    "Pemain dapat memilih kegiatan dengan cara {b}memilih icon{/b} yang ada di map." 

    "Pemain akan berpindah ke lokasi yang dituju, dan melakukan kegiatan sesuai icon yang dipilih."

    call screen tutorial_maps1 with dissolve

    "Setiap memilih suatu kegiatan pada map, maka {b}waktu akan berganti{/b} menjadi fase waktu berikutnya." 
    
    "Pada game ini terdapat 3 jenis waktu, yaitu {b}Pagi -> Siang/Sore -> Malam.{/b}"

    "Setelah melakukan aktivitas pada {b}Malam hari{/b}, maka {b}hari akan berubah.{/b}"

    "Hari, Waktu, dan Tempat dapat dilihat pada bagian {b}kiri atas layar{/b}."

    "Game ini akan berjalan selama {b}30 hari{/b}." 

    "Setelah hari ke 30 selesai, pemain akan mendapatkan ending dari game ini."

    call screen tutorial_daytimes1 with dissolve

    "Sekarang cobalah menggunakan menu Map untuk berpindah ke lokasi berikutnya."

    jump first_map

    return

label first_map:

    scene bg black
    with fade

    pause 2.0
    
    "Untuk memilih kegiatan yang akan dilakukan selanjutnya, kamu dapat mengarahkan pointer ke arah icon yang ada pada {b}Map{/b}."

    "Untuk sekarang pilihlah Icon Minimart, kemudian tekan klik kiri."

    "Lalu pilih opsi pertama untuk menuju lokasi selanjutnya."

    # hide screen days_screen

    call screen mapUI with dissolve
    # ($day, $timephase)

    return

label day2:


    scene bg black
    with Dissolve(2.0)

    pause 3.0

    show day2 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 3.0

    call change_day

    show screen trans_screen with dissolve

    pause 2.0

    scene bg kos morn with dissolve

    show screen stats_screen with dissolve

    show screen days_screen with dissolve

    #alarm sound
    "{i}Kringgggg!!!{/i}"
    with vpunch

    "{i}Kringgg!!!{/i}"
    with vpunch

    "{i}Kringgg!!!{/i}"
    with vpunch

    "Alarmmu berbunyi beberapa kali sebelum kamu bangun dan mematikannya."

    "Dengan mata yang masih sipit, kamu meraba-raba di sekeliling tempat tidurmu."

    "Menggenggam ponsel, kamu melihat banyak notifikasi dari grup chat LANEmu. Kamu mengabaikannya dan matamu fokus untuk mencari waktu yang sudah menunjukan pukul 5 pagi."

    "Melihat sinar matahari yang sudah masuk melalui jendela kamarmu, kamu bangun dan merapikan tempat tidurmu."

    "Setelah selesai merapikan tempat tidur, kamu berjalan ke arah kamar mandi untuk membasuh mukamu."

    show mc normal jacket:
        xalign 0.2 yalign -0.3
    with dissolve

    mc "Uahhhh….. Masih ngantuk…"

    "Sambil menguap, kamu mengggosok-gosok matamu dengan tangan"

    mc "{i}Disini pagi hari begini tidak begitu dingin tapi kok malah keringatan begini ya?!{/i}"

    "Kamu menyadarinya ketika kamu merasakan mukamu dipenuhi dengan minyak"

    mc "Enggak enak sekali bangun bangun muka berminyak seperti ini."

    "Sesampainya di kamar mandi kamu langsung membasuh muka dan menggosok gigimu."

    # Sfx grumbling
    "Grugggg"
    with vpunch

    mc "…. Laparr…."

    "{b}!Stats drop tutorial{/b}!"

    "Beberapa stats yang dimiliki {b}dapat berkurang{/b}."

    "Penyebab berkurangnya stats yang ada dapat dikarenakan oleh {b}pemilihan pilihan{/b} maupun berkurang {b}secara otomatis{/b}."

    "Pemilihan pilihan seperti kegiatan {i}olahraga{/i} dapat mengurangi tingkat {b}energimu{/b} namun menambah tingkat {b}fit{/b}mu."

    "Sementara stats dapat berkurang secara otomatis jika hari berganti, stats yang dapat berkurang secara otomatis adalah main {b}stats kesehatan{/b}."

    call screen tutorial_statsdrops1 with dissolve
    
    "Setelah selesai membasuh muka dan menggosok gigi, kamu kembali ke kamar kosmu."
    
    mc "Aku masih punya makanan sisa tidak ya?"

    "Kamu mencari makanan yang ada di kamar kosmu."

    if rotiAwal == True:
        
        mc "Oh iyaa, kemarin aku masih menyimpan roti, lumayanlah buat sarapan."

        "Kamu mengambil roti yang kamu beli di Minimart kemarin dan langsung memakannya."

        call eat

        "Lumayan buat ganjel perut hehehe."

    else:
        mc "Yahhh tidak ada apa-apa, roti yang kubeli kemarin juga langsung aku makan."

        mc "Apa boleh buat, sekalian nanti siang sajalah makannya."
    
    "Duduk di tempat tidur, kamu mengambil HP dan memainkannya."

    "Kemudian kamu mengingat terdapat banyak notifikasi dari grup chat LANE ketika bangun tadi."

    "Merebahkan tubuhmu di kasur, kamu mengambil ponselmu dan mulai men scroll chat-chat yang ada di grup."

    show phone groupchat:
        yalign 0.5
        xalign 0.8
    with moveinbottom

    "Seperti grup chat pada umumnya, terdapat beberapa orang yang selalu muncul dan memulai chat."

    "Kemudian anggota grup lainnya mulai muncul membalas dengan chat maupun hanya dengan sticker."

    "Scroll"

    "Scroll"

    "Scroll"

    "Kamu mulai membaca chat dengan timestamp pagi hari ini."

    "Beberapa chat masih berisi candaan antar anggota grup, namun pada beberapa chat terakhir terdapat chat dengan text bold yang dikirimkan oleh username bernama Claris."

    mc "{i}Untuk mahasiswa dengan DPA Pak Andy, diharapkan dapat hadir di kampus siang ini untuk melakukan bimbingan bersama{/b}."

    "Kemudian kamu membaca beberapa balasan dari chat itu."

    t normal "{i}DPA itu apa guyss?{i}"

    t "{i}Maaf, cara cek punya DPA siapa dimana ya{/i}??"

    t "{i}DPAku Pak Andy juga nihh, jadinya jam berapa itu siangnya?{/i}"

    "Pertanyaan yang ada tersebut dijawab oleh pengirim pesan tersebut sekaligus."

    "Scroll"

    "Scroll"

    "Scroll"

    t "{i}DPA itu {b}Dosen Pembimbing Akademik{/b}, intinya yang intinya ya yang bimbing kegiatan akademik kamu selama berkuliah. Kalau mau konsultasi, bimbingan, maupun tanya yang lain baiknya sama DPA kamu{/i}."

    t "{i}Kalau mau cek siapa DPA kamu, bisa lihat di website akademik kita {b}Simaster{/b}.{/i}"
    
    t "{i}Di simasternya nanti pilih menu {b}Akademik kemahasiswaan{/b}.{/i}"
    
    t "{i}Lalu akan muncul beberapa submenu, disitu nanti pilih menu {b}Akademik{/b}.{/i}"
    
    t "{i}Kemudian akan muncul lagi banyak sub menu, pilih menu {b}Diskusi DPA{/b}, nanti akan kelihatan siapa DPA kita.{/i}."

    mc "{i}Ohh begitu ya cara lihatnya, apa aku coba juga ya?{/i}."

    call screen simaster_dpa with dissolve

    "Setelah membaca informasi yang kamu dapat dari grup chat, kamu ikut mencoba mengecek siapa dosen pembimbingmu."

    hide phone chat with moveoutbottom

    "Membuka browsermu, kamu berhasil masuk kedalam beranda Simaster."

    window show

    show home simaster:
        xalign 0.9
        yalign 0.4     
    with dissolve

    mc "Dari beranda kemudian...."

    mc "Oh iya pilih menu Akademik Kemahasiswaan."

    hide home simaster

    show home akademik:
        xalign 0.9
        yalign 0.4     
    with dissolve

    mc "Dari menu Akademik terus apa ya?"

    mc "{i}Habis itu pilih Menu Akademik {/i} Ohhh iya...."

    hide home akademik

    show home akademik dpa:
        xalign 0.9
        yalign 0.4     
    with dissolve

    mc "Terus pilih diskusi...."

    mc "Diskusi DPA.... oh ketemu."

    hide home akademik dpa

    show diskusi dpa:
        xalign 0.9
        yalign 0.4     
    with dissolve

    mc "Ohhh ternyata DPAku juga Pak Andy."

    "Setelah mengecek siapa DPAmu di Simaster, kamu kembali membuka groupchat Lanemu untuk membaca chat yang ada dibawahnya."

    hide diskusi dpa with dissolve

    t "{i}Untuk jam berapanya masih kutanyakan ya teman-temann{/i}."

    t "{i}Okee Clariss{/i}."

    "Scroll"

    "Scroll"

    "Chat yang ada dibawahnya dilanjutkan dengan candaan oleh beberapa orang yang ada di grup."

    mc "{i}Hmmm sepertinya si Claris ini bakal jadi tokoh ketua di angkatan deh{/i}."

    mc "{i}Belum masuk kuliah aja sudah jadi informan begini..{/i}"

    "Scroll"

    "Scroll"

    t "{i}Oh ini teman-teman Pak Andy sudah bales chatku!{/i}"

    t "{i}Jam berapa tuh Claris?{/i}"

    t "{i}Iya jam berapa?{/i}"

    t "{i}Kalau yang bukan Pak Andy kita bimbingannya kapan gengs?{/i}"

    mc "{i}Ohh ternyata tidak semua mahasiswa DPAnya Pak Andy ya?{/i}"

    mc "{i}Hmmm iya juga sih, satu angkatan banyak mahasiswa kalau dosen pembimbingnya cuma satu gamungkin sih...{/i}"

    t "{i}Kata Pak Andy nanti siang antara jam 12 sampai jam 1 nih, di Lab TRPL katanya{/i}."

    t "{i}Waduh dimana itu..{/i}"

    t "{i}Iya dimana itu?{/i}"

    "Chat yang ada di grup masih bermunculan satu persatu, namun kamu mengabaikannya."

    "Kamu melirik melihat jam yang ada di HPmu."

    "Waktu telah menunjukan pukul 07.30."

    mc "{i}Masih nanti siang yaa bimbingannya, mau ngapain dulu ya pagi ini?{/i}"

    "Melihat waktu yang masih pagi, dan bimbingan akan diadakan di siang hari kamu memutuskan untuk mengisi waktu pagimu."

    "Kamu memutuskan untuk…."

    window hide

    $ prologueCount += 1
    #go to kampung
    call screen mapUI with dissolve

    return

label day3:

    scene bg black
    with Dissolve(1.0)

    pause 2.0

    show day3 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 2.0

    hide day3 pro with dissolve

    call change_day

    show screen trans_screen with dissolve

    pause 2.0

    scene bg kos morn with dissolve

    show screen stats_screen with dissolve

    show screen days_screen with dissolve

    "Bangun dari tidurmu, rutinitas yang pertama kamu lakukan setelah membuka mata adalah membuka smartphone."
    
    "Lalu melirik ke arah jam digital untuk mengetahui jam ketika dirimu bangun."

    "Kemudian masih dalam keadaan linglung kamu bangun dari posisi tidur ke posisi duduk."
    
    "Selama beberapa menit kamu terdiam di posisi yang sama untuk mengumpulkan niat pada pagi hari."

    "Setelah mengumpulkan niat, kamu berdiri dan berjalan menuju kamar mandi untuk membasuh muka."

    "Ketika berjalan ke kamar mandi kamu melewati kamar-kamar kos lain."

    "Seperti beberapa hari sebelumnya, kamu melihat satu kamar kos yang masih terkunci rapat."
    
    "Sementara kamar yang sudah berpenghuni, kebanyakan penghuninya belum menampakan diri." 
    
    "Entah mereka masih tertidur atau mereka sudah berangkat pagi-pagi."

    "Karena memungkinkan jika beberapa dari penghuni kos sudah mulai bekerja bukan seorang mahasiswa lagi."

    scene bg black with dissolve

    #sfx shower

    "…………."

    "….."

    "…………"

    scene bg kos morn with dissolve

    "Kembali dari kamar mandi, kamu langsung mengambil HPmu dan membuka group Lane." 
    
    "Sebelumnya kamu melihat notifikasi di group chat Lane mu ketika bangun tidur."

    show phone groupchat:
        xalign 0.5
        yalign 0.4    
    with fade

    "Scroll"

    "Scroll"

    "Scroll"

    "Seperti biasa group chat dipenuhi oleh gurauan mahasiswa-mahasiswa lain." 
    
    "Berbagai stickers dan meme memenuhi kebanyakan isi chat yang ada dalam group."

    "Namun kondisi group chat saat ini sudah agak berbeda dengan beberapa hari lalu, ketika masih melakukan kegiatan orientasi."

    "Satu-persatu anggota baru masuk, jumlahnya sekarang sudah hampir 90an orang."

    "Selain anggota yang makin bertambah, kamu juga melihat sepertinya orang-orang yang ada di dalam group sudah sedikit lebih mengenal satu sama lain."

    "Terlihat dari bagaimana cara mereka berbalas chat satu sama lain."

    "Entah karena mereka sudah menyempatkan waktu untuk bertemu satu sama lain atau mereka sudah hafal satu sama lain selama mereka ada di group chat ini."

    "Satu dua chat perkenalan dikirim ke dalam group chat oleh para pendatang baru." 
    
    "Kemudian para penghuni lama menyambut satu-persatu."

    "Menelusuri banyak chat yang baru, kamu akhirnya melihat salah satu chat yang dikirim oleh username Rosainne."

    "Rossaine yang kamu kenal dengan nama Rissa telah mengirimkan chat yang berisi:"

    nvl show dissolve

    n "{i}Ini Pak Andy ngirim ke aku begini:{/i}"

    n "Berikut {i}Kode Mata Kuliah{/i} - {i}Nama Mata Kuliah{/i} - {i}Kelas{/i}"
    n "Pastikan memilih sesuai kode yang diberikan, untuk kelas jika kapasitas sudah penuh bisa ambil kelas yang lain."
    n "Jika ada masalah atau kendala, bisa hubungi saya atau bagian akademik kampus."

    nvl clear
    
    n "SVPL01011 - Algoritma dan Pemrograman Dasar I - PL1AA"
    n "SVPL02012 - Pengantar Teknologi Informasi - PL1AA"
    n "SVPL04010 - Desain Elementer - PL1AB"
    n "SVPL01013 - Struktur Data I - PL1AA"
    n "SVPL01014 - Basis Data I - PL1AA"
    n "SVPL02013 - Pemrograman Web I - PL1AB"
    n "SVPL01016 - Pemrograman Berbasis Objek I - PL1AA"
    n "SVPL02014 - Jaringan Komputer I - PL1AB"
    
    nvl clear
    
    n "{i}Total ada 8 mata Kuliah ya temen-temen.{/i}"
    n "{i}Caranya seperti yang dikatakan Pak Andy kemarin, lewat Simaster lalu akademik lalu Pengisian KRS{/i}"
    n "{i}Itu nanti kalau mau ngisi bareng-bareng bisa ke Perpustakaan Pusat.{/i}"
    n "{i}Kalau mau coba sendiri-sendiri juga enggak apa, kalau ada pertanyaan bisa tanya langsung ke Pak Andy atau tanya aku nanti aku tanyain.{/i}"
    # n "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    
    nvl hide dissolve

    mc normal jacket "Hmmm pada mau bareng-bareng enggak ya?"

    mc "Coba sendiri nanti bingung, tapi kalau bareng-bareng juga males keluarnya."

    "Melanjutkan membaca chat yang ada di grup, terdapat beberapa balasan dari teman seangkatanmu."

    t normal "{i}Rosa perpustakaan pusat itu yang deket sama Graha itu kan?{/i}"

    r normal2 "{i}Iya, nanti kalau udah disana ku share lokasinya.{/i}"

    t "{i}Jam berapa tuuh?{/i}"

    r normal2"{i}Enaknya jam berapa man-temans?{/i}"

    t "{i}Agak siangan aja Ros.{/i}"

    t "{i}Aku jam 9 lebih baru bisa gas.{/i}"

    t "{i}Jangan siang-siang tapi, takut kalau hujan maless…{/i}"

    r "{i}Jam 10 sih bisaa, gimana yang lain?{/i}"

    t "{i}Iya jam 10 aja gimana? {/i}"

    t "{i}Okee gass.{/i}"

    t "{i}Siappp{/i}"

    r "{i}Jam 10 ya noted.{/i}"

    mc "Apa aku sekalian kucoba sekarang aja apa ya?"

    mc "Kalau bingung tinggal tanya si Rissa saja lah nanti."

    "Memutuskan untuk mencoba melakukan pengisian KRS, kamu mengambil laptop yang berada di dalam tas dan menghidupkannya."

    "Menunggu beberapa menit hingga laptopmu selesai booting, kamu membuka browser dan membuka halaman Simaster."

    "Setelah halaman terbuka kamu memasukan username dan password yang kamu terima dari kampus." 
    
    "Kemudian memasukan captcha yang muncul sebelum pada akhirnya berhasil masuk ke dalam Simaster menggunakan akunmu."

    hide phone groupchat

    show home simaster:
        xalign 0.5
        yalign 0.4    
    with dissolve
    
    mc "Hmm setelah masuk kemudian menu apa ya… "
    
    mc "Oh iya {i}Akademik kemahasiswaan{/i}.. {i}Akademik{/i}… oh ini di kiri atas."

    hide home simaster

    show home akademik:
        xalign 0.5
        yalign 0.4    
    with dissolve 
    
    mc "Lalu habis itu menu {i}Akademik{/i}… Lalu..."

    hide home akademik

    show home akademik krs:
        xalign 0.5
        yalign 0.4    
    with dissolve 
    
    mc "Hmm habis ini kalau kata Pak Andy masuk ke menu {b}Pengisian KRS{/b}."

    hide home akademik krs

    show pengisian krs:
        xalign 0.5
        yalign 0.4    
    with dissolve 
    
    "{i}GRUGRUGRUGRUGRU{/i}"

    with vpunch

    mc "Ughhhh"

    "Suara perutmu terdengar pertanda tubuhmu memerlukan pasokan makanan."

    mc "Ughh… keroncongan begini pagi-pagi."

    mc "Cari sarapan dulu apa ya?"

    hide pengisian krs

    "Tuing"

    "Kamu mendengar suara notifikasi dari HPmu."

    show phone groupchat:
        xalign 0.5
        yalign 0.4    
    with dissolve

    "{i}[name] kamu nanti ikut isi KRS barengan di perpustakaan apa enggak?{/i}"

    "Notifikasi yang kamu baca barusan, dikirim oleh nomor yang belum kamu simpan."

    "Penasaran, kamu membuka aplikasi Lane mu, tidak langsung membaca chat dari nomor yang belum kamu simpan."
    
    "Namun membuka group Lanemu dan mencari anggota dengan nomor yang baru saja mengechatmu."

    "Scroll"

    "Scroll"

    "Scroll"

    mc "Ahhh ternyata nomor si Rissa tah"

    "Mengetahui siapa pengirim chat dengan nomor tersebut yang ternyata memiliki username Rossaine atau yang lebih kamu kenal dengan Rissa."

    "Kamu langsung membuka chatnya dan menyimpan nomor Rissa." 

    mc "Kubalas gimana yaa ?"

    menu:

        "Ikut KRS Bersama":
            $KRS3 = True
            $KRS = False

            mc "Mungkin ikut nanti, kabari ya kalau sudah pada sampai sana Riss."

        "KRSan Sendiri":
            $KRS3 = False
            $KRS4 = True
            mc "Kayaknya enggak dulu deh, aku tanya aja ya kalau bingung ke kamu hahaha."
    
    mc "Kirim."

    hide phone groupchat

    "Setelah membalas chat dari Rissa kamu mengganti pakaianmu dan keluar dari kamar untuk mencari makan."

    mc "Cari makan dimana ya enaknya pagi-pagi begini."

    mc "Kalau keluar pake motor masih muter-muter juga, bensinnya juga lupa seberapa."

    "Mengecek bensin yang ada di motormu, terlihat indikator berada di bagian warna merah"

    "Kamu teringat sudah hampir seminggu sejak kamu terakhir mengisi bensin pada motormu."

    mc "Hmmm, kalau sekalian isi bensin sih mengding keluar jauh sekalian juga."

    mc "Apa coba warmindo sebelah ya?"

    "GRUGRUGRUGRU"
    with vpunch

    mc "Yaudahlah, sambil nyoba siapa tahu enak."

    "Sudah berganti ke pakaian yang lebih rapi, kamu berjalan menuju warmindo terdekat."

    scene bg town street 1 with fade

    "Sesampainya di warmindo yang dekat dari tempat kos, menu dan harga terpampang digantung di dinding warung."

    "Selagi asik memilih menu, kamu melihat salah satu menu yang belum pernah kamu lihat sebelumnya."
    
    "Menu tersebut yaitu mie dok dok."

    mc normal jacket "Mas mie dok-dok itu gimana ya?"

    "Melihat penjaga warung yang sudah siap dengan pesananmu, kamu menanyakan tentang menu itu."

    aa1 "Itu mie goreng begitu a’, tapi nanti dicampur sama bumbu sama telur dan nanti disajikannya berkuah, simplenya sih begitu."

    mc "Wah boleh itu mas, satu ya."

    aa1 "Siap a’ pedes atau tidak mienya?"

    mc "Pedes, sama minumnya Es Teh Tarik ya."

    aa1 "Oke mie dok-dok pedes, sama es teh tarik."

    "Tidak perlu teralalu lama, pesananmu sudah siap untuk di hidiangkan."

    "Mie goreng berkuah yang kamu pesan ada di depanmu."

    "Slurppp"

    mc" Panass, tapi enak juga ternyata mie goreng dikuahin begini."

    "Kamu menikmati waktu sarapan pagimu ini."

    aa1 "Mahasiswa baru ya a’?"

    mc "Iya mas, baru masuk ini."

    "Tidak ada orang lain selain dirimu, penjaga warung membuka percakan denganmu."

    mc "Biasanya kalau warung ini buka tutupnya jam berapa ya?"

    aa1 "Biasanya sih kalau saya bangun pagi ya jam 6 kurang sudah buka."

    mc "Wah bangun pagi terus ya mas."

    aa1 "Ya begitu sih aa'"

    aa1 "Kalau tutupnya biasanya jam 1 atau jam 2 malam gitu."

    mc "Ohhh…. Sampai malam juga ya ternyata."

    mc "{i}Kalau buka tutup jam segitu sih aman ya kalau lapar malam-malam atau pagi-pagi begini.{/i}"

    "Menghabiskan waktu dengan percakapan basa-basi dengan penjaga warung warmindo, tidak terasa apa yang disajikan di depanmu sudah habis."

    call eat 
    
    "Kamu menikmati sarapanmu dengan santai sambil bermain HP."

    "Hingga jam digital yang terdapat pada HPmu menunjukkan pukul 08.45."

    mc "{i}Oh udah jam segini aja, habis ini pulang langsung mandi lah biar badan segar.{/i}"

    "Memutuskan untuk pulang, kamu berdiri dan mengeluarkan dompet untuk membayar pesananmu."

    mc "Jadi berapa itu mas?"

    aa1 "Mie dok-dok sama es tah tarik ya?"

    mc "Iya."

    aa1 "10.000 sama 4500, 14.500 a’."

    mc "Ini mas uangnya, pas ya."

    aa1 "Terimakasih aa’"

    "Setelah membayar kamu berjalan menuju ke kosanmu, untuk mandi dan melakukan kegiatan berikutnya."

    if KRS3 == True:
        jump persiapan_krs
    
    else:
        $prologueCount += 1
        $KRS4 = True
        call screen mapUI with dissolve

    return

label day4:
    scene bg black
    with Dissolve(1.0)

    pause 2.0

    show day4 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 2.0

    hide day4 pro with dissolve

    call change_day

    pause 2.0

    scene bg kos morn with dissolve

    show screen stats_screen with dissolve

    show screen days_screen with dissolve

    #SFX alarm

    "Nggtttt"
    with hpunch

    "Nggttttt"
    with hpunch

    "Ngtttttttt"
    with hpunch

    "HPmu bergetar selama beberapa detik sebelum mengeluarkan suara ringtone alarm mengeluarkan bunyi yang membuatmu terbangun dari tidur."

    mc normal jacket "Hmmhhh..."

    "Membuka mata, kamu memaksa badanmu untuk bangun dan duduk di pinggir tempat tidurmu."

    "Meraba-raba disekitar tempat tidurmu, mencari HPmu yang masih terus mengeluarkan suara." 
    
    "Kamu mengambilnya kemudian menggeser layar HP ke atas untuk menghentikan alarm yang aktif."

    "Jam digital yang ada pada HPmu sudah menunjukan pukul 05.10. Jam dimana biasanya kamu bangun tidur setiap harinya."

    mc "Huahhhhh"

    "Menguap, kamu beranjak dari tempat tidur dan berjalan menuju ke kamar mandi."
    
    "Berjalan sembari mengusap-usap mukamu, kamu menengok ke arah kamar-kamar kos yang ada disekitar."

    mc "Emang yang punya kamar belum dateng ya, apa kosong sih itu kamar? Perasaan waktu mau ambil ini kos ibu kos cuma bilang 1 kamar aja yang kosong."

    "Kamu masih melihat terdapat satu kamar yang masih terkunci rapat dan belum ada tanda penghuni yang menempatinya."

    "Sampai di kamar mandi, seperti biasa kamu melakukan kebiasan pagi harimu."

    "Setelah menyelesaikan kegiatan di kamar mandi, kamu kembali menuju kamarmu."
    
    "Ketika berjalan, terdengar suara mesin motor yang mendekati bangunan kos."

    "Suara motor itu berhenti tepat di depan pintu gerbang masuk ke dalam kos."

    "Srekkkkkkkk"

    "Tak lama kemudian gerbang masuk kos dibuka, setelah pintu gerbang dibuka, pengemudi motor itu masuk mendorong motornya."

    "Menengok ke arahmu, kalian berdua saling bertatap muka."

    "Menyadari dirimu yang berada diluar kamar, pengemudi motor itu menganggukkan kepalanya kepadamu." 
    
    "Kamupun membalas anggukan kepala kepada pengemudi motor yang baru saja masuk itu."

    "Setelah menganggukkan kepalamu, kamu masuk ke dalam kamar."

    scene bg kos morn with fade

    "Seperti biasa setelah kembali dari kamar mandi, kegiatanmu di pagi hari selanjutnya adalah mengecek chat yang ada di grup Lane."

    "Scrolll"

    "Scrolll"

    "Scrolll"

    "Kamu membaca beberapa chat mengenai pengisian KRS." 
    
    "Rata-rata teman seangkatanmu mempertanyakan mengenai proses pengisiannya, kemudian satu persatu pertanyaan itu dijawab oleh Rissa."

    if KRS3 == True:

        "Selesai membaca dan mencari informasi yang ada di group chat, kamu mengeklik icon aplikasi sosial media lain yang ada di hpmu."


    else :

        "Belum melakukan KRS, kamu membaca satu persatu pertanyaan mengenai proses pengisian KRS itu."
        
        "Membaca satu persatu pertanyaan dan jawaban dari Rissa dengan teliti." 
        
        "Setelah memahami informasi tambahan mengenai pengisian KRS tersebut, kamu kemudian mencatat langkah-langkah penting pada kertas note."

        "Selesai mencatat informasi yang ada di group chat, kamu menutup aplikasi Lane lalu mengeklik icon aplikasi sosial media lain yang ada di HPmu."

    "Kamu membuka aplikasi PhoGram dimana orang-orang dapat mengunggah foto atau video mereka ke sosial media. Kemudian pengguna lain melihat apa yang kamu unggah pada aplikasi, lali dapat berinteraksi dengan unggahan yang ada."

    "Terdapat berbagai macam konten yang ada pada sosial media tersebut yang membuatmu memainkan dengan waktu yang lama."
    
    "Terlalu menikmati konten yang ada, tanpa sadar waktu telah cepat berlalu tanpa kamu menyadarinya, hingga kamu tersadar setelah perutmu berbunyi."

    "GRUGRUGRUGRU"
    with vpunch

    mc normal jacket "Ughhh… oh iya, sarapan-sarapan."

    mc "Nonton konten isinya makanan semua begini jadi keinget belum sarapan."

    mc "Makan kemana ya? Kalo pesen jam segini masih sedikit pilihannya."

    "Kamu sempat memikirkan untuk mengorder makanan. Namun pilihan makanan yang ada ketika pagi hari kamu rasa kurang banyak, sehingga kamu mengurungkan niatmu."

    "Jam digital yang ada pada HPmu masih menunjukkan pukul 8.30."

    mc "Keluar pakai motor males, ke warmindo aja lah."

    "Pada akhirnya kamu memutuskan untuk sarapan di warmindo yang ada di dekat kosan."

    "Memutuskan untuk pergi sarapan di warmindo yang ada di dekat kos, kamu beranjak dari tempat tidurmu dan berjalan menuju warmindo."

    "Tokk tokk tokk"

    #SFX knock

    "Belum sampai kamu membuka pintu kamar, terdengar suara seseorang mengetuk pintu kamar kosmu dari luar."

    mc "Sebentar..."

    "Membuka pintu kamar, terdapat seorang laki-laki yang tidak kamu kenal berdiri di depan kamarmu."

    siapa "Permisi.."

    mc "Iya mas, ada apa ya?"

    siapa "Oh ini saya bawa makanan dari rumah, buat dibagi untuk anak-anak kos sini."

    "Tetangga kosmu itu terlihat membawa kantong plastik besar yang di dalamnya terdapat box-box putih."

    "Mengambil salah satu box dari dalam kantong plastik, kemudian ia mengulurkan tangannya yang memegang box putih itu kepadamu."

    mc "Wah makasih banget mas, kebetulan pas mau cari makan juga hehe. Oh iya ini sama mas siapa ya? Saya [name]"

    siapa "Saya Kevin mas, masnya baru masuk kos tahun in ya?"

    mc "Iya, mahasiswa baru saya, kalau masnya?"

    kev  "Tahun kemarin masuk sini saya, kamar saya yang pojok deket kamar mandi yang bagian kiri itu mas."

    mc "Ohh disitu…"

    kev "Kalau gitu yaudah mas, tak bagiin ke yang lain juga ya."

    mc "Oke mas, makasih ya ini."

    kev "Iya mas, sama-sama."

    show screen get_box2 with dissolve

    "Cklekk"

    "Menutup pintu, kamu duduk dan menaruh box makanan itu di meja belajar." 

    mc "Lumayan..... rezeki emang enggak kemana. Dari kemarin dapat makan gratis terus."
    
    "Dengan hati yang senang, kamu segera membuka apa yang ada di dalam kotak makanan itu."

    "Kotak yang barusan kamu buka tersebut berisikan berbagai macam donat, tanpa pandang bulu kamu mulai mengambilnya satu persatu."

    "Meletakan hp di meja belajar, kamu memutar video di internet untuk menemani sarapanmu."

    call small_eat

    "Setelah selesai sarapan, tepatnya pukul 9 lebih kamu mengambil handuk yang ada pada gantungan pakaian dan keluar kamar untuk mandi pagi."

    if KRS3 == True:

        scene bg kos morn with fade

        "Siang harinya selesai mandi, kamu merasa bosan karena tidak ada satupun hal yang bisa kamu lakukan." 
        
        "Kamu berniat melakukan kegiatan untuk mengisi waktu di siang hari ini."

        "Kamu memutuskan untuk:"

        call screen mapUI
    
    else:

        hide screen days_screen

        hide screen stats_screen

        jump kos_krs4
    
    return

label day5:

    call change_day
    pause 2.0
    show screen stats_screen with dissolve
    show screen days_screen with dissolve
    scene bg kos morn with dissolve

    "Udara dingin dipagi hari membuatmu terbangun dari tidurmu. 
    Rasa dingin yang terasa menusuk tulang dan suara kokokan ayam yang saling berpadu tidak memberimu kesempatan lain untuk kembali tidur."

    "Duduk termenung di tempat tidur, kamu mengambil HP yang terletak disebelahmu. 
    Tidak ada alasan khusus yang membuatmu harus melihat layar HP ketika baru saja bangun dari tidur, hanya kebiasaanmu mengisi waktu ketika baru saja terbangun."

    "Kamu tidak melihat adanya satupun notifikasi khusus, hanya terlihat tulisan note yang ada di HPmu."

    "{b}Masuk kuliah! jam 7.15{/b}"

    mc normal jacket "Ahh iya, hari ini aku sudah mulai ada kelas kuliah ya.... Huh...."

    "Rasa gugup dan tidak sabar saat ini sedang mengisi perasaanmu. 
    Gugup karena tidak tahu apa yang nanti akan kamu dapatkan dan lakukan pada perkuliahan, 
    dan tidak sabar menunggu untuk melakukan aktivitas perkuliahan itu sendiri."

    "Beranjak dari tempat tidurmu, pagi hari ini kamu berinisiatif untuk mengemas apa yang kamu perlukan di perkuliahan nanti."

    mc "Kira-kira aku perlu bawa laptop enggak ya? Apa nggak usah? 
    Tapi biasanya di kuliah-kuliah orang-orang kan pada bawa laptop ya? Apa kubawa aja lah, siapa tahu kepakai…"

    "Setelah berdebat dengan pikiranmu sendiri, kamu memutuskan untuk membawa laptopmu ke kelas nanti. 
    Kemudian kamu mulai menyiapkan apa yang sekiranya kamu butuhkan waktu perkuliahan."

    mc "Buku, alat tulis, ohh iya nanti buku pelajaran pakai apa ya kalau kuliah? Kalau waktu dulu kan di sekolah dipinjami sama perpus... Hmmm"

    "Selesai mempersiapkan semua yang dirasa perlu dibawa untuk kuliah, kamu membuka kembali group chat Lanemu."

    r normal2 "Teman-teman untuk kelas PLIAA nanti kuliahnya di ruang U203 yaa!!! Semangat hari pertama masukk!!"

    "Rissa mengirim pesan informasi untuk kelas nanti, dibawah chat Rissa juga sudah banyak balasan dari teman-teman kelasmu yang lain."

    "Matamu melirik ke arah jam digital yang ada di HPmu. Sekarang waktu sudah menunjukkan pukul 04.30 pagi."

    "Kamu terbangun pukul 4 kurang tadi pagi, dan menggunakan waktumu untuk mempersiapkan peralatan untuk kuliah hingga beberapa waktu lalu."

    "Karena kelas pagi dimulai pukul 07.15 dan masih ada sekitar 2 jam lebih sebelum kelas dimulai kamu memikirkan untuk melakukan aktivitas lainnya untuk mengisi waktu terlebih dahulu."

    "Sebelum memutuskan kegiatan selanjutnya, seperti biasa kamu melakukan kebiasaan pagi harimu di kamar mandi."

    $prologue = False
    # $ timephase = 3
    call screen mapUI with dissolve

label day28:
    
    call change_day
    $placeKeys = 3
    show screen trans_screen with dissolve
    scene bg kos night with fade
    pause 2.0

    "Sepulang dari bioskop, kini kamu telah merebahkan badan di tempat tidurmu."

    "Kamu memandang langit-langit kosan dan memikirkan kuliahmu selama satu tahun ajaran ini."

    "Awalnya memang semua terasa sangat baru untukmu, namun lama kelamaan semuanya terasa biasa saja."

    "Dan dalam lubuk hatimu kamu juga merasakan kebosanan dari pengulangan-pengulangan yang terjadi tiap harinya."

    "Meskipun begitu, kamu tetap merasa bersyukur telah melewati perkuliahan satu tahun ini."

    "Entah bagaimana hasil yang kamu dapatkan, tapi paling tidak kamu telah melewatinya."

    "Hari ini adalah hari terakhir ujian dilaksanakan, yang berarti sudah tidak ada lagi perkuliahan hingga pergantian semester nanti."

    "Kini kamu hanya tinggal menikmati waktu liburan sembari menunggu hasil kuliahmu keluar."

    "Setelah lama berpikir dan menikmati waktu malam harimu di tempat tidur, kini rasa kantuk telah menyelimutimu."

    "Kamu memutuskan untuk mengakhiri harimu dan tidur."

    scene bg black  with fade

    call change_day

    show screen trans_screen with dissolve
    scene bg kos morn with dissolve
    pause 2.0

    with vpunch
    with vpunch

    "Pagi harinya, kamu terbangun oleh suara  alarm harianmu yang selalu berbunyi pada waktu yang sama."

    "Dengan rasa kantuk yang masih membuat kepalamu berat, kamu paksakan untuk bangun dan melakukan peregangan."

    "Kamu mengambil HPmu yang masih terus berdering dengan suara alarm."

    "Setelah mematikan alarm, kamu melihat sudah banyak notifikasi pesan masuk yang terdapat pada aplikasi Lane."

    "Hari ini merupakan hari perayaan selesainya ujian akhir yang diadakan minggu lalu."

    "Seharusnya acara yang akan diadakan hari sudah ditentukan oleh teman-temanmu."

    "Kamu kemudian membuka aplikasi Lane dan membaca chat yang sudah terdapat di dalamnya sejak semalem."

    "Setelah membaca cukup banyak percakapan untuk saling merekomendasikan apa yang akan dilakukan untuk kegiatan tersebut, akhirnya teman sekelasmu setuju untuk melakukan sebuah pesta pada suatu rumah makan."

    "Tempat tersebut telah disewa mulai pukul 11 pagi hingga pukul 4 sore. Siapapun yang ingin ikut hanya tinggal datang dan membayar uang sewa yang sudah ditentukan."

    "Di acara tersebut kita akan disediakan menu makanan dan minuman untuk masing-masing peserta. Selain itu terdapat beberapa permainan board games yang dapat dimainkan untuk mengisi waktu luang. "

    "Jika tidak kita bisa hangout dan menghabiskan waktu dengan mengobrol dengan teman sekelas."

    "Selain chat yang terdapat pada grup Lanemu, terdapat pesan masuk lainnya dari [r]."

    "‘Hai… jadi gimana? Nanti ikut enggak ke pestanya?’ merupakan pesan yang dikirimkan oleh [r] untukmu."

    "Selain tersebut terdapat beberapa pesan di bawahnya yang berisi lokasi dan informasi detail mengenai pesta tersebut."

    "Kemudian pada pesan terakhir [r] mengirimkan ‘Kalau bisa dijawab segera ya, biar bisa tahu nanti kira-kira butuh apa aja, kutunggu!’."

    "Dengan begitu kamu harus mengirimkan jawabanmu secepat mungkin untuk mempermudah teman-temanmu yang mengurus penyewaan tempat untuk pesta tersebut."

    "Kamu masih memikirkan apa yang akan kamu jawab, apakah kamu akan menghadiri pesta tersebut atau tidak."

    "Berdiam sejenak kamu memikirkan apa yang akan kamu tulis pada pesan balasan tersebut."

    scene bg black with fade

    if social >= 70: 

        "Setelah mengirimkan balasan kamu melanjutkan aktivitas pagi seperti biasanya."

        "Tidak lama setelah kamu pergi menuju kamar mandi, HPmu bergetar pertanda terdapat pesan masuk."

        "‘Oke! Nanti aku kabarin lagi yaa…’"

        "Terlihat pada notifikasi pesan Lane yang muncul pada layar HPmu."

        jump pesta_akhir

    else:

        "Setelah mengirimkan balasan kamu melanjutkan aktivitas pagi seperti biasanya."

        "Tidak lama setelah kamu pergi menuju kamar mandi, HPmu berdering yang menandakan terdapat pesan masuk untuk dirimu."

        "‘Yahhh! Tapi kalau mau nyusul, tinggal berangkat aja yaa…’"

        "Terlihat pada notifikasi pesan Lane yang muncul pada layar HPmu."

        "Setelah mengirim balasan kamu pergi menuju kamar mandi untuk melakukan aktivitas pagimu seperti biasanya"

        call screen mapUI with dissolve

label day29:

    $placeKeys = 3
    show screen trans_screen with dissolve
    scene bg kos night with fade
    pause 2.0

    "Selesai dengan aktivitas malammu, kini dirimu sedang memainkan HP di meja belajar kosan."

    "Membuka aplikasi Lane, kamu mendapati banyak notifikasi pesan di grup kelasmu."

    "Setelah membuka pesan grup kelasmu itu, kebanyakan pesan membahas pesta kelas yang tadi siang diadakan."

    "Kebanyakan mahasiswa di kelasmu mengikutinya, sehingga bukan menjadi hal yang aneh ketika kegiatan tersebut dibicarakan lagi."

    "Terlihat pesta kelas yang diadakan tadi siang diminati oleh banyak teman kelasmu."

    "Menscroll pesan sampai pesan yang paling baru, kini teman-temanmu sedang membahas pembayaran bagi yang mengikuti kegiatan tersebut."

    "Karena pembayaran dilakukan setelah acara selesai, maka sedang dilakukan pendataan di grup kelas."

    "Terdapat list dari temanmu yang mengikuti pesta kelas tersebut, untuk yang sudah membayar terlihat ikon centang di sebelah kanan namanya."

    "Kamu tidak  lupa membayar bagianmu untuk pesta yang tadi siang kamu ikuti."

    "Dapat dilihat ikon centang juga sudah terdapat di sebelah kanan namamu yang terdapat dalam list mahasiswa yang datang ke pesta."

    "Setelah merasa cukup membaca pesan pada Lane, kamu beranjak dari meja belajar dan merebahkan tubuhmu untuk tidur."

    "Setelah selesai mengatur alarm, ketika kamu akan mengunci HPmu, tiba-tiba terdapat pesan masuk dari [r]."

    "Kamu tidak langsung membuka pesan itu, kamu hanya membacanya saja melalui jendela pop  up dari notifikasi."

    "“[name] besok ada kelas tambahan untuk pengembangan game, bukan kelas sih lebih ke kakak tingkat mau berbagi ilmu…”"

    "“Jadi kalau bisa datang yaa… ikut ngeramain acara sama nambah ilmu kan lumayan hehe…”"

    "“Kutunggu yaa besok!!”"

    "Sesuai isi pesan yang baru saja kamu baca, besok akan diadakan semacam kelas tambahan mengenai pengembangan gim."

    "Sebenarnya kamu tertarik dengan materi yang akan dibawakan besok, namun untuk mengikutinya kamu masih memikirkannya."

    "Meskipun tidak ada kejelasan mengenai lokasi kegiatan tersebut, kamu menebak seharusnya kegiatan tersebut akan dilakukan di kampus."

    "Untuk sekarang kamu memilih untuk tidak memikirkan apakah kamu akan mengikutinya atau tidak, memejamkan matamu kamu memilih untuk mengakhiri malam ini."

    "Day [day] END"

    scene bg black with fade

    call change_day

    show screen trans_screen with dissolve
    scene bg kos morn with dissolve
    pause 2.0

    "Pagi harinya seperti pagi-pagi sebelumnya kamu terbangun setelah alarm dari HPmu berbunyi selama beberapa detik."

    "Mengingat kini sudah memasuki hari libur dari perkuliahan kamu memilih untuk melanjutkan tidurmu lagi."

    "Zzzzzz"
    with vpunch
    "Zzzzzz"
    with vpunch

    "Zzzzz"
    with vpunch
    "Zzzzz"
    with vpunch

    "Getaran dari HPmu ketika alarm berbunyi membangunkanmu untuk kedua kalinya pada pagi ini."

    "Kamu masih merasa sangat mengantuk dan malas untuk beraktivitas pada pagi hari ini. Kamu ingin bermalas-malasan sedikit lebih lama di hari liburmu."

    "Untuk kedua kalinya kamu memejamkan matamu kembali setelah menunda dan memundurkan waktu di alarm yang di HPmu."

    "Merasa matamu masih memerlukan beberapa menit untuk diistirahatkan kembali."

    Zzzzzz
    with vpunch
    Zzzzzz
    with vpunch

    Zzzzzz
    with vpunch
    Zzzzzz
    with vpunch

    "Untuk ketiga kalinya di pagi hari ini, alarmmu berbunyi dan untuk ketiga kalinya juga di pagi hari ini kamu terbangun oleh deringan dan getaran dari alarmmu."

    mc normal jacket "Huhhhhh"

    mc "Maless bangettt…."

    mc "Kenapa tidur waktu tidur begini kaya cepet banget sih… perasaan aku nyetting alarmnya juga lamaan…."

    "Setelah mengeluh untuk beberapa saat kamu beranjak dari tempat tidurmu dan melakukan aktivitas pagi harimu seperti biasanya."

    scene bg black with dissolve

    "Kembali dari kamar mandi seusai menggosok gigi dan mencuci muka, kini kamu memutuskan untuk melakukan aktvitas di pagi hari ini."

    "Kamu memilih untuk:"

    call screen mapUI with dissolve    

label day30:

    call change_day
    show screen trans_screen with dissolve
    scene bg kos morn with dissolve
    pause 2.0

    "ZZZZZZZZZZ"
    with vpunch
    "ZZZZZZZZZZ"
    with vpunch

    "Kamu terbangun setelah merasakan getaran dari HPmu."

    "Hari ini merupakan hari dimana dirimu akan pulang ke rumah."

    "Seperti pagi-pagi sebelumnya, kamu melakukan rutinitas pagimu."

    "Pergi ke kamar mandi untuk menggosok gigi dan mencuci mukamu."

    "Melihat ke arah langit pagi hari ini, terlihat cerah dan matahari mulai menjulang tinggi."

    "Dengan cuaca yang cerah seperti ini, kamu memutuskan untuk pulang hari ini."

    "Kembali ke kamar kosan, kamu mengambil peralatan mandi dan membawanya kembali ke kamar mandi."

    scene bg black with dissolve

    scene bg kos morn with fade

    "Selesai mandi, kini dirimu sudah berada di kamar kosan, memakai pakaian kemudian mengemas barang-barang yang akan kamu bawa pulang."

    "Karena belum mempersiapkan dari malam sebelumnya, masih banyak barang yang harus kamu kemas, dan akan memerlukan beberapa waktu untuk mengemasnya."

    mc normal jacket "Huhhh… banyak juga ternyata, karena bakalan pulang agak lama juga sih, jadi sekalian banyak yang ku bawa pulang…"

    mc "Hadehh…"

    "Dengan mengeluh kamu memulai mengemas barang-barangmu."

    scene bg black with dissolve

    scene bg kos morn with dissolve

    "Kini waktu sudah menunjukkan pukul 9.30, semua barang yang akan kamu bawa pulang sudah kamu kemas."

    "Sekarang dirimu sedang menyiapkan dan mengikat barang-barangmu di sepeda motor."

    "Setelah hampir semua barang sudah terikat di sepeda motormu, dan semua tas sudah terisi barang-barang lainnya kamu kemudian menutup dan mengunci pintu kamar kosan."

    mc "Huhh… akhirnya pulang juga yaa… setelah setahun gak pulang…."

    "Setelah memastikan semua siap, kamu menghidupkan sepeda motormu dan menaikinya."

    "Dengan semua barang dan tasmu yang kamu bawa pulang, sepeda motormu menjadi terasa lebih berat dan penuh."

    "Sebelum kamu memulai perjalanan pulangmu, kamu mengeluarkan HP untuk mengecek chat yang mungkin dikirimkan kepadamu."

    if rissa_fond >= 70:

        "Terdapat pesan yang kamu terima dan kamu bisa melihatnya dari notifikasi yang muncul pada layar HPmu."

        "[r] mengirim pesan kepadamu yang berisi ‘hati-hati dijalan’"

    if trije_fond >= 70 :

        "[TriJe] mengirim pesan kepadamu yang berisi ‘katanya pulang ya? Hati-hati di jalan’."

    if kevin_fond >= 70 :

        "[k] mengirimkan pesan kepadamu yang berisi ‘Hati-hati bro dijalan, selamat liburan!!’"

    else:

        "Kamu tidak memiliki pesan masuk yang dikirimkan kepadamu."
    
        "Setelah melihat ke arah layar HPmu, kamu hanya bisa tersenyum."

    "Kamu mengembalikan HP ke dalam saku celana, kemudian memulai perjalanan pulang kampungmu."

    "FIN"

    # Show stats screen

    # Show Ending screen

    # Ending screen…


label days:

    call change_day

    if day == 8:

        call bangun_libur

    elif day == 13:

        show screen trans_screen with dissolve
        scene bg kos morn with dissolve
        pause 2.0

        "RINGGG RINGGG RINGGG"
        with vpunch
        with vpunch

        "Bunyi alarm membangunkan dirimu dari tidur lelapmu."

        "Dengan mata yang masih setengah terbuka, meraba-raba bagian tempat tidurm yang disebelah kepalamu untuk mencari HPmu."

        "Setelah menemukannya, kamu langsung mematikan alarm yang terus berdenging nyaring."

        "Melihat waktu yang masih pagi, sebenarnya kamu masih merasa ngantuk."

        "Namun kamu paksakan tubuhmu untuk pindah ke posisi duduk, dan mencoba menghilangkan rasa kantuk itu."

        "Beberapa menit kemudian, kesadaranmu sudah hampir sepenuhnya kembali dan rasa kantuk sudah tidak kamu rasakan lagi."

        "Hari ini merupakan hari pertama UTS dimulai, kamu ingin mempersiapkan tubuh dan pikiranmu semantap mungkin sebelum UTS dimulai."

        "Agar tidak terburu-buru kamu mulai mempersiapkan peralatan yang dibutuhkan untuk ujian nanti, kartu ujianpun kamu masukan ke dalam tas agar tidak terlupa."

        "Setelah merasa persiapan untuk ujian nanti selesai, kamu beranjak dari tempat tidurmu."

        "Berdiri dan berjalan keluar dari kamar menuju kamar mandi, lalu bersiap melakukan aktivitas pagi hari ini."

        call screen mapUI with dissolve

    elif day == 16:

        show screen trans_screen with dissolve
        scene bg kos morn with dissolve
        pause 2.0

        "RINGGG RINGGG RINGGG"
        #sfx alarm

        "Bunyi alarm membangunkan dirimu dari tidur lelapmu."

        "Dengan mata yang masih setengah terbuka, meraba-raba bagian tempat tidurm yang disebelah kepalamu untuk mencari HPmu."

        "Setelah menemukannya, kamu langsung mematikan alarm yang terus berdenging nyaring."

        "Melihat waktu yang masih pagi, sebenarnya kamu masih merasa ngantuk."

        "Namun kamu paksakan tubuhmu untuk pindah ke posisi duduk, dan mencoba menghilangkan rasa kantuk itu."

        "Beberapa menit kemudian, kesadaranmu sudah hampir sepenuhnya kembali dan rasa kantuk sudah tidak kamu rasakan lagi."

        "Kamu bersandar pada salah satu sisi tembok yang ada pada kamarmu."

        "{i}Bzzzzz... Test... Test... 1..2.. 3..{/i}"
        
        "{i}Selamat pagi warga.....{/i}"

        "Tiba-tiba terdengar suara toa dari masjid."

        "Kamu diam dan mendengarkan pengumuman yang disiarkan pagi hari itu."

        "............"

        scene bg kos morn with fade

        "Pengumuman tersebut berkumandang selama beberapa menit."

        "Setelah mendengarkan pengumuman dari awal hingga akhir, kamu mengetahui bahwa akan diadakan kerja bakti dilingkungan tempat kosanmu."

        "Kerja bakti itu akan diadakan pagi hari dan selesai ketika matahari sudah berada tepat diatas kepala."

        "Pengumuman tersebut ditujukan bagi para warga dan penghuni kosan yang berada lingkungan sekitar."

        "Tidak perlu membawa peralatan masing-masing, karena sudah disiapkan oleh warga sekitar."

        "Kamu bisa memilih untuk mengikuti kerja bakti tersebut atau tidak."

        "Setelah beberapa waktu berpikir, akhirnya kamu memutuskan untuk:"

        menu:

            "Ikut kerja bakti":

                mc normal jacket "Tidak ada salahnya aku ikut kegiatan tersebut, anggap aja sambil bersosialisasi sekaligus olahraga hahaha."

                "Setelah memutuskan untuk mengikuti kegiatan kerja bakti, kamu tidak segera menyiapkan diri dan keluar dari kosan."

                "Namun kamu kembali berbaring di atas tempat tidurmu, sambil memeluk bantal dan menutupi tubuhmu dengan selimut."
                
                "Karena kegiatan kerja bakti masih akan dilakukan sekitar satu jam lagi, kamu kembali bermalas-malasan di atas tempat tidur."

                "Kamu menghabiskan waktu sembari meneruskan tidurmu hingga kegiatan kerja bakti dimulai."

                jump kerja_bakti

            "Tidak Ikut kerja bakti":

                mc normal jacket "Pengin ikut sih, tapi kok badan masih kerasa capek begini yaa?"

                mc "Apa mending gausah ikut aja ya, males juga keluar pagi-pagi gini."
            
                mc "Uahhhhhhhhhhhh"

                "Kamu menguap dan merangkan badanmu sebelum akhirnya kembali menyelimuti badanmu menggunakan selimut."

                "Kamu kembali terlelap untuk beberapa menit hingga kamu kembali terbangun dan bersiap melakukan aktivitas pagi harimu."

                call screen mapUI with dissolve
                
    elif day == 17:

        jump bangun

    elif day == 25:

        show screen trans_screen with dissolve
        scene bg kos morn with dissolve
        pause 2.0

        "RINGGG RINGGG RINGGG"
        with vpunch
        with vpunch

        "Seperti hari-hari biasanya, matamu terbuka setelah mendengarkan bunyi alarm yang keluar dari HPmu."

        "Memandang ke langit-langit kosan sambil mengucek-ucek matamu yang masih terasa berat untuk dibuka."

        "Dengan mata yang masih setengah terbuka, kamu meraba-raba bagian tempat tidur disebelah kepalamu untuk mematikan sumber bunyi yang membuatmu terbangun pada pagi hari ini."

        "Setelah merasakan dingin dari layar hpmu, kamu langsung mematikan alarm yang masih terus berdering nyaring."

        "Dengan mata yang masih mengantuk, kamu menyempatkan dirimu untuk membuka Lane yang terlihat sudah terdapat banyak notifikasi."

        "Salah satu pesan yang terdapat pada layar HPmu, adalah pesan dari [r] bertuliskan '{i}Semangat buat ujian hari ini!!{/i}'"

        "Membaca pesan tersebut, kamu teringat akan ujian yang akan dimulai pada hari ini."

        "Meskipun matamu masih terasa berat, namun kamu paksakan tubuhmu dari yang semula masih berbaring pada tempat tidurmu untuk pindah ke posisi duduk, dan mencoba menghilangkan rasa kantuk."

        "Setelah duduk untuk sementara waktu, beberapa menit kemudian kesadaranmu sudah hampir sepenuhnya kembali dan rasa kantuk sudah tidak kamu rasakan lagi."

        "Kamu berdiri dan berjalan keluar dari kamar menuju kamar mandi, lalu bersiap melakukan aktivitas pagi hari ini, sebelum berangkat menuju kampus dan memulai minggu ujian akhirmu."

        call screen mapUI with dissolve

    elif day == 26:

        show screen trans_screen with dissolve
        scene bg kos morn with dissolve
        pause 2.0

        "RINGGG RINGGG RINGGG"
        with vpunch
        with vpunch

        "Seperti hari-hari biasanya, matamu terbuka setelah mendengarkan bunyi alarm yang keluar dari HPmu."

        "Memandang ke langit-langit kosan sambil mengucek-ucek matamu yang masih terasa berat untuk dibuka."

        "Dengan mata yang masih setengah terbuka, kamu meraba-raba bagian tempat tidur disebelah kepalamu untuk mematikan sumber bunyi yang membuatmu terbangun pada pagi hari ini."

        "Setelah merasakan dingin dari layar hpmu, kamu langsung mematikan alarm yang masih terus berdering nyaring."

        "Dengan mata yang masih mengantuk, kamu menyempatkan dirimu untuk membuka Lane yang terlihat sudah terdapat banyak notifikasi."

        "Salah satu pesan yang terdapat pada layar HPmu, adalah pesan dari [r] bertuliskan '{i}Semangat buat ujian hari kedua!!{/i}'"

        "Membaca pesan tersebut, kamu teringat kamu sedang berada pada minggu ujian dan sekarang adalah hari kedua dari ujian akhir."

        "Meskipun matamu masih terasa berat, namun kamu paksakan tubuhmu dari yang semula masih berbaring pada tempat tidurmu untuk pindah ke posisi duduk, dan mencoba menghilangkan rasa kantuk."

        "Setelah duduk untuk sementara waktu, beberapa menit kemudian kesadaranmu sudah hampir sepenuhnya kembali dan rasa kantuk sudah tidak kamu rasakan lagi."

        "Kamu berdiri dan berjalan keluar dari kamar menuju kamar mandi, lalu bersiap melakukan aktivitas pagi hari ini, sebelum berangkat menuju kampus dan memulai minggu ujian akhirmu."

        call screen mapUI with dissolve

    elif day == 27:

        show screen trans_screen with dissolve
        
        scene bg kos morn with dissolve
        pause 2.0

        "RINGGG RINGGG RINGGG"
        with vpunch
        with vpunch

        "Seperti hari-hari biasanya, matamu terbuka setelah mendengarkan bunyi alarm yang keluar dari HPmu."

        "Kamu bangun dari tidurmu lalu mematikan alarm yang masih terus berbunyi."

        "Kesedaranmu masih belum sepenuhnya pulih, pandanganmu masih kabur dan kamu masih belum bisa berpikir jernih."

        "Untuk beberapa menit kemudian, kamu hanya duduk terdiam di kasur sembari menunggu kesadaranmu kembali."

        "Setelah merasa cukup bugar, kamu mengambil HP yang berada di atas tempat tidurmu."

        "Terdapat pesan masuk yang terlihat dari jendela notifikasi."

        "Pesan itu merupakan pesan yang dikirim oleh [r] bertuliskan '{i}Semangat buat ujian hari terakhir!!! Jangan sampai telat yaa!{/i}'"

        "Kamu tersadar hari ini merupakan hari ujian akhir dilakukan, yang berarti setelah hari ini kuliahmu untuk tahun ini akan berakhir."

        "Setelah duduk dan membaca beberapa pesan yang terdapat pada group chat untuk sementara waktu, kamu beranjak dari tempat tidurmu."

        "Kamu berjalan keluar dari kamar menuju kamar mandi, lalu bersiap melakukan aktivitas pagi hari ini, sebelum berangkat untuk menghadapi ujian akhirmu yang terakhir."

        call screen mapUI with dissolve

    else:

        jump bangun

    return

label sleep:

    $placeKeys = 3
    show screen trans_screen with dissolve
    scene bg kos night with fade
    pause 2.0

    "Seusai selesai dengan kegiatan malammu, kini kamu sudah berada di atas tempat tidur."

    "Memegang hp, kamu memastikan alarm sudah di set pada waktu yang tepat."

    "Lalu untuk jaga-jaga kamu membuka aplikasi Lanemu mencari informasi jika ada info tertentu."

    #check info baru

    if day == 11 and hima_intro == False:
        "Kamu teringat hari ini ada pertemuan pertama untuk pengurus himpunan mahasiswa program studimu yang kamu tidak hadiri."

        "Terdapat chat dari [r] yang berisi '[name] ini ada informasi kamu masuk aja di grup ini."

        "Dalam chat [r] terdapat link untuk bergabung pada grup himpunan mahasiswa program studimu."

        "Setelah mengklik link tersebut, kamu masuk ke dalam grup dimana kamu melihat hasil pertemuan tadi siang."

        "Kamu melihat note untuk hasil pertemuan tadi siang kebanyakan besar hanyalah perkenalan dari masing-masing anggota."

        "Setelah menscroll lebih jauh kamu melihat namamu masuk kedalam suatu divisi, dalam divisi tersebut juga terdapat [j]."

        "Divisi yang kamu masuki memiliki tugas mingguan yaitu {b}{i}Melakukan kegiatan pelajaran tambahan pada hari ketiga perkuliahan.{/i}{/b}"

        "Pelajaran tambahan akan diisi oleh {b}{i}Kakak tingkat atau yang berpengalaman dalam bidang tersebut.{/i}{/b}"

        "Itu merupakan informasi penting yang ada dalam grup selain informasi-informasi tambahan yang tidak terlalu penting."

        "Menelaah lebih lanjut informasi yang ada, setelah dirasa cukup kamu menutup aplikasi Lane dan bersiap untuk tidur."

    elif day == 23:

        "Terlihat terdapat beberapa notifikasi pesan pada grup kelasmu."

        "[r] mengirim beberapa pesan yang berisi ajakan untuk mengikuti kegiatan belajar bersama mempersiapkan ujian akhir yang akan dilaksanakan minggu depan."

        "Beberapa pesan balasan dikirimkan oleh teman-teman sekelasmu menanggapi ajakan dari [r]. Kebanyakan menanggapinya dengan positif dan tidak sabar melakukan kegiatan tersebut,
        namun juga terdapat beberapa dari teman sekelasmu yang langsung memberikan alasan untuk tidak menghadiri kegiatan belajar bersama."

        "Setelah beberapa percakapan dan pembahasan mengenai kegiatan esok, akhirnya disepakati untuk melakukan kegiatan tersebut pada lokasi yang sama 
        ketika melakukan kegiatan belajar bersama pada waktu ujian tengah semester."

        "Lalu setelah merasa cukup menerima informasi yang ada pada grup Lane, kamu memutuskan untuk tidur."

    else:

        "Namun setelah menscroll pesan yang ada di group kelas hingga pesan yang paling baru, kamu tidak menemukan adanya informasi khusus."

    "Kemudian kamu menutup Lane dan menaruh HPmu disebelah tempat tidurmu"

    "Karena tidak ada hal lain yang perlu dilakukan malam ini, kamu memutuskan untuk tidur."

    "Memejamkan matamu, kamu mengingat apa yang terjadi hari ini."

    #stat info

    if day == 5:

        "Kamu merasa senang dengan hari pertama kuliahmu hari ini, dan tidak sabar untuk menerima mengikuti kuliah selanjutnya."

    elif day == 7:

        "Sebelum tertidur, kamu mengingat informasi dari [r] mengenai himpunan mahasiswa."

        "Kamu memikirkan apa saja keuntungan dan kerugian yang mungkin dirasakan ketika dirimu bergabung dalam himpunan."

        "Tentu saja pengalaman, pengetahuan, relasi, dan pengembangan diri lainnya akan kamu rasakan ketika dirimu aktif dalam berorganisasi."

        "Namun untuk selalu aktif kamu juga perlu mengorbankan waktumu, 
        kamu takut jika dirimu akan terlalu disibukan dengan organisasi sehingga melalaikan kewajiban utamamu sebagai mahasiswa."

        "Terjadi perdebatan pada pikiranmu yang membuat dirimu berpikir, akan tetapi rasa kantuk lah yang memenangkan perdebatan pada malam ini."
    
    elif day == 8:

        if hima == True:

            "Sebelum tertidur, kamu mengingat apa yang kamu lakukan hari ini."

            "Kamu mencoba mendaftar untuk bergabung menjadi pengurus himpunan mahasiswa pada program studimu."

            "Kamu memutuskan untuk mendaftarkan karena banyak keuntungan yang bisa kamu dapatkan, terutama pengalaman."

            "[k] menjelaskan tugas, kewajiban, event kegiatan yang dilakukan oleh himpunan mahasiswa pada program studimu."

            "Hari ini kamu berkenalan dengan [j] yang ternyata sangat friendly."

            "[j] juga mendaftar menjadi pengurus himpunan mahasiswa."

            "Kamu terkejut karena wawancara yang dilakukan hanya sebentar saja."

        else:

            "Sebelum tertidur, kamu mengingat apa yang kamu lakukan hari ini."

            "Kamu tidak memutuskan untuk mendaftar menjadi pengurus himpunan mahasiswa pada program studimu."

            "Kamu takut akan meneledorkan akademikmu karena waktu yang tersita untuk berorganisasi."

            "Tidak banyak hal yang kamu lakukan setelah itu."
    
    elif day == 11:

        if hima_intro == True:

            "Sebelum tertidur, kamu mengingat apa yang kamu lakukan hari ini."

            "Kamu mengikuti pertemuan pertama pengurus himpunan mahasiswa pada program studimu."

            "Kegiatan tersebut kebanyakan besar berisi perkenalan dan pengenalan tugas divisi-divisi yang ada."

            "Kamu berada dalam satu divisi dengan [j] yang memiliki kegiatan mingguan untuk melakukan pembelajaran tambahan."

            "Selain kegiatan pertemuan pengurus, kamu mengingat perkataan [r] yang akan mengadakan belajar bersama untuk persiapan UTS."

            "Belajar bersama dengan [r] dan teman sekelasmu akan diadakan setiap hari seblum UTS pada malam hari di foodcourt minimart."

        else:

            "Sebelum tertidur, kamu mengingat apa yang kamu lakukan hari ini."

            "Kamu tidak menghadiri pertemuan pertama pengurus himpunan mahasiswa pada program studimu."

            "Setelah mengirimkan pesan alasan ketidakhadiranmu pada [r] kamupun pulang untuk beristirahat."

            "Tidak banyak hal yang kamu lakukan setelah berada di kos."

            "Selain kegiatan pertemuan pengurus, kamu mengingat perkataan [r] yang akan mengadakan belajar bersama untuk persiapan UTS."

            "Belajar bersama dengan [r] dan teman sekelasmu akan diadakan setiap hari seblum UTS pada malam hari di foodcourt minimart."
    
    elif day == 12:

        "Kamu teringat besok merupakan hari pertama untuk UTS dimulai."

        "Kamu sudah mempersiapkan kartu untuk ujianmu untuk ujian esok hari."

        "Terasa sedikit gelisah karena besok merupakan kali pertama kamu menjalani UTS pada masa kuliah."

        "Dalam hatimu, kamu berdoa agar dapat melewati dan mendapatkan hasil yang memuaskan selama UTS berlangsung."

    elif day == 13:

        "Kamu telah menyelesaikan hari pertama ujian tengah semestermu."

        "Rasa cemas menghantuimu, kamu takut jika hasil ujianmu mengecewakan."

        "Namun kamu merasa sudah berusaha semaksimal mungkin sewaktu melaksankan ujian."

        "Kamu berpikir kamu dapat mendapatkan hasil yang lebih maksimal jika kamu lebih giat dalam belajar."

        "Namun kamu harus tetap berfokus untuk ujian yang masih akan berlangsung selama beberapa hari lagi."

    elif day == 15:

        "Hari ini ujian tengah semester telah berakhir."

        "Kamu merasa lega karena ujian telah berakhir meskipun rasa cemas akan hasil ujian masih kamu rasakan."

        "Paling tidak minggu-minggu ujian telah berakhir, dan kamu kembali menjalani aktivitas kuliah seperti biasanya."

    elif day == 17:

        "Kamu teringat hasil ujian tengah semester sudah keluar dan bisa untuk dilihat."

        "Kamu merasa cukup puas dengan apapun hasil yang kamu dapatkan, karena kamu merasa dirimu sudah cukup berusaha sewaktu ujian kemarin."

        "Meskipun begitu, kamu menyadari jika dirimu masih harus terus lebih giat dalam berkuliah, sehingga hasil yang didapatkan meningkat."

    elif day == 23:

        "Kamu teringat hari ini merupakan hari terakhir pembelajaran kuliah normal pada tahun ini. Besok adalah hari terakhir kamu bisa menikmati liburan, 
        meskipun kamu juga harus belajar untuk ujian di hari berikutnya."

        "Seperti yang baru saja kamu baca pada aplikasi Lane, kegiatan belajar bersama untuk ujian juga akan diadakan setiap hari sebelum ujian akhir dilaksanakan."

        "[r] menyerukan kepada teman-teman sekelas untuk bergabung dan meramaikan kegiatan belajar sama seperti sewaktu ujian tengah semester."

        "Kamu masih belum tahu apakah dirimu akan mengikuti kegiatan belajar tersebut atau tidak. Sekarang kamu hanya memikirkan apa yang ingin kamu lakukan esok hari."

    elif day == 25 or day == 26 :

        "Kamu telah menjalani hari ujian akhir semestermu."

        "Kamu merasa sudah melakukan yang terbaik ketika mengerjakan ujian akhirmu hari ini."

        "Kini kamu hanya bisa berharap untuk mendapatkan hasil yang maksimal."

        "Kamu juga tidak sabar untuk melaksanakan ujian akhir esok hari dan segera menyelesaikan ujian akhir ini."

    elif day == 28:

    else:
        pass

    "Mengingat apa yang ada dalam pikiranmu dalam sehari ini membuatmu tambah mengantuk."

    "Kemudian tidak lama berselang, kesadaranmu perlahan mulai menghilang."

    "Setelah mata tertutup dan pandanganmu menjadi gelap, kamu tertidur pulas pada malam hari ini."

    "Day [day] END"

    jump days

label mandi:

    $placeKeys = 3
    show screen trans_screen with dissolve
    scene bg kos morn
    pause 2.0

    "Selesai melakukan aktivitas dipagi harimu, kamu mengambil peralatan mandi dan berjalan menuju kamar mandi."

    "Menggantung handukmu lalu tidak lupa untuk menggosok gigimu."

    "Setelah itu kamu mulai mengguyur tubuhmu dengan air yang ada di bak mandi."

    "Terasa dingin untuk beberapa saat, namun setelah itu rasa dingin yang dirasakan berubah menjadi rasa segar."

    #sfx mandi

    scene bg kos morn with fade

    "Selesai mandi, kamu kembali ke kamar untuk bersiap-siap."

    "Berganti pakaian dan berdandan, bersiap untuk melakukan aktivitas yang akan kamu lakukan siang hari ini."

    if day == 27:
        call change_timephase
        jump bocor

    elif day == 29:

        call change_timephase

        scene bg kos morn with fade

        "Siang harinya, kamu teringat kamu mendapatkan pesan dari [r] mengenai kegiatan dari kakak tingkat mengenai kelas pengembangan gim."

        "Kamu membuka riwayat pesanmu dengan [r], kini sudah ada terdapat beberapa pesan tambahan yang memberikan detail mengenai kegiatan tersebut."

        mc normal jacket "Hmmm… jam 11 sampai jam 2, di ruangan 402 ya."

        mc "Sekarang jam… eh… udah jam 10.40 ternyata, ikut kegiatan ini enggak ya?"

        if community >= 50:

            mc normal jacket "Hmmm… sebelum pulang rumah mungkin ikut acara ini aja apa ya? Lagipula siang ini aku enggak ada acara apa-apa, bosen di kosan terus."

            mc "Hmmm… iyalah, ikut aja toh bisa pergi ditengah acara kalau aku bosen hahaha"

            mc "Oh iya… bales chat [r] dulu jangan lupa."

            "Mengeluarkan HP dari saku celanamu, kamu membalas ajakan [r] untuk mengikuti kegiatan kelas tambahan."

            jump kelas_game

        else: 

            mc normal jacket "Kayaknya enggak dulu deh, capek banget dah rasanya hari ini, mending molor lagi ahh…"

            mc "Oh iya, harus bales chat [r] dulu… ‘sorry kayaknya aku skip dulu deh hari ini.’"

            mc "Yeahh… send…"
            
            "Setelah membalas pesan dari [r], kamu kembali ke tempat tidurmu tidak lupa menghidupkan kipas angin lalu merebahkan badanmu."

            jump rebahan 


    else:
        call change_timephase
        call screen mapUI with dissolve

label bangun:

    show screen trans_screen with dissolve
    scene bg kos morn with dissolve
    pause 2.0

    "RINGGG RINGGG RINGGG"
    with vpunch
    with vpunch

    "Bunyi alarm membangunkan dirimu dari tidur lelapmu."

    "Dengan mata yang masih setengah terbuka, meraba-raba bagian tempat tidur disebelah kepalamu untuk mencari HPmu."

    "Setelah menemukannya, kamu langsung mematikan alarm yang terus berdering nyaring."

    "Melihat waktu yang masih pagi, sebenarnya kamu masih merasa ngantuk."

    "Namun kamu paksakan tubuhmu untuk pindah ke posisi duduk, dan mencoba menghilangkan rasa kantuk itu."

    "Beberapa menit kemudian, kesadaranmu sudah hampir sepenuhnya kembali dan rasa kantuk sudah tidak kamu rasakan lagi."

    "Kamu berdiri dan berjalan keluar dari kamar menuju kamar mandi, lalu bersiap melakukan aktivitas pagi hari ini."

    call screen mapUI with dissolve

label bangun_libur:

    show screen trans_screen with dissolve
    scene bg kos morn with dissolve
    pause 2.0

    "RINGGG RINGGG RINGGG"
    #sfx alarm

    "Bunyi alarm membangunkan dirimu dari tidur lelapmu."

    "Dengan mata yang masih setengah terbuka, meraba-raba bagian tempat tidurm yang disebelah kepalamu untuk mencari HPmu."

    "Setelah menemukannya, kamu langsung mematikan alarm yang terus berdenging nyaring."

    "Melihat waktu yang masih pagi, sebenarnya kamu masih merasa ngantuk."

    "Namun kamu paksakan tubumu untuk pindah ke posisi duduk, dan mencoba menghilangkan rasa kantuk itu."

    "Beberapa menit kemudian, kesadaranmu sudah hampir sepenuhnya kembali dan rasa kantuk sudah tidak kamu rasakan lagi."

    "Hari ini merupakan hari libur, saatnya dirimu untuk bersenang-senang dan melupakan kuliah untuk sementara."

    "Merasa tidak ada dorongan untuk segera beranjak dari tempat tidurmu, kamu kembali merebahkan tubuhmu di kasur untuk beberapa menit lagi."

    #case

    if day ==8:

        "Membuka matamu untuk kedua kalinya pada pagi hari ini, kamu teringat ada perekrutan anggota himpunan mahasiswa baru siang ini."

        "Menghela nafas... kamu beranjak dari tempat tidur."

        mc normal jacket "Mending ikut engga ya?"

        mc "Pengin tapi kok males juga...."

        mc "huh....."

        mc "Siap-siap dulu dah, dari pada tiduran mulu...."

    elif day == 12:

        "Beberapa menit kemudian kamu terbangun untuk kedua kalinya pada pagi hari ini."

        "Terdapat beberapa chat yang masuk pada grup chat Lane kelasmu. Chat-chat tersebut berisi pembahasan tentang UTS yang akan dimulai besok."

        "Perbincangan tersebut membicarakan mengenai jadwal dan kisi-kisi UTS yang akan dilaksanakan."

        "Salah satu chat dari [r] yang dikirimkan pada grup memiliki informasi yang penting."

        "{b}Jadwal UTS yang dilakukan sama dengan jadwal kuliah seperti biasa.{/b}"

        "{b}Materi yang akan keluar pada UTS adalah materi yang sudah pernah dipelajari pada perkuliahan biasa.{/b}"

        "Selain informasi tersebut ada juga ajakan untuk belajar bersama di foodcourt sama seperti ajakan [r] kepadamu."

        "Merasa cukup dengan informasi yang didapatkan, kamu menutup aplikasi dan meletakan hpmu kemudian beranjak dari tempat tidur."

    "Kamu berdiri dan berjalan keluar dari kamar menuju kamar mandi, lalu bersiap melakukan aktivitas pagi hari ini."

    call screen mapUI with dissolve

label nothing:

    scene bg black

    "nothing here, you're wrong"

    return



#activities
label eat:

    $energy +=10
    $hunger +=35
    $vit +=5

    "Stats Berubah!!!"
    show screen stats_changer("eat", 0)

    return

label small_eat:

    $hunger +=20

    "Stats Berubah!!!"
    show screen stats_changer("small_eat", 0)

    return

label drink:

    $energy +=10
    $hunger += 15
    show screen stats_changer("drink", 0)

    "Stat Berubah!!!"

    return

label nap:

    $ energy += 25
    $ hunger -= 10
    $ vit += 5
    show screen stats_changer("nap", 0)

    return

label change_timephase:

    if timephase != 3:
        $ timephase += 1
    else:
        $ timephase = 1   

    $ vit -= 5
    $ energy -= 30
    $ hunger -= 15

    show screen stats_changer("change_timephase", 0)
    call stat_change

    return

label change_day:

    $ day += 1
    if timephase != 3:
        $ timephase += 1
    else:
        $ timephase = 1   

    $ energy += 45
    $ hunger -= 25
    $ vit -= 10

    $k_days +=1

    show screen trans_screen with dissolve

    show screen stats_changer("change_day", 0)
    call stat_change

    return

#sport
label jog:

    $ vit += 25
    $ energy -= 20
    $ hunger -= 15

    "Stats Berubah!!!"
    show screen stats_changer("jog", 0)

    return

label jalan_sehatS:

    $ vit += 35
    $ energy -= 30
    $ hunger -= 20

    "Stats Berubah!!!"
    show screen stats_changer("jalan_sehatS", 0)

    return

label futsal:

    $ vit += 35
    $ public += 10
    $ energy -= 30
    $ hunger -= 25

    "Stats Berubah!!!"
    show screen stats_changer("futsal", 0)

    return

#class
label attend_class:

    $ knowledge +=1
    $ practice +=1
    show screen stats_changer("class", 0)

    "Stat Berubah!!!"

    return

#social
label kerja_bakti_kampung:
    
    $ public += 20
    $ vit += 15
    $ community += 10
    $ hunger += 10
    show screen stats_changer("kerja_bakti", 0)

    "Stat Berubah!!!"

    return

label hangout:

    $ public += 10
    $ hunger += 10
    $ friend += 5
    show screen stats_changer("hangout", 0)

    "Stat Berubah!!!"

label hima_act:

    $ public += 10
    $ community += 20
    $ friend += 5
    show screen stats_changer("hima_act", 0)

    "Stat Berubah!!!"

label stat_change:

    if hunger >= 100:
        $hunger = 100
        $obesseCount +=1

    if hunger <= 0:
        $hunger = 0
        $thinCount +=1

    if energy >= 100:
        $energy = 100
        $healthyCount +=1

    if energy <= 0:
        $energy = 0
        $sickCount +=1

    if vit >= 100:
        $vit = 100
        $fitCount +=1

    if vit <= 0:
        $vit = 0
        $weakCount +=1 
    
    return



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
