
label first_kampung:

    $ firstKampung = False

    scene bg town street 2 with Dissolve(2.0)

    # show screen days_screen with dissolve

    # show screen stats_screen with dissolve

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

label first_kota:

    scene bg town street 1 with dissolve

    call change_timephase

    show screen trans_screen with dissolve

    pause 3.0

    "Pada siang harinya, kamu memutuskan untuk pergi berkeliling area sekitar untuk mengisi waktu luangmu."

    "Mengendarai sepeda motormu, kamu mulai menarik gas secara perlahan." 
    
    "Tanpa tujuan yang pasti kemana kamu akan pergi dengan motormu, kamu mengendari motor keluar dari parkiran kosan."

    "Cuaca yang cerah pada siang hari ini mempermudah untuk orang-orang berpergian." 
    
    "Langit biru dihiasi awan Cirrocumulus dengan sinar matahari yang bersinar terik terlihat ketika kamu menengok ke atas."

    scene bg town street 3 with dissolve
    
    mc normal jacket "Cuaca cerah seperti ini, memang cocok buat jalan-jalan."

    mc "Kemarin habis hujan juga, sekarang jadi segar cuacanya."

    mc "Hmmm... pergi kemana ya? Ke kota apa daerah kampus ya? Hmmm..."

    "Melewati gapura dan keluar dari jalanan kampung, kamu melihat kondisi jalan raya yang ramai dipenuhi oleh kendaraan-kendaraan pribadi."

    "Mungkin karena sekarang merupakan musim liburan yang hampir berakhir, jadi orang-orang menggunakan kesempatan terakhir mereka untuk berpergian sebelum kembali kerutinitas harian masing-masing."

    "Meski jalanan dipenuhi oleh kendaraan-kendaraan yang berlalu-lalang, tapi tidak terlihat adanya kemacetan. Hanya ada antrian yang lumayan panjang di area yang dekat dengan lampu lalu lintas."

    "Dengan lincahnya kamu mengemudikan sepeda motormu untuk melewati beberapa kendaraan yang ada di depanmu."

    scene bg black with dissolve

    scene bg project with fade

    "Berkendara selama beberapa menit, pandanganmu teralihkan setelah melihat sebuah bangunan tinggi yang sedang dalam proses pembangunan."

    "Beberapa kendaraan dan alat konstruksi bangunan terlihat berada di sekitar kawasan proyek."

    "Kamu menyempatkan waktumu untuk menepi di pinggiran jalan dan mengamati konstruksi yang ada di depanmu matamu itu."

    "Gedung yang mungkin akan menjadi apartemen dengan perkiraan memiliki puluhan lantai terlihat sedang dibangun."

    "Tower Crane yang terlihat sedang mengangkat material-material berat pada proyek konstruksi. Kontraktor bangunan juga terlihat berlalu langan di sekitar area proyek. "

    "Kamu juga melihat beberapa kontraktor bangunan sedang beristirahat di warung-warung makanan kaki lima di sekitar jalan di dekat lokasi proyek."

    "Setelah beberapa menit mengamati konstruksi kamu meneruskan perjalananmu."

    scene bg black with dissolve

    scene bg hospital 1 with fade

    "Tidak jauh kamu mengendarai sepeda motormu, kamu melihat sebuah rumah sakit yang berada di dekat gedung-gedung kampus di universitasmu."

    "Satu dua mobil ambulance datang datang mengantarkan ataupun pergi untuk menjemput pasien."

    "Tepat di seberang jalan atau lebih tepatnya di depan rumah sakit, kamu melihat gedung kampus yang memiliki papan nama bertuliskan Fakultas Kedokteran, Kesehatan Masyarakat dan Keperawatan."

    "Mungkin karena lokasi rumah sakit yang berada di seberang gedung kampus, kamu melihat beberapa orang yang terlihat seperti mahasiswa berlalu-lalang di dekat area rumah sakit."

    "Entah karena mereka memiliki urusan di rumah sakit ataupun mereka memiliki urusan di gedung kampus mereka."

    "Selesai mengamati, kamu meneruskan perjalananmu."

    scene bg minimart_out with fade

    "Kamu mengendarai motormu melewati gedung kampusmu." 
    
    "Tidak jauh dari gedung kampusmu terdapat minimarket dimana kamu dan Rissa pergi kesana ketika kegiatan orientasi berakhir."

    "Melewati minimarket kamu melihat bangunan rumah sakit lain." 

    scene bg hospital 2 with fade
    
    "Sama seperti bangunan rumah sakit yang sebelumnya, rumah sakit yang ada di depanmu itu juga terletak berseberangan dengan bangunan dari kampusmu.."

    "Melihat bagian depan rumah sakit itu, terlihat masih sangat rapi dan baru membuatmu berpikir itu merupakan rumah sakit yang baru saja selesai dibangun atau paling tidak baru saja selesai direnovasi."

    "Tidak berhenti lama, setelah mengamati rumah sakit itu selama beberapa waktu kamu melanjutkan perjalananmu."

    scene bg mosque 1 with fade

    "Setelah berkendara selama beberapa menit, kamu mencapai {i}landmark{/i} berikutnya."

    "Terlihat sebuah masjid besar berada di sebelah kirimu. Masjid yang berada di sebelah kiri jalan itu merupakan masjid kampus."

    scene bg jog spot with fade

    "Tidak jauh dari masjid kampus, kamu melihat track untuk jogging, yang berada disepanjang pinggir jalan. Kamu juga melihat beberapa bangunan yang digunakan untuk olahraga indoor beberapa puluh meter di depanmu."

    scene bg softball with fade
    
    "Lapangan untuk softball juga nampak pada sisi kiri jalan. Meskipun untuk menuju lapangan tersebut tidak ada jalan langsung dari jalan, dan harus mencari jalan masuk lain."

    scene bg sport building with fade

    "Setelah lapangan softball kamu juga melihat bangunan yang nampak seperti stadion. Kamu tidak dapat melihat bangunan apa itu sepenuhnya dari pinggir jalan."

    "Selain dibatasi dengan pagar pembatas, bangunan itu juga terletak di samping pepohonan yang tinggi dan rimbun. Terdapat banyak tumbuhan merambat yang ikut menutupi pandanganmu."

    "Di sepanjang sisi kiri jalan kamu melihat berbagai fasilitas untuk olahraga, dan taman yang dipenuhi banyak tumbuhan."

    "Sementara tidak jauh setelah mengendarai sepeda motormu untuk beberapa puluh meter kedepan, kamu melihat gedung kampus di sisi kanan jalan raya."

    "Namun gedung kampus yang terdapat pada sisi kanan jalan tersebut bukanlah gedung kampus milik universitas dimana kamu berkuliah. Melainkan gedung kampus dari universitas lainnya, yang memang bertempat bersebelahan dengan universitasmu."

    "Sama seperti sebelumnya, di dekat gedung kampus kamu juga melihat beberapa orang yang nampak seperti mahasiswa berlalu-lalang."

    "Kemudian kamu melanjutkan perjalananmu untuk menjelajahi area disekitar kampusmu."

    scene bg town street 3 with fade

    pause 1.0

    scene bg town street 1 with fade

    "Tidak hanya jalan raya yang kamu lalui, kamu juga mengendarai sepeda motormu untuk masuk ke area perkampungan."

    "Terlihat banyak sekali rumah-rumah kos yang berada di perkampungan sekitar. Hal tersebut merupakan hal yang wajar, mengingat dekatnya perkampungan dengan kampus yang ada."

    "Lama berputar-putar mengelilingi area sekitar, warna langit yang semula biru laut sudah berubah menjadi warna orange."

    "Siang yang sudah berubah menjadi sore membuatmu memtuskan untuk kembali ke kosan."

    jump kos_krs4_night

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