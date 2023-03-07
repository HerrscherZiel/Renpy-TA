
label first_kos:

    $ firstKos = False

    scene bg kos night with dissolve
    pause 2.0

    # show screen days_screen
    # show screen stats_screen 

    
    "Malam hari setelah rangkaian kegiatan orientasi berakhir, kamu merebahkan diri di kasur kosmu."

    "Sebelum memejamkan mata, kamu meluangkan waktu untuk membuka HPmu."

    "Kamu melihat banyak notifikasi dari aplikasi LANE, kamu memutuskan untuk membukanya."

    "Notifikasi yang ada berasal dari grup chat angkatanmu. Setelah membaca beberapa baris chat, dari berbagai macam topik chat yang ada kamu mengikuti percakapan mengenai bimbingan dengan dosen pembimbing."

    show phone groupchat:
        xalign 0.5
        yalign 0.6 
    with moveinbottom

    "Beberapa mahasiswa di angkatanmu membicarakan untuk melakukan bimbingan dengan dosen pembimbing mereka."

    "Beberapa dari mereka bahkan ada yang sudah menghubungi dosen pembimbing masing-masing untuk bertemu."

    "Pada saat melakukan bimbingan sendiri, mahasiswa dapat menanyakan berbagai macam hal seputar perkuliahan."

    "Mahasiswa dapat menyakan mengenai prospek dari program studi, peluang pekerjaan, jalannya perkuliahan, pemilihan mata kuliah, mata kuliah, informasi mengenai kampus, dan pertanyaan seputar perkuliahan yang lain."

    "Mengetahui isi chat yang ada dalam grup angkatanmu, kamu juga memutuskan untuk menemui dosen pembimbingmu untuk melakukan bimbingan."

    "Selain itu kamu juga ingin menanyakan mengenai pengambilan SKS pada dosen pembimbingmu."

    "Kamu mengingat perkataan pemandumu selama kegiatan orientasi."
    
    show phone groupchat:
        linear 0.8 xalign 0.8
        ease 50

    show mc normal jacket:
        xalign 0.2 yalign -0.3

    mc "Sebelum memulai kegiatan perkuliahan, kalian nantinya harus melakukan pengambilan SKS terlebih dahulu setiap awal semesternya."

    mc  "Dalam pengambilan SKS nantinya kalian akan memilih kode mata kuliah yang akan kalian dapatkan selama satu semester."

    mc  "Pilihan mata kuliah tergantung pada apa yang sudah dipilihakan atau dipaketkan oleh kampus yang sifatnya wajib untuk diambil. Meskipun begitu terkadang kalian juga dapat memilih mata kuliah tidak wajib."

    mc  "Lalu kalian juga…"

    mc  "Bicara apalagi ya waktu itu… lupa aku."

    "Mencoba mengingat perkataan pemandu kegiatan orientasimu namun kamu tetap tidak bisa mengingatnya, kemudian kamu hanya terdiam melihat langit-langit kamarmu."

    "....................."

    "............"

    "......"

    mc  "UAHHHHHH… ngantuk. Jam berapa sih udah ngantuk begini..."

    "Melihat waktu menunjukan 12.30 pada jam digital yang ada pada HPmu. Kamu meletakan HP disebelahmu, kemudian mematikan lampu kamar."

    hide phone groupchat
    with moveoutbottom

    show bg kos night dark with dissolve

    "Mending sekalian aku tanyakan besok sajalah waktu bimbingan."

    "Sekarang lanjut tidurrr!"

    "Kamu menggunakan selimutmu dan mulai memejamkan matamu."

    "Tidak ada 5 menit, kamu sudah terlelap menanti apa yang akan terjadi di hari esok."

    "................................."

    "....................."

    "............"

    "......"

    hide screen days_screen

    hide screen stats_screen

    jump day2

    return

label kos_krs3:

    if KRS3 == True:
        $placeKeys = 3
        show screen trans_screen with dissolve

        scene bg black with dissolve

        "Menghabiskan hampir seluruh waktu siang harimu berada di perpustakaan, hampir tidak ada energi lagi yang tersisa untuk melakukan aktivitas lain pada siang ini."

        "10 menit kurang lebih perjalanan pulang yang dilalui menjadi semakin berat dengan panas terik yang terus menanak tubuhmu."

        "Belum lagi perutmu yang sudah keroncongan dan dahaga terasa di kerongkonganmu."

        "Dengan sisa-sisa energimu, kamu mampir ke warmindo yang berada di dekat dengan kosan membungkus makanan untuk makan malam nanti."

        "Sesampainya di kos, setelah memarkir motor kamu langsung menuju ke kamarmu."

        "Meletakan tas ransel di atas meja belajar kemudian merebahkan tubuhmu di atas kasur."

        "Rasa letih yang dirasakan memenangkan kendali atas tubuhmu."

        "Tanpa melakukan aktivitan lainnya, kamu tertidur pulas."

        scene bg black with dissolve

        call change_timephase
        show screen trans_screen with dissolve

        scene bg kos night with fade

        pause 2.0

        "Merasa cukup dengan tidurmu, matamu terbuka ketika matahari telah turun dari katulistiwa."

        hide screen kod_matkul_btn

        "Suara gemuruh dan angin yang berhembus kencang adalah hal yang pertama kamu dengarkan setelah bangun dari tidurmu."

        "Hujan deras dan angin kencang tampaknya akan menemani sisa malam harimu."

        #sfx grumbling

        "GRUGRUGRUGRUGRU"
        with vpunch

        "Bukan hanya suara petir yang bergemuruh, tampkanya perutmu juga memberontak meminta jatah makanan."

        mc normal jacket "Oh iya, tadi belum sempet makan malah ketiduran… Huhhh...."

        "Teringat dirimu yang tidak sempat melakukan apa-apa di siang hari selain hanya melakukan Pengisian KRS kamu menghela nafasmu."

        mc "Tadi kutaruh mana ya tadi bungkusannya?"

        mc "Apa masih di cantolan motor ya?"

        "Bangun dari tempat kasur, kamu berjalan keluar dari kamarmu."
        
        "Meskipun terlindung dari guyuran hujan secara langsung, bagian dalam dari bangunan kos terlihat dibasahi oleh percikan air hujan."
        
        "Atap asbes yang seharusnya melindungi dari air hujan tidak dapat melindungi dari percikan air yang masuk terbawa oleh angin."

        "Kamu segera mengambil makanan yang kamu beli tadi di cantolan motormu dan bergegas kembali kedalam kamar."

        mc "Tadi panas banget, sekarang bisa hujan deras kaya begini hhhuuuuuu…"

        "Dengan badan yang menggigil, kamu mengambil selimut dari tempat tidur untuk menghatkan tubuhmu."

        "Kemudian setelah meletakan makanan pada piring, dan menghidupkan laptopmu, kamu mulai memutar video yang ada pada Utube."

        scene bg kos night with fade

        "Video yang diputar pada Utube menjadi teman yang menemaniw makan malammu."

        call eat
        show screen stats_changer("eat", 0)

        "Merasa santai karena sudah melakukan kewajiban Pengisian KRS, kamu berniat untuk menikmati malammu dengan menonton film semalaman."

        "Sekitar pukul 02.00 dini hari ketika matamu sudah tidak kuasa menahan kantuk kamu menutup laptomu."
        
        "Kamu memutuskan untuk tidur dan menutup harimu."

        "Setelah semua lampu indikator yang ada pada laptop mati sepenuhnya, kamu kembali membaringkan punggungmu ke atas kasur."

        "Seperti biasa, kamu menyetel alarm dan memainkan playlist lagu penuntun tidurmu."

        "Dengan senandung lullaby yang terdengar dari HPmu, kamu tertidur dan mengakhiri harimu."

        "Day 3 End"
   
    else:
        $placeKeys = 3
        window hide

        show screen trans_screen with dissolve

        pause 2.0
        
        scene bg kos morn with dissolve

        "Sesampainya di kamar kos, kamu menghabiskan sisa waktu siangmu dengan tidur siang."

        "Karena merasa gerah, kamu melepas bajumu dan mengarahkan kipas angin ke arah tubuhmu yang sudah lemas di tempat tidur."

        "Merasakan sejuknya angin yang berhembus dari kipas angin membuat kesadaranmu mulai memudar."

        "Tidak memakan waktu yang lama untuk tertidur dengan pulas."

        call change_timephase
        pause 1.0
        scene bg kos night with fade
        pause 1.0

        mc normal jacket "HAccihhh!!! Huuuu kok dingin banget sih. Hhuhuuuuu tadi siang perasaan gerah banget."
        with vpunch

        "Terbangun dari tidur siang, tubuhmu menggigil merasakan dinginnya kondisi saat ini."

        "Mematikan kipas angin yang masih mengembuskan angin sepoi-sepoi ke arah tubuhmu, kamu berdiri mendekat ke jendela yang ada di kamar."

        "Shhhhhhh Shhhhhh Shhhhhh"

        #sfx heavy rain

        "Langit gelap dan hujan deras disertai oleh angin kencang sudah menggantikan cuaca panas terik yang dirasakan sejak siang tadi."

        mc "Memang benar ya, siang panas terik habis itu hujan deras kayak gini.... Hacihhhh."

        "Cuaca dingin malam ini membuat tubuhmu menggigil kedinginan."

        mc "Baju mana baju tadi… dingin banget."

        "Merasakan hawa dingin yang menusuk tulang, kamu tersadar kondisi tubuhmu yang masih setengah telanjang badan."
        
        "Kamu mengambil bajumu yang menggantung di gantungan pakaian."

        mc "Hachihhh… Berasa mau masuk angin begini."

        mc "Minum es, kipas angin, tidur nggak pakai baju, diluar hujan angin. Hmmm kurang apa coba hadehhh."

        "Untuk kedua kalinya di hari ini kamu menyesal dengan apa yang kamu lakukan."

        mc "Hujan begini gamungkin bisa keluar sih, enaknya ngapain ya?"

        mc "Ohh iya tadi yang krsan bersama di perpustakaan sudah pada selesai belum ya?"

        "Kembali ke tempat tidurmu, kamu mengambil selimut kemudian bersandar ke dinding di pojokan kamar lalu membuka HPmu."

        "Beberapa notifikasi dari group Lane terlihat dari lockscreen HPmu. Kamu menggeser gambar gembok untuk membuka lockscreen kemudian membuka aplikasi Lane."

        "Setelah membuka group chat, kamu membaca chat yang ada secara sekilas."

        mc "Kayanya pada lancar-lancar aja sih ya. Enggak ada masalah besar kayaknya."

        mc "Hmmm... apa kucoba sekarang aja ya KRSannya?"

        "Berniat untuk melakukan pengisian KRS malam hari ini, kamu mengambil laptop yang berada di dalam tas."
        
        "Meletakan laptop yang baru saja diambil di atas meja belajar, kamu berpindah dari tempat tidur ke meja belajarmu masih diselimuti oleh selimut yang membungkus badanmu."

        "Setelah menekan tombol power untuk menghidupkan laptop, kamu menunggu proses booting selesai."

        "Tuingg"

        "Belum sempat membuka browser untuk mencoba KRSmu, terdapat pesan yang masuk pada Lanemu."

        t normal "{i}Oiii broo.. Ayo mabar lah mumpung pada on nih, tunggu di discred ya, yang lain nunggu!{/i}"

        mc "Sering banget kalau orang mau produktif malah diajak main, huhhhh....." 
        
        mc "Tapi yaudah lah, lagian masih bisa KRSan besok."

        "Setelah itu, kamu membuka game yang ada pada laptopmu dan menghabiskan malam hari dengan bermain game bersama temanmu hingga pagi hari."

        "Sekali lagi dalam hari ini kamu membuat keputusan yang akan membuatmu menyesal kedepannya."

        "Namun apapun yang kamu pilih waktu akan terus berjalan, dan kamu tidak mungkin bisa mengulangnya lagi."

        "Day 3 End"

    hide screen days_screen

    hide screen stats_screen
    window hide

    jump day4

label kos_krs4:

    scene bg kos morn with dissolve

    call change_timephase

    show screen trans_screen with dissolve

    pause 2.0

    "Selesai mandi, kewajiban melakukan pengisian KRS masih ada dalam to do listmu hari ini."
    
    "Setelah berganti pakaian, kamu mengambil laptop dari dalam tasmu."

    "Kamu duduk dan meletakan laptopmu di meja belajar." 
    
    "Setelah menekan tombol power on pada laptop, kamu mengambil kertas note yang kamu siapkan pagi tadi."

    mc normal jacket "Semoga ga ada masalah KRSannya."

    "Kamu membuka browser dan membuka website Simaster."

    "Merasa sudah paham dengan alur pengisiannya, kamu mencoba tanpa melihat kertas catatan yang kamu tulis."

    mc "Di simaster kemudian pilih tombol"

    menu: 
        "Pilih Sign In kemudian isikan ID dan Password":

            mc "Sign In terus isikan data diri kita, terus nanti isi captcha yang muncul."

    show home simaster:
        xalign 0.5
        yalign 0.4
    
    with dissolve
    
    mc "Setelah itu kita kan masuk ke halaman beranda akun Simaster."

    mc "Lalu dari halaman beranda simaster, harusnya selanjutnya aku memilih menu:"

    hide home simaster

    menu:
        "Pilih menu Akademik Kemahasiswaan":

            mc "Pilih menu Akademik Kemahasiswaan di kiri atas layar."
            
            mc "Benar, pilih menu Akademik Kemahasiswaan."

        "Pilih menu Adminstrasi":

            mc "Pilih menu Administrasi?"

            mc "Hmmm kayaknya bukan, coba aku lihat kertas notenya."

            "Kamu melirik kearah kertas note yang berisi catatan panduan pengisian KRS."

            mc "Ohhh pilih Menu Akademik Kemahasiswaan."


    show home akademik:
        xalign 0.5
        yalign 0.4
    
    with dissolve

    mc "Setelah memilih menu Akademik Kemahasiswaan, akan muncul banyak pilihan sub menu."

    mc "Disini kemudian harusnya memilih:"

    hide home akademik


    menu: 
        
        "Pilih sub menu Akademik lalu Pengisian KRS":
            
            mc "Pilih sub menu Akademik terus kalau gak salah pilih lagi menu Pengisian KRS kan ya?"

            mc "Oh Bener-bener, pilih sub menu Akademik lalu pilih Pengisian KRS."

        "Pilih sub menu Akademik lalu Bimbingan DPA":

            mc "Menu Akademik terus Bimbingan DPA? "

            mc "Kok malah bimbingan DPA sih, kan mau Pengisian KRS."

            mc "Harusnya habis milih sub menu Akademik, aku milih menu Pengisian KRS."


    show home akademik krs:
        xalign 0.5
        yalign 0.4
    
    with dissolve

    mc "Kemudian, setelah masuk halaman Pengisian KRS, langkah selanjutnya yaitu."

    hide home akademik krs

    menu: 

        "Pilih aksi pada periode pengisian KRS yang ada":

            mc "Pilih aksi pada periode pengisian KRS ini kan?"

            mc "Tambah KRS kan berarti ini, di periode Pengisian KRS yang ada."


    show pengisian krs:
        xalign 0.5
        yalign 0.4
    
    with dissolve

    mc "Setelah memilih aksi pada periode pengisian KRS yang terbuka, kita akan dapat melakukan pemilihan mata kuliah yang ditawarkan."

    mc "Hmmmm... Mata kuliah apa saja sih yang seharusnya dipilih?"

    hide pengisian krs

    menu:

        "Memilih mata kuliah sesuai kode mata kuliah yang dibagikan":

            hide pengisian krs

            mc "Memilih mata kuliah sesuai kode mata kuliah yang ada."

            mc "Waduh, listnya enggak kutulis di note, apa aja ya mata kuliah yang ada di list itu?"

            "Berpikir sebentar, kamu akhirnya mengingat sesuatu."

            mc "Oh kalau tidak salah, list untuk mata kuliah pilihan di share Rissa di group Lane."

            "Membuka grup lane yang ada pada hpmu, kamu mulai mencari daftar mata kuliah dan kode mata kuliah pilihan."

            "Scroll"

            "Scroll"

            "Scroll"

            "Setelah beberapa kali menggeser-geser layar hpmu, kamu melihat chat yang dikirim oleh Rissa." 
            
            "Chat tersebut berisikan nama mata kuliah beserta kode mata kuliah juga kelas untuk tiap mata kuliah."
            
            "Chat tersebut diketik dengan bold sehingga terlihat lebih mencolok ketimbang chat lainnya."

            mc "Ohh oke-oke ketemu, berarti tinggal dipilih yang ada disini kan ya."

            mc "Hmmm mending kusalin dulu aja ke noteku, biar gampang lihatnya nanti."

            "Kamu menulis chat yang di kirimkan oleh Rissa itu pada notemu."

            scene bg black with fade

            #sfx writing

            pause 1.0

            window hide

            call screen kode_matkul with dissolve

            show screen kod_matkul_btn

            # pause

            "Untuk dapat melihat kode mata kuliahnya lagi, kamu dapat memilih tombol 'KODE' yang ada di samping kanan layar."

            "Setelah melihat kode mata kuliah yang ada pada catatan grup Lane, kamu mencoba memilih mata kuliah sesuai kode mata kuliah yang ada."

            call screen isi_krs with fade

            "Setelah selesai memilih mata kuliah sesuai kode mata kuliah yang ada di chat group kamu mencari save untuk menyimpan pilihanmu. Namun setelah lama mencari kamu masih belum menemukan tombol save."

            scene bg kos morn with fade

            hide screen kod_matkul_btn with dissolve
            
            mc normal jacket "Ini emang gabisa disave atau error ya? Hmmm enggak ada tombol save ini, apa aku tanya Rissa aja ya? Tanya aja lah biar cepet selesai."

            "Mengambil ponselmu, kamu mencari kontak Rissa pada aplikasi lane."

            mc "{i}Eh Ris, mau tanya itu yang pengisian KRS memang enggak ada tombol save kah?{/i}"

            "Setelah mengirimkan chat itu, belum sampai kamu meletakan kembali HPmu di meja, indikator chat sudah berubah menjadi warna biru."

            "Tidak lama kemudian chat balasan dari Rissa muncul di layar Hpmu."

            r normal2"{i}Pasti belum baca di grup yaa hahahaha{/i}"

            mc "{i}Di grup? Emang ada ya?{/i}"

            r "{i}Untuk tombol save emang enggak ada, itu kemarin aku tanya sama Pak Andy emang enggak ada, asalkan sudah pilih terus masukin captcha katanya sudah kepilih.{/i}"

            mc "{i}Ohhh yaudah kalau gitu, selesai berarti aku.{/i}"

            r "{i}Baru pengisian KRS ya [name]{/i}?"

            mc "{i}Hehe iyaa…{/i}"

            r "{i}Kemarin kamu enggak ikut ke perpustakaan pusat sih…{/i}"

            mc "{i}Gabisa aku kemarin, yaudah makasih yaa.{/i}"

            r "{i}Oke-oke masama…{/i}"

            "Kamu mengembalikan Hp di atas meja, kemudian kembali memandang ke layar laptopmu yang masih ada pada halaman Pengisian KRS."

            mc "Udah selesai berarti kan ya… Huhh capek juga ternyata."

            # screen KRS    

    scene bg kos morn with fade

    "Mematikan laptop, kamu bersandar di tembok pojok tempat tidurmu sambil bermain game yang ada di hpmu."

    mc normal jacket "Sudah selesai pengisian KRS jadi kerasa tenang begini."
    
    mc "Aman juga sih, tadi enggak banyak masalah selama KRSan."

    mc "Kalau sampai kejadian kehabisan kelas karena kuota penuh sih payah. Tapi kayaknya teman seangkatan di grup enggak ada yang kena."

    mc "Selesai KRS berarti tinggal nunggu ACCan dari dosen pembimbing. Kalau begitu siang ini ngapain ya?."

    mc "Tidur aja kali ya?"

    "Merasa bingung karena tidak memiliki aktivitas lain untuk mengisi siang harimu, kamu merebahkan badan dan menutup mata."

    jump kos_krs4_night

    return

label kos_krs4_night:

    call change_timephase

    $ placeKeys = 3 

    show screen trans_screen with dissolve

    pause 1.4

    scene bg kos night with dissolve

    "Tap tap tap tap tap"

    "Pada malam harinya kamu sedang asyik bermain game dengan laptopmu. Kamu telah bermain game sejak sekitar pukul 7 malam, setelah ada seorang temanmu yang mengajak untuk bermain."

    "Tiga jam sudah berlalu semenjak kamu menghabiskan waktu dengan temanmu. Kini kamu hanya bersandar di kursi meja belajar."

    "Setelah salah satu dari temanmu berhenti bermain, satu-persatu temanmu yang lain juga ikut menghilang dari voice channel di grup discerd."

    "Sekarang hanya tersisa dirimu sendiri yang masih berada di voice channel, kamu menekan icon micmu untuk mute kemudian membuka browser."

    "Masuk kedalam Utube dan mulai menonton video yang masuk di berandamu."

    "Tuing"

    "Mendengar suara notfikasi pesan masuk, kamu mengambil HPmu yang kamu letakan di sebelah laptop."

    show phone groupchat:
        xalign 0.5
        yalign 0.5
    with dissolve

    r normal2"{i}Teman-teman untuk KRSnya kata Pak Andy sudah di approve yaa!{/i}"

    r "{i}Coba cek punya kalian masing-masing ya!{/i}"

    r "{i}Caranya : Masuk Simaster => Akademik Kemahasiswaan => Akademik => Rencana Studi{/i}"

    r "{i}Nanti di kolom approval, dicek sudah di approve belum yaa.{/i}"

    "Seperti biasanya, Rissa sebagai {i}tokoh penting{/i} dalam kelas mengirim chat informasi di grup Lane." 
    
    "Kemudian satu persatu teman-temanmu menanggapi apa yang di kirim oleh Rissa."

    t normal "{i}Clear punyaku.{/i}"

    t "{i}Punyaku sudah hijau semuaa.{/i}"

    t "{i}Sipp sudah di approve.{/i}"

    "Melihat apa yang dikirim Rissa, kamu juga ikut mengecek apakah KRSmu sudah di setujui atau belum."

    mc normal jacket "Emmm Akademik Kemahasiswaan….. Akademik…. Rencana Studi…."

    "Melakukan seperti instruksi yang diberitahukan oleh Rissa, kamu mendapati semua KRSmu sudah bertuliskan approve."

    "Tuingg"

    r normal2"{i}[name] punyamu udah di approve kan?{/i}"

    "Kamu membuka pesan yang baru saja Rissa kirim."

    mc "{i}Punyaku sudah, barusan aku cek, sudah approve semua.{/i}"

    r "{i}Bagus-bagus, berarti sudah semua yang dosen pembimbingnya Pak Andy.{/i}"

    mc "{i}Oh iya hari pertama kita masuk jam berapa ya Ris?{/i}"

    r "{i}Kita jam 07.15, kelas pagi mulai jam segitu di jadwal.{/i}"

    mc "{i}Ohh oke-oke.{/i}"

    r "{i}Oke kalau gitu, besok waktu masuk jangan sampai telat ya hahaha.{/i}"

    mc "{i}Ya masak masuk pertama mau nelat hehehe, oke makasih yaa.{/i}"

    r "{i}Sama-sama{/i}"

    "Selesai berbalas chat, kamu kembali menatap layar laptop dan melanjutkan aktivitasmu sebelumnya."

    scene bg kos night with fade

    "Berada di dalam kamar dengan waktu yang lama membuatmu merasa jenuh. Kamu keluar dari kamar kemudian berjalan menuju warmindo yang ada di dekat kosan."

    "Sesampainya di warmindo, kamu hanya memesan satu es kopi untuk dibungkus."

    "Malam ini kamu melihat warmindo dipenuhi oleh orang-orang yang terlihat sedang bermain game bersama sembari menongkrong."

    "Setelah kamu menerima pesananmu dan membayarnya kamu segera kembali ke menuju kosmu." 
    
    "Sesampainya di kos, kamu tidak langsung masuk ke kamarmu. Berhenti di teras depan kosan kemudian duduk pada salah satu kursi yang ada."
    
    "Kamu mengambil hp yang ada di saku celanamu."

    "Waktu yang ada pada hpmu menunjukkan pukul 11.15 malam. Suasana jalanan dan lingkungan sekitar sudah mulai sepi. Sudah tidak banyak suara kendaraan yang berlalu-lalang"

    "Malam yang cerah dimana bintang-bintang berbaur menghiasi langit yang tak terbebas dari kawanan awan." 
    
    "Bulan menjadi benda langit yang paling terang menerangi langit malam ini."

    "Kamu duduk bersandar menikmati heningnya malam dan hembusan angin malam yang berhembus semilir."

    "Membuka tali karet yang menutup bungkus plastik es kopi yang kamu beli, kamu mulai meminum sembari menghadap ke langit malam."

    mc normal jacket "{i}Enggak berasa minggu kemarin masih di rumah, besok sudah mau masuk kuliah aja.{/i}"

    mc "{i}Perasaan baru kemarin kegiatan orientasi selesai.{/i}"

    mc "{i}Perasaan juga baru kemarinnya lagi aku dapat pengumuman diterima kuliah disini.{/i}"

    mc "{i}Rasanya cepat banget ya, kalau sudah dijalani.{/i}"

    mc "{i}Huhhh… Lega akhirnya bisa masuk kuliah disini.{/i}"

    mc "{i}Sekarang memang masih belum punya banyak kenalan sih, cuma Rissa sama mas Kos sebelah.{/i}"

    mc "{i}Kira-kira besok kuliah bagaimana ya? Apa seperti waktu SMA dulu? Semoga pelajarannya enggak terlalu susah…{/i}"

    mc "{i}Hmmm… Kuliah… masih belum tahu nantinya gimana, tapi semoga menyenangkan dan mempermudah masa depanku nanti.{/i}"

    "Memikirkan bagaimana masa kuliahmu nanti, kamu menikmati waktumu merenung sendiri duduk di teras depan kamarmu."

    scene bg black with dissolve

    scene bg kos night with fade

    "Sruttttt"

    "Lama menatapi langit tidak terasa es kopi yang ada di bungkus plastik yang kamu pegang sudah habis. Badanmu juga sudah mulai merasakan dinginnya malam di kota yang baru ini."

    "Membuang sampah pada tempat sampah yang ada di depan kos, kamu kemudian kembali ke dalam kamar kos."

    "Waktu telah cepat berlalu semenjak kamu duduk di teras kamarmu."

    "Sekarang waktu sudah menunjukan pukul 12.45, kamu masuk kedalam kamar dan bersiap untuk tidur." 
    
    "Seperti biasa, kamu menyetel waktu alarm dan memainkan playlist lagu untuk tidur."

    "Setelah menyelimuti badanmu dengan selimut, kamu mulai mencoba menutup mata untuk menutup hari."

    "Mendengar alunan nada yang menenangkan, kesadaranmu mulai menghilang. Hingga pada akhirnya kamupun tertidur lelap."

    "DAY 4 END"

    jump day5

    return

#Common Day Case

#Case1
label kos_dayS1:

    pause 2.0 

    scene bg kos morn with dissolve

    "Setelah melakukan kegiatan di pagi hari, kamu berbaring lemas di atas tempat tidurmu."

    "Bukan karena lelah, bukan juga karena lapar, kamu hanya berbaring lemas di atas tempat tidurmu karena malas melakukan kegiatan lain."

    "Dengan tatapan kosong kamu melihat ke arah atas, hanya melihat ke langit-langit kamar tanpa memikirkan apapun."

    mc normal jacket "Hmmm…. Bosan banget, enaknya ngapain ya?"

    mc "Mau keluar males, di kos juga nggak ada aktivitas lain selain main HP sama laptop... Hmmmm."

    mc "Cobalah ku cek dulu kalo ada informasi di grup Lane angkatan."

    "Setelah mengumpulkan niat, kamu berdiri kemudian mengambil HPmu yang sedang dicharge di atas meja belajar."

    "Setelah mengambil HP, kamu kembali merubuhkan tubuhmu di atas tempat tidur."

    "Dengan posisi badan tengkurap, kamu membuka lock yang ada di hp kemudian membuka aplikasi Lane."

    "Scroll"

    "Scroll"

    "Scroll"

    mc "Enggak ada informasi baru tentang kuliah, cuma obrolan teman-teman saja."

    "Menutup aplikasi lane, lalu kamu menekan icon aplikasi phogram dan mulai menikmati konten yang ada di fypmu."

    "Setelah merasa bosan dengan konten-konten yang ada, kamu menutup phogram dan menekan icon aplikasi lain."

    "Kali ini kamu membuka permainan yang ada di HPmu. Melakukan misi harian selama beberapa menit, lalu menutup permainanmu itu."

    "Merasa bosan dan tidak tahu ingin melakukan apa, kamu hanya berpindah dari satu aplikasi ke aplikasi lain."

    "Selama beberapa menit kamu melakukan hal ini secara berulang-ulang."

    "Tidak lama kemudian kamu beralih memainkan lock screen di HPmu."

    mc "Hmmmm..."

    mc "Hahhh..."
    
    mc "Bosan banget… "

    mc "Butuh musik penyemangat kayaknya aku, biar jadi produktif."

    "Membuka aplikasi musik kamu memainkan playlistmu yang berjudul Rock. Berharap dengan mendengarkan lagu yang ada di playlist itu dapat membuatmu mendapatkan energi untuk melakukan aktivitas lain."

    "Setelah suara musik mulai berdendang, kamu membalik badanmu menghadap kembali menghadap langit-langit kamar."

    "Beberapa menit musik berputar, bukannya menambah semangat, kamu malah merasakan sebaliknya dan merasa semakin lemas."

    "Sedikit demi sedikit rasa kantuk kembali kamu rasakan."

    "Silau sinar matahari yang masuk lewat celah-celah jendela ditambah hembusan kipas angin yang kamu hidupkan membuat matamu tertutup secara perlahan."

    "Pada akhirnya kamu hanya menghabiskan sisa waktu di siang harimu dengan kembali tertidur pulas."

    call nap

    "Tidak melakukan hal produktif seperti yang kamu inginkan. Tapi paling tidak, kamu telah menambah energi untuk melakukan kegiatan selanjutnya."

    "........."

    "....."

    "..."
    
    if KRS3 is True:
        $KRS3 = False
        jump kos_krs4_night

    else:
        call screen mapUI
    return






