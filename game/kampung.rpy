
label first_kampung:

    $ firstKampung = False

    scene bg town street 2 with Dissolve(2.0)

    "Kamu memutuskan untuk menghabiskan waktu pagimu dengan berjalan mengelilingi lingkungan sekitar."

    "Mengganti celanamu dengan celana panjang, kamu keluar dari kamar kos."

    "Tidak ada destinasi atau tujuan khusus yang ingin kamu tuju."

    "Hanya berjalan sembari mengamati kondisi lingkungan disekitar area kos."

    "Selama berjalan mengilingi lingkungan sekitar, kamu banyak menjumpai orang-orang yang sedang berolahraga.
        Beberapa orang sedang berlari kecil, ada juga yang mengendarai sepeda mengitari kampung."

    "Selain menjumpai banyak orang, kamu juga mengamati macam-macam bangunan yang ada disekitar.
        Kamu banyak melihat banyak bangunan kos, baik kos perempuan maupun kos laki-laki."

    "Selain bangunan kos juga terdapat banyak warung makan, mulai dari warung makan kecil sampai warung makan yang lumayan besar."

    "Warung makan kecil yang banyak bertuliskan Warmindo, bahkan kamu menemui banyak Warmindo di tengah-tengah kampung, ada juga yang lokasinya berseberangan jalan.
        Sementara warung makan yang lebih besar biasanya terletak di pinggir jalan besar."

    "Selain warung makan, banyak juga kamu melihat tempat-tempat yang menyediakan banyak layanan untuk para mahasiswa nantinya.
        Seperti tempat untuk print, toko alat tulis, toko sehari-hari, dan tempat laundry pakaian."

    scene bg town street 1 with fade

    "Kamu terus berjalan sembari mengamati keadaan disekitarmu."

    "{i}Gubrakkk!!!{/i}"
    with vpunch
    with vpunch
    # Sfx things fell
    # Shake

    "Tiba-tiba kamu mendengar suara keras dari arah pertigaan yang ada di depanmu."

    "Merasa penasaran, kamu mendekati asal suara tersebut."

    "Setelah beberapa langkah mendekat, kamu melihat kerumunan orang di dekat sebuah mobil angkut."

    # show w normal

    "Penasaran, kamu mendekati kerumunan yang ada di depanmu dan bertanya kepada salah seorang yang ada disana."

    mc normal jacket  "Ada apa ini mas?"

    # hide w normal with dissolve

    w normal "Ohh ini mas, ada yang lagi angkut-angkut barang pindahan mahasiswa baru itu."

    w  "Diangkut pake mobil waktu mau ambil barang-barang yang ada di mobil angkut, malah ban mobilnya jeblos diselokan mas. Jadi barang-barangnya pada jatuh."
    
    "Melihat kearah mobil yang terpelosot dalam selokan, kamu melihat banyak barang berserakan di sekeliling mobil angkut itu."

    "{b}!Special event tutorial!{/b}"

    "Terkadang ketika memilih suatu kegiatan kamu akan menjumpai {b}Special Event{/b}."

    "{b}Special Event{/b} dapat ditemukan karena dua hal yaitu {b}Poin Stats yang cukup{/b}, juga {b}waktu dan hari yang tepat{/b}."

    "Selain menampilkan event tertentu, terkadang dengan menemukan {b}Special Event{/b} kamu bisa mendapatkan sebuah {b}hadiah{/b} tertentu."

    "{b}Hadiah{/b} yang didapat, dapat berupa macam bentuknya, semisal {b}Makanan{/b}, {b}Barang{/b}, {b}Stats{/b}, dan hal lainnya."

    call screen tutorial_specialevents1 with dissolve
    
    "Melihat barang-barang yang berserakan di tanah dan mobil yang terjeblos di selokan, kamu memutuskan untuk:"

    menu: 
        "Membantu mengambil barang-barang yang terjatuh":
            call ambil_jatuh from _call_ambil_jatuh
        "Membantu mengeluarkan ban mobil yang jeblos":
            call mobil_jeblos from _call_mobil_jeblos

    scene bg town street 1 with dissolve
    
    "Beberapa menit kemudian semua masalah sudah berhasil di selesaikan."

    "Kini orang-orang yang ikut membantu mengeluarkan mobil yang terjeblos dan juga orang-orang yang ikut mengambil barang-barang yang terjatuh di jalanan sedang beristirahat di teras rumah."

    "Kamu juga ikut mengistirahatkan tubuhmu dan berteduh dari sinar matahari di teras rumah pemilik barang, bersama dengan warga yang lainnya."
    
    "Setelah beberapa menit beristirahat dan mengobrol bersama warga, kamu memutuskan untuk kembali ke kos."

    "Kamu berniat untuk berpamitan dengan warga yang tadi kamu temui."

    "Setelah menunggu beberapa waktu, karena tidak melihat warga yang kamu cari, kamu hanya berpamitan kepada warga yang ada disekitarmu."

    "Seusai berpamitan, kamu meninggalkan rumah warga tersebut dan berjalan ke arah kos."

    "......"

    "..."

    "Beberapa langkah berjalan, tiba-tiba ada yang memanggilmu dari belakang."

    "Kamu melihat warga yang sebelumnya kamu ajak bicara berjalan mendekatimu."

    w normal "Kok keburu pulang saja mas, ini yang punya barang tadi memberi ini buat yang bantu-bantu tadi."

    "Warga itu membawa sebuah kotak box putih pada kedua tangannya, kemudian ia menyulurkan tangan dan memberikan box putih tersebut kepadamu."

    "Tanpa sadar kamu langsung menerima kotak box putih dari warga tersebut."

    show screen get_box with dissolve

    mc normal jacket "Wah terimakasih ya mas"

    w "Tidak apa, malah saya yang terimakasih mas, tadi sudah dibantu sama masnya saya. Malah saya minta maaf sudah ngerepoti."

    mc "Tidak apa kok mas, ya kalau ada yang bisa dibantu yang ikut membantu kan mas. Ini bener-bener makasih mas, udah dikasih segala."
    
    w "Ya sama-sama mas, hati-hati dijalan."

    mc "Iya mas, saya pamit dahulu."

    "Kemudian kamu melanjutkan perjalananmu pulang ke arah kos."

    "Mengeluarkan HP dari saku celanamu kamu melihat jam yang sudah menunjukan pukul 10.00."

    mc "Habis ini sampai kos, istirahat langsung mandi lalu siap-siap ke kampus berarti."

    "Setelah menentukan tujuan selanjutnya kamu pulang ke kosmu."

    scene bg black with fade

    "Selesai mandi dan telah bersiap-siap, kamu menyalakan motormu untuk pergi kekampus."

    # hide screen days_screen

    # hide screen stats_screen

    $ prologueCount += 1
    window hide

    call screen mapUI with dissolve

    return

label ambil_jatuh:

    mc "Kalau begitu saya bantu ambil barang-barang yang jatuh pak."

    w "Maaf mas, merepotkan saja."

    mc "Tidak apa-apa kok pak."

    w "Terimakasih ya mas."

    "Kamu mulai mengambil barang-barang yang terjatuh di dekat mobil."

    "Barang-barang seperti kipas angin, rice cooker, galon dan barang rumahan yang sepertinya akan dipakai oleh anak kosan terlihat di depanmu."

    "Bersama dengan beberapa orang yang ada disekitar lokasi, kamu mulai mengambil barang yang jatuh satu persatu."

    $ energy -= 10

    $ public += 10

    scene bg black with dissolve


    return

label mobil_jeblos:
    
    mc "Kalau begitu saya bantu tarik mobilnya pak."

    w "Oh ya mas, ayo tarik bareng-bareng."

    "Kamu dan beberapa warga mulai berbaris menggenggam tali tambang yang sudah diikatkan pada mobil."

    "Pada hitungan ke 3 secara bersama-sama kamu dan warga lainnya menarik mobil yang jeblos sampai pada akhirnya ban mobil yang jeblos dapat dikeluarkan dari selokan."

    $ energy -= 15

    $ public += 10

    scene bg black with dissolve

    return

label kerja_bakti:

    scene bg kos morn with fade

    "Jam sudah menunjukan pukul 7.30, sudah saatnya kamu keluar dari kosan dan berangkat menuju kegiatan kerja bakti."

    "Kamu mengganti pakaianmu dengan kaos lengan pendek dan celana trainingmu."

    "Setelah selesai mengganti pakaian, kamu segera keluar dari kamar kosmu."

    "Diluar kamar, meskipun sebagian kamar kos masih tertutup rapat kamu melihat beberapa penghuni kosan juga sudah bersiap untuk mengikuti kerja bakti."

    "Salah satu penghuni kos yang juga akan mengikuti kegiatan kerja bakti adalah [kev]"

    "[kev] juga memakai pakaian yang sama denganmu, dengan celana training berwarna biru."

    kev normal "Yoo [name], ikut juga?"

    mc normal jacket "Yo [kev], iya nih, kamu juga ikut?"

    kev "Yoiii, oiya kita gak usah bawa peralatan sendiri kan?"

    mc "Tadi sih dipengumumannya gak usah bawa peralatan masing-masing, katanya udah disiapkan disananya nanti."

    kev "Oke kalau gitu, malah enak gaperlu peralatan sendiri."

    kev "Yaudah yuk berangkat [name]"

    mc "Ayo..."

    "Kalian berdua berangkat menuju tempat dimana kerja bakti akan dilaksanakan."

    "Dibelakang kalian, beberapa penghuni kos lainnya berjalan mengikuti."

    scene bg town street 1 with dissolve

    "Berjalan sembari mengobrol dengan [kev] dan teman kosanmu yang lain, tidak terasa kamu sudah sampai ke keramaian yang kamu tuju."

    "Sudah banyak anak kosan lain dan warga sekitar lingkungan yang sudah berkumpul."

    "Terlihat juga peralatan-peralatan yang sudah disiapkan untuk kegiatan kerja bakti."

    "Peralatan seperti cangkul, sabit, sekop, sapu lidi, dan lain sebagainya sudah disiapkan untuk kegiatan kerja bakti."

    "Kerja bakti kali ini bertujuan untuk menjaga kebersihan lingkungan dan terutama selokan agar tidak mampat dan menyebabkan banjir."

    "Setelah menunggu beberapa menit menunggu peserta kegiatan kerja bakti yang lain datang, salah seorang warga menjelaskan tata cara kegiatan 
    agar kerja bakti menjadi lebih efektif dan efisien."

    "Semua peserta mendengarkan penjelasan yang diberikan sebelum satu persatu mengambil posisi dan peralatan masing-masing."

    "Kamupun bersiap pada posisi yang kamu ambil, kamu memilih untuk membantu dalam:"

    menu:
        "Membersihkan selokan.":

            "Mencincing celana panjangmu, kamu masuk kedalam selokan membawa sekop untuk mengeruk sampah-sampah pada dasar selokan."

            "Bersama dengan warga dan anak kosan lainnya kamu saling membantu membersihkan dasar selokan."

            "Ada beberapa dari kalian yang mengambil sampah yang mengambang pada selokan."

            "Ada juga yang membantu mengumpulkan sampah yang sebelumnya diambil dari selokan kemudian mengumpulkannya dengan sampah-sampah yang lain."

            "Meskipun tidak kenal, kamu mampu bekerja sama dengan baik dengan peserta kerja bakti lainnya."

            "Tidak terasa waktu sudah menjelang siang, dan selokanpun sudah menjadi lebih bersih."

            "Kamu dan peserta lainnya yang berada di selokan segera menyudahi aktivitas dan beristirahat di tempat yang sudah disediakan."
        
        "Membersihkan rumput dan sampah disekitar area kerja bakti.":

            "Mengambil sabit, dan memakai sapu tangan kamu bergerak menuju tepi jalanan yang ditumbuhi rumput-rumput liar."

            "Sabit kamu gunakan untuk memotong rumput-rumput yang panjang serta untuk mengkorek rerumputan kecil yang terdapat pada sela-sela jalanan."

            "Ketika kamu membersihkan rerumputan dari jalanan, terkadang terdapat orang yang membawa karung sampah dimana sampah rerumputan yang kamu kumpulkan 
            akan dimasukan."

            "Tidak perlu waktu yang lama, rerumputan liar yang berada dijalanan sudah hampir semuanya dicabut."

            "Kamu meletakan sabitmu, dan dengan tanganmu kamu memungut sampah rerumputan yang kamu kais sendiri."

            "Setelah dirasa cukup bersih kamu meletakan sampah yang sudah kamu masukan karung ketumpukan sampah-sampah lainnya."

            "Lalu setelah membersihkan diri dan meletakan peralatan yang kamu pakai, kamu beristirahat bersama peserta kerja bakti lainnya pada tempat yang sudah disediakan."

    scene bg town street 1 with fade

    w normal "Terimakasih atas partisipasinya dalam kerja bakti hari ini. Silahkan dimakan snack yang sudah disiapkan, kalau mau minum juga silahkan diambil."

    "Pada tempat untuk beristirahat sudah disiapkan banyak makanan kecil dan minuman berbungkus untuk peserta kerja bakti."

    "Kamu ikut mengambil apa yang ada dihadapanmu dan menyantapnya bersama peserta kerja bakti lainnya."

    kev normal "Gimana tadi? Lancar aja kan?"

    mc normal jacket "Yah gitu dah, kamu tadi ngapain bro?"

    kev "Bantu-bantu milah sampah, katanya sebagian mau dirongsokin."

    mc "Lumayan juga sih kalau dirongsokin, tadi aku liat banyak botol-botol sama besi."

    kev "Iya dapet lumayan banyak kok, lupa berapa kilonya tapi."

    "Kamu mengisi waktu istirahatmu mengobrol dengan [kev] dan peserta kerja bakti lainnya."

    "Hingga pada akhirnya peserta kerja bakti dipersilahkan untuk pulang."

    "Sebelum pulang, peserta kerja bakti mendapatkan box makanan untuk dibawa pulang."

    show screen get_box with dissolve

    "Setelah menerima box makanan milikmu, kamu bergegas pulang untuk mandi."

    "Matahari yang sudah mulai menyengat ditambah keringat setelah melakukan aktivitas sebelumnya membuatmu harus segera mandi."

    call kerja_bakti_kampung from _call_kerja_bakti_kampung

    "Sama seperti waktu berangkat, kamu berjalan pulang menuju kosan sambil mengobrol bersama kawan kosmu."

    "Sesampainya di kosan, kamu langsung menuju kamar mandi sebelum penghuni kosan lainnya mendahuluimu."

    "Selesai mandi, kamu bersiap untuk mengisi waktu siang harimu."

    call change_timephase from _call_change_timephase_23
    call screen mapUI with dissolve


#daily 
label choice_kampung_morn:

    scene bg town street 1 with dissolve
    pause 2.0

    if day == 5:
        jump kamp_mornS2
    else:
        pass

    "Pada pagi hari kamu lebih memilih untuk keluar dari kos dan menghabiskan waktu di sekitaran kampung."

    "Ada beberapa hal yang dapat kamu lakukan di kampung pada pagi hari, kamu memilih untuk:"

    menu:
        "Jogging pagi":
            jump kamp_mornS1
        
        "Pergi ke Warmindo untuk sarapan":
            jump kamp_mornS2

label choice_kampung_noon:

    scene bg town street 1 with dissolve
    pause 2.0

    "Siang hari kamu memilih untuk menghabiskan waktumu di sekitaran kampung."

    "Ada beberapa hal yang dapat kamu lakukan di kampung pada siang hari, kamu memilih untuk:"

    menu:
        "Mencari makan siang":
            jump kamp_noonS1
        
        "Mencuci pakaian kotor":
            jump kamp_noonS2

label choice_kampung_night:

    scene bg black with dissolve
    pause 2.0

    "Keluar dari kamar kos, kamu memilih menghabiskan waktu malam harimu di sekitaran kampung."

    "Beberapa hal dapat kamu lakukan di kampung pada malam hari, kamu memilih untuk:"

    menu:
        "Pergi ke Warmindo":
            jump kamp_nightS1
        
        "Mencari angin malam":
            jump kamp_nightS2

#morn
label kamp_mornS1:

    call sport_mornS1 from _call_sport_mornS1
    $ olahragac += 1
    call change_timephase from _call_change_timephase_24
    call screen mapUI with dissolve

label kamp_mornS2:

    "Keluar dari kamar, kamu berjalan menuju warmindo yang berada dekat dengan kosan."
    $ makanc += 1
    call eat from _call_eat_8

    if day == 5:
        jump persiapan_kuliah
    else:
        jump mandi

#night
label kamp_noonS1:

    "Merasa perutmu keroncongan, kamu mencari tempat makan yang ada disekitaran kampung."
    $ makanc += 1
    call eat from _call_eat_9

    call change_timephase from _call_change_timephase_25
    call screen mapUI with dissolve

label kamp_noonS2:
    $ malasc += 1
    "Merasa capek untuk mencuci pakaian kotormu, kamu berniat untuk melaundrykan semua pakaian kotor yang sudah menumpuk dikeranjang baju."

    call change_timephase from _call_change_timephase_26
    call screen mapUI with dissolve
#night
label kamp_nightS1:

    "Membawa HPmu kamu pergi menuju warmindo yang ada di dekat kos."
    $ makanc += 1
    call eat from _call_eat_10

    jump sleep
  
label kamp_nightS2:
    $ jalanc += 1
    "Penat berada di dalam kamar kos terus menerus, kamu keluar dari kamar dan berjalan di sekitaran kampung untuk menikmati angin malam."

    jump sleep
  

