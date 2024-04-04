
label first_kos:

    $ firstKos = False

    scene bg kos night with dissolve
    pause 2.0

    
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

            show screen stats_screen with dissolve

            show screen days_screen with dissolve
            
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

    call eat
    
    "Membuang sampah pada tempat sampah yang ada di depan kos, kamu kemudian kembali ke dalam kamar kos."

    "Waktu telah cepat berlalu semenjak kamu duduk di teras kamarmu."

    "Sekarang waktu sudah menunjukan pukul 12.45, kamu masuk kedalam kamar dan bersiap untuk tidur." 
    
    "Seperti biasa, kamu menyetel waktu alarm dan memainkan playlist lagu untuk tidur."

    "Setelah menyelimuti badanmu dengan selimut, kamu mulai mencoba menutup mata untuk menutup hari."

    "Mendengar alunan nada yang menenangkan, kesadaranmu mulai menghilang. Hingga pada akhirnya kamupun tertidur lelap."

    "DAY 4 END"

    jump day5

    return

label persiapan_kuliah:

    $ placeKeys = 3
    show screen trans_screen
    scene bg kos morn with fade
    pause 2.0

    "Setelah menyelesaikan aktivitas pada pagi harimu, sekarang sudah waktunya untuk dirimu mempersiapkan diri sebelum kuliah."
    
    "Saat ini waktu sudah menunjukkan pukul 06.45, kamu segera pergi ke kamar mandi sebelum terlalu siang."

    "Merasakan segarnya air di pagi hari, membuat pikiranmu kembali fresh, kamu tidak sabar untuk segera berkuliah."

    "Mengguyur tubuhmu dengan air sembari bersiul-siul untuk menghilangkan rasa dingin yang dirasakan, 
    tidak memerlukan 10 menit untukmu keluar dari kamar mandi dan kembali ke kamarmu."

    "Selesai mengenakan pakaian yang kamu siapkan sebelumnya, kamu berdiri terdiam di depan cermin yang menggantung pada almari pakaian."

    mc normal jacket "Huh akhirnya aku masuk kuliah… huhhh good luck me!!"

    "Kamu menepuk kedua sisi wajahmu untuk menyiapkan dirimu berangkat menuju kelas kuliah pertamamu." 
    
    "Kemudian kamu mengenakan tas dan mengambil kunci motor yang kamu gantungkan di gantungan pakaian, 
    setelah mengambilnya kamu segera keluar dari kamar."

    scene bg town street 1 with dissolve

    "Brmmm brmmm"

    "Memanaskan motor selama beberapa menit, kamu mendorongnya sampai depan pintu masuk kosan."

    "Terlihat beberapa kamar kos masih terbuka, dan masih mterdengar suara guyuran air dari dalam kamar mandi."

    mc normal jacket "Apa mungkin mereka berangkat siang ya? Kok pada belum siap begitu? Apa mereka enggak takut telat?"

    mc "Ahh…. ngomong-ngomong tentang telat…."

    "Tersadar kelas pertamamu dimulai pukul 07.15, kamu panik dan segera mengambil HP untuk melihat waktu saat ini."

    "07.02"

    mc "Haaaaa…. Kupikir sudah mepet banget ternyata masih lumayan lah ya…. sekitar 15 menit lagi..."

    mc "Perjalanan dari sini ke kampus juga paling sekitar 10 menitan…. Yasudah berangkat saja lah…"

    "BRUMMMM"

    "Menarik gas motor, kamu mengendarai sepeda motormu keluar dari lingkungan kampung menuju jalan raya."

    scene bg town street 3 with fade

    "Berbeda dengan pagi-pagi sebelumnya, pagi hari ini kamu melihat jalanan dipenuhi oleh mahasiswa yang sedang berangkat kuliah." 
    
    "Terlihat sebagian dari mereka ada yang berjalan kaki, mengendarai sepeda atau sepeda motor, menaiki alat transportasi umum, 
    maupun menggunakan ojek online."

    "Jalanan terasa lebih ramai dari biasanya, meskipun begitu kamu dengan handal mengendarai sepeda motormu melaju dengan lancar."

    scene bg campus parking lot with fade
    $ placeKeys = 8

    "Sekitar 10 menit mengendarai sepeda motormu, kamu telah sampai di parkiran motor yang ada di area kampus."

    "Banyak mahasiswa yang datang bersamaan denganmu, tampaknya banyak juga mahasiswa yang memiliki kelas dipagi hari."

    "Kamu turun dari motor lalu mengambil HP dari saku celanamu untuk mengecek waktu saat ini."

    mc normal jacket "Sekarang jam…"

    "07.11"

    mc "Ohhh udah hampir 07.15, aku harus cepat-cepat cari ruang kelasnya!"

    mc "Oh iya… kalau tidak salah tadi Rissa sudah sempat ngirim pesan ruang kelasnya di group chat, sebentar aku cek."

    "Sembari berjalan ke arah gedung kampusmu, terdapat banyak chat yang memenuhi group chat."

    "Kamu terus menscroll pesan yang ada untuk mencari chat dari Rissa mengenai ruangan yang ditempati untuk kelas nanti." 
    
    "Setelah lama menscroll di group chat, akhirnya kamu menemukan pesan tersebut."

    "{i}HY U-203, lantai dua ruangan ketiga dari Lab TRPL.{/i}"

    "Setelah membaca chat tersebut, kamu memasukan HP kembali ke dalam saku, lalu bergegas ke ruangan yang ada pada pesan itu."

    jump first_class

label kos_d5N:
    
    call screen trans_screen with dissolve

    scene bg kos morn with dissolve

    # Materi+link tugas

    "Sesampainya di kosan, merasa sangat lelah kamu langsung merubuhkan tubuhmu ke tempat tidur."

    "Menghadap ke langit-langit kamu sempat memikirkan kejadian dan pelajaran saat kelas tadi."

    "Namun kesadaranmu lambat laun memudar."
    
    "Kamu memejamkan mata dan tak lama kemudian dirimu terlelap dalam mimpi."
    
    scene bg black with fade

    pause 2.0

    scene bg kos morn with dissolve

    "Bangun dari tidurmu, kamu melihat dari celah jendela matahari sudah mulai tenggelam." 
    
    "Langit yang semula berwarna biru sudah berubah warna menjadi orange."

    "Merasa sangat jenuh kamu memutuskan untuk mandi dan menyegarkan tubuhmu." 
    
    "Kamu mengambil handuk dan peralatan mandi lalu pergi menuju kamar mandi."

    #sfx shower

    scene bg black with fade

    call change_timephase

    call screen trans_screen with dissolve

    scene bg kos night with dissolve

    "Selesai mandi dan berganti pakaian, kamu merapikan tempat tidurmu dan menghabiskan waktu hingga matahari sepenuhnya tenggelam."

    "Kamu membaca chat baru yang dikirim pada group chat Lane."

    "Terdapat pesan dari Rissa, mengenai {b}{i}Tugas {/i}{/b} dan {b}{i}Materi {/i}{/b}."

    r normal "Temen-temen ini aku udah buatin link G-drive buat materi tadi siang dan folder buat link pengiriman tugas ya."

    "Terdapat teks tautan berwarna biru dengan nama PTI-TRPL23. Kemudian anak kelas mulai menanggapi satu persatu."

    mc normal jacket "Oh iya, tadi waktu kelas Pak Andy ninggalin tugas ya buat kita..."

    "Kamu mencoba mengecek berapa temanmu yang sudah mengerjakan tugas yang diberikan oleh Pak Andy."

    "Setelah mengeklik link yang dikirim oleh Rissa dan melihat isi dari folder tugas PTI, hanya terlihat 6 file dari mahasiswa."

    mc "Hmmm baru tadi siang udah ngumpulin aja mereka."

    "{b}!!TUGAS!!{/b}"

    "{i}Untuk mengerjakan tugas kamu dapat memilih tombol {b}'TASK'{/b} yang terletak pada kanan atas layar{/i}."

    mc "Hmmm... aku ngerjain kapan ya? Deadlinenya juga masih minggu depan."

    "Berpikir karena tidak ada kegiatan pasti yang harus kamu lakukan malam ini."
    
    "Untuk mengisi waktu malam hari, kamu memutuskan untuk melakukan kegiatan pada waktu luangmu."

    "Kamu memutuskan untuk:"

    call screen mapUI with dissolve


#Common Day Case
label choice_kos_morn:

    show screen trans_screen with dissolve
    scene bg kos morn with dissolve
    pause 2.0

    "Pada sisa waktu di pagi harimu, kamu memilih untuk tetap berada di kos."

    "Beberapa hal dapat kamu lakukan pagi hari ini, kamu memilih untuk:"

    menu:
        "Merebahkan tubuh pada tempat tidur":
            jump kos_mornS1
        
        "Membersihkan Kosmu":
            jump kos_mornS2

        "Mengerjakan tugas":
            jump kos_mornS3

label choice_kos_noon:

    show screen trans_screen with dissolve
    scene bg kos morn with dissolve
    pause 2.0

    "Kamu memilih untuk menghabiskan waktu siangmu di kosan saja."

    "Ada beberapa hal yang dapat kamu lakukan siang ini, pada akhirnya kamu memilih untuk:"

    menu:
        "Merebahkan tubuh pada tempat tidur":
            jump kos_dayS1
        
        "Menghabiskan waktu merapikan dan membersihkan area kos":
            jump kos_noonS2

        "Membugarkan tubuhmu":
            jump kos_noonS3

label choice_kos_night:

    show screen trans_screen with dissolve
    scene bg kos night with dissolve
    pause 2.0

    "Kamu memilih untuk menghabiskan sisa waktumu pada hari ini di kosan."

    "Ada beberapa hal yang dapat kamu lakukan malam ini, pada akhirnya kamu memilih untuk:"

    menu:
        "Menyudahi harimu lebih awal":
            jump kos_nightS1
        
        "Menikmati angin malam":
            jump kos_nightS2

        "Menghabiskan waktu dengan teman onlinemu":
            jump kos_nightS3
    
#morn
label kos_mornS1:

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
    $ malasc += 1
    call nap

    "Tidak melakukan hal produktif seperti yang kamu inginkan. Tapi paling tidak, kamu telah menambah energi untuk melakukan kegiatan selanjutnya."

    "........."

    "....."

    "..."
    
    if KRS3 is True:
        $KRS3 = False
        jump kos_krs4_night

    else:
        jump mandi

label kos_mornS2:

    "Mengambil peralatan kebersihan, kamu membersihkan area kosmu."
    $ bersihc += 1
    $vit += 5
    $energy -= 15
    $hunger -= 10
    $public +=5
    
    jump mandi

label kos_mornS3:

    "Kamu menyempatkan waktumu untuk mengerjakan tugas."
    jump mandi

#noon1
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
    $ tidurc += 1
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

label kos_noonS2:

    "Mengambil peralatan kebersihan, kamu membersihkan area kosmu."
    $ bersihc += 1
    $vit += 5
    $energy -= 15
    $hunger -= 10
    $public +=5

    return

label kos_noonS3:
    $ olahragac += 1
    jump sport_noonS2

#night
label kos_nightS1:

    "Waktu menunjukkan pukul 08.30 malam."
    
    "Dari pada melakukan aktivitas lainnya pada malam hari ini, kamu lebih memilih untuk menyudahi harimu lebih awal."
    $ malasc += 1
    $ tidurc += 1

    call nap

    jump sleep

label kos_nightS2:

    "Kamu memutuskan untuk menikmati angin malam(beli makan asongan) duduk di depan kos"
    $ jajanc += 1
    $ mainc += 1
    call small_eat

    jump sleep

label kos_nightS3:
    $ malasc += 1
    "Membuka laptop, lalu bermain gim dengan teman temanmu"

    jump sleep

label rebahan:

    scene bg kos morn with fade

    "Tidak ada aktivitas yang kamu lakukan pada siang hari."
    call nap
    pause 2.0

    "Kamu hanya merebahkan tubuhmu dan menghabiskan waktu dengan beristirahat."

    jump day29_night

label day29_night:

    $placeKeys = 3
    call change_timephase
    show screen trans_screen with dissolve
    scene bg kos night with fade
    pause 2.0

    "Sekarang waktu sudah menunjukan pukul 20.15 malam, kini dirimu sedang bersantai di depan teras kosan menikmati angin malam yang sejuk dan semilir."

    "Namun malam ini kamu tidak sendirian berada pada teras depan kosanmu."

    "[k] salah satu teman kosanmu sedang menemani mengobrol di teras depan kosanmu."

    kev normal "Gimana semester ini? Kampusmu udah kelar kan bro?"

    mc normal jacket "Yaaa begitulah… lu sendiri gimana? Bukannya masih ujian besok?"

    kev "Hahaha jangan tanya dong kalau aku, ya pasti ga baik-baik aja lahh"

    mc "Dasarrr… udah ga baik-baik aja malah nyantai gini… masih ujian kan lu besok?"

    kev "Yoii… santai aja bro… jangan dipikir susah, udah usaha semaksimal mungkin kan? Hehe…"

    mc "Semaksimal mungkin gimana? Sekarang aja malah engga belajar gini… hadehh…"

    kev "Udah broo… sekarang lagi penuh pikiranku jadi perlu refreshing dulu…"

    mc "Yaelah… bilang aja udah males apa capek belajar kan?"

    kev "Hehehe benar sekali."

    "[k] menghadap kearahmu dan memberikan isyarat jempol kepadamu."

    kev "Bro.. mau ke burjo gak? Makan apa minum kek?"

    mc "Lu kalo habis belajar jadi laper ya?"

    kev "Engga lah hahaha ini emang pengen nongkrong aja disana broo…"

    kev "Gimana mau engga? Kalau engga aku sendiri juga gapapa."

    mc "Yuk lah cuss… pengen minum yang seger-seger gue."

    kev "Asikk… jalan dulu aku ambil dompet bentar bro."

    "Kemudian kamu mulai berjalan sendiri ke arah warmindo untuk membeli minuman."

    "Tidak lama setelah itu [k] berlari dan menyusulmu."

    "Kalian kemudian mengobrol dan pergi ke warmindo bersama."

    scene bg warmindo with dissolve

    mc normal jacket "Es kopinya satu A’"

    aa1 normal "A’ yang satunya ? "

    kev normal "Aku magelangannya satu ya, sama es jeruk."

    aa1 "Oke-oke tunggu bentar yaa…"

    "Sesampainya di warmindo kalian langsung memesan menu yang kalian inginkan."

    mc "Oh iya, lu ujiannya sampai kapan sih?"

    kev "Keseluruhan masih sampai minggu depan sih, tapi prodiku cuma sampai lusa aja."

    mc "Enak dong, bisa langsung cabut pulang?"

    kev "Pengennya sih gitu… tapi kayaknya masih ada kerjaan lain deh."

    mc "Yahh sok sibuk lu…"

    kev "Bukan sok sibuk… emang ada kerjaan aja hadeh…"

    kev "Lu jadi pulang besok kan bro?"

    mc "Niatnya pulang besok sih… kalau engga hujan hahaha"

    kev "Males juga ya kalau hujan… emang perjalanan berapa jam sih?"

    mc "Ya ga jauh-jauh amat perjalanannya… sekitar 2 sampai 2 setengah jam an."

    kev "Wohh lumayan juga ya…"

    mc "Kalo lu berapa lama emang?"

    kev "Sekitar 4 jam?"

    mc "Lah lu sendiri malah lebih lama gitu bro…"

    kev "Ya gimana, kan emang begitu."

    "Tidak lama mengobrol pesanan kalian datang."

    aa1 "Ini a’ es kopinya, terus ini magelangan sama es jeruknya ya…"

    kev "Makasih"

    mc "Makasih…"

    kev "Waktunya makannn!!!"

    mc "Kalau makan aja semangat… giliran belajar kabur lu…"

    kev "Udah-dah belajarnya nanti lagi, makan nih…"

    mc "Silahkan-silahkan dinikmati…"

    "[k] menikmati makan malamnya dengan gembira."

    "Sementara dirimu hanya meminum minumanmu sembari membuka HP."

    "Kamu membuka notifikasi dari Lane yang sudah menumpuk. Di dalamnya sudah terdapat banyak chat antara teman sekelasmu mengenai liburan."

    "Terdapat berbagai hal yang temanmu lakukan pada liburan kali ini. Beberapa dari mereka ada yang menetap di kota ini dan menikmati liburan mereka bermain ke daerah sekitar."

    "Beberapa temanmu yang lain juga ada yang berlibur terlebih dahulu di kota sekitar, namun kemudian pulang ke kampung halaman mereka."

    "Dan yang terakhir, seperti dirimu yang langsung pulang ke kampung halaman ketika liburan dimulai."

    "Setelah membaca chat dari teman-temanmu, kamu menutup Lane kemudian berpindah membuka gim yang ada di HP."

    "Kamu menghabiskan waktumu di warmindo dengan bermain gim HP sembari menunggu dan mengobrol dengan [k]."

    scene bg black  with dissolve

    scene bg kos night with fade

    call eat

    "Sekitar 40 menit berlalu, kini kamu sudah berada di area teras depan kosanmu bersama [k]."

    "Sebelum kembali ke kosan, kamu membeli lagi es kopi di warmindo."
    
    "Kamu kembali menyinggahi kursi di area teras depan kosan sambil menikmati es kopi dibungkus plastik yang ada di tanganmu."

    kev normal "Bro aku lanjut belajar lagi ya…"

    mc normal jacket "Nah gitu dong rajin luu."

    kev "Yee emang anak rajin ini!"

    mc "Hahaha yaudah sana, aku mau ngadem dulu…"

    kev "Oke-okee, duluan bro!"

    "Beberapa menit menemanimu di teras kosan, [k] memutuskan untuk kembali ke kamarnya dan belajar."

    "Kini tinggal dirimu sendiri yang berada di teras kosan. Sembari menikmati minuman kamu memandang langit malam."

    "Malam ini langit terlihat cerah, tidak terdapat awan yang menutupi lautan bintang."

    mc "Hmm… sudah setahun yah… lama juga ternyata."

    mc "Satu tahun ini aku belajar banyak selama hidup disini."

    mc "Aku mulai beradaptasi dengan lingkungan yang ada di sekitarku."

    mc "Aku juga sudah memiliki beberapa teman disini."

    mc "Aku sudah mempelajari banyak hal baru yang ada di perkuliahan."

    mc "Aku juga sudah melalui beberapa ujian di perkuliahan."

    mc "Satu tahun ini, menurutku bukanlah hal yang buruk bagiku."

    mc "Meskipun begitu aku masih harus memperbaiki beberapa hal ketika aku hidup disini…"

    mc "Tahun-tahun berikutnya bakalan kaya gimana ya?"

    mc "Hmmm…."

    "Beberapa menit kamu menikmati waktu sendirimu malam ini."

    "Merasa cukup, dan kini badanmu sudah merasakan hawa dingin yang dibawa angin malam, kamu memutuskan untuk kembali ke kamar dan menyudahi harimu."

    scene bg kos night with fade

    "Tidak ada aktivitas lain yang kamu lakukan malam ini, kamu mengatur alarmmu sebelum mulai memejamkan kedua matamu."

    "Beberapa menit berselang, kamu telah terlelap di atas tempat tidur kosanmu."

    "Day [day] END"

    jump day30
