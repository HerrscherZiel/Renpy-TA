
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

label first_kota:

    call screen trans_screen

    scene kos depan with dissolve

    "Pada siang harinya, kamu memutuskan untuk pergi berkeliling area sekitar untuk mengisi waktu luangmu."

    "Mengendarai sepeda motormu, kamu mulai menarik gas secara perlahan." 
    
    "Tanpa tujuan yang pasti kemana kamu akan pergi dengan motormu, kamu mengendari motor keluar dari parkiran kosan."

    "Cuaca yang cerah pada siang hari ini mempermudah untuk orang-orang berpergian." 
    
    "Langit biru dihiasi awan Cirrocumulus dengan sinar matahari yang bersinar terik terlihat ketika kamu menengok ke atas."

    scene town street 2 with dissolve
    
    mc normal jacket "Cuaca cerah seperti ini, memang cocok buat jalan-jalan."

    mc "Kemarin habis hujan juga, sekarang jadi segar cuacanya."

    mc "Hmmm... pergi kemana ya? Ke kota apa daerah kampus ya? Hmmm..."

    "Melewati gapura dan keluar dari jalanan kampung, kamu melihat kondisi jalan raya yang ramai dipenuhi oleh kendaraan-kendaraan pribadi."

    "Mungkin karena sekarang merupakan musim liburan yang hampir berakhir, jadi orang-orang menggunakan kesempatan terakhir mereka untuk berpergian sebelum kembali kerutinitas harian masing-masing."

    "Meski jalanan dipenuhi oleh kendaraan-kendaraan yang berlalu-lalang, tapi tidak terlihat adanya kemacetan. Hanya ada antrian yang lumayan panjang di area yang dekat dengan lampu lalu lintas."

    "Dengan lincahnya kamu mengemudikan sepeda motormu untuk melewati beberapa kendaraan yang ada di depanmu."

    scene bg black with dissolve

    scene bg road 1 with fade

    "Berkendara selama beberapa menit, pandanganmu teralihkan setelah melihat sebuah bangunan tinggi yang sedang dalam proses pembangunan."

    "Beberapa kendaraan dan alat konstruksi bangunan terlihat berada di sekitar kawasan proyek."

    "Kamu menyempatkan waktumu untuk menepi di pinggiran jalan dan mengamati konstruksi yang ada di depanmu matamu itu."

    "Gedung yang mungkin akan menjadi apartemen dengan perkiraan memiliki puluhan lantai terlihat sedang dibangun."

    "Tower Crane yang terlihat sedang mengangkat material-material berat pada proyek konstruksi. Kontraktor bangunan juga terlihat berlalu langan di sekitar area proyek. "

    "Kamu juga melihat beberapa kontraktor bangunan sedang beristirahat di warung-warung makanan kaki lima di sekitar jalan di dekat lokasi proyek."

    "Setelah beberapa menit mengamati konstruksi kamu meneruskan perjalananmu."

    scene bg black with dissolve

    scene bg road 2 with fade

    "Tidak jauh kamu mengendarai sepeda motormu, kamu melihat sebuah rumah sakit yang berada di dekat gedung-gedung kampus di universitasmu."

    "Satu dua mobil ambulance datang datang mengantarkan ataupun pergi untuk menjemput pasien."

    "Tepat di seberang jalan atau lebih tepatnya di depan rumah sakit, kamu melihat gedung kampus yang memiliki papan nama bertuliskan Fakultas Kedokteran, Kesehatan Masyarakat dan Keperawatan."

    "Mungkin karena lokasi rumah sakit yang berada di seberang gedung kampus, kamu melihat beberapa orang yang terlihat seperti mahasiswa berlalu-lalang di dekat area rumah sakit."

    "Entah karena mereka memiliki urusan di rumah sakit ataupun mereka memiliki urusan di gedung kampus mereka."

    "Selesai mengamati, kamu meneruskan perjalananmu."

    scene bg minimart_out fade

    "Kamu mengendarai motormu melewati gedung kampusmu." 
    
    "Tidak jauh dari gedung kampusmu terdapat minimarket dimana kamu dan Rissa pergi kesana ketika kegiatan orientasi berakhir."

    "Melewati minimarket kamu melihat bangunan rumah sakit lain." 

    scene bg road 3 with fade
    
    "Sama seperti bangunan rumah sakit yang sebelumnya, rumah sakit yang ada di depanmu itu juga terletak berseberangan dengan bangunan dari kampusmu.."

    "Melihat bagian depan rumah sakit itu, terlihat masih sangat rapi dan baru membuatmu berpikir itu merupakan rumah sakit yang baru saja selesai dibangun atau paling tidak baru saja selesai direnovasi."

    "Tidak berhenti lama, setelah mengamati rumah sakit itu selama beberapa waktu kamu melanjutkan perjalananmu."

    scene bg road 4 with fade

    "Setelah berkendara selama beberapa menit, kamu mencapai {i}landmark{/i} berikutnya."

    "Terlihat sebuah masjid besar berada di sebelah kirimu. Masjid yang berada di sebelah kiri jalan itu merupakan masjid kampus."

    "Tidak jauh dari masjid kampus, kamu melihat track untuk jogging, yang berada disepanjang pinggir jalan. Kamu juga melihat beberapa bangunan yang digunakan untuk olahraga indoor beberapa puluh meter di depanmu."

    scene bg road 5 with fade
    
    "Lapangan untuk softball juga nampak pada sisi kiri jalan. Meskipun untuk menuju lapangan tersebut tidak ada jalan langsung dari jalan, dan harus mencari jalan masuk lain."

    "Setelah lapangan softball kamu juga melihat bangunan yang nampak seperti stadion. Kamu tidak dapat melihat bangunan apa itu sepenuhnya dari pinggir jalan."

    "Selain dibatasi dengan pagar pembatas, bangunan itu juga terletak di samping pepohonan yang tinggi dan rimbun. Terdapat banyak tumbuhan merambat yang ikut menutupi pandanganmu."

    "Di sepanjang sisi kiri jalan kamu melihat berbagai fasilitas untuk olahraga, dan taman yang dipenuhi banyak tumbuhan."

    "Sementara tidak jauh setelah mengendarai sepeda motormu untuk beberapa puluh meter kedepan, kamu melihat gedung kampus di sisi kanan jalan raya."

    "Namun gedung kampus yang terdapat pada sisi kanan jalan tersebut bukanlah gedung kampus milik universitas dimana kamu berkuliah. Melainkan gedung kampus dari universitas lainnya, yang memang bertempat bersebelahan dengan universitasmu."

    "Sama seperti sebelumnya, di dekat gedung kampus kamu juga melihat beberapa orang yang nampak seperti mahasiswa berlalu-lalang."

    "Kemudian kamu melanjutkan perjalananmu untuk menjelajahi area disekitar kampusmu."

    scene bg town street 3 with fade

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