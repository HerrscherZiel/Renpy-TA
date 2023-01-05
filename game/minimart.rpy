
label minimart_pertama:

    $ firstMart = False

    show day1 miniout:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 2.0

    scene bg minimart_out
    with fade

    show screen days_screen
    
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

    show screen stats_screen

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
    call screen mapUI

    return

