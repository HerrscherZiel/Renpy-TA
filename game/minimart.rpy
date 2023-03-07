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
#morn
label mart_mornS1:

    "mart morn 1"

label mart_mornS2:

    "mart morn 2"

label mart_mornS3:

    "mart morn 3"

#noon
label mart_dayS1:

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

    jump kos_krs4_night

label mart_dayS2:

    "mart day 2"

label mart_dayS3:

    "mart day 3"

    return
    # call screen mapUI


    # stat +

#night
label mart_nightS1:

    "mart night 1"

label mart_nightS2:

    "mart night 2"

label mart_nightS3:

    "mart night 3"

