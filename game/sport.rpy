

#day


#morning
label sport_mornS1:

    "Mengambil sepatu larimu, kamu mulai berlari kecil mengelilingi kampung."

    call jog
    jump mandi

label sport_mornS2:

    "Keluar dari kamar, kamu berjalan menuju warmindo yang dekat dengan kosan."

    call eat
    jump mandi

label sport_mornS3:

    "Keluar dari kamar, kamu berjalan menuju warmindo yang dekat dengan kosan."

    call jog
    jump mandi
#noon
label sport_dayS1:

    pause 2.0

    scene bg kos morn with dissolve

    "Merasakan tubuhmu yang sudah mulai pegal dan kaku, kamu berencana untuk melakukan olahraga untuk kembali menyegarkan tubuhmu."

    "Kamu berniat untuk melakukan jogging mengitari area kampung sekitar."

    "Celanamu yang semula celana pendek kamu ganti menggunakan celana training. Celana training bewarna biru yang sering dijumpai dimana saja."

    "Kemudian kamu mengambil jaket olahraga yang ada di dalam lemari pakaianmu."

    "Tidak lupa juga membawa botol minuman yang sebelumnya telah  diisi dengan air mineral."

    "Setelah siap, kamu keluar dari kamar kos kemudian duduk di teras depan kamar kos untuk memakai sepatu olahraga."

    scene bg town street 1 with dissolve

    "Selesai mengenakan sepatu olahraga, kamu tidak langsung memulai jogging namun melakukan pemanasan terlebih dahulu."

    mc normal jacket "Tu dua tiga empat lima enam tujuh delapan… "

    "Seperti pemanasan pada  umumnya, kamu melakukan pemanasan dan mulai berhitung."

    mc "Huhh tu dua tiga…."

    "Memutar kepala, memutar bahu, memutar lengan, memutar kaki, kamu melakukannya satu persatu."

    "Melakukan pemanasan sebelum berolahraga merupakan suatu hal yang tidak boleh dilupakan. Pemanasan sebelum berolahraga dapat mengurangi risiko terjadinya cedera."

    "Kamu melakukan pemanasan secara menyeluruh selama beberapa menit untuk menghindari dari cidera."

    scene bg town street 2 with fade
    
    "Setelah merasa cukup melakukan pemanasan, kamu keluar dari gerbang masuk kos dan mulai berlari kecil."

    "Kamu menengok ke arah atas dan melihat yang dipenuhi oleh awan."

    "Cuaca siang hari itu tidaklah panas dan tidak juga dingin. Meskipun langit dipenuhi awan, hangatnya sinar matahari tetap kamu rasakan pada tubuhmu."

    "Kamu berlari tanpa memikirkan rute lari sebelumnya, disetiap ada persimpangan jalan kamu memilih sesuai apa kata hatimu."

    "Karena sebelumnya kamu pernah mengitari area kampung sekitar, kamu sudah hafal jalanan di sekitar area kosmu. Sehingga kamu tidak kebingunan lagi arah jalan untuk pulang nanti."

    "Setelah sekian menit berlari, meskipun cuaca sedang mendukung keringat mulai bercur-curan dari tubuhmu. Bukan karena cuaca yang panas melainkan karena pakaian tebal yang kamu pakai."

    "Tidak lama kemudian, dengan keringat yang bercucur deras dari dalam tubuhmu. Kamu mulai merasakan rasa haus dalam setiap langkahmu."

    mc normal jacket "Huhhh huhhhh huhhh huhhhh huhhhh"

    mc "Kurang olahraga staminaku jadi kurang begini…."

    mc "Huhhh… Gilaa udah haus kehabisan stamina lagi…"

    "Merasa keletihan, kamu menghentikan larimu dan beristirahat di bangku yang ada di trotoar jalan. Kamu meminum air mineral yang sudah kamu siapkan sebelumnya. Kemudian kamu beristirahat untuk mengembalikan nafasmu yang terengah-engah."

    "Merasakan keletihan yang sudah mulai menghilang, kamu meneruskan larimu. Karena dirasa sudah cukup jauh berlari kamu memutuskan untuk kembali ke kos."

    "Setelah beberapa menit berlari, akhirnya kamu sampai di area kosmu."

    scene bg town street 1 with fade

    call jog

    "Hal pertama yang kamu lakukan setelah sampai di kosmu adalah melakukan pendinginan, sebelum kembali beristirahat hingga keringat selesai bercucuran dari dalam tubuhmu. "

    "Setelah itu kamu mandi untuk membersihkan tubuh dan menyudahi aktivitas di siang harimu."

    if day == 4:

        jump kos_krs4_night
    
    else:

        call screen mapUI
    
label sport_noonS2:

    "Untuk mengembalikan kebugaran tubuhmu, kamu memutuskan untuk melakukan senam lantai."
    call change_timephase
    call screen mapUI with dissolve
    return

label sport_noonS3:

    scene bg kampus graha

    "Ketika matahari sudah terlihat redup, kamu keluar dari kos dan menuju ke area graha di kampusmu."
    
    "Mengenakan sepatu lari dan celana training, kamu berniat berjogging di sore hari mengelilingi area kampus."

    call jog

    if day == 28:
        scene bg black with dissolve

        $placeKeys = 3

        call change_timephase

        show screen trans_screen with dissolve

        scene bg kos night with dissolve

        "Pukul 8 malam tepat, kamu baru saja terbangun dari tidurmu sejak sore tadi."

        "Sebenarnya kamu tidak merasakan mengantuk karena siang tadi kamu sudah cukup mengisi waktumu dengan tidur siang."

        "Hanya saja tidak banyak aktivitas yang kamu dapat lakukan sore hari ini, kemudian kamu memutuskan untuk merebahkan badanmu untuk sementara."

        "Kini dirimu sudah merasa capai merebahkan tubuhmu di tempat tidur, kamu merasa sudah saatnya dirimu untuk melakukan aktivitas lainnya."

        "Malam ini kamu memutuskan untuk:"

        jump choice_kota_night

    else:
        jump sleep

    return

#night
label sport_nightS1:

    "Kamu memutuskan untuk berolahraga malam, jogging di malam hari mengelilingi area kota."

    call jog

    if day == 28:
        jump day29
    else:
        jump sleep
  

label sport_nightS2:

    "Kamu mendapatkan ajakan untuk bermain futsal bersama dengan teman sekelasmu."

    call futsal
    if day == 28:
        jump day29
    else:
        jump sleep

  