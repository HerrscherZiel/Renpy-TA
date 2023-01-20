
label minimart_pertama:

    $ firstMart = False

    # show day1 miniout:
    #     xalign 0.5 yalign 0.5
    # with dissolve

    pause 2.0

    scene bg minimart_out
    with fade

    # show screen days_screen
    
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

    show screen stats_screen with dissolve

    mc  "Beli apa ya? Roti atau Minum hmmm…."

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

    "..............."

    "........"

    "..."

    scene bg streets
    with dissolve

    "Setelah selesai membayar, ketika keluar dari minimart terlihat matahari sudah hampir terbenam, dan hari sudah menjadi gelap."

    "Kamu bergegas kembali ke parkiran motor yang ada di kampus."

    "Selagi berjalan kamu memilih:"

    menu:

        "Mengkonsumsi apa yang kamu beli.":

            show mc normal jacket:
                xalign 0.2 yalign -0.5
            
            mc  "Langsung kumakan sekarang saja lah, sudah agak lapar juga."
        
            "Kamu duduk di kursi umum yang ada di pinggir jalan untuk menikmati apa yang dibeli di minimart sebelumnya."

            "Kamu memakan roti yang kamu beli!"
            "Stats berubah!"

            $ energy += 10
            $ hunger += 15
            $ health = round((hunger+energy+vit) / 3)

        "Menyimpannya untuk besok pagi.":

            $ rotiAwal = True
            mc  "Buat besok sajalah makannya, nanti keburu malam."

            show mc normal jacket:
                xalign 0.2 yalign -0.5
    
    "Kemudian kamu bergegas ke arah parkiran motor kampus dan segera mengendarai motormu untuk pulang."

    "Pilih {b}Ikon Kos{/b} untuk pulang ke kosanmu."

    # hide screen days_screen
    # hide screen stats_screen
    $ prologueCount +=1
    call screen mapUI with dissolve

    return

label mini2S:

    # BG Minimart Out

    # mc Hahhh… bisa segar begini di dalem, diluar panasnya gak masuk akal gilaaa.

    # Di dalam kamu merasakan suhu yang berbanding terbalik 180O. Matahari terik panas tanpa ada satupun awan yang menutup sinarnya.

    # Sementara di dalam minimart kamu merasakan sejuknya ruangan ber AC.

    # Suhu yang tinggi membuat berkeringat, di dalam minimart hal yang pertama kali kamu lakukan adalah mencari tempat duduk.

    # If $day3 is True

    # Terdapat beberapa tempat duduk yang ditempatkan pada sisi minimart.

    # Entah karena minimart ini biasa dipenuhi oleh pembeli, atau karena memang desain awal minimart ini sudah menyiapkan ruang untuk tempat duduk.

    # Meskipun disebut dengan mini-mart, namun apa yang ada di dalamnya sudah tidak termasuk mini lagi.

    # Terdapat sektor pembelanjaan, baik kebutuhan harian, food court, maupun kebutuhan lain. 

    # Mendapatkan tempat duduk kosong di dekat food court di dalam minimart, pandanganmu tertuju ke berbagai penjuru ruangan mengamati apa yang ada didalamnya.

    # mc Mini apanya? Ini sih sudah bisa dibilang seperti mall- mini-mall sih.

    # Setelah mendinginkan badan sejenak, kamu beranjak mendekati salah satu stall yang menjual minuman.

    # Mendekati stall minuman tersebut kamu tidak melihat satu orang pun yang berada di dalam stall.

    # mc Hmm lagi isoma mungkin kali ya?

    # Kamu mendekati stall itu dan melihat daftar menu yang ada.

    # mc Teh tarik.. Kopi… Es degan… hmm mending beli apa nih?

    # stall Ada yang bisa dibantu kak?

    # Tiba-tiba ada yang memanggilmu dari belakang.

    # mc Oh ah ini kak, mau pesan minum.

    # stall pesan apa kak, ada macam-macam teh, kopi, es buah dan es degan.

    # stall Oh iya kak, kebetulan lagi ada promo, untuk setiap pembelian satu kopi dapat tambahan 1 kopi free kak.

    # mc boleh itu, yaudah kak pesen kopinya satu.

    # stall Tapi ada syaratnya kak, harus follow EG nya duluu..

    # mc Oh gitu, EG nya yang disini ya kan kak?

    # stall iya itu kak, ini kopinya es atau hangat ya?

    # mc Es kak dua dua nya, lagi pengin ya dingin-dingin panas begini.

    # mc Oh iya, ini udah ku follow ya.

    # stall oke siap! Tunggu sebentar ya kak.

    # Stall tadi sudah nunggu lama ya kak?

    # mc Oh belum kok, baru datang tadi. Di luar panas banget kak ngadem dulu tadi hahaha.

    # stall iyasih emang, kalau jam segini lagi panas-panasnya di luar.

    # mc Ini lagi musimnya panas kaya gini, atau biasanya kak disini?

    # stall Ya lagi musimnya, panas-panas begini nanti sorenya hujan.

    # mc Wah payah juga, kalau habis panas hujan gitu.

    # Stall ya anehnya begita kak, malah kalau mendung gitu ga hujan-hujan.

    # mc bisa begitu juga ya hahaha

    # stall kuliah di situ juga ya kak?

    # mc Iya, baru masuk tahun ini aku.

    # stall Wah mahasiswa baru dong, jurusan apa kak?

    # mc Iya, di komputer begitu, di vokasi aku.

    # stall Wah sering-sering mampir sini kak, dekat kan kampusnya.

    # mc Hahaha siap.

    # Beberapa menit kemudian, setelah lama berbincang dengan penjaga stall minuman kamu menerima pesananmu dan kembali ke tempat duduk semula.

    # stall Oke, terimakasih kak.

    # Else 👍

    #     Setelah mendapatkan tempat duduk, kamu berdiam menikmati udara dingin sebelum selanjutnya memutuskan untuk membeli minuman di stall minuman terdekat.

    #     mc Kak es kopi ya, large satu.

    #     stall1 oke kak, ditunggu sebentar ya.

    #     mc Tumben ya siang-siang begini sudah ramai disini.

    #     Stall1 iya kak, kayaknya karena di bagian kebutuhan harian lagi ada diskon mingguan, karena terbatas ya jadi rebutan begitu.

    #     mc Diskon sih emang menarik sih ya hahaha

    #     stall1 Ya begitu, namanya anak kuliahan kan, bukan anak kuliahan semua juga sih. Kalau namanya diskon ya pasti banyak yang mau.

    #     mc Memang banyak diskon ya disini.

    #     stall1 iya kak, narik pelanggan biasa.

    #     stall1 Oh ini kak, es kopi latte cup largenya. Terimakasih.

    #     Setelah membayar untuk kopimu, kamu kembali ke tempat dudukmu di bagian food court minimart.

    # Setelah kembali ke tempat duduk, kamu langsung mengeluarkan smartphonemu, dan membuka salah satu permainan yang ada di dalamnya.

    # Di sekelilingmu kamu juga melihat beberapa orang menikmati jam istirahat siang mereka.

    # Pekerja kantoran, anak kuliahan, bahkan anak SMA terlihat asyik menikmati waktu mereka. Memakan makan siang, berbincang dengan teman, dan tentu saja terdapat orang membuka laptop untuk melanjutkan pekerjaan mereka di sela-sela waktu.

    # Sambil menyeruput es kopi yang kamu beli dari stall minuman, kamu fokus kembali pada layar smartphonemu.

    # Henshin Effect tertulis pada loading screen layar smartphonemu

    # If $day3 is true 
    # Henshin merupakan permainan yang akhir-akhir ini populer di khalayak luas. Permainan open world yang memiliki grafis dan gameplay yang menyegarkan mata dan fitur yang paling menarik adalah gacha.

    # mc Siang-siang begini selesain daily quest lumayan lah.

    # mc Bentar-bentar questnya dimana aja ini…, Wohh lets goo deket-deket semua gausah travel.

    # Seru dalam duniamu sendiri, tak sadar satu cup yang kamu beli sudah habis.

    # Baterai smartphone juga sudah menjadi merah, kamu menutup permainan dan memasukan smartphonemu ke dalam saku.

    # mc niat mau beli minum sebentar malah jadi nongkrong lama begini, diluar juga kayaknya sudah enggak sepanas tadi, waktunya pulang.

    # mc Kopinya enak juga, besok kalau kesini lagi aku beli lah.


    # stat +


