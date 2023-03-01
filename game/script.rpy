# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# label splashscreen:
#     call screen confirm(message="Proceed to play the game?", yes_action=Return(), no_action=Quit(confirm=False))
#     return

define r = Character("Rissa", image="r")
# define mc = Character("Mc", image="mc") 
define mc = Character("You", image="mc")
define w = Character("Warga", image="anonM")
define pa = Character("Pak Andy", image="pa")
define aa1 = Character("Aa'", image="anonM")
define kev = Character("Kevin", image="anonM")
define t = Character("Teman", image="t")
define stall = Character("Stall", image="anonM")
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
default capa = '1'
default note = ""

default maps = False




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

    $ day += 1
    if timephase != 3:
        $ timephase += 1
    else:
        $ timephase = 1   

    $ energy += 30
    $ hunger -= 25
    $ vit -= 10

    scene bg black
    with Dissolve(2.0)

    pause 3.0

    show day2 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 3.0

    hide day2 pro with dissolve

    call screen trans_screen with dissolve

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
    
    mc "aku masih punya makanan sisa tidak ya?"

    "Kamu mencari makanan yang ada di kamar kosmu."

    if rotiAwal == True:
        
        mc "Oh iyaa, kemarin aku masih menyimpan roti, lumayanlah buat sarapan."

        "Kamu mengambil roti yang kamu beli di Minimart kemarin dan langsung memakannya."

        $ energy += 15
        $ hunger += 30
        $ vit += 10

        "{b}!Stats berubah!{/b}"

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

    "Setelah mengecek siapa DPAmu di Simaster, kamu melanjutkan scrolling chat di grupmu."

    "Untuk jam berapanya masih kutanyakan ya teman-temann."

    "{i}Okee Clariss{/i}."

    "Scroll"

    "Scroll"

    "Chat selanjutnya masih dilanjutkan dengan candaan oleh beberapa tokoh yang ada di grup."

    mc "{i}hmmm sepertinya si Claris ini bakal jadi tokoh ketua kelas di angkatan deh{/i}."

    mc "{i}Belum masuk aja sudah jadi penghubung begini..{/i}"

    "Scroll"

    "Scroll"

    "{i}Oh ini teman-teman Pak Andy sudah bales chatku!{/i}"

    "{i}Jam berapa tuh Claris?{/i}"

    "{i}Iya jam berapa?{/i}"

    "{i}Kalau yang bukan Pak Andy kita kapan gengs?{/i}"

    mc "{i}Ohh ternyata tidak semua Pak Andy ya?{/i}"

    mc "{i}Hmmm iya juga sih, satu angkatan banyak mahasiswa kalau dosen pembimbingnya cuma satu gamungkin sih...{/i}"

    "{i}Kata Pak Andy nanti siang antara jam 12 sampai jam 1 nih, di Lab TRPL katanya{/i}."

    "{i}Waduh dimana itu..{/i}"

    "{i}Iya dimana itu?{/i}"

    "Chat yang di grup masih bermunculan satu persatu, namun kamu mengabaikannya."

    hide diskusi dpa with dissolve

    "Kamu melirik melihat jam yang ada di ponselmu."

    "07.30 adalah waktu yang ditunjukan."

    mc "{i}masih nanti siang yaa, mau apa dulu ya pagi ini?{/i}"

    "Melihat waktu yang masih pagi, dan bimbingan akan diadakan di siang hari kamu memutuskan untuk mengisi waktu pagimu."

    "Kamu memutuskan untuk…."

    # hide screen stats_screen
    window hide

    $ prologueCount += 1

    call screen mapUI with dissolve

    return

label day3:

    $ day += 1
    if timephase != 3:
        $ timephase += 1
    else:
        $ timephase = 1   

    $ energy += 30
    $ hunger -= 25
    $ vit -= 10

    scene bg black
    with Dissolve(1.0)

    pause 2.0

    show day3 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 2.0

    hide day3 pro with dissolve

    call screen trans_screen with dissolve

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

    "{i}Rosa perpustakaan pusat itu yang deket sama Graha itu kan?{/i}"

    "{i}Iya, nanti kalau udah disana ku share lokasinya.{/i}"

    "{i}Jam berapa tuuh?{/i}"

    "{i}Enaknya jam berapa man-temans?{/i}"

    "{i}Agak siangan aja Ros.{/i}"

    "{i}Aku jam 9 lebih baru bisa gas.{/i}"

    "{i}Jangan siang-siang tapi, takut kalau hujan maless…{/i}"

    "{i}Jam 10 sih bisaa, gimana yang lain?{/i}"

    "{i}Iya jam 10 aja gimana? {/i}"

    "{i}Okee gass.{/i}"

    "{i}Siappp{/i}"

    "{i}Jam 10 ya noted.{/i}"

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
    call change_day
    scene bg black
    with Dissolve(1.0)

    pause 2.0

    show day4 pro:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 2.0

    hide day4 pro with dissolve

    call screen trans_screen with dissolve

    pause 2.0

    scene bg kos morn with dissolve

    show screen stats_screen with dissolve

    show screen days_screen with dissolve

    scene bg kos morn with fade

    #SFX alarm

    "Nggtttt"

    "Nggttttt"

    "Ngtttttttt"

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

    "Cklekk"

    mc "Lumayan..... rezeki emang enggak kemana. Dari kemarin dapat makan gratis terus."

    "Menutup pintu, kamu duduk dan menaruh box makanan itu di meja belajar." 
    
    "Dengan hati yang senang, kamu segera membuka apa yang ada di dalam kotak makanan itu."

    "Meletakan hp di meja belajar, kamu memutar video di internet untuk menemani sarapanmu."

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

    call screen trans_screen with dissolve

    "persiapan pagi"

label days:

    call change_day

    if day == 8:

        "first free day"
    
    elif day == 9:

        "himakomsi"
    
    elif day == 13:

        "UTS"

    elif day == 17:

        "ban bocor"

    elif day == 25:

        "UAS"

    elif day == 27:

        "ban bocor"
    else:
        "ending"

    return

    
    

label nothing:

    scene bg black

    "nothing here, you're wrong"

    return

label eat:

    $energy +=10
    $hunger +=35
    $vit +=5

    call stat_change

    "Stats Berubah!!!"

    return

label drink:

    $energy +=5
    $hunger += 15

    call stat_change

    "Stat Berubah!!!"

    return

label change_timephase:

    if timephase != 3:
        $ timephase += 1
    else:
        $ timephase = 1   

    $ vit -= 5
    $ energy -= 20
    $ hunger -= 10

    call stat_change

    return

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

label change_day:

    $ day += 1
    if timephase != 3:
        $ timephase += 1
    else:
        $ timephase = 1   

    $ energy += 30
    $ hunger -= 25
    $ vit -= 10

    call stat_change

    return

label nap:

    $ energy += 15
    $ hunger -= 10
    $ vit -= 5
    call stat_change

    return


# label change_time:

#     if timephase != 3:
#         $ timephase += 1
#     else:
#         $ timephase = 1   

#     $ energy += 30
#     $ hunger -= 25
#     $ vit -= 10

#     call stat_change

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
