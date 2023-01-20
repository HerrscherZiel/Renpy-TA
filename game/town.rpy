
label first_kampung:

    $ first_kampung = False


    scene bg town street 2 with Dissolve(2.0)

    # show screen days_screen with dissolve

    # show screen stats_screen with dissolve

    "Kamu memutuskan untuk menghabiskan waktu pagimu dengan berjalan mengelilingi lingkungan sekitar."

    "Berganti menggenakan celana panjang, kamu keluar dari kamar kosmu."

    "Tidak ada destinasi khusus yang ingin kamu tuju."

    "Hanya berjalan sembari mengamati kondisi lingkungan disekitar dirimu."

    "Selama berjalan mengilingi lingkungan sekitar, kamu banyak berjumpa dengan orang-orang yang sedang berjogging."

    "Kamu juga banyak melihat banyak bangunan kos, baik kos perempuan maupun kos laki-laki."

    "Selain bangunan kos juga terdapat banyak warung makan, mulai dari warung makan kecil sampai warung makan yang lumayan besar."

    "Warung makan kecil yang banyak bertuliskan Warmindo, bahkan kamu menemui banyak Warmindo di tengah-tengah kampung, ada juga yang lokasinya berseberangan jalan."

    "Sementara warung makan yang lebih besar biasanya terletak di pinggir jalan besar."

    "Selain warung makan, banyak juga kamu melihat tempat-tempat yang menyediakan banyak layanan untuk mahasiswa nantinya."

    "Seperti tempat print, alat tulis, toko sehari-hari, dan tempat laundry pakaian."

    scene bg town street 1 with fade

    "Kamu terus berjalan sembari mengamati keadaan disekitarmu."

    "{i}Gubrakkk!!!{/i}"

# Sfx things fell
# Shake

    "Tiba-tiba kamu mendengar suara yang keras dari arah di depanmu."

    "Setelah mendekatinya, kamu melihat kerumunan orang di dekat sebuah mobil angkut."

    show w normal

    "Penasaran, kamu mendekati kerumunan yang ada di depanmu dan bertanya kepada salah seorang yang ada disana."

    mc normal jacket  "Ada apa ini mas?"

    hide w normal with dissolve

    w normal"Ohh ini mas, ada yang lagi angkut, angkut pindahan mahasiswa baru itu."

    w  "Diangkut pake mobil waktu mau ambil barang-barang yang ada di mobil angkut, malah ban mobilnya jeblos diselokan mas. Jadi barang-barangnya pada jatuh.
    Kamu melihat barang-barang berserakan di sekeliling mobil angkut."

    "{b}!Social stats tutorial!{/b}"

    "Kegiatan dengan masyarakat luas maupun organisasi dapat meningkatkan stats {b}Sosial{/b}mu."

    "Stats sosial yang tinggi terkadang akan menampilkan {b}event tertentu{/b} dalam game."

    "Selain menampilkan event tertentu, terkadang dengan melakukan kegiatan sosial kamu akan mendapatkan {b}hadiah{/b} tertentu."

    "Kamu memutuskan untuk:"

    menu: 
        "Membantu mengambil barang-barang yang terjatuh":
            call ambil_jatuh
        "Membantu mengeluarkan ban mobil yang jeblos":
            call mobil_jeblos

    scene bg town street 1 with dissolve
    
    "Beberapa menit kemudian semua masalah sudah berhasil di selesaikan."

    "Kini orang-orang yang ikut membantu mengeluarkan mobil yang terjeblos juga mengambil barang-barang yang terjatuh di jalanan sedang beristirahat di teras rumah."

    "Kamu yang juga ikut membantu juga beristirahat di teras rumah bersama warga lain."
    
    "Setelah beberapa menit beristirahat dan mengobrol bersama warga, kamu memutuskan untuk kembali ke kosmu."

    "Tidak melihat warga yang tadi kamu temui di awal tadi, kamu berpamitan kepada warga yang ada disekitarmu."

    "Kemudian kamu meninggalkan rumah warga tersebut dan berjalan ke arah kosmu."

    "......"

    "Beberapa langkah berjalan, ada yang memanggilmu dari belakang."

    "Kamu melihat bapak-bapak yang sebelumnya kamu ajak bicara berjalan mendekatimu."

    w normal"Kok keburu pulang saja mas, ini yang punya barang tadi memberi ini buat yang bantu-bantu tadi."

    "Melihat kebelakang, kamu melihat warga yang awal kamu temui di awal tadi."

    "Warga itu membawa sebuah kotak box putih, dan memberikan itu kepadamu."

    "Kamu menerima kotak box putih dari bapak-bapak tersebut."

    # Bg box putih

    mc normal jacket "Terimakasih mas"

    w "Tidak apa, malah saya yang terimakasih mas, tadi sudah dibantu segala sudah merepoti sayanya."

    mc "Tidak apa kok mas, kalau begitu saya pamit pulang dulu mas."

    w "Oh ya ya, hati-hati mas."

    "Kamu berjalan pulang ke arah kosmu."

    "Mengeluarkan ponsel dari saku celanamu kamu melihat jam yang sudah menunjukan pukul 10.00."

    mc "habis ini terus pulang, mandi lalu siap-siap ke kampus."

    "Setelah menentukan tujuan selanjutnya kamu pulang ke kosmu."

    scene bg black

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