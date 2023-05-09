
default a_strukdatA = 0
default a_strukdatT = 0
default a_strukdatC = 0
default a_strukdatTS = 0
default a_strukdatAS = 0
default a_strukdatN = 0

label strukdat_1:

    scene bg campus class with dissolve

    "Setelah sampai di ruang kelas yang akan digunakan untuk pembelajaran pagi hari ini, kamu segera masuk ke ruang kelas tersebut."

    "Di dalam kelas, sudah ramai diisi oleh teman-teman sekelasmu."

    "Memasuki kelas, seperti biasa kamu memilih posisi tempat duduk yang berada di barisan tengah dan dekat dengan jendela."

    "Tak lama setelah kamu menempati tempat dudukmu, [bn] masuk ke dalam ruang kelas."

    bn normal "Selamat pagi teman-teman…"

    t normal "Selamat pagi bu…"

    bn "Sebelumnya kalau tidak salah, sudah pernah ketemu saya ya?"

    r normal2 "Sudah bu, kemarin sewaktu mata kuliah Algoritma Pemrograman."

    bn "Oh iya-iya…"

    bn "Jadi pada pagi hari ini ibu akan mengajar mata kuliah Struktur Data."

    bn "Pada pertemuan pagi hari ini, ibu akan menerangkan mengenai pengertian struktur data dan contoh-contohnya."

    show screen strukdat_1_1 with dissolve

    bn "Kita mulai saja dari pengertian struktur data, struktur data adalah sebuah metode atau cara dalam menyusun, mengatur, atau menyimpan data dalam suatu komputer agar dapat dimanfaatkan secara lebih efektif dan efisien."

    bn "Sementara pengertian data sendiri adalah sebuah fakta atau keterangan pasti yang dapat direpresentasikan sebagai symbol, gambar, teks, suara, atau sinyal."

    bn "Pagi hari ini saya akan memberikan contoh mengenai 3 struktur data, yaitu array, stack, dan queue"

    bn "Array merupakan Array adalah kumpulan item data yang disimpan di lokasi memori yang berdekatan. 
    Tujuannya adalah untuk menyimpan beberapa item dari jenis yang sama secara bersama-sama."
    
    bn "Hal ini memudahkan untuk menghitung posisi setiap elemen hanya dengan menambahkan offset ke nilai dasar, yaitu lokasi memori elemen pertama array."
    
    # Show array

    hide screen strukdat_1_1

    show screen strukdat_1_2 with fade
    
    bn "Lalu terdapat stack, stack merupakan struktur data yang bekerja atau berfungsi menggunakan konsep LIFO(Last in First Out). 
    Kita dapat membayangkan semisal pada sebuah tumpukan buku, dimana buku terakhir yang ditumpuk maka akan dapat diambil atau dikeluarkan terlebih dahulu." 
    
    bn "Sementara buku yang pertama dimasukan ke dalam sebuah stack baru dapat dikeluarkan terakhir FILO(First In Last Out)."

    bn "Sehingga ketika kita menggunakan Stack maka data yang dapat kita akses adalah data yang berada pada posisi paling atas dari tumpukan."

    bn "dan sewaktu kita menambah data, maka data tersebut akan berada pada posisi paling atas pada tumpukan."

    # Show stack

    bn "Kemudian struktur data queue, berbeda dengan stack struktur data queue berfungsi menggunakan konsep urutan operasi First In First Out (FIFO) atau elemen data yang lebih dulu ditambahkan juga akan keluar lebih dulu. "
    
    bn "Sesuai namanya, kita dapat membayangkan semisal antrian ketika kita akan membeli sesuatu. 
    Orang yang pertama mengantri akan dapat menyelesaikan transaksinya terlebih dahulu, kemudian akan berurutan sampai pada antrian terakhir."
    
    bn "Dalam struktur queue, data dimasukkan pada salah satu ujung dan dihapus dari ujung lainnya."
    
    # show queue

    bn "Kemudian menggambarkan dan memberi contoh pada ketika struktur data yang baru saja dijelaskan pada papan tulis."

    "Kamu dan teman sekelasmu diam, mencatat dan memperhatikan apa yang dijelaskan oleh [bn]."

    hide screen strukdat_1_2

    scene bg campus class with fade

    bn normal "Tidak terasa pertemuan hari ini sudah selesai, saya akan melanjutkan mengenai contoh struktur data pada pertemuan selanjutnya."

    bn "Terimakasih sudah hadir dan mengikuti pertemuan pada pagi hari ini, sampai bertemu pada kesempatan selanjutnya."

    t normal "Terimakasih buu!!!"

    r normal2 "Terimakasih…."

    mc normal jacket "Terimakasih…."

    "Setelah [bn] pergi meninggalkan ruang kelas, kamu dan teman sekelasmu mengemas barang-barang dan berpindah pada ruang kelas berikutnya."

    call attend_strukdat
    call attend_class
    
    jump basdat_1

label strukdat_2:

    "Strukdat 2"

    jump basdat_2

label strukdat_3:

    "Strukdat 3"

    jump basdat_3

label strukdat_4:

    "Strukdat 4"

    jump basdat_4

label attend_strukdat:

    $ a_strukdatA +=1
    $ a_strukdatN +=8

    return