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
    elif day == 24:
        jump belajar_uas1
    elif day ==25:
        jump belajar_uas2
    elif day == 26:
        jump belajar_uas3

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

    call hangout

    "Setelah berkumpul cukup lama bersama teman kelasmu, kamu akhirnya memutuskan untuk pulang."

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

    r normal2 "Kemudian pada pertemuan kedua Struktur Data yang dipelajari adalah:"

    call belajar_strukdat_2

    r normal2 "Kurang lebih itu yang pernah kita pelajari pada mata kuliah Struktur Data, 
    sekiranya soal yang keluar untuk uts ada pada esok hari dari materi pelajaran tersebut."

    r "Kemudian kita lanjut pada mata kuliah kedua besok yaitu Basis Data."

    r "Minggu pertama pada mata kuliah Basis Data adalah:"

    call belajar_basdat_1

    r normal2 "Kemudian pada pertemuan kedua Basis Data yang dipelajari adalah:"

    call belajar_basdat_2

    r normal2 "Itu semua merupakan hal yang sudah kita pelajari pada mata kuliah Basis Data, kemudian mata kuliah terakhir yang akan diujikan besok adalah Pemrograman Web."

    r "Berikut materi yang sudah kita terima pada mata kuliah Web pada pertemuan pertama:"

    call belajar_web_1

    r normal2"Kemudian pada pertemuan kedua Web yang dipelajari adalah:"

    call belajar_web_2

    r normal2 "Kira-kira itu semua yang sudah kita pelajari pada mata kuliah Pemrograman Web."

    r "Itu juga semua materi yang mungkin akan menjadi bahan untuk soal ujian besok."

    r "Karena sekarang juga sudah hampir jam 10 malam, mungkin sampai sini dulu ya belajarnya?"

    r "Kalau ada pertanyaan sharing aja di grup kelas kita temen-temen."

    t normal "Okey-okey makasih [r]"

    "Kemudian kegiatan belajar bersama untuk malam ini ditutup. Teman-temanmu mulai meninggalkan foodcourt satu persatu."

    "Namun tidak semua temanmu pergi untuk pulang, masih ada dari mereka yang berlanjut belajar bersama di tempat yang lain."

    mc normal jacket "Makasih ya [r], besok ada lagi kan ya?"

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

    r normal2 "Kemudian pada pertemuan kedua Jaringan Komputer yang dipelajari adalah:"

    call belajar_jarkom_2

    r normal2 "Kira-kira itu semua yang sudah kita pelajari pada mata kuliah Jaringan Komputer."

    r "Itu juga semua materi yang mungkin akan menjadi bahan untuk soal ujian besok."

    r "Karena besok cuma dua mata kuliah kurasa cukup itu aja materi yang dibahas temen-temen"

    r "Mungkin kalau ada pertanyaan bisa langsung ditanyain aja, mumpung masih ada waktu ini."

    "Setelah itu kegiatan belaja berubah menjadi sesi tanya jawab."

    "Teman-temanmu saling bertukar pertanyaan hingga dirasa cukup untuk malam ini."

    scene bg foodcourt with fade

    "Kemudian kegiatan belajar bersama untuk malam ini disudahi."

    "Berbeda dengan malam sebelumnya, kini karena masih belum terlalu malam kamu dan teman-temanmu menghabiskan waktu bersama untuk mengobrol terlebih dahulu."

    #public ++

    t normal "Akhirnyaa belajar terakhir selesai yeyyyy"

    t "Jadi bisa males-malesan lagi hahaha."

    t "Jangan gitu, masih besok lho selesainya hati-hati nanti kepleset ahahaha."

    t "Ihh kok gitu sihh? Kalau doa tuh yang baik-baik gitu hahaha."

    "Teman-temanmu sudah tidak sabar untuk mengakhiri ujian kali ini."

    "Kalian memesan makanan dan bergurau hingga larut malam."

    r normal2 "Makasih ya teman-teman, kegiatan belajar untuk ujian kali ini selesai."

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

    mc normal jacket "Makasih juga, aku dapet materi buat belajar juga hahaha."

    r "Hahaha yaudah kalau mau pulang dulu, tiati di jalan ya!"

    "Melihatmu sudah mengkemas barang-barangmu [r] sudah mengira kamu akan segera pulang."

    mc "Kamu gak langsung pulang kah?"

    r "Aku mau main dulu sih ahahah, habis belajar kan biar gak kaku begitu."

    mc "Hahaha, oke aku pulang dulu ya."

    r "Siapp hati-hati!"

    "Setelah berpamitan pada [r] kamu keluar dari minimart dan langsung pulang ke kosan."

    jump sleep


#belajarUAS
label belajar_uas1:

    scene bg black with dissolve

    "Malam harinya kamu teringat perkataan [r] yang akan kembali mengadakan kegiatan belajar bersama untuk ujian akhir yang akan dimulai besok."

    "Sama seperti ketika UTS, kegiatan bersama ini juga akan dilakukan pada bagian foodcourt minimart."

    "Kamu membawa buku catatanmu dan pergi menuju foodcourt yang ada di minimart."

    scene bg foodcourt with dissolve

    "Sesampainya di minimart kamu melihat beberapa kerumpulan orang sedang membuka laptop atau buku catatan."

    "Karena terdapat beberapa gerombolan mahasiswa yang juga melakukan belajar bersama, kamu mengamati beberapa gerombolan mahasiswa tersebut."

    "Setelah menemukan gerombolan belajarmu, kamu langsung mendekati gerombolan tersebut dan menyapa teman-temanmu."

    r normal2 "Oh hai [name] kamu datang ya..."

    mc normal jacket "Udah pada dateng dari tadi ya?"

    r "Udah lumayan sih nggak tadi-tadi banget tapi."

    mc "Udah mulai?"

    r "Baru tuker-tukeran catatan aja ini."

    mc "Ohhh okey-okey."

    "Disekitar kamu melihat teman sekelasmu yang sudah datang, sudah memesan makanan dan minuman dari foodcourt sebagai teman belajar."

    mc "Aku pesan dulu aja dah, bentar ya [r]."

    r "Santai ini kita nggak buru-buru juga kok."

    "Kemudian kamu berjalan menuju salah satu stand dan memesan menu yang ada."

    scene bg black with dissolve
    pause 1.0

    scene bg foodcourt with dissolve

    "Setelah beberapa menit menunggu pesananmu telah siap, selesai membayar kamu kembali ke kerumpulan teman sekelasmu membawa apa yang kamu pesan."

    "Ketika kembali, [r] sedang mulai menjelaskan mengenai mata kuliah 'Pengantar Teknologi Informasi' yang akan menjadi mata kuliah pertama yang diujikan besok."

    r normal2 "Jadi ini aku punya beberapa soal latihan yang sesuai kisi-kisi."

    r "Di lembar baliknya juga sudah terdapat kunci jawabannya jadi bisa kalian lihat sendiri ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_pti0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai kisi-kisi untuk ujian akhir mata kuliah PTI?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_pti0

    r normal2 "Kurang lebih itu yang pernah kita pelajari pada mata kuliah pengantar teknologi informasi."

    r "Kemudian kita lanjut mengenai soal latihan sesuai kisi-kisi untuk mata kuliah Algoritma Pemrograman."

    r "Sama seperti tadi, kunci jawaban untuk soal ada di balik lembar soalnya ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_alpro0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai soal latihan mata kuliah Alpro ini?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_alpro0

    r normal2"Itu semua merupakan hal yang sudah kita pelajari pada mata kuliah Alpro"

    r "Kemudian kita akan berlanjut ke mata kuliah terakhir yang akan di ujikan besok yaitu Desain Elementer."
    
    r "Yang terakhir kita akan latihan menggunakan soal latihan untuk mata kuliah DE."

    r "Sama seperti tadi, kunci jawaban untuk soal ada di balik lembar soalnya ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_de0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai soal latihan mata kuliah DE ini?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_de0

    r normal2 "Itu semua soal latihan untuk ujian akhir besok ya, semoga yang besok soal yang diujikan mirip-mirip."

    r "Karena sekarang juga sudah hampir jam 10 malam, mungkin sampai sini dulu belajar bersamanya?"

    r "Kalau ada pertanyaan sharing aja di grup ya temen-temen!"

    t normal "Okey-okey makasih [r]"

    "Kemudian kegiatan belajar bersama untuk malam ini diakhiri. Teman-temanmu mulai meninggalkan foodcourt satu persatu."

    "Namun tidak semua temanmu pergi dan pulang ke rumah masing-masing, masih ada dari mereka yang berlanjut belajar bersama di tempat yang lain."

    mc normal jacket "Makasih ya [r], besok ada belajar bersama lagi kan?"

    r "Tentu ada dong! Kalau mau ikut, dateng lagi aja besok."

    mc "Okey-okey, yaudah pulang duluan ya aku."

    r "Sip, hati-hati di jalan [name]."

    "Setelah berpamitan pada [r] kamu keluar dari minimart dan langsung pulang ke kosan."
    $ energy += 10
    $ fit -= 5
    $ public += 10
    $ rissa_fond += 10
    $ hunger += 15
    jump sleep

label belajar_uas2:

    scene bg black with dissolve

    "Seperti perkataan [r] semalam kegiatan belajar bersama untuk ujian akhir hari yang kedua akan dilaksanakan lagi malam ini."

    "Lokasi yang sama  yaitu di bagian foodcourt minimart akan menjadi tempat belajar bersama lagi malam ini."

    "Kamu membawa buku catatanmu dan pergi menuju foodcourt yang ada di minimart."

    scene bg foodcourt with dissolve

    "Sesampainya di minimart kamu langsung mencari kerumpulan teman-temanmu."

    "Tidak lama kemudian kamu melihar [r] melambaikan tangnnya kepadamu, lalu kamu berjalan menuju ke arah [r] dan teman sekelasmu."

    "Kamu mendekati kerumpulan teman sekelasmu dan menyapa mereka."

    r normal2 "Oh hai [name] kamu datang lagi ya..."

    mc normal jacket "iya hehe, tadi cukup membantu waktu ujian."

    r "Bagus kalau begitu deh."

    mc "Udah mau mulai kah?"

    r "Ohh belum, lagi pada mesen makan sama minum ini."

    mc "Ohhh okey-okey aku juga pesan dulu aja ya berarti."

    r "Iyaa, ini juga sambil nungguin temen-temen yang belum dateng kok."

    mc "Okey kalau begitu."

    r "Santai ajaa ini kita nggak buru-buru juga kok."

    "Kemudian kamu berjalan menuju salah satu stand dan memesan menu yang ada."

    scene bg black with dissolve
    pause 1.0

    scene bg foodcourt with dissolve

    "Setelah beberapa menit menunggu pesananmu telah siap, selesai membayar kamu kembali ke kerumpulan teman sekelasmu membawa apa yang kamu pesan."

    "Setelah membawa apa yang kamu pesan, kamu sempat mengobrol selama beberapa menit bersama teman sekelasmu sebelum kegiatan belajar bersama dimulai."

    #mulai

    "Ketika kegiatan dimulai, [r] mulai menjelaskan mengenai mata kuliah 'Struktur Data' yang akan menjadi mata kuliah pertama yang diujikan besok."

    r normal2 "Seperti kemarin, aku akan membagikan beberapa soal latihan yang sesuai dengan kisi-kisi ujian akhir."

    r "Di lembar baliknya juga sudah terdapat kunci jawabannya jadi bisa kalian lihat sendiri ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_strukdat0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai kisi-kisi untuk ujian akhir mata kuliah Strukdat?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_strukdat0

    r normal2 "Kurang lebih itu yang pernah kita pelajari pada mata kuliah Struktur Data."

    r "Kemudian kita lanjut mengenai soal latihan sesuai kisi-kisi untuk mata kuliah Basis Data."

    r "Sama seperti tadi, kunci jawaban untuk soal ada di balik lembar soalnya ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_basdat0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai soal latihan mata kuliah Basdat ini?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_basdat0

    r normal2"Itu semua merupakan hal yang sudah kita pelajari pada mata kuliah Basis Data"

    r "Kemudian kita akan berlanjut ke mata kuliah terakhir yang akan di ujikan besok yaitu Pemrograman Web."
    
    r "Yang terakhir kita akan latihan menggunakan soal latihan untuk mata kuliah Web."

    r "Sama seperti tadi, kunci jawaban untuk soal ada di balik lembar soalnya ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_web0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai soal latihan mata kuliah web ini?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_web0

    r normal2 "Itu semua soal latihan untuk ujian akhir besok ya, semoga yang besok soal yang diujikan mirip-mirip."

    r "Karena sekarang juga sudah hampir jam 10 malam, mungkin sampai sini dulu belajar bersamanya?"

    r "Kalau ada pertanyaan sharing aja di grup ya temen-temen!"

    r "Makasih yang udah ikut datang dan meraimakan temen-temen!"

    t normal "Okey-okey makasih [r]"

    "Kemudian kegiatan belajar bersama untuk malam ini diakhiri. Teman-temanmu mulai meninggalkan foodcourt satu persatu."

    "Namun tidak semua temanmu pergi dan pulang ke rumah masing-masing, masih ada dari mereka yang berlanjut belajar bersama di tempat yang lain."

    mc normal jacket "Makasih ya [r], besok hari terakhir ada lagi kan?"

    r "Tentu ada dong! Kalau mau ikut, dateng lagi aja besok."

    mc "Okey-okey, yaudah pulang duluan ya aku."

    r "Siappp, hati-hati di jalan [name]."

    "Setelah berpamitan pada [r] kamu keluar dari minimart dan langsung pulang ke kosan."

    $ energy += 10
    $ fit -= 5
    $ public += 10
    $ rissa_fond += 10
    $ hunger += 15

    jump sleep

label belajar_uas3:

    scene bg black with dissolve

    "Malam ini adalah malam terakhir kegiatan belajar bersama akan diadakan."

    "Lokasi yang sama yaitu di bagian foodcourt minimart akan menjadi tempat belajar bersama lagi malam ini."

    "Kamu membawa buku catatanmu dan pergi menuju foodcourt yang ada di minimart."

    scene bg foodcourt with dissolve

    "Sesampainya di minimart kamu langsung mencari kerumpulan teman-temanmu."

    "Tidak lama kemudian kamu melihar [r] melambaikan tangnnya kepadamu, lalu kamu berjalan menuju ke arah [r] dan teman sekelasmu."

    "Kamu mendekati kerumpulan teman sekelasmu dan menyapa mereka."

    r normal2 "Oh hai [name], selamat datangg..."

    mc normal jacket "Hari terakhir malah tambah rame ya?"

    r "Iyaa, soalnya kan besok cuma dua mata kuliah, jadi selesai lebih cepet, terus mau bahas kegiatan habis ujian gituu."

    mc "Ohhh mau makan-makan lagi kah?"

    r "Ohh belum tau kalau itu, yang penting kamu ikut aja okeyy."

    mc "Lets see, semoga bisa ikut."

    r "yeee kamu mah sukanya gitu."

    mc "hehehe ya kan siapa tahu tidak bisa ikut."

    r "Harus ikut sih kalau ini hahaha."

    "Kamu menghabiskan waktumu dengan berbincang dengan [r] sembari menunggu kegiatan belajar bersama dimulai dan menunggu pesananmu diantarkan."

    scene bg black with dissolve
    pause 1.0

    scene bg foodcourt with dissolve

    "Setelah beberapa menit menunggu pesananmu telah siap, selesai membayar kamu kembali ke kerumpulan teman sekelasmu membawa apa yang kamu pesan."

    "Setelah membawa apa yang kamu pesan, kamu sempat mengobrol selama beberapa menit bersama teman sekelasmu sebelum kegiatan belajar bersama dimulai."

    #mulai

    "Ketika kegiatan dimulai, [r] mulai menjelaskan mengenai mata kuliah 'Pemrograman Berorientasi Objek' yang akan menjadi mata kuliah pertama yang diujikan besok."

    r normal2 "Seperti kemarin, aku akan membagikan beberapa soal latihan yang sesuai dengan kisi-kisi ujian akhir."

    r "Di lembar baliknya juga sudah terdapat kunci jawabannya jadi bisa kalian lihat sendiri ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_pbo0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai kisi-kisi untuk ujian akhir mata kuliah PBO?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_pbo0

    r normal2 "Kurang lebih itu yang pernah kita pelajari pada mata kuliah Pemrograman Berorientasi Objek."

    r "Kemudian kita lanjut mengenai soal latihan sesuai kisi-kisi untuk mata kuliah Jaringan Komputer."

    r "Sama seperti tadi, kunci jawaban untuk soal ada di balik lembar soalnya ya."

    r "Sebisa mungkin jawab sendiri dulu, sebelum melihat kunci jawabannya."

    call screen bl_uas_jarkom0

    r normal2 "Apakah kalian sudah cukup mengerti mengenai soal latihan mata kuliah jarkom ini?"

    menu:

        "Sudah paham":

            "Sudah paham, lanjut saja."

        "Belum, ulang dong!":

            "Belum, bisa diulaingi sekali lagi?"

            call screen bl_uas_jarkom0

    r normal2"Itu semua merupakan hal yang sudah kita pelajari pada mata kuliah Jaringan Komputer"

    r normal2 "Itu semua soal latihan untuk ujian akhir besok ya, semoga yang besok soal yang diujikan mirip-mirip."

    r "Karena sekarang juga sudah hampir jam 10 malam, mungkin sampai sini dulu belajar bersamanya?"

    r "Kalau ada pertanyaan sharing aja di grup ya temen-temen!"

    r "Makasih yang udah ikut datang dan meraimakan temen-temen!"

    t normal "Okey-okey makasih [r]"

    r "Oh iya kalau yang masih ada waktu minta waktunya sebentar ya, kita mau bahas kegiatan setelah ujian nanti."

    "Setelah mendengarkan perkataan [r], sebagian besar temanmu masih tetap di lokasi."

    "Namun tidak semua temanmu ikut berdiskusi, masih ada dari mereka yang berlanjut belajar bersama di tempat yang lain atau pulang."

    "Diskusi berjalan tidak begitu lama."

    "Meskipun belum mempunyai keputusan apa yang akan dilakukan, namun kelas mendapatkan beberapa pilihan yang dapat dipilih."

    "Diskusi pun selesai dan sudah waktunya untuk pulang."

    mc normal jacket "Makasih ya [r], kabari aku ya jadinya mau bagaimana."

    r "Okeyy... besok kita liat habis ujian aja."

    mc "Okey-okey, yaudah pulang duluan ya aku."

    r "Siappp, hati-hati di jalan [name]."

    "Setelah berpamitan pada [r] kamu keluar dari minimart dan langsung pulang ke kosan."

    jump sleep

    $ energy += 10
    $ fit -= 5
    $ public += 10
    $ rissa_fond += 10
    $ hunger += 15
#Special Events   

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