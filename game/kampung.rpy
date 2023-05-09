
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
            call ambil_jatuh
        "Membantu mengeluarkan ban mobil yang jeblos":
            call mobil_jeblos

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
        
        "Pergi ke Warmindo untuk sarapan":
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

    call sport_mornS1

    return

label kamp_mornS2:

    "Keluar dari kamar, kamu berjalan menuju warmindo yang berada dekat dengan kosan."

    call eat

    if day == 5:
        jump persiapan_kuliah
    else:
        jump mandi

#night
label kamp_noonS1:

    "Merasa perutmu keroncongan, kamu mencari tempat makan yang ada disekitaran kampung."

    call eat

    return

label kamp_noonS2:

    "Merasa capek untuk mencuci pakaian kotormu, kamu berniat untuk melaundrykan semua pakaian kotor yang sudah menumpuk dikeranjang baju."

    return

#night
label kamp_nightS1:

    "Membawa HPmu kamu pergi menuju warmindo yang ada di dekat kos."

    call eat

    jump sleep
  
label kamp_nightS2:

    "Penat berada di dalam kamar kos terus menerus, kamu keluar dari kamar dan berjalan di sekitaran kampung untuk menikmati angin malam."

    jump sleep
  

