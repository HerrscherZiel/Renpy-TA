
label persiapan_krs:
    
    # Showe sound

    scene bg black with dissolve

    pause 2.0

    "Sesampainya di kos, hal pertama yang kamu lakukan adalah mengambil handuk dan pergi untuk mandi."

    scene bg kos morn with fade

    mc normal jacket "Segar banget habis mandi."

    "Tuing"

    "Suara notifikasi chat masuk terdengar dari smartphonemu di dalam saku celana yang kamu gantung di kamar mandi."

    mc "Sudah pada sampai di perpustakaan kah?"

    "Selesai mengeringkan tubuhmu dengan handuk, kamu mengambil smartphone yang ada di celanamu."

    "Terdapat satu pesan yang dikirim oleh Rissa."

    "{i}Ini disini ya.{/i}"

    "Rissa mengirim pesan dan alamat lokasi yang akan digunakan untuk melakukan pengisian KRS bersama."

    "Kamu membuka alamat peta yang dikirimkan oleh Rissa"

    # Map Perpus

    show perpus:
        xalign 0.5
        yalign 0.4

    with dissolve

    mc "Hoo yang disana tah, lumayan deket dari kos sih, paling enggak sampai 10 menit."

    mc "{i}Okey, aku berangkat habis ini.{/i}"

    mc "{i}Udah banyak yang datang kah?{/i}"

    "Kamu membalas chat Rissa sekaligus bertanya mengenai siapa saja yang sudah datang."
    
    hide perpus with dissolve

    "Tidak lama kamu keluar dari kamar mandi, terdengar suara notifikasi dari HPmu lagi."

    "Tuingg"

    "{i}Baru 4 orang sih, mungkin molor sedikit seperti biasa hahaha.{/i}"

    mc "{i}Emang kira-kira yang berangkat ke perpustakaan berapa nanti?{/i}"

    "{i}Mungkin 10an anak atau belasan, yang kontakan sama aku cuma segituan sih.{/i}"

    mc "{i}Oh oke, aku sekitar jam 10.15an paling sampai sananya nanti.{/i}"

    "{i}Okey okey, Jangan lupa bawa laptop.{/i}"

    "{i}Siap Siap{/i}"

    mc "Gak rame-rame banget lah kalau cuma sepulugan orang, kukira bakal lebih banyak."

    mc "Sekarang masih…. jam 9.50 bentarlah, sambil nungguin pada dateng."

    mc "Hmmm jangan lupa bawa laptop..."

    mc "Ohhh iya lupa belum kumatiin dari tadi."

    "Teringat laptop yang belum kamu matikan sejak pagi tadi, kamu bergegas menuju kamar kosmu."

    scene bg kos morn with fade

    "Sesampainya di kamar, kamu mengganti pakaianmu juga tidak lupa mematikan laptop yang masih menyala."

    "Setelah memasukan laptop ke dalam tas, kamu bersiap-siap untuk berangkat menuju perpustakaan pusat."

    "Berdiri di dekat motormu, kamu berdiam melihat layar HPmu."

    "Setelah menelaah lokasi yang ada dalam gmaps di HPmu, kamu menyalakan motormu."

    mc normal jacket "Oh iyaa… lupa belum jadi isi bensin aku." 
    
    mc "apa nanti habis krsan ya? Kayaknya masih cukup kalau cuma ke perpustakaan."

    mc "Coba kucek aja dulu tangki bensinnya."

    "Clug clug"

    mc "Masih-masih, yaudah tinggal berangkat aja berarti."

    "Mengingat lokasi perpustakaan yang tidak terlalu jauh, kamu memutuskan untuk berangkat tanpa mengisi bensin motormu terlebih dahulu."

    "Brrrrr….."

    #SFX Engine
    $prologueCount +=1

    call screen mapUI with dissolve

label krs:

    scene bg perpustakaan with fade

    "Setelah melewati jalur yang sudah kamu tentukan sebelumnya dari gmaps." 
    
    "Kurang dari 10 menit perjalanan kamu sudah memarkirkan motormu di parkiran perpustakaan."

    "Selesai memarkir motor, kamu berjalan menuju pintu depan bangunan perpustakaan."
    
    "Terlihat kerumunan yang ada di depan gedung perpustakaan."
    
    "Sekitar 8 orang yang sedang duduk pada bangku umum yang ada di depan gedung."

    "Mereka sedang mengobrol dan tampak seperti sedang menunggu sesuatu."

    "Merasa bahwa kerumunan orang itu adalah teman kelasmu, kamu membuka HP lalu menekan notifikasi chat Lane yang muncul."

    show phone groupchat :
        xalign 0.5
        yalign 0.4
    with dissolve

    "{i}Udah sampai nih, aku di depan sama si X,Y,Z.{/i}"

    "{i}Ohh oke sebentar aku hampir sampai.{/i}"

    "{i}Bentar masih dijalan aku.{/i}"

    "{i}Nanti ditunggu di tempat duduk depan gedungnya yaa…{/i}"

    "{i}Okee…{/i}"

    "{i}Nihh si L udah dateng, yang belum yukk{/i}"

    hide phone groupchat

    mc normal jacket "{i}Ohh jadi memang itu mereka yang kumpul.{/i}"

    "Setelah memastikan kerumunan orang yang berada di depanmu merupakan teman kelasmu, kamu berjalan mendekati mereka."

    "Ketika sudah cukup dekat dengan mereka, saat ingin menyapa temanmu tiba-tiba ada seseorang yang berlari ke arah mereka dari dalam gedung perpustakaan."
    
    r normal2 "Eh ayoo, masuk sekarang aja temen-temen." 
    
    t "Gimana Riss? Ada tempat kosong kah di dalam?"

    r "Iyaa tapi di lantai atas, nanti masuk terus naik ke lantai 3 ya."

    t "Lantai 3 ya? Bagian mananya Ris?"

    r "Lantai 3 kosong sih, terserah mau bagian mananya."
    
    t "Ohh oke-oke"
    
    t "Yukk naik yukk"

    t "Pakai elevator yuk capek aku kalau naik tangga."

    t "Ngikut dahh"

    "Tidak lama kemudian hanya kamu dan Rissa yang masih ada di depan gedung perpustakaan."

    r "Oh kamu udah datang [name], udah lama datangnya?"

    "Menyadari adanya dirimu, Rissa berjalan mendekatimu."

    mc "Baru aja sampai aku." 
    
    mc "Enggak sekalian naik kita Ris?"

    r "Aku nunggu disini dulu, nunggu kalau ada yang datang lagi nanti. Takutnya dikira enggak jadi kalau udah enggak ada yang kelihatan disini."

    "Melirik sepintas ke arah jam digital pada HPmu."

    mc "Ohh.. iya baru jam 10.10 ternyata, pasti ada yang nelat juga sih ya hahaha"

    r "Ya biasanya gitu kan hahahaha."
    
    "Melihat Rissa yang berniat untuk masih menunggu di luar gedung perpustakaan, kamu memutuskan untuk:"

    menu:

        "Ikut menunggu bersama Rissa":
            $rissa_fond += 10

            mc "Kalau begitu aku juga ikut nunggu luar saja lah, sambil cari angin juga hehehe."

            r "Bener? Gapapa kok kalau mau masuk duluan [name]."

            mc "Iya mau lihat-lihat suasana di luar gedung seperti apa kok."

            r "Yaudah, tapi kalau mau masuk duluan, tinggal masuk aja oke?"

            mc "Siap, Oke-oke!"

            scene bg perpustakaan with fade

            "Setelah percakapan barusan, kalian berdua hanya terduduk diam di bangku umum depan gedung perpustakaan."

            "Selama beberapa menit, kalian berdua hanya melakukan aktivitas masing-masing."

            "Kamu hanya memandangi suasana di lingkungan sekitar gedung perpustakaan."

            "Sementara Rissa asik bermain dengan HP yang sedang ia pegang."

            "Merasa canggung, karena tidak ada percakapan yang terjadi. Dirimu mencoba membuka percakapan."

            mc normal jacket"Oh iya Ris, usernamemu di Lane itu yang Rossaine itu kan ya?"

            r normal2"Iya, nama panjangku itu, agak aneh ya? Hehe"

            mc "Engga sih, cuma bingung aja awalnya aku, ku kira tadinya orang lain."

            r "Ahhh… iya nama panjangku Clarissa Rossaine, dari dulu panggilanku Rossa, sekarang mau ganti panggilan saja hehehe."

            r "Makanya waktu kenalan kemarin aku nyebut namaku Rissa, begituuu..."

            mc "Rossa? Kayaknya ada yang pernah manggil kamu begitu di grup ya?"

            r "Iya, itu temen SMAku dulu, kebetulan masuk satu jurusan juga."

            mc "Hoo…"

            "Setelah itu, kalian mulai mengobrol mengenai hal-hal lain yang terpintas di pikiran kalian."

            "Selama 10 menit kamu berbincang dengan Rissa, tidak ada satupun temanmu yang lain yang datang ke gedung perpustakaan."

            "Kalian berdua kemudian memutuskan untuk masuk ke dalam gedung perpustakaan." 
            
            "Naik ke tempat teman-temanmu yang lain yang sudah terlebih dahulu memasuki gedung perpustakaan."
            
            "Sesampainya di lantai 3, kalian berdua melihat teman-teman kelasmu sudah menempati bagian kiri gedung."
            
            "Karena melihat kebanyakan meja sudah ditempati oleh teman-temanmu, kamu dan Rissa menempati meja kosong yang berada paling dekat dengan jendela."

            scene bg black with dissolve
        

        "Masuk ke gedung perpustakaan lebih dulu":

            mc "Kalau begitu aku naik duluan ya Riss."

            r "Okeyy bilangin ke temen-temen yang lain aku masih nunggu yang belum dateng di bawah ya.."

            mc "Siap, nanti ku bilangin ke temen-temen."

            "Kemudian kamu berjalan masuk ke dalam gedung perpustakaan. Memasuki gedung, kamu melihat banyak mahasiswa lain yang sedang berada di dalam."

            "Kamu menengok ke atas dan melihat gedung perpustakaan dimana sekarang kamu sedang berada memiliki, sekitar 5 lantai atau lebih."

            "Terdapat tangga melingkar menuju lantai berikutnya." 
            
            "Sepasang elevator juga ditempatkan untuk dapat digunakan untuk naik ke lantai atas."

            "Kamu memutuskan untuk:"

            menu:

                "Naik menggunakan elevator":

                    mc "Pakai elevator sajalah, bakal capek ke lantai 3 kalau naik tangga."

                    "Znnnnnnn"

                    "Setelah pintu elevator terbuka kamu segera masuk kedalamnya."

                    "Di dalam kamu menekan tombol untuk naik ke lantai 3."

                    scene bg black with dissolve

                    #SFX elevator

                    pause 3.0


                "Naik melewati tangga":

                    mc "Mungkin lewat tangga saja kali ya?"

                    mc "Sudah lama enggak olahraga, itung-itung olahraga ringan hehehe."

                    "Memutuskan untuk naik melewati tangga, kamu mulai mengangkat kakimu menaikai anak tangga yang ada."

                    "Huhhh Huhhh Huhhh"

                    "Kamu berjalan menaiki anak tangga menuju ke lantai 3."

                    $vit += 15

                    $energy -= 10

                    call stat_change

                    "Stas UP!!!"

                    scene bg black with dissolve

                    pause 2.0

            scene bg perpustakaan with fade
                
            "Sesampainya di lantai 3, terlihat teman-temanmu sudah duduk berkelompok menempati meja-meja yang ada." 
            
            "Hanya tersisa satu meja kosong yang berada paling dekat dengan jendela."

            "Tanpa pikir panjang kamu duduk dan membuka HPmu untuk menghabiskan waktu sampai Rissa dan temanmu yang lain menyusul."

            "........."

            "......"

            "..."

            "Sekitar 10 menit berlalu sejak kamu memainkan HPmu, Rissa akhirnya datang."

            "Tidak ada satu orang pun yang datang bersama Rissa, berarti tidak ada temanmu yang lain yang datang ke perpustakaan. Kecuali mereka yang sudah datang sebelum dirimu."

            "Melihat meja lain sudah digunakan oleh teman-temanmu lain, Rissa berjalan mendekatimu."

            r normal2"Aku duduk sini yaa, kosong kan?"

            mc normal jacket "Iya kosong kok."

            "Rissa duduk disebelahmu dan langsung mengeluarkan laptopnya."

    scene bg perpustakaan with fade

    "Setelah semuanya siap untuk melakukan pengisian KRS, Rissa memimpin semua orang dalam pengisian KRS dengan memberikan arahan."

    r normal2 "Teman-teman cara buka sampai ke halaman pengisian KRS sudah pada tahu kan ya?"

    "Rissa menanyakan kepada teman kelasmu yang sudah siap dengan laptop mereka masing-masing."

    t "Sudahh"

    t "Lewat simaster itu kan?"

    t "Eh ajarin aku dong."

    r "Mungkin aku kirim arahannya di chat grup Lane aja ya?"

    t "Boleh-boleh"

    t "Iya biar sekalian yang enggak datang kesini juga tahu."

    r "Oke kalau gitu, aku buat chatnya dulu, kalau kalian mau coba-coba dulu gapapa."

    t "Okee"

    t "Aku nunggu yang lain aja lah"

    "Melihat temanmu yang lain mulai mencoba melakukan pengisian KRS, kamu ikut mengeluarkan laptop dari dalam tas."

    mc normal jacket"Kamu udah coba-coba kah Riss?"

    r "Ohh, belum aku, ya cuma lihat-lihat aja belum sampai milih. Kamu gimana udah nyoba?"

    mc "Sama juga, cuma sampai yang milih periode pengisian krs itu."

    r "Coba kamu cobain sekarang, sekalian aku ketik di group chat arahan ke temen-temen, aku sedikit lupa."

    mc "Oh oke-oke…"

    "Rissa memintamu untuk mempraktikkan cara mengakses sampai halaman pengisian KRS. "
    
    "Setelah laptopmu selesai dari keadaan Booting, kamu membuka browser kemudian kamu mencoba mempraktikkannya:"

    r "Langkah pertama:"

    menu:
        "Buka web Simaster":

            mc "Buka web simaster."

            r "Yup, buka website simaster."

    r "Kemudian isikan:"

    menu:
        "Pilih Sign In kemudian isikan ID dan Password":

            mc "Sign In terus isikan data diri kita, terus nanti isi captcha yang muncul."

            r "Iya, langkah kedua pilih Sign In lalu isi data diri, ID, password, dan nanti isi captcha yang muncul."

        "Pilih Registrasi akun":

            r "Bukan, kita kan sudah punya akunnya. "

            mc "Oh iya, lupa aku."

            r "Langkah kedua pilih Sign In lalu isi data diri, ID, password, dan nanti isi captcha yang muncul."

    show home simaster:
        xalign 0.5
        yalign 0.4
    
    with dissolve
    
    r "Setelah itu kita akan masuk ke halaman beranda akun Simaster kita."

    r "Lalu dari halaman beranda simaster, kita memilih menu:"

    menu:
        "Pilih menu Akademik Kemahasiswaan":

            mc "Pilih menu Akademik Kemahasiswaan di kiri atas layar."
            
            r "Benar, pilih menu Akademik Kemahasiswaan."

        "Pilih menu adminstrasi":

            mc "Pilih menu administrasi?"

            r "bukan, ingat-ingat lagi coba [name]"

            mc "Menu Akademik Kemahasiswaan kan?"

            r "Iyupss"

    hide home simaster

    show home akademik:
        xalign 0.5
        yalign 0.4
    
    with dissolve

    r "Setelah memilih menu Akademik Kemahasiswaan, akan muncul banyak pilihan sub menu."

    r "Disitu kemudian kita memilih:"

    menu: 
        
        "Pilih sub menu Akademik lalu Pengisian KRS":
            
            mc "Lalu pilih Akademik terus menu Pengisian KRS kan?"

            r "Bener-bener, pilih sub menu Akademik lalu pilih Pengisian KRS."

        "Pilih sub menu Akademik lalu Bimbingan DPA":

            mc "Menu Akademik terus Bimbingan DPA? "

            r "Bukan dong, itu kan buat bimbingan sama DPA kita."

            r "Kamu ngelawak ya hahahaha, pilih Pengisian KRS dong."

    hide home akademik

    show home akademik krs:
        xalign 0.5
        yalign 0.4
    
    with dissolve

    r "Kemudian, setelah sampai halaman Pengisian KRS apa yang kita lakukan?"

    menu: 

        "Pilih aksi pada periode pengisian KRS yang ada":

            mc "Pilih aksi pada periode pengisian KRS ini kan?"

            r "Yups, pilih periode pengisian KRS yang terbuka."

    hide home akademik krs

    show pengisian krs:
        xalign 0.5
        yalign 0.4
    
    with dissolve

    r "Setelah memilih aksi pada periode pengisian KRS yang terbuka, kita akan dapat memilih mata kuliah yang ditawarkan."

    r "Mata kuliah apa saja yang seharusnya kita pilih?"

    menu:

        "Memilih mata kuliah sesuai kode mata kuliah yang dibagikan":

            hide pengisian krs

            mc "Memilih mata kuliah sesuai kode mata kuliah yang ada."

            r "Iya, kita memilih mata kuliah sesuai dengan mata kuliah yang kodenya dibagikan oleh Pak Andy."

            mc "Kamu ada listnya kan Rissa? Coba sini aku lihat, aku coba pilih mata kuliahnya."

            r "Ada-ada, sebentar aku ambilin di tasku."

            "Rissa mengambil buku note dari dalam tas yang ia bawa."

            "Setelah membuka dimana catatan itu berada, kemudian Rissa menaruh buku note tersebut di sampingmu."

            "Kamu dapat melihat catatan Kode Mata Kuliah, Nama Mata Kuliah, dan Kelas pada buku note tersebut."

            window hide

            call screen kode_matkul
            show screen kod_matkul_btn

            # pause

            "Untuk dapat melihat kode mata kuliahnya lagi, kamu dapat memilih tombol 'KODE' yang ada di samping kanan layar."

            "Setelah melihat kode mata kuliah yang ada pada catatan Rissa, kamu mencoba memilih mata kuliah sesuai kode mata kuliah yang ada."

            call screen isi_krs

            # screen KRS

    scene bg black with fade

    mc normal jacket"Sudah semua kan ini? Apa aku masih ada yang kurang?"

    r normal2"Coba kamu hitung, apakah benar sudah ada 8 mata kuliah?"

    mc "Sebentar-sebentar aku teliti lagi..."

    "Kamu menghitung dan mencocokkan mata kuliah yang kamu pilih, apakah sudah benar atau tidak."

    mc "Sudah 8 nih Riss."

    r "Coba kulihat dulu."

    "Rissa berdiri dan meneliti apa yang kamu pilih."

    r "Harusnya sih sudah, sudah 24 SKS juga itu tulisannya."

    mc "Oke-oke kalau gitu."

    mc "Ini emang enggak ada tombol simpannya ya kalau sudah selesai?"

    r "Hmm emang enggak ada ya? Coba aku tanya ke Pak Andy dulu."

    t "Iyaa coba tanyain ke Pak Andy buat mastiinnya"

    r "Oke, oke tunggu bentar ya.."

    "Kemudian semua menunggu jawaban dari Pak Andy mengenai penyimpanan pengisian KRS."

    "Tak berselang lama, Rissa mendapatkan balasan dari Pak Andy."

    r "Eh ini Pak Andy sudah bales chatnya, ku foward ke grup chat Lane aja ya."

    "Tuingg"

    "Kamu membuka notifikasi yang ada di HPmu"

    "{i}Jadi kalau sudah memilih mata kulaih dan sudah memilih captcha itu sudah otomatis kesimpan.{/i}"

    "{i}Kalau mau dibatalin, pilih opsi batal di pilihannya.{/i}"

    "{i}Kalau tidak ada pilihan kelas karena kelas penuh bisa bilang ke bagian akademik, nanti akan ditambah kelas baru.{/i}"

    "{i}Kalau sudah memilih memilih semua, nanti tinggal tunggu DPA menyetujui saja.{/i}"

    r "Jadi begitu temen-temen, kalau sudah semua ngisi KRSnya nanti kubilangin ke Pak Andy lagi, kalau ada yang kesusahan tanya aja ya, selagi masih pada disini."

    "Rissa berbicara ke seluruh teman sekelas yang sedang mengisi KRS"

    mc "Ini sudah begini aja kan Riss?"

    r "Iya, begitu aja tinggal nunggu disetujuin saja sama DPA punyamu KRSnya."

    mc "Oke, kalau begitu kalau sekarang kamu mau gantian ngisi KRSnya nanti aku bantu milih mata kuliahnya."

    r "Okeee, makasih yaa."

    "Setelah kamu selesai dengan Pengisian KRS, kamu meminjamkan laptopmu kepada Rissa."

    "Kini giliran dirimu membantu Rissa untuk mengisi KRSnya."

    scene bg perpustakaan with fade

    "Tidak banyak masalah selama proses pengisian KRS." 
    
    "Pada akhirnya kelas untuk suatu mata kuliah rata-rata terbagi menjadi 2 kelas." 
    
    "Tidak ada atau setidaknya belum ada teman sekelasmu yang tidak mendapatkan kelas pada suatu mata kuliah."

    "Setelah selesai dengan pengisian KRSnya, Rissa membantu teman-teman sekelas lainnya untuk mengisi KRS mereka. "

    "Beberapa jam sudah berlalu, semua orang sudah menyelesaikan pengisian KRS." 
    
    "Selesai mengisi KRS, semua orang berbincang dan mengakrabkan diri lebih lanjut satu sama lain." 
    
    "Kamu ikut menghabiskan waktu bersama teman barumu."

    t "Wah sudah jam 2 aja, perasaan tadi kita selesai ngisi jam 12an."

    t "Iya juga ya cepet banget rasanya."

    t "Udah jam segini ya, waktunya pulang nih keburu hujan."

    t "Kok bisa hujan ? Sekarang lagi cerah sama panas banget begini."

    t "Katanya kalau cerah begini nanti jadi hujan deras ya?"

    t "Iyasih biasanya begitu."

    t "Yaudah pulang yuk, gak bawa jas hujan aku."

    t "Aku bonceng kamu ya!."

    "Selesai mengobrol dengan teman sekelas, Rissa berjalan kembali ke arahmu."

    r normal2"Begitu katanya, kamu langsung pulang juga [name]?"

    "Menyambung obrolan teman-teman mengenai hujan, Rissa menanyakannya kepadamu."

    mc normal jacket"Kalau begitu sih mending pulang langsung aku."

    r "Hmmm, kalau begitu aku juga langsung pulang juga."

    r "Yaudah aku tutup dulu kali ya?"

    "Rissa kembali berdiri, meminta perhatian kemudian mulai berbicara."

    r "Oke temen-temen, makasih ya sudah dateng kesini, sudah kumpul sama KRSan bareng. Berhubung sudah semakin siang, kalau mau pulang dipersilahkan. Hati-hati di jalan jangan lupa!"

    "Setelah itu satu-persatu temanmu mengemas barang-barang yang mereka bawa."

    "Kamu juga ikut mengemas barang bawaanmu."
    
    scene bg perpustakaan with fade

    r normal2 "Kalau begitu aku duluan ya [name], sampai ketemu esok di kelas!"

    mc normal jacket "Okee, hati-hati."

    r "Byee."

    mc "Byee"

    "Setelah Rissa meninggalkanmu, kini hanya ada dirimu yang masih tersisa di lantai 3 gedung perpustakaan."

    "Tidak lama kemudian dirimu juga bergegas keluar."

    "Sampai di luar gedung perpustakaan kamu merasakan perbedaan suhu yang sangat jelas."
    
    "Di dalam gedung terdapat air conditioner sehingga  udara terasa sejuk, sementara setelah berada di luar kamu merasakan sengatan panas matahari."

    mc "Gila, bisa beda banget begini rasanya di dalam sama di luar gedung."

    "Suasana di luar gedung terlihat cerah, dan tidak ada satupun awan yang menutupi matahari."

    mc "Tapi kata temen-temen tadi nanti bakal hujan deras kah? Tapi masak iya, langit cerah-cerah begini."

    mc "Hujan atau enggak, mending pulang ajalah panas begini."

    mc "Oh iya, beli bensin sekalian makan apa ya?"

    mc "Gampanglah nanti di jalan."

    "Menyalakan motor yang ada di parkiran, kamu melanjutkan perjalananmu selanjutnya."

    jump kos_krs

    return
