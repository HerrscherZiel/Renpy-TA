#prologue fist mart
label minimart_pertama:

    $ firstMart = False

    scene bg minimart_out
    with fade

    pause 2.0

    show screen days_screen with dissolve
    
    show r normal2 at right
    with dissolve

    r   "[name] ! Itu minimartnya ada di seberang jalan."

    "Tidak ada 5 menit setelah berjalan dari kampus, terlihat sebuah bangunan bertingkat di seberang jalan."

    "Rissa kembali melambai-lambaikan tangannya kepadamu, menyuruhmu untuk mendekat selagi menunggu jalanan sepi."

    show mc normal jacket:
        xalign 0.2 yalign -0.3

    mc "Dekat juga ya ternyata."

    r   "Iya sudah kubilangkan, minimartnya tidak jauh dari kampus."

    r   "Aku ingin beli alat tulis untuk besok, apa yang ingin kamu beli [name]?"

    mc  "Cuma makanan dan minuman untuk nanti malam."

    r   "Camilan malam kayaknya enak juga ya, jadi pengin."

    r   "Sebelum masuk, kita harus menitipkan barang kita dulu ke tempat penitipan disana."

    "Setelah menunjuk ke arah tempat penitipan barang, Rissa berjalan kearah tempat penitipan."

    "Kamu mengikuti Rissa untuk ikut menitipkan barangmu."

    "Setelah selesai menitipkan barang bawaan, dan mendapatkan nomor pengambilan kamu dan Rissa memasuki minimart."

    scene bg black
    with dissolve

    scene bg minimart_in
    with dissolve

    "Setelah berada di dalam minimart, kamu melihat berbagai barang yang terpampang di sektor masing-masing."

    show mc normal jacket:
        xalign 0.2 yalign -0.5

    mc  "Woww, ternyata di dalam sangat luas yaa.."

    show r normal2 at right
    with dissolve
    
    r   "Iya, meskipun luas seperti ini, jika sedang ramai tetap saja penuh."

    mc  "Apakah di sini biasanya sering ramai?"

    r   "Hahaha, kamu perlu merasakannya sendiri ketika sudah memasuki waktu kuliah normal."

    mc "hmmmm...."

    r   "Oh ya, kalau begitu aku ke lantai 2 dulu ya, temanku sudah menunggu di sana."

    mc  "Oh sudah janjian sama teman, makasih sudah mengantarku kesini ya..."

    r   "Sama-sama, sampai ketemu besok [name], bye!"

    mc  "Sampai ketemu!"

    ".................."

    ".........."

    "......"

    hide r normal2 with dissolve

    "Setelah melihat Rissa pergi, kamu berjalan ke sektor makanan dan minuman."

    "Game ini memiliki fitur {b}stats{/b}, terdapat tiga stat utama yaitu {b}Kesehatan{/b}, {b}Akademik{/b}, dan {b}Social{/b}."

    "Stats yang ada akan {b}dipengaruhi oleh pilihan kegiatan{/b} yang dipilih." 
    
    "Semisal {b}makan{/b} akan memengaruhi stat {b}kesehatan{/b}."

    "Menghadiri {b}kelas{/b} akan memengaruhi stat {b}akademik{/b}."

    "Menghadiri {b}acara organisasi{/b} akan memengaruhi stat {b}sosial{/b}."

    "Buatlah stats yang ada menjadi sebaik mungkin, karena {b}kondisi terakhir stats{/b} yang ada pada hari ke 30 akan {b}menentukan ending{/b} yang di dapatkan pada game ini."

    "Stats {b}kesehatan{/b} dapat dilihat pada bagian {b}kanan atas layar{/b}, sementara untuk stats Akademik dan Social, dapat dilihat dengan cara membuka {b}menu stats{/b} dengan {b}tombol all stats{/b} yang ada di bagian kanan atas layar."

    "Stats yang berubah akan terlihat ketika kamu berganti fase waktu."

    window hide

    call screen tutorial_stats1 with dissolve

    mc  "Beli apa ya? Roti atau Minum hmmm…."

    show screen stats_screen with dissolve


    "Kamu memutuskan untuk:"

    menu:
        "Beli Roti":

            mc  "Beli roti saja lah, lumayan ganjel lapar."

            "Kamu membeli Roti."
    
    "Setelah mengambil apa yang ingin kamu beli, kamu membawanya ke arah kasir."

    "Terdapat banyak nomor kasir, namun tidak ada satupun yang kosong."

    "Ada beberapa orang yang sudah mengantri untuk melakukan pembayaran."

    "Beberapa mahasiswa baru yang masih mengenakan atribut orientasi juga terlihat dalam barisan."

    "Salah satunya ada seorang laki-laki kurus dengan postur badan tinggi yang sempat kamu lihat ketika kegiatan orientasi."

    mc  "{i}Hmmm ternyata banyak juga ya mahasiswa yang berbelanja disini{/i}"

    mc  "{i}Ya meskipun wajar sih, karena lokasinya dekat dengan kampus{/i}"

    "Beberapa menit mengantri akhirnya tiba giliranmu untuk melakukan pembayaran."

    show screen get_bread with dissolve

    "..............."

    "........"

    "..."

    "Seusai membayar roti yang kamu pilih, ketika keluar dari minimart terlihat matahari sudah hampir terbenam, dan hari sudah menjadi gelap."

    "Kamu langsung mengambil tas yang dititipkan pada penitipan barang yang ada diluar minimart dan langsung berjalan kearah gedung kampus."

    scene bg minimart_out with fade

    pause 1.0

    scene bg streets with fade

    "Melewati jalan yang sama seperti yang kamu lalui bersama dengan Rissa, kamu sudah berada di lingkungan area gedung kampusmu."

    "Kamu bergegas berjalan menuju parkiran motor yang ada di kampus."
    
    "Selagi berjalan menuju parkiran kampus, kamu berpikiran untuk memakan roti yang baru saja kamu beli."

    call screen tutorial_statschange1 with dissolve
    
    "Kemudian kamu memutuskan untuk:"

    menu:

        "Mengkonsumsi roti yang kamu beli.":

            show mc normal jacket:
                xalign 0.2 yalign -0.5
            
            mc  "Langsung kumakan sekarang saja lah, sudah agak lapar juga."
        
            "Kamu duduk di kursi umum yang berada di pinggir jalan untuk menikmati roti yang dibeli di minimart sebelumnya."

            "Kamu memakan roti yang kamu beli!"
            "Stats berubah!"

            call eat
            

        "Menyimpannya untuk besok pagi.":

            $ rotiAwal = True

            show mc normal jacket:
                xalign 0.2 yalign -0.5
            mc  "Buat besok sajalah makannya, nanti keburu petang."
    
    "Kemudian kamu bergegas ke arah parkiran motor kampus dan segera mengendarai motormu untuk pulang."

    "Pilih {b}Ikon Kos{/b} untuk pulang ke kosanmu."

    # hide screen days_screen
    # hide screen stats_screen
    $ prologueCount +=1
    window hide
    call screen mapUI with dissolve

    return
#prologue 3rd day noon
label mini3N:

    scene bg minimart_in with dissolve
    pause 2.0

    mc normal jacket "Hahhh… bisa segar begini di dalem, diluar panasnya gak masuk akal gilaaa."

    "Kamu baru saja memasuki minimarket, dan merasakan perbedaan suhu yang signifikan."

    "Di dalam kamu merasakan suhu yang berbanding terbalik 180 derajat. Matahari bersinar terik tanpa ada satupun awan yang menghalangi sinarnya."

    "Sementara di dalam minimart kamu merasakan kesejukan ruangan ber AC."

    "Karena panasanya suhu diluar ruangan, tubuhmu berada dalam kondisi yang berkeringat."

    "Oleh karena itu, hal yang pertama kali kamu lakukan di dalam minimart adalah mencari tempat untuk mendinginkan tubuh dan beristirahat."

    "Tidak perlu jauh-jauh berjalan, kamu menenemukan beberapa tempat duduk umum yang berada di sektor foodcourt di area minimart."

    "Meskipun disebut dengan mini-mart, ketika masuk ke dalam bangunannya akan terasa seperti mini-mall."

    "Di dalam minimart terbagi menjadi sektor pembelanjaan. Sektor-sektor yang berbeda itu terletak di lantai yang berbeda."

    "Terdapat sektor pembelanjaan, baik kebutuhan harian, food court, maupun kebutuhan lain."

    scene bg foodcourt with fade 

    "Mendapatkan tempat duduk kosong di dekat food court di dalam minimart, pandanganmu tertuju ke berbagai penjuru ruangan mengamati apa yang ada didalamnya."

    "Suasana minimart saat ini sedang tidak dipenuhi oleh pengunjung. Terdapat beberapa pengunjung yang keluar masuk ke dalam minimart."

    "Setelah duduk mendingkan tubuh selama beberapa menit, kamu berjalan mendekati stand minuman yang ada di depanmu tertarik dengan minuman yang ada."

    "Berada di depan stand minuman tersebut kamu tidak menemui satu orang pun yang berada di dalam stand."

    mc normal jacket"Hmm lagi isoma mungkin kali ya?"

    "Kamu mendekati papan menu yang ada di bagian samping stand untuk melihat minuman yang dijual."

    mc "Teh tarik.. Kopi… Es degan… hmm mending beli apa ya?"

    siapa "Ada yang bisa dibantu kak?"

    "Mendengar suara dari belakangmu, kamu menoleh ke arah suara tersebut."

    mc "Oh... ah ini kak, mau pesan minum."

    "Asal dari suara tersebut ternyata merupakan suara dari penjaga stand minuman yang ada di depanmu."

    stall "Mau pesan apa kak? Disini ada macam-macam variasi minuman teh, kopi, es buah dan es degan."

    stall "Oh iya kak, kebetulan lagi ada promo, untuk setiap pembelian satu variasi kopi akan mendapatkan 1 kopi free kak."

    mc "Boleh itu, pesen kopinya satu berarti."

    stall "Tapi ada syaratnya kak, harus follow PhoGram nya duluu.. setelah buat story dan tag akun PhoGram kami kak."

    mc "Oh begitu, EG nya yang ada disini ya kan kak?"

    stall "Iya itu kak, Oh iya ini kopinya es atau hangat ya?"

    mc "Es kak dua dua nya ya kak."

    mc "Oh iya, ini udah ku follow ya."

    stall "Oke siap! Mohon ditunggu sebentar ya kak."

    mc "Okee."

    stall "Tadi sudah menunggu lama ya kak?"

    mc "Oh belum kok, baru aja datang tadi."

    stall "Oh maaf ya tadi baru saja istirahat saya."

    mc "Oh enggak apa kok."

    mc "Ngomong-ngomong ini memang lagi musimnya panas kaya begini, atau memang begini kalau disini ya kak?"

    stall "Ya lagi musimnya kalau sekarang, biasanya siang panas-panas begini nanti sore atau malemnya bakalan hujan."

    mc "Oh begitu yaa..."

    stall "Kuliah di situ juga ya kak?"

    "Penjaga stand minuman tersebut menunjuk ke arah gedung kampusmu yang berada di dekat lokasi minimart."

    mc "Iya, baru masuk tahun ini aku."

    stall "Wah mahasiswa baru dong, jurusan apa kak?"

    mc "Program Studi D4 Teknologi Rekayasa Perangkat Lunak."

    stall "Itu mempelajari apa kak jurusannya?"

    mc "Macem-macem sih kak, teknologi begitu, ya gampangnya komputer begitu kak."

    stall "Ohhh kaya Ilmu Komputer begitu ya... Sering-sering mampir sini kak, dekat kan kampusnya."

    mc "Hahaha siap."

    "Beberapa menit kemudian, setelah lama berbincang dengan penjaga stand minuman kamu menerima pesananmu."
    
    mc "Ini ya kak Uangnya."

    stall "Oke, terimakasih kak."

    "Setelah itu kamu kembali ke tempat duduk semula."

    "Sampai di tempat duduk, kamu langsung mengeluarkan HPmu, dan membuka salah satu permainan yang ada di dalamnya."

    "Mengamati sekelilingmu kamu melihat beberapa orang sedang menikmati jam istirahat siang mereka."

    "Terdapat berbagai macam pengunjung yang sedang beristirahat di sektor foodcourt minimart."

    "Pekerja kantoran, anak kuliahan, bahkan anak SMA terlihat asyik menikmati waktu mereka." 
    
    "Memakan makan siang, berbincang dengan teman, dan tentu saja terdapat orang yang membuka laptop untuk melanjutkan pekerjaan mereka di sela-sela waktu."

    "Sambil menyeruput es kopi yang kamu beli dari stall minuman, kamu fokus kembali pada layar HPmu yang sedang membuka permainan."

    "Henshin tertulis pada loading screen layar HPmu."

    "Begitu layar pada HPmu sudah berganti dari layar loading screen, kamu langsung berfokus memainkan game yang ada."

    mc "Siang-siang begini selesain daily quest lumayan lah."

    scene bg foodcourt with fade

    "Seru dalam duniamu sendiri, tak sadar satu cup kopi yang kamu beli sudah habis."

    call drink

    "Indikator baterai dari HPmu juga sudah berubah menjadi warna merah. Kamu menutup permainan dan memasukan HPmu ke dalam saku."

    mc normal jacket "Niatnya cuma mau beli minum sebentar malah jadi nongkrong lama begini huhhhhh."
    
    "Kamu menyesal menghabiskan waktumu terlalu lama di minimart. Sekarang jam sudah menunjukan pukul 4 Sore, dan dirimu hanya menghabiskan waktu siangmu berada di minimart."
    
    "Langit sudah mulai berubah warna. Kamu memutuskan untuk kembali ke kosan."

    mc "Kopinya enak juga, besok kalau kesini lagi aku beli lah."

    "Membawa satu bungkus kopi yang kamu dapat dari promo, kamu keluar dari minimart dan mengendarai motor ke kos."

    $prologueCount+=1

    jump kos_krs3

    return
#mart normal scenario picker
label mart_scene_pick:

    # return a random integer between 1 and 20
    $ d3roll = renpy.random.randint(1, 3)

    if d3roll == 1:
        if timephase == 1:
            jump mart_mornS1
        elif timephase == 2:
            jump mart_dayS1
        else:
            jump mart_nightS1
    elif d3roll == 2:
        if timephase == 1:
            jump mart_mornS2
        elif timephase == 2:
            jump mart_dayS2
        else:
            jump mart_nightS2
    else:
            if timephase == 1:
                jump mart_mornS3
            elif timephase == 2:
                jump mart_dayS3
            else:
                jump mart_nightS3

label choice_mart_noon:

    show screen trans_screen with dissolve
    scene bg minimart_out with dissolve
    pause 2.0

    "Siang harinya, kamu memilih menggunakan waktumu untuk pergi ke minimart."

    "Ada beberapa hal yang dapat kamu lakukan di minimart pada siang hari, kamu memilih untuk:"

    menu:
        "Pergi ke foodcourt":
            jump mart_noonS1
        
        "Belanja keperluan sehari-hari":
            jump mart_noonS2

label choice_mart_night:

    show screen trans_screen with dissolve
    scene bg minimart_out with dissolve
    pause 2.0

    "Malam harinya, kamu memilih untuk pergi ke minimart."

    "Ada beberapa hal yang dapat kamu lakukan di minimart pada malam hari, kamu memilih untuk:"

    if day == 12:
        jump belajar_1
    elif day ==13:
        jump belajar_2
    elif day == 14:
        jump belajar_3

    menu:
        "Membeli snack untuk camilan":
            jump mart_nightS1
        
        "Berkumpul bersama teman":
            jump mart_nightS2

#noon
label mart_noonS1:

    scene bg minimart_out with dissolve

    pause 2.0

    "Pada siang hari, kamu pergi menuju minimarket dimana biasanya kamu berbelanja."

    "Siang hari ini, matahari bersinar terik membuat suhu di luar ruangan menjadi sangat panas."

    "Sesampainya di minimarket, kamu bersegera masuk ke dalam bangunan."

    mc normal jacket "Hahhh… bisa segar begini di dalem, diluar panasnya gak masuk akal gilaaa."

    "Di dalam kamu merasakan suhu yang berbanding terbalik 180 derajat. Matahari bersinar terik tanpa ada satupun awan yang menghalangi sinarnya."

    "Sementara di dalam minimart kamu merasakan kesejukan ruangan ber AC."

    "Karena panasanya suhu diluar ruangan, tubuhmu berada dalam kondisi yang berkeringat."

    "Oleh karena itu, hal yang pertama kali kamu lakukan di dalam minimart adalah mencari tempat untuk mendinginkan tubuh dan beristirahat."

    "Tidak perlu jauh-jauh berjalan, kamu menenemukan beberapa tempat duduk umum yang berada di sektor foodcourt di dalam minimart."

    scene bg foodcourt with fade

    "Kamu duduk di dekat bagian food court di dalam minimart, pandanganmu tertuju ke berbagai penjuru ruangan mengamati apa yang ada didalamnya."

    "Suasana minimart saat ini sedang tidak dipenuhi oleh pengunjung. Terdapat beberapa pengunjung yang keluar masuk ke dalam minimart."

    "Setelah duduk dan mendingkan tubuh selama beberapa menit, kamu berjalan mendekati stand minuman yang ada di depanmu untuk membeli minum."

    "Sesampainya di stand minuman, kamu memesan minuman dingin untuk menyegarkan tubuhmu."

    "Sembari menunggu, kamu menghabiskan waktu dengan berbincang dengan penjaga stand minuman."

    "Tidak lama kemudian pesananmu selesai dibuat."

    stall "Ini kak pesanannya."

    "Kamu membayar pesananmu dan menerimanya."

    mc normal jacket "Terimakasih."

    stall "Sama-sama kak, jangan lupa mampir lagi."

    "Menganggukkan kepala, kamu berjalan kembali ke tempat dudukmu sebelumnya."

    "Sampai di tempat duduk, kamu langsung mengeluarkan HP dan membuka salah satu permainan yang ada di dalamnya."

    "Dengan layar HP yang sedang menunjukan tampilan {i}loading{/i} kamu mengalihkan pandanganmu dari layar HP menuju lingkungan sekitarmu."
    
    "Mengamati sekelilingmu kamu melihat beberapa orang sedang menikmati jam istirahat siang mereka."

    "Terdapat berbagai macam pengunjung yang sedang beristirahat di sektor foodcourt minimart."

    "Pekerja kantoran, anak kuliahan, bahkan anak SMA terlihat asyik menikmati waktu mereka." 
    
    "Memakan makan siang, berbincang dengan teman, dan tentu saja terdapat orang yang membuka laptop untuk melanjutkan pekerjaan mereka di sela-sela waktu."

    "Sambil menyeruput minuman dingin yang kamu beli dari stand minuman, kamu mengarahkan kembali perhatianmu pada layar Hpmu."

    "Begitu layar pada HPmu sudah berganti dari layar {i}loading{/i} screen, kamu langsung berfokus memainkan game yang ada."

    mc "Siang-siang begini selesain daily quest lumayan lah."

    scene bg foodcourt with fade

    call drink

    "Seru dalam duniamu sendiri, tak sadar satu cup kopi yang kamu beli sudah habis."

    "Indikator baterai dari HPmu juga sudah berubah menjadi warna merah. Kamu menutup permainan dan memasukan HPmu ke dalam saku."

    mc normal jacket "Niat mau beli minum sebentar malah jadi nongkrong lama begini huhhhhh."
    
    "Kamu menyesal menghabiskan waktumu terlalu lama di minimart. Sekarang jam sudah menunjukan pukul 4 Sore, dan dirimu hanya menghabiskan waktu siangmu berada di minimart."
    
    "Langit sudah mulai berubah warna. Kamu memutuskan untuk kembali ke kosan."

    mc "Kopinya enak juga, besok kalau kesini lagi aku beli lah."

    "Membawa satu bungkus kopi yang kamu dapat dari promo, kamu keluar dari minimart dan mengendarai motor ke kos."

    window hide

    if day == 4:

        jump kos_krs4_night

    else:
        pass

    call change_timephase
    call screen mapUI with dissolve

label mart_noonS2:

    "Teringat ada beberapa barang yang perlu kamu beli, kamu "

    call change_timephase
    call screen mapUI with dissolve

#night
label mart_nightS1:

    "Membeli camilan"

    call small_eat

    jump sleep

label mart_nightS2:

    "Membaca pesan dari group Lane, kamu ikut bergabung bersama teman sekelasmu di minimart"

    jump sleep
  
#belajarUTS

label belajar_1:

    scene bg foodcourt with dissolve

    "Malam harinya kamu memutuskan untuk mengikuti kegiatan belajar bersama dengan teman sekelasmu untuk mempersiapkan UTS esok hari."

    "Kamu membawa buku catatanmu menuju ke foodcourt yang ada di minimart."

    "Sesampainya di minimart kamu melihat beberapa kerumpulan orang sedang membuka laptop maupun buku."

    "Kamu mengamati untuk beberapa waktu untuk memastikan kamu tidak mendatangi kerumpulan yang salah, 
    sampai akhirnya kamu melihat [r] pada salah satu kerumpulan yang ada."

    r normal2 "Oh hai [name] kamu datang ya..."

    mc normal jacket "Udah pada dateng tadi ya?"

    r "Udah sih nggak tadi-tadi banget tapi."

    mc "Udah mulai?"

    r "Baru tuker-tukeran catatan aja sih."

    mc "Ohhh okey-okey."

    "Disekitar kamu melihat teman sekelasmu yang sudah datang, sudah memesan makanan dan minuman dari foodcourt sebagai teman belajar."

    mc "Aku pesan dulu aja dah, bentar ya [r]."

    r "Santai ini kita nggak buru-buru juga kok."

    "Kemudian kamu berjalan menuju salah satu stand dan memesan menu yang ada."

    scene bg black with dissolve
    pause 1.0

    scene bg foodcourt with dissolve

    "Setelah beberapa menit menunggu pesananmu telah siap, selesai membayar kamu kembali ke kerumpulan teman sekelasmu membawa apa yang kamu pesan."

    "Ketika kembali, [r] sedang mulai menjelaskan mengenai mata kuliah 'Pengantar Teknologi Informasi' yang akan menjadi mata kuliah pertama pada jadwal UTS besok."

    r normal2 "Jadi langsung kujelaskan ya kisi-kisinya."

    call belajar_pti_1

    r "Kemudian pada pertemuan kedua PTI yang dipelajari adalah:"

    call belajar_pti_2

    r normal2 "Kurang lebih itu yang pernah kita pelajari pada mata kuliah pengantar teknologi informasi, 
    sekiranya soal yang keluar untuk uts ada pada esok hari dari materi pelajaran tersebut."

    r "Kemudian kita lanjut mengenai materi-materi pada mata kuliah Algoritma Pemrograman."

    call belajar_alpro_1

    r normal2"Kemudian pada pertemuan kedua Alpro yang dipelajari adalah"

    call belajar_alpro_2

    r normal2"Itu semua merupakan hal yang sudah kita pelajari pada mata kuliah Alpro, kemudian mata kuliah terakhir yang akan di UTSkan besok adalah Desain Elementer."

    r "Berikut materi yang sudah kita terima pada mata kuliah DE pada pertemuan pertama"

    call belajar_de_1

    r normal2"Kemudian pada pertemuan kedua DE yang dipelajari adalah"

    call belajar_de_2

    r normal2"Kira-kira itu semua yang sudah kita pelajari pada mata kuliah Desain Elementer."

    r "Itu juga semua materi yang mungkin akan menjadi bahan untuk soal UTS besok."

    r "Karena sekarang juga sudah hampir jam 10 malam, mungkin sampai sini dulu ya?"

    r "Kalau ada pertanyaan sharing aja di grup temen-temen."

    t normal "Okey-okey makasih [r]"

    "Kemudian kegiatan belajar bersama untuk malam ini diakhiri. Teman-temanmu mulai meninggalkan foodcourt satu persatu."

    "Namun tidak semua temanmu pergi untuk pulang, masih ada dari mereka yang berlanjut belajar bersama di tempat yang lain."

    mc normal jacket"Makasih ya [r], besok ada lagi kah?"

    r "Ada sih, kalau mau ikut ikut aja besok tinggal dateng kok."

    mc "Okey-okey, yaudah pulang duluan ya aku."

    r "Sip, hati-hati di jalan [name]."

    "Setelah berpamitan pada [r] kamu keluar dari minimart dan langsung pulang ke kosan."

    jump sleep

label belajar_2:

    scene bg foodcourt with dissolve

    "Malam hari kedua sewaktu minggu ujian kamu memutuskan untuk mengikuti kegiatan belajar bersama dengan teman sekelasmu untuk kedua kalinya."

    "Kamu membawa buku catatanmu menuju ke foodcourt yang ada di minimart."

    "Sesampainya di minimart kamu melihat beberapa kerumpulan orang sedang membuka laptop maupun buku."

    r normal2 "Halo [name] kamu datang lagi ya..."

    mc normal jacket "Iya hehe...?"

    r "Gimana uts tadi ? Bisa kan?"

    mc "Ya gitu dahh hahaha... lumayan sih"

    r "Bagus kalau gitu, makanya kesini ikut belajar kan hahaha."

    mc "Kamu gimana? Kalo kamu mah pasti ezepeze kan [r]?"

    r "Hahaha nggak segitunya lahh... tapi ya bisa kan udah belajar."

    "Setelah mengobrol untuk beberapa waktu, kamu pergi menuju stand minuman sembari menunggu teman-teman kelasmu yang lain untuk datang."

    "Kamu memesan minuman dingin untuk menemanimu belajar pada malam hari ini."

    "Menunggu hingga beberapa teman kelasmu datang, akhirnya kegiatan belajar bersama dimulai."

    scene bg black with dissolve
    pause 1.0

    scene bg foodcourt with dissolve

    r normal2 "Karena sudah agak malem, kubagikan ya, materi yang pernah diajarkan ke kita beberapa minggu lalu."

    r "Untuk besok yang pertama ada Struktur Data, jadi pada minggu pertama materi yang kita dapatkan adalah:"

    call belajar_strukdat_1

    r "Kemudian pada pertemuan kedua Struktur Data yang dipelajari adalah:"

    call belajar_strukdat_2

    r "Kurang lebih itu yang pernah kita pelajari pada mata kuliah Struktur Data, 
    sekiranya soal yang keluar untuk uts ada pada esok hari dari materi pelajaran tersebut."

    r "Kemudian kita lanjut pada mata kuliah kedua besok yaitu Basis Data."

    r "Minggu pertama pada mata kuliah Basis Data adalah:"

    call belajar_basdat_1

    r "Kemudian pada pertemuan kedua Basis Data yang dipelajari adalah:"

    call belajar_basdat_2

    r "Itu semua merupakan hal yang sudah kita pelajari pada mata kuliah Basis Data, kemudian mata kuliah terakhir yang akan diujikan besok adalah Pemrograman Web."

    r "Berikut materi yang sudah kita terima pada mata kuliah Web pada pertemuan pertama:"

    call belajar_web_1

    r "Kemudian pada pertemuan kedua Web yang dipelajari adalah:"

    call belajar_de_2

    r "Kira-kira itu semua yang sudah kita pelajari pada mata kuliah Pemrograman Web."

    r "Itu juga semua materi yang mungkin akan menjadi bahan untuk soal ujian besok."

    r "Karena sekarang juga sudah hampir jam 10 malam, mungkin sampai sini dulu ya belajarnya?"

    r "Kalau ada pertanyaan sharing aja di grup kelas kita temen-temen."

    t normal "Okey-okey makasih [r]"

    "Kemudian kegiatan belajar bersama untuk malam ini ditutup. Teman-temanmu mulai meninggalkan foodcourt satu persatu."

    "Namun tidak semua temanmu pergi untuk pulang, masih ada dari mereka yang berlanjut belajar bersama di tempat yang lain."

    mc "Makasih ya [r], besok ada lagi kan ya?"

    r "Ada sih, kalau mau ikut lagi ikut aja besok tinggal dateng kok."

    mc "Okey-okey, yaudah aku pulang duluan ya."

    r "Sip, hati-hati di jalan [name]."

    "Setelah berpamitan pada [r] kamu keluar dari minimart dan langsung pulang ke kosan."

    jump sleep

label belajar_3:

    scene bg foodcourt with dissolve

    "Besok merupakan hari terakhir ujian tengah semester dilaksankan. 
    Kamu lebih memilih untuk menghabiskan malam ini mengikuti kegiatan belajar bersama."

    "Membawa buku catatan dan peralatan tulis, kamu berangkat menuju tempat kegiatan tersebut dilakukan."

    "Sama seperti hari-hari sebelumnya, kamu melihat berbagai kerumpulan orang yang memiliki tujuan yang sama dengan dirimu."

    "Setelah mengamati untuk beberapa waktu, kamu melihat [r] dan berjalan menghampirinya."

    mc normal jacket "Halo [r], udah mulai kah?"

    r normal2 "Halo [name] iya ini, karena cuma dua besok jadi pengen pada cepet selesai hahaha"

    mc normal jacket "Wajar sih, pengen cepet selesai juga aku."

    "Melihat teman-temanmu sudah mulai membuka dan membaca materi, kamu ikut mengeluarkan buku dari ranselmu."

    "[r] mendatangimu dengan membawa kertas materi untuk ujian besok."

    r "Btw ini materi yang udah dibahas tadi ya"

    mc "Ohhh okey, makasih [r]."

    "Karena sudah tertinggal kamu langsung membaca materi yang diberikan oleh [r]"

    scene bg black with dissolve
    pause 1.0

    scene bg foodcourt with dissolve

    "Mata kuliah yang akan diujikan pertama untuk besok adalah Pemrograman berorientasi objek(PBO)."

    "Materi untuk minggu pertama pertemuan mata kuliah tersebut adalah sebagai berikut:"

    call belajar_pbo_1

    "Kemudian pada pertemuan kedua PBO yang dipelajari adalah:"

    call belajar_pbo_2

    "Selesai membaca materi PBO, kamu sudah menyusul teman-temanmu yang sedang membahas materi mata kuliah yang selanjutnya."

    r normal2 "Teman-teman materi ini materi yang kita pelajari ya untuk mata kuliah Jaringan Komputer."

    "Membagikan kertas berisikan materi, kemudian [r] lanjut menjelaskan materi-materi yang ada."

    r "Materi pada minggu pertama pertemuan mata kuliah Jaringan Komputer adalah:"

    call belajar_jarkom_1

    r "Kemudian pada pertemuan kedua Jaringan Komputer yang dipelajari adalah:"

    call belajar_jarkom_2

    r "Kira-kira itu semua yang sudah kita pelajari pada mata kuliah Jaringan Komputer."

    r "Itu juga semua materi yang mungkin akan menjadi bahan untuk soal ujian besok."

    r "Karena besok cuma dua mata kuliah kurasa cukup itu aja materi yang dibahas temen-temen"

    r "Mungkin kalau ada pertanyaan bisa langsung ditanyain aja, mumpung masih ada waktu ini."

    "Setelah itu kegiatan belaja berubah menjadi sesi tanya jawab."

    "Teman-temanmu saling bertukar pertanyaan hingga dirasa cukup untuk malam ini."

    scene bg foodcourt with fade

    "Kemudian kegiatan belajar bersama untuk malam ini disudahi."

    "Berbeda dengan malam sebelumnya, kini karena masih belum terlalu malam kamu dan teman-temanmu menghabiskan waktu bersama untuk mengobrol terlebih dahulu."

    #public ++

    t "Akhirnyaa belajar terakhir selesai yeyyyy"

    t "Jadi bisa males-malesan lagi hahaha."

    t "Jangan gitu, masih besok lho selesainya hati-hati nanti kepleset ahahaha."

    t "Ihh kok gitu sihh? Kalau doa tuh yang baik-baik gitu hahaha."

    "Teman-temanmu sudah tidak sabar untuk mengakhiri ujian kali ini."

    "Kalian memesan makanan dan bergurau hingga larut malam."

    r "Makasih ya teman-teman, kegiatan belajar untuk ujian kali ini selesai."

    r "Semoga kegiatan ini membantu kita semua dalam mengerjakan ujian yang sebelumnya dan juga besok."

    r "Semoga kita mendapatkan hasil yang memuaskan sesuai dengan apa yang kita usahakan."

    t "Makasih [r]! Besok-besok agendakan lagi ya hahaha."

    t "Iyaa, setiap ada ujian agendakan dongg."

    r "Kalau pada mau sih oke-oke aja aku."

    t "Yeyy bisa nongki-nongki lagi kalau malem jadinya hahaha."

    t "Belajar oii belajar hahaha."

    r "Yaudah, aku tutup kalau pada mau pulang silahkan yang mau main lagi juga silahkan."

    "[r] kemudian berjalan mendekatimu."

    r "Makasih ya udah ikut kegiatan ini terus [name]!"

    mc "Makasih juga, aku dapet materi buat belajar juga hahaha."

    r "Hahaha yaudah kalau mau pulang dulu, tiati di jalan ya!"

    "Melihatmu sudah mengkemas barang-barangmu [r] sudah mengira kamu akan segera pulang."

    mc "Kamu gak langsung pulang kah?"

    r "Aku mau main dulu sih ahahah, habis belajar kan biar gak kaku begitu."

    mc "Hahaha, oke aku pulang dulu ya."

    r "Siapp hati-hati!"

    "Setelah berpamitan pada [r] kamu keluar dari minimart dan langsung pulang ke kosan."

    jump sleep

label belajar_pti_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Pengantar Teknologi Informasi kita membahas mengenai."

    show screen pti_1 with dissolve

    "Pengertian dan Perkembangan Teknologi Informasi."

    "Apa itu teknologi informasi dan perkembangan teknologi informasi tiap zaman dibahas pada pertemuan ini."

    hide screen pti_1

    show screen pti_1_2 with fade

    "Selain itu kita juga sedikiti membahas mengenai penggunaan teknologi informasi pada kehidupan sehari-hari."

    "Apa pentingnya dan bagaimana sebaiknya kita menggunakan teknologi informasi dibahas disini."

    ""

    hide screen pti_1_2

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah PTI pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_pti_1

label belajar_pti_2:

    scene bg foodcourt with fade

    "Pertama pada minggu kedua mata kuliah Pengantar Teknologi Informasi kita membahas mengenai."

    show screen pti_2 with dissolve

    "Pengertian data, informasi, dan pengetahuan."

    "Apa itu data, apa itu informasi, dan apa itu pengetahuan dibahas pada pertemuan ini."

    hide screen pti_2
    show screen pti_2_2 with fade

    "Selain itu pertemuan ini juga membahas mengenai pengertian Sistem Operasi, beberapa fungsi sistem operasi."

    "Apa itu sistem informasi dan fungsi sistem operasi bagi perangkat lunak dibahas disini."

    hide screen pti_2_2

    show screen pti_2_3 with fade

    "Sebelum pertemuan berakhir, contoh dan penjelasan Sistem operasi juga sempat dibahas."

    "Beberapa contoh sistem operasi beserta penjelasan dibahas pada pertemuan ini."

    ""

    hide screen pti_2_3

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah PTI pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_pti_2

label belajar_alpro_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Algoritma Pemrograman kita membahas mengenai."

    show screen alpro_1_1 with dissolve

    "Pengertian program, dan 3 level bahasa pemrograman."

    "Apa itu program, dan penjelasan mengenai 3 level bahasa pemrograman dibahas pada pertemuan ini."

    hide screen alpro_1_1

    show screen alpro_1_2 with fade

    "Selain itu pertemuan ini juga membahas mengenai pengertian Algoritma beserta ciri-ciri sebuah algoritma."

    "Apa itu algoritma dan apa saja ciri-ciri dari sebuah algoritma dibahas disini."
    
    ""
    hide screen alpro_1_2

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah Alpro pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_alpro_1

label belajar_alpro_2:

    scene bg foodcourt with fade

    "Kemudian pada minggu kedua mata kuliah Algoritma Pemrograman kita membahas mengenai."

    show screen alpro_2_1 with dissolve

    "Macam-macam konstruksi yang ada pada algoritma."

    "Pengertian algoritma sekuensial, percabangan, dan pengulangan dibahas pada pertemuan ini."

    hide screen alpro_2_1

    show screen alpro_2_2 with fade

    "Selain itu pertemuan ini juga membahas mengenai Pseudocode dan Flowchart."

    "Pengertian dan penjelasan mengenai Pseudocode dan Flowchart dibahas disini."

    hide screen alpro_2_2

    show screen alpro_2_3 with fade

    "Sebelum pertemuan berakhir, contoh dan penjelasan dari Pseudocode dan Flowchart juga sempat dibahas."

    "Berikut contoh Pseudocode dan Flowchart juga dibahas pada pertemuan ini."

    ""

    hide screen alpro_2_3

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah Alpro pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_alpro_2

label belajar_de_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Desain Elementer kita membahas mengenai."

    show screen de_1_1 with dissolve

    "Pengertian Desain Elementer dan Unsur-unsur yang ada didalamnya."

    "Apa itu Desain elementer, dan unsur-unsur seni dibahas pada pertemuan ini."

    hide screen de_1_1

    show screen de_1_2 with fade

    "Unsur Bidang dan Warna dijelaskan pada bagian ini."

    ""

    ""

    hide screen de_1_2

    show screen de_1_3 with fade

    "Unsur Tekstur dan Ruang dijelaskan pada bagian ini."

    ""

    ""

    hide screen de_1_3

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah DE pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_de_1

label belajar_de_2:

    scene bg foodcourt with fade

    "Kemudian pada minggu kedua mata kuliah Desain elementer kita membahas mengenai."

    show screen de_2_1 with dissolve

    "Prinsip-prinsip seni."

    "Pengertian prinsip Kesatuan, Keseimbangan, Irama, Penekanan, Proporsi, dan Keselarasan dibahas pada pertemuan ini."

    hide screen de_2_1

    show screen de_2_2 with fade

    "Selain itu pertemuan ini juga membahas mengenai Teori Warna dan Roda Warna."

    "Pengertian dan penjelasan mengenai Teori Warna dan Roda Warna dibahas disini."

    hide screen de_2_2

    show screen de_2_3 with fade

    "Sebelum pertemuan berakhir, contoh dan penjelasan dari Warna Primer, Sekunder, dan Tersier juga sempat dijelaskan."

    "Berikut penjelasan mengenai hal tersebut pada pertemuan ini."

    ""

    hide screen de_2_3

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah Alpro pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_de_2

label belajar_strukdat_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Pengantar Teknologi Informasi kita membahas mengenai."

    show screen strukdat_1_1 with dissolve

    "Pengertian Struktur Data dan contohnya."

    "Apa itu struktur data dan penjelasan contoh struktur data Array dijelaskan disini."

    hide screen strukdat_1_1

    show screen strukdat_1_2 with fade

    "Selain itu kita juga membahas mengenai struktur data Stack dan Queue."

    "Penjelasan mengenai struktur data Stack dan Queue kita dapatkan disini."

    ""

    hide screen strukdat_1_2

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah struktur data pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_strukdat_1

label belajar_strukdat_2:

    scene bg foodcourt with fade

    "Pertama pada minggu kedua mata kuliah Struktur Data kita membahas mengenai."

    show screen strukdat_2_1 with dissolve

    "Kita membahas lanjut jenis struktur data yang sudah dibahas diminggu sebelumnya."

    "Apa itu struktur data Tree, Linked List, dan Graph dibahas pada pertemuan ini."

    hide screen strukdat_2_1

    show screen strukdat_2_2 with fade

    "Slide ini menjelaskan lanjutan penjelasan mengenai struktur data Tree."

    "Selain itu pada slide ini terdapat juga penjelasan mengenai struktur data Graph"

    hide screen strukdat_2_2

    show screen strukdat_2_3 with fade

    "Sebelum pertemuan berakhir, manfaat penggunaan atau pengaplikasian struktur data juga sempat dibahas."

    "Beberapa manfaat dari struktur data dibahas pada pertemuan ini."

    ""

    hide screen strukdat_2_3

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah struktur data pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_strukdat_2

label belajar_basdat_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Basis Data kita membahas mengenai."

    show screen basdat_1_1 with dissolve

    "Pengertian basis data."

    "Apa itu basis data? Apa yang dapat dilakukan basis data? Dibahas pada pertemuan ini."

    hide screen basdat_1_1

    show screen basdat_1_2 with fade

    "Selain itu pertemuan ini juga membahas mengenai manfaat dan pentingnya basis data."

    "Beberapa manfaat basis data dan penjelasannya dijelaskan pada slide ini."
    
    ""
    hide screen basdat_1_2

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah basis data pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_basdat_1

label belajar_basdat_2:

    scene bg foodcourt with fade

    "Kemudian pada minggu kedua mata kuliah Basis Data kita membahas mengenai."

    show screen basdat_2_1 with dissolve

    "Sistem manajemen basis data."

    "Pengertian mengenai sistem manajemen basis data juga kelebihan dan kekurangan dari penggunaannya dibahas pada pertemuan ini."

    hide screen basdat_2_1

    show screen basdat_2_2 with fade

    "Selain itu pertemuan ini juga membahas mengenai contoh sistem manajemen basis data dan komponen pentingnya."

    "Contoh-contoh dan komponen-komponen sistem manajemen basis data dibahas disini."

    hide screen basdat_2_2

    show screen basdat_2_3 with fade

    "Sebelum pertemuan berakhir, Data Definition Language(DDL) dan Data Manipulative Language(DML) juga sempat dibahas."

    "Sedikit penjelasan mengenai DDL dan DML dijelaskan pada slide ini."

    ""

    hide screen basdat_2_3

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah basis data pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_basdat_2

label belajar_web_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Pemrograman Web kita membahas mengenai."

    show screen web_1_1 with dissolve

    "Pengertian Web, Websites, dan cara kerja."

    "Penjelasan singkat mengenai web dan websites juga penjelasan mengenai bagaimana mengakses sebuah web dijelaskan pada slide ini."

    hide screen web_1_1

    show screen web_1_2 with fade

    "Pertemuan ini juga menjelaskan mengenai HTTP, URL, dan jenis web dijelaskan pada bagian ini."

    ""

    ""

    hide screen web_1_2

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah Web pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_web_1

label belajar_web_2:

    scene bg foodcourt with fade

    "Kemudian pada minggu kedua mata kuliah Pemrograman Web kita membahas mengenai."

    show screen web_2_1 with dissolve

    "Teknologi-teknologi pada pengembangan web."

    "Pengertian mengenai browser dan HTML dibahas pada pertemuan ini."

    hide screen web_2_1

    show screen web_2_2 with fade

    "Penjelasan mengenai komponen-komponen HTML juga dijelaskan pada slide ini."

    "Komponen-komponen seperti Tag, Atribut, dan Element."

    hide screen web_2_2

    show screen web_2_3 with fade

    "Kemudian terdapat penjelasan mengenai fungsi-fungsi dari HTML."

    ""

    hide screen web_2_3

    show screen web_2_4 with fade

    "Bahasa pemrograman seperti CSS dan Javascript dijelaskan pada slide ini."

    ""

    hide screen web_2_4

    show screen web_2_5 with fade

    "Sebelum kuliah berakhir, dijelaskan juga mengenai Client Side Programming dan Server Side Programming."

    ""
    hide screen web_2_5

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah Pemrograman Web pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_web_2

label belajar_pbo_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Pemrograman Berorientasi Objek kita membahas mengenai."

    show screen pbo_1_1 with dissolve

    "Pengertian dan Konsep yang ada pada PBO."

    "Pengertian mengenai PBO dan konsep seperti kelas dan objek pada PBO dijelaskan disini."

    hide screen pbo_1_1

    show screen pbo_1_2 with fade

    "Selain itu kita juga membahas mengenai karakteristik dari objek dijelaskan."

    "Penjelasan mengenai State dan Behaviour dijelaskan pada slide ini."

    ""

    hide screen pbo_1_2

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah PBO pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_pbo_1

label belajar_pbo_2:

    scene bg foodcourt with fade

    "Pertama pada minggu kedua mata kuliah Pemrogrmaan Berbasis Objek kita membahas mengenai."

    show screen pbo_2_1 with dissolve

    "Kita membahas prinsip-prinsip yang ada dalam PBO."

    "Prinsip enkapsulasi dan abtraksi dijelaskan pada slide ini."

    hide screen pbo_2_1

    show screen pbo_2_2 with fade

    "Slide ini menjelaskan lanjutan penjelasan mengenai prinsip-prinsip yang ada pada PBO."

    "Prinsip inheritance dan polymorphism dijelaskan pada slide ini."

    hide screen pbo_2_2

    show screen pbo_2_3 with fade

    "Sebelum pertemuan berakhir, manfaat penggunaan atau pengaplikasian PBO juga sempat dibahas pada pertemuan ini."

    "Beberapa manfaat dari PBO dibahas pada slide ini."

    ""

    hide screen pbo_2_3

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah struktur data pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_pbo_2

label belajar_jarkom_1:

    scene bg foodcourt with fade

    "Pertama pada minggu pertama mata kuliah Jaringan Komputer kita membahas mengenai."

    show screen jarkom_1_1 with dissolve

    "Pengertian mengenai jaringan komputer dan jenis jaringan komputer."

    "Pengertian jaringan komputer dan jenis jaringan berdasarkan geografisnya dijelaskan pada pertemuan ini."

    hide screen jarkom_1_1

    show screen jarkom_1_2 with fade

    "Kemudian pada slide selanjutnya terdapat lanjutan mengenai jenis jaringan komputer berdasarkan geografisnya dijelaskan."

    "Jaringan MAN dan WAN dijelaskan pada slide ini."
    
    ""
    hide screen jarkom_1_2

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah jaringan komputer pertemuan 1?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_jarkom_1

label belajar_jarkom_2:

    scene bg foodcourt with fade

    "Kemudian pada minggu kedua mata kuliah Jaringan Komputer kita membahas mengenai."

    show screen jarkom_2_1 with dissolve

    "Jenis jaringan komputer berdasarkan fungsinya."

    "Pengertian mengenai jaringan client server dibahas pada slide ini."

    hide screen jarkom_2_1

    show screen jarkom_2_2 with fade

    "Masih pada jenis jaringan komputer berdasarkan fungsinya."

    "Pengertian mengenai jaringan peer-to-peer dibahas disini."

    hide screen jarkom_2_2

    show screen jarkom_2_3 with fade

    "Kemudian masih ada materi mengenai jenis jaringan komputer berdasarkan distribusi datanya."

    "Slide ini membahas mengenai jaringan dengan distribusi data Terpusat dan Terdistribusi."

    hide screen jarkom_2_3

    show screen jarkom_2_4 with fade

    "Sebelum pertemuan berakhir, jenis jaringan komputer berdasarkan media transmisinya juga sempat dibahas."

    "Sedikit penjelasan mengenai jaringan komputer dengan media berkabel dan nirkabel dijelaskan pada slide ini."

    ""

    hide screen jarkom_2_4

    "Apakah kalian sudah mengerti mengenai kisi-kisi dari pertemuan pertama mata kuliah jaringan komputer pertemuan 2?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

            return

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call belajar_jarkom_2

label makan_makan:

    scene bg minimart_out with dissolve

    "Panas terik hari ini membuat dirimu ingin segera memasuki minimart."

    "Jalanan tidak terlalu ramai, namun antrian kendaraan yang memanjang tetap tidak terhindarkan di area perempatan."

    "Setelah bergelut dengan terik matahari, akhirnya kamu sampai di area parkir minimart."

    "Memarkir motormu, kamu segera memasuki minimart."

    scene bg minimart_in with fade

    scene bg foodcourt with fade

    "Setelah berada dalam minimart, foodcourt merupakan tempat pertama yang kamu tuju."

    "Sesampai di foodcourt beberapa temanmu melambaikan tangannya kepadamu menunjukkan dimana tempat kalian duduk bersama."

    "Mendekati teman-teman kelasmu kamu melihat sekitar sepertiga dari kelasmu mengikuti acara makan-makan ini."

    t normal "[name] gimana ujiannya bisa kan?"

    mc normal jacket "Ya gitu dah, lu gimana?"

    t "Hahaha ya sama gitu dahh."

    t "Udah-udah pesen dulu aja, yang udah selesai biarin, punyaku aja entah gimana nilainya ahahaha."

    "Kemudian kamu diberikan kertas menu yang sudah berisikan beberapa pesanan temanmu."

    "Memutuskan untuk memilih menu ayam bakar geprek dan es kopi susu, kamu menulis menu tersebut pada kertas pesanan dan memberikannya kepada temanmu yang juga belum menulis."

    r normal2 "Ini udah semua kan yang pesen? Kukasih sana ya?"

    t "Udahhh..."

    t "Okee makasih [r]!"

    "[r] mengantar kertas pesanan untuk semua temanmu."

    "Meskipun disebut acara makan-makan, pada dasarnya acara ini hanya digunakan untuk berkumpul bersama dengan teman sekelas."

    "Dari awal hingga akhir acara hanya diisi dengan cerita-cerita teman kelasmu sebagai pelampiasan stress ujian dari beberapa hari lalu."

    call eat

    "Acara berakhir ketika matahari sudah mulai terbenam."

    "Satu persatu temanmu mulai meninggalkan minimart, tidak lama kemudian kamupun ikut menyusul."

    call change_timephase
    call screen mapUI with dissolve