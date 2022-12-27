
label first_boarding_house:

    $ firstKos = False
    $ timephase += 1

    show day1 kosnight:
        xalign 0.5 yalign 0.5
    with dissolve

    pause 2.0

    scene bg kos night
    with fade

    show screen days_screen
    show screen stats_screen 
    
    "Malam hari setelah rangkaian kegiatan orientasi berakhir, kamu merebahkan diri di kasur kosmu."

    "Sebelum memejamkan mata, kamu meluangkan waktu untuk membuka ponselmu."

    "Kamu melihat banyak notifikasi dari aplikasi LANE, kamu memutuskan untuk membukanya."

    "Notifikasi yang ada berasal dari grup chat angkatanmu. Setelah membaca beberapa baris chat, dari berbagai macam topik chat yang ada kamu mengikuti percakapan mengenai bimbingan dengan dosen pembimbing."

    show phone groupchat 
    with moveinbottom

    "Beberapa mahasiswa di angkatanmu membicarakan untuk melakukan bimbingan dengan dosen pembimbing mereka."

    "Beberapa dari mereka bahkan ada yang sudah menghubungi dosen pembimbing masing-masing untuk bertemu."

    "Pada saat melakukan bimbingan sendiri, mahasiswa dapat menanyakan berbagai macam hal seputar perkuliahan."

    "Mahasiswa dapat menyakan mengenai prospek dari program studi, peluang pekerjaan, jalannya perkuliahan, pemilihan mata kuliah, mata kuliah, informasi mengenai kampus, dan pertanyaan seputar perkuliahan yang lain."

    "Mengetahui isi chat yang ada dalam grup angkatanmu, kamu juga memutuskan untuk menemui dosen pembimbingmu untuk melakukan bimbingan."

    "Selain itu kamu juga ingin menanyakan mengenai pengambilan SKS pada dosen pembimbingmu."

    "Kamu mengingat perkataan pemandumu selama kegiatan orientasi."

    mc normal2 "Sebelum memulai kegiatan perkuliahan, kalian nantinya harus melakukan pengambilan SKS terlebih dahulu setiap awal semesternya."

    mc  "Dalam pengambilan SKS nantinya kalian akan memilih kode mata kuliah yang akan kalian dapatkan selama satu semester."

    mc  "Pilihan mata kuliah tergantung pada apa yang sudah dipilihakan atau dipaketkan oleh kampus yang sifatnya wajib untuk diambil. Meskipun begitu terkadang kalian juga dapat memilih mata kuliah tidak wajib."

    mc  "Lalu kalian juga…"

    mc  "Bicara apalagi ya waktu itu… lupa aku."

    mc  "UAHHHHHH… ngantuk."

    "Kamu meletakan ponselmu, kemudian mematikan lampu kamarmu"

    hide phone groupchat
    with moveoutbottom

    show bg kos dark

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

