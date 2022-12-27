
label first_kampung:

    $ first_kampung = False

    scene bg black

    with Dissolve(2.0)

    show day2 kammorn:
        xalign 0.5 yalign 0.5
    with dissolve(3.0)

    scene bg kampung with dissolve

    show screen days_screen with dissolve

    show screen stats_screen with dissolve

    "Kamu memutuskan untuk menghabiskan waktu pagimu dengan berjalan mengelilingi lingkungan sekitar."

    "Selama berjalan mengilingi lingkungan sekitar, kamu banyak berjumpa dengan orang-orang yang sedang berjogging."

    "Kamu juga banyak melihat banyak bangunan kos, baik kos perempuan maupun kos laki-laki."

    "Selain bangunan kos juga terdapat banyak warung makan, mulai dari warung makan kecil sampai warung makan yang lumayan besar."

    "Warung makan kecil yang banyak bertuliskan Warmindo, bahkan dapat ditemui di tengah-tengah kampung."

    "Sementara warung makan yang lebih besar biasanya terletak di pinggir jalan besar."

    "{i}Gubrakkk!!!{/i}"

# Sfx things fell
# Shake

    "Kamu mendengar suara yang keras dari arah di depanmu."

    "Setelah mendekatinya, kamu melihat kerumunan orang di dekat sebuah mobil angkut."

    "Penasaran, kamu mendekati kerumunan yang ada di depanmu dan bertanya kepada salah seorang yang ada disana."

    mc normal2  "Ada apa ini pak?"

    w1  "Ohh ini mas, ada yang lagi angkut, angkut pindahan mahasiswa baru itu."

    w1  "Diangkut pake mobil waktu mau ambil barang-barang yang ada di mobil angkut, malah ban mobilnya jeblos diselokan mas. Jadi barang-barangnya pada jatuh.
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

    "Setelah selesai membantu dan beristirahat sebentar, kamu memutuskan untuk kembali ke kosmu."

    "Beberapa langkah berjalan, ada yang memanggilmu dari belakang."

    "Kamu melihat bapak-bapak yang sebelumnya kamu ajak bicara berjalan mendekatimu."

    w1 "Kok keburu pulang saja mas, ini yang punya barang tadi memberi ini buat yang bantu-bantu tadi."

    "Kamu menerima kotak box putih dari bapak-bapak tersebut."

    # Bg box putih

    mc "Terimakasih pak"

    w1 "Tidak apa, malah saya yang terimakasih mas, tadi sudah dibantu segala sudah merepoti masnya."

    mc "Tidak apa kok pak, kalau begitu saya pamit pulang dulu pak."

    w1 "Oh ya ya, hati-hati mas."

    "Kamu berjalan pulang ke arah kosmu."

    "Mengeluarkan ponsel dari saku celanamu kamu melihat jam yang sudah menunjukan pukul 10.00."

    mc "habis ini terus pulang, mandi lalu siap-siap ke kampus."

    "Setelah menentukan tujuan selanjutnya kamu pulang ke kosmu."

    scene bg black

    "Selesai mandi dan telah bersiap-siap, kamu menyalakan motormu untuk pergi kekampus."

    hide screen days_screen

    hide screen stats_screen

    call screen mapUI

    return

label ambil_jatuh:

    mc "Kalau begitu saya bantu ambil barang-barang yang jatuh pak."

    w1 "Maaf mas, merepotkan saja."

    mc "Tidak apa-apa kok pak."

    w1 "Terimakasih ya mas."

    "Kamu mulai mengambil barang-barang yang terjatuh di dekat mobil."

    "Barang-barang seperti kipas angin, rice cooker, galon dan barang rumahan yang sepertinya akan dipakai oleh anak kosan terlihat di depanmu."

    "Bersama dengan beberapa orang yang ada disekitar lokasi, kamu mulai mengambil barang yang jatuh satu persatu."

    return

label mobil_jeblos:
    
    mc "Kalau begitu saya bantu tarik mobilnya pak."

    w1 "Oh ya mas, ayo tarik bareng-bareng."

    "Kamu dan beberapa warga mulai berbaris menggenggam tali tambang yang sudah diikatkan pada mobil."

    "Pada hitungan ke 3 secara bersama-sama kamu dan warga lainnya menarik mobil yang jeblos sampai pada akhirnya ban mobil yang jeblos dapat dikeluarkan dari selokan."

    return