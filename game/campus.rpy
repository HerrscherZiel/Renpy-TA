    
label first_kampus:    

    $ first_kampus = False

    scene bg black

    with Dissolve(2.0)

    # show day2 kampusnoon:
    #     xalign 0.5 yalign 0.5
    # with dissolve(3.0)

    scene bg campus hall with dissolve

    "Setelah memarkir motormu di parkiran, kamu berjalan memasuki gedung kampus."

    "Gedung Herman Yohannes atau biasa disebut oleh orang-orang gedung HY merupakan gedung dimana progam studi TRPLmelakukan aktivitas kuliah."

    "Gedung HY juga merupakan gedung yang sama yang digunakan sebagai tempat untuk kegiatan orientasi hari sebelumnya."

    "Memasuki gedung, kamu mengira akan melihat banyak teman seangkatanmu yang menunggu untuk bimbingan, namun ternyata tidak ada satupun yang mahasiswa yang sedang menunggu di lobby."

    "Sempat kamu menengok ke kanan dan ke kiri untuk mencari gerombolan mahasiswa, namun masih tidak terlihat satupun mahasiswa kecuali kamu."

    mc normal jacket "Huh masih setengah 12, apa mungkin aku kepagian ya datangnya?"

    "11.35 terlihat dari HPmu yang baru saja kamu ambil dari saku."

    "Ada beberapa notif dari grup chat yang belum kamu buka lagi dari pagi tadi."

    mc "{i}Paling juga basa-basi seperti pagi tadi, kalau tidak salah juga jam 12 sampai jam 1an kan janjian ketemuannya.{/i}"
    
    mc  "{i}Mungkin jam setengah 1 kali ya? Aku cari ruang kelasnya.{/i}"

    "Mengingat janji jam pertemuan yang ada pada grup chat, kamu memutuskan untuk tidak langsung mencari ruang kelas pertemuan."

    "Mengabaikan notif dari grup chat yang ada kamu mengeklik icon dari salah satu game yang ada di HPmu."

    mc "{i}Login harian dulu aja lah, sambil nyelesain daily mission.{/i}"

    "Kamu duduk kursi yang ada di pinggir lobby dan mulai memainkan permainan yang ada di hpmu."

    "..............."

    "......."

    "..."

    "..."

    "......."

    "................"

    "15 menit berlalu namun masih tidak ada satupun mahasiswa lain yang memasuki gedung."

    mc "{i}Ini memang orang-orang yang mepet semua atau gimana ya?{/i}"

    mc "{i}Hmmm gimana ya? Jadi resah gini.{/i}"

    mc "{i}Yaudahlah mending cari ruangnya dulu.{/i}"

    "Memasukan HP ke dalam saku, kamu mulai bergerak mencari Lab TRPL yang disebutkan di chat grup Lane tadi pagi."

    "Gedung HY sendiri memiliki bentuk seperti huruf  UU, dan memiliki 2 lantai."

    "Setelah berkeliling di area bawah kamu tidak menemukan ruangan bertuliskan Lab TRPL."

    "Kamu kemudian berjalan menuju lantai 2 menggunakan tangga di dekat lobby yang terletak di tengah gedung."

    scene bg campus upper hall with fade

    "Setelah menaiki anak tangga, kamu berjalan menelusuri lorong lantai 2."

    "Pada sisi kiri gedung kamu melihat beberapa ruangan, dan terdapat satu ruangan dengan pintu terbuka."

    mc normal jacket "Yang mana ya?, ternyata diatas juga banyak ruangan begini."

    mc "{i} Apa yang pintunya terbuka itu ya?{/i}"

    "Melewati beberapa kelas yang pintunya tertutup, kamu berjalan menuju kelas dengan pintu yang terbuka."

    "Ketika berjalan mendekati ruangan tersebut, tiba-tiba pintu ruangan yang ada dibelakangmu terbuka."

    "Kamu menoleh kebelakang, dan melihat seorang mahasiswa yang kamu kenal."

    mc "Rissa kamu sedang cari ruanganya juga?"

    r normal2"Ohh halo [name], engga kok, itu disitu ruangannya, Pak Andy sudah masuk juga, sudah mulai sekitar 10 menit lalu."

    mc "Sudah mulai ??"

    r "Iyaa, di grup kan sudah kubilang kata Pak Andy dimajuin bimbingannya."

    mc "Kamu chat begitu di grup?"

    "Kamu langsung mengambil HP dalam sakumu dan membuka grup chat Lane."

    show phone groupchat:
        xalign 0.5
        yalign 0.6 
    with moveinbottom

    "Scroll"

    "Scroll"

    "Scroll"

    "Terdapat chat dari Rossaine dengan text yang di bold."

    "Teman-teman kata Pak Andy bimbingannya jadi sekitar jam setengah 12an yaa.."

    hide phone groupchat
    with moveoutbottom
        
    r "Iyaa kann??"

    mc "Baru buka HP aku, pantas saja kutunggu engga ada mahasiswa yang masuk gedung."

    r "Hahaha, sudah kuduga, cepat masuk sana, aku mau cari toilet dulu."

    mc "Iya iya."

    r "Oh iya [name] kamu tahu toilet paling dekat ada dimana?"

    mc "Kalau tidak salah di bawah kita ini terus dipojokan ke arah sana yang paling dekat."

    r "Oh oke oke makasih ya."

    "Rissa langsung berjalan menuju arah yang kamu tunjukan."

    "Sementara kamu mendekati ruangan yang baru saja Rissa keluar dari ruangan tersebut."

    "Knock knock knock"

    scene bg campus class with fade

    # Sfx knock

    mc normal jacket "Permisi"

    show pa normal

    # show r normal2 at left

    "Memasuki ruangan terlihat seorang pria muda yang sedang duduk dan beberapa mahasiswa yang sedang mendengarkan pria tersebut."

    hide pa normal with dissolve

    pa normal"Oh ada yang masuk lagi ini teman-teman."

    mc "Permisi pak."

    pa "Masuk saja mas, silahkan mau duduk dimana terserah."

    "Kamu melihat hampir semua kursi yang ada di kursi belakang sudah dipenuhi oleh mahasiswa lain."

    pa "Nha, karena baru masuk mungkin bisa perkenalan dulu? Supaya teman-teman yang ada disini dan saya juga tahu masnya?"

    "Kamu berdiri di depan kelas, kemudian menghadap ke arah teman-temanmu."

    mc "Baik pak, Perkenalkan nama saya [name]."

    pa "Baik mas [name], silahkan duduk, sembari menunggu teman-teman yang belum datang."

    "Mengangguk, kamu berjalan menuju kursi kosong yang ada di barisan depan."

    "............."

    "......."

    "...."

    scene bg black 
    with Dissolve(1.0)

    scene bg campus class 
    
    with dissolve

    "...."

    "......."

    "............."

    "Menunggu beberapa menit, beberapa mahasiswa lainnya memasuki ruangan dan melakukan perkenalan seperti yang kamu lakukan sebelumnya."

    "Salah satunya adalah mahasiswa yang kemarin sore kamu lihat di minimart, yang bernama Joji."

    pa normal "Yak karena sudah jam segini, bapak mulai saja."

    pa "Jadi sebelumnya kalau bimbingan seperti ini, biasanya satu persatu, bisa bareng-bareng tapi nanti biasanya satu persatu karena yang ditanyakan berbeda-beda."

    pa "Tapi karena ini pertama kali, dan biasanya yang ditanyakan sama juga jadi saya kumpulkan menjadi satu."

    pa "Besok-besok kalau mau bimbingan tinggal chat saya saja, tanya bisanya kapan, nanti saya tentukan, atau bisa juga lewat {i}Simaster{/i} nanti saya jelaskan."

    show semester:
        xalign 0.5
        yalign 0.4    
    with dissolve
    
    pa "Nah, jadi perkuliahan itu semester gasal itu dimulai biasanya dimulai dari bulan Agustus sampai Desember."

    pa "Setelah Desember nanti akan ada libur panjang semester."
    
    pa "Kemudian semester genap dimulai dari bulan Febuari sampai bulan Juni."

    hide semester
    
    show pertemuan:
        xalign 0.5
        yalign 0.4    
    with dissolve

    pa "Selama satu semester itu terdapat {b}14 minggu pertemuan total{/b}."
    
    pa "Ditambah {b}satu minggu{/b} masing-masing untuk {b}UTS{/b} dan {b}UAS{/b}."

    pa "{b}UTS{/b} dan {b}UAS{/b} akan dilakukan setelah 7 pekan perkualiahan normal"

    hide pertemuan

    show krs:
        xalign 0.5
        yalign 0.4    
    with dissolve

    pa "Sebelum mulai kuliah kalian bisa melakukan pengisian KRS, KRS sendiri itu merupakan singkatan dari {b}{i}Kartu Rencana Studi{/i}{/b}."
    
    pa "Seperti namanya, KRS merupakan rencana studi kamu yang akan diambil selama {b}satu semester{/b}."

    pa "Jadi nanti yang dimaksut pengisian KRS adalah {b}{i}proses memilih mata kuliah untuk satu semester kedepan{/i}{/b}."

    pa "Untuk kalian di semester pertama, baiknya memilih mata kuliah yang sudah di {b}wajibkan{/b} oleh kampus."

    pa "Karena ada beberapa mata kuliah yang {b}wajib{/b} untuk diambil, dan ada juga mata kuliah yang {b}bisa di ambil setelah menyelesaikan mata kuliah sebelumnya{/b}."
    
    pa "Mata kuliah wajib merupakan mata kuliah yang wajib diselesaikan selama kamu berkuliah."

    pa "Sementara contoh mata kuliah yang bisa diambil setelah menyelesaikan mata kuliah sebelumnya adalah, contoh mata kuliah {b}{i}Basis Data II bisa diambil setelah menyelesaikan Basis Data I{/i}{/b}."

    hide krs with dissolve

    show krs 1:
        xalign 0.5
        yalign 0.4    
    with dissolve 

    pa "Setiap mata kuliah memiliki kapasitasnya masing-masing. Kapasitas yang dimaksud adalah jumlah mahasiswa per kelasnya."

    pa "Setiap mata kuliah juga memiliki nilai atau bebas SKSnya masing-masing."

    pa "SKS adalah Satuan Kredit Semester, dimana dalam satu semester kalian paling banyak dapat memiliki sebanyak 24 SKS."

    pa "Untuk menyelesaikan kuliah S1 sendiri diperlukan 144-148 SKS untuk bisa lulus."

    hide krs 1 with dissolve

    show krs 2:
        xalign 0.5
        yalign 0.4
    with dissolve 

    pa "Nah setelah kalian memilih semua mata kuliah yang diambil. Kalian menunggu persetujuan  dari dosen pembimbing akademik kalian."

    pa "Kalian baiknya menginformasikan mata kuliah yang kalian ambil ke dosen pembimbing, untuk meminta persetujuan dan jika ingin bertanya mengenai mata kuliah yang dipilih."

    pa "Sekiranya untuk KRS seperti itu, nanti saya beri tahu mata kuliah apa saja yang kalian ambil di semester ini."

    hide krs 2 with dissolve

    call screen trivia_perkuliahan1 with dissolve

    pa "Bagaimana apakah ada pertanyaan mengenai alur perkuliahan ?"

    pa "Bapak tunggu kalau ada...."

    ".........."

    "......"

    "..."

    pa "Ya karena sepertinya belum ada, bapak lanjut menjelaskan mengenai pengisian KRS."

    show home simaster:
        xalign 0.5
        yalign 0.4    
    with dissolve
    
    pa "Pertama, untuk melakukan pengisian KRS kalian bisa membuka website {b}{i}Simaster{/i}{/b}"

    pa "Masuk menggunakan akun masing-masing yang sudah diberi oleh kampus ya."

    hide home simaster

    show home akademik:
        xalign 0.5
        yalign 0.4    
    with dissolve 

    pa "Kemudian kalian pilih menu {b}Akademik Kemahasiswaan{/b} yang ada pada bagian atas kiri."
    
    pa "Melalui menu {b}Akademik Kemahasiswaan{/b} nanti kalian pilih sub menu {b}Akademik{/b}."

    hide home akademik

    show home akademik krs:
        xalign 0.5
        yalign 0.4    
    with dissolve 
    
    pa "Pada sub menu akademik, kemudian kalian pilih menu {b}Pengisian KRS{/b}."

    hide home akademik krs

    show pengisian krs:
        xalign 0.5
        yalign 0.4    
    with dissolve 

    pa "Nah ini halaman Pengisian KRSnya."

    pa "Pada halaman {i}Pengisian KRS{/i}, kamu dapat memilih periode pengisian KRS, kemudian setelah mengklik maka kalian akan melihat banyak nama mata kuliah beserta kode mata kuliahnya.
        Disitulah kalian melakukan pengisian KRS."
    
    pa "Di halaman itu kalian tinggal memilih mata kuliah sesuai dengan nama atau kode mata kuliahnya, disitu juga terdapat keterangan kelas dan dosen pengampunya."

    hide pengisian krs
  
    call screen simaster_pengisiankrs with dissolve

    pa "Kurang lebih seperti itu untuk Pengisian KRSnya."

    pa "Oh iya, untuk bimbingan bersama DPA yang melalui Simaster sekalian bapak jelasin juga."

    show home akademik:
        xalign 0.5
        yalign 0.4
    with dissolve

    pa "Pertama dari halaman beranda di {b}{i}Simaster{/i}{/b} kalian memilih menu {b}Akademik Kemahasiswaan{/b}."
    
    pa "Sama seperti pengisian KRS, kemudian kalian pilih sub menu {b}Akademik{/b}."

    hide home akademik

    show home akademik dpa:
        xalign 0.5
        yalign 0.4
    with dissolve
    
    pa "Nah disini bedanya kalian memilih sub menu yang berbeda."

    pa "Pada sub menu akademik, pilihlah {b}Diskusi DPA{/b}."

    hide home akademik dpa

    show diskusi dpa:
        xalign 0.5
        yalign 0.4
    with dissolve

    pa "Pada halaman tersebut, kalian bisa menulis pesan disitu untuk menghubungi saya."

    pa "Atau kalau saya sendiri, jika kalian mau juga bisa langsung mengechat saya melalui nomor telepon untuk bimbingan."

    hide diskusi dpa

    pa "Di bimbingan sendiri, kalian bisa tanya mengenai berbagai macam seputar perkuliahan."

    pa "Dari penjelasan Alur perkuliahan, Sarana yang ada selama Kuliah, Bimbingan mata kuliah, Prospek masa depan, dan lain sebagainya."

    pa "Jadi semisal ketika kalian bingung kedepannya ingin memilih mata kuliah seperti apa yang sekiranya sesuai dengan minat, bakat, ataupun pekerjaan yang ingin kalian dapatkan besok, bisa dikomunikasikan dengan dosen pembimbing."

    pa "Hmm apalagi ya? Sudah ngomong banyak saya, mungkin dari teman-teman ada yang ingin ditanyakan?"

    mc normal jacket "{i}Tanya apa yaa, baru dikasih tahu informasi sebanyak itu, masih memproses informasi aku.{/i}"

    r normal2"Oh iya pak, saya waktu orientasi kemarin sempat denger, ada kantin kejujuran ya pak disini?"

    pa "Oh iyaa, itu nanti tempatnya kalian lurus saja, ada di lantai 2 kok, perbatasan antara gedung X dan gedung HY."

    pa "Ya sesuai namanya, mungkin waktu SMA atau SMK di sekolah kalian juga ada kan, nanti biasanya penjual dari luar, atau mungkin mahasiswa, menitipkan jajanan di tempat itu."

    pa "Biasanya sudah ada toples untuk uang, beserta dengan daftar harga dari makanannya, jadi kalian tinggal ambil dan bayar sesuai saja."

    pa "Ada lagi kah pertanyaannya?"

    r "Pak Andy, untuk UTS dan UASnya kalau di perkuliahan bagaimana ya?"

    pa "Sebenarnya seperti kalau kalian di sekolah sebelumnya, kalian dapat jadwal, ada nomor kursi, dan tinggal mengerjakan."

    pa "Kalau mekanismenya untuk UTS atau UAS sendiri tergantung dosen pengampunya juga."

    pa "Mungkin bisa ditanyakan sebelum UTS atau UAS kepada dosen pengampu mata kuliahnya."

    pa "Seperti itu kurang lebihnya untuk UTS dan UAS, mungkin ada pertanyaan yang lain kah?"

    "Kemudian satu persatu mahasiswa lainnya mulai bertanya mengenai kehidupan perkuliahan."

    scene bg black with dissolve

    pause 2.0

    scene bg campus hall with dissolve

    "Ketika waktu sudah menunjukan pukul 12.30 Pak Andy mengakhiri sesi bimbingan yang dilakukan."

    "Sebelum meninggalkan ruangan, Pak Andy berkata akan menitipkan daftar mata kuliah yang akan digunakan untuk memilih KRS kepada Rosainne."

    "Rosainne yang ada dalam grup chat Lane ternyata adalah Rissa."

    "Setelah Pak Andy meninggalkan ruangan, mahasiswa lain saling berkenalan dan mengakrabkan diri satu sama lain, meskipun terdapat beberapa mahasiswa yang langsung meningalkan ruangan."

    "Kamu sendiri ikut bersosialisasi dengan teman-teman barumu."

    "Melakukan perbincangan ringan dan mengobrol mengenai kehidupan kuliah nantinya."

    "Setelah beberapa menit berbincang, beberapa mahasiswa memutuskan untuk pulang."

    "Beberapa dari mahasiswa juga ada yang mengusulkan untuk makan bersama di suatu tempat makan."

    "Ada beberapa mahasiswa yang merespon dengan positif, ada juga beberapa yang lebih memilih untuk pulang, salah satunya adalah kamu."

    mc normal jacket"Aku duluan ya teman-teman, aku gabisa ikut makan-makannya."

    r normal2 "Beneran gak ikut kamu [name]?"

    mc "Engga Ris, ada urusan lain aku."

    mc "{i}Tentu saja cuma alasan hahaha{/i}"

    r "Wahh gak seru nih, yasudah hati-hati yaa!"

    mc "Besok besok kalau ada lagi mungkin ikut aku." 
    
    mc "Yaudah, duluan yaa."

    r "Okee"

    "............"

    "......."

    "Setelah berpamitan kamu langsung berjalan menuju parkiran untuk pulang."

    mc "Entah kenapa kalau habis ketemu orang gitu capek banget ya aku."

    mc "Pulang makan tidur lahh."

    mc "Oh iya ngisi KRSnya sudah bisa mulai besok kan ya? Kalau gak salah."

    mc "Tinggal nanti malem tanya si Rissa aja lah gimananya."

    mc "Sekarang yang penting tidur duluuu."

    scene bg black with dissolve

    "Dalam perjalanan kamu menyempatkan diri untuk berhenti di warmindo yang ada dekat dengan kampusmu."

    "Perutmu yang sudah keroncongan memaksamu untuk mengisinya terlebih dahulu sebelum mengistirahatkan badan."

    "Kamu memesan dan memakannya di tempat."

    call eat

    "Kemudian setelah makanan yang kamu pesan habis, kamu langsung melanjutkan perjalanan ke kos karena merasakan badanmu yang sudah sangat lelah."

    scene bg black with fade

    window hide
    
    $placeKeys = 3

    show screen trans_screen with dissolve

    pause 2.0

    "Setelah sampai di kamar kosmu, kamu merasakan rasa lelah yang membuatmu mengantuk."

    "Meletakan barang bawaanmu di meja belajar, tanpa mengganti pakaian kamu langsung merebahkan tubuhmu diatas kasur."

    "Tidak lama setelah merebahkan badan kesadaranmu mulai menghilang dengan cepat"
    
    "Belum sampai beberapa menit dirimu sudah terlelap dan tertidur dengan pulas."

    scene bg black

    pause 2.0

    call change_timephase

    show screen trans_screen with dissolve

    scene bg kos night with dissolve

    pause 2.0

    "Kamu terbangun setelah matahari sudah tak terlihat lagi."

    "Karena langsung tertidur, kamu belum sempat melakukan aktivitas lain di siang harinya."

    "Perutmu yang siang tadi sudah kamu isi, sudah mengeluarkan suara gemuruh lagi."

    mc normal jacket "Aduhh tidurku kelamaan, sudah malem begini."

    mc "Laper banget lagi…"

    mc "Makan apa ya? Apa ke Warmindo lagi aja yah?"

    mc "Mandi dulu mungkin ya, keringetan begini."

    "Memutuskan untuk mandi terlebih dahulu, kamu bangun dari tempat tidur dan mengambil pakaian ganti di dalam lemari."
    
    "Kemudian kamu berjalan ke arah kamar mandi kos."

    ".............."

    "........."

    "...."

    "Kos yang kamu tempati merupakan kos khusus laki-laki."

    "Kos tersebut memeliki 7 buah kamar dan 2 kamar mandi."

    "Selama beberapa hari menempati kos, hanya dirimu yang sudah datang dan menempati kos." 
    
    "Sementara kamar yang lain masih terlihat gelap dan terkunci."

    "Namun beberapa hari terakhir, para penghuni kos lainnya mulai berdatangan."

    "Satu demi satu penghuni mulai datang dan meramaikan tempat kos."

    "Masih terlihat satu kamar yang masih gelap gulita, sementara yang lain sudah terdengar suara dari dalam kamar kos."

    "Melihat kamar mandi yang terlihat kosong, kamu langsung masuk ke dalamnya dan mandi."

    "............"

    "......"

    # Sfx shower

    scene bg black with dissolve

    pause 1.0

    scene bg kos night with dissolve

    "......."

    "............."

    "Selesai mandi dan kembali ke kamar, ketika ingin keluar dari kamar kosmu kamu teringat box putih yang diberikan kepadamu pagi tadi."

    "Box putih itu kamu letakan di atas meja belajar."

    mc normal jacket "Oh iyaa, tadi pagi aku dapet ini yaa."

    "Kamu mengambil kotak box tersebut dan membukanya."

    mc "Wohh nasi kotak !!"
    
    mc "Udah sama aja makan malam ini, gaperlu keluar nyari makan jadinya."

    "Setelah membuka box putih yang ternyata berisi satu paket nasi kotak, kamu mengurungkan niatmu untuk pergi ke warmindo."

    mc "Oh iya sambil makan sambil lihat chat grup Lane kalau ada info baru lagi."

    show phone groupchat:
        xalign 0.5

        yalign 0.5

    with dissolve

    "Scroll"
    
    "Scroll"
    
    "Scroll"

    mc "Hmm belum ada chat dari Rissa, berarti Pak Andy belum jadi mengirim kode mata kuliah ya?"

    # mc "Kalau belum "

    mc "Terus malem ini ngapain ya enaknya?"

    hide phone chat with dissolve

    mc "hmmm…"

    "Memikirkan apa yang ingin kamu lakukan malam itu, kamu membuka laptop dan menyalakannya."

    "Menunggu proses booting selesai, tanpa sadar kamu sudah menghabiskan apa yang ada di dalam box makanan tersebut."

    call eat

    "Setelah laptopmu selesai booting, kamu kemudian membuka aplikasi Stem dan masuk menggunakan akunmu."

    "Dalam library game yang ada pada akun Stemmu, kamu memilih MonHan kemudian menekan tombol {i}Play{/i}"

    mc "Maen MonHan asik kayaknya…"

    "{i}Bro vc discred ? Mabar MonHan kita, bantu Fatalis gimana?{/i}"

    "Kamu mengirim chat itu ke salah satu kontak yang ada di Lanemu."

    "Kamu menghabiskan waktu malammu di depan laptop, dan bermain game sampai malam suntuk."

    scene bg black with dissolve

    "Ketika waktu sudah menunjukan pukul 1 pagi lebih, kamu mematikan laptopmu."

    "Mematikan lampu kamar, kemudian membaringkan tubuh di atas kasur."

    "Seperti biasa, sebelum terlelap kamu memainkan playlist lagu yang ada di HPmu."

    "Tidak lupa untuk mengecek apakah jam alarm sudah pada waktu yang tepat atau belum."

    "Tidak lama menutup mata, kamu sudah tertidur pulas untuk yang kedua kalinya di hari itu."

    "Hari ke 2 selesai."

    hide screen days_screen

    hide screen stats_screen

    jump day3

    return
