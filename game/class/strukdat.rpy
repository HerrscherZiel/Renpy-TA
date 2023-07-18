
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

    scene bg campus class with dissolve

    call awal_kelas

    bn normal "Selamat pagi teman-teman, semoga hari ini kalian dalam keadaan baik-baik saja."

    bn "Pagi ini kita akan meneruskan pembahasan kita mengenai jenis-jenis Struktur Data."

    bn "Jika kemarin kita sudah membahasa mengenai jenis Struktur Data Array, Stack, dan Queue."

    bn "Kemudian kita akan membahas mengenai manfaat penggunaan struktur data."

    show screen strukdat_2_1 with fade

    bn "Langsung saja yang pertama ada Struktur Data Linked List."

    bn "Linked List berbeda dengan Array, Linked List menyimpan element list dilokasi yang tidak berdekatan melainkan terhubung melalui pointer yang ada."

    bn "Linked List merupakan sebuah rantai simpul dimana setiap simpul memiliki value data dan pointer untuk mengarahkan menuju lokasi list berikutnya. 
    Simpul pertama pada Linked List bernama Head, dan pointer pada simpul terakhir(Tail) biasanya NULL."

    bn "Linked List memiliki keuntungan yaitu mudahnya untuk menyisipkan atau menghapus data karena menggunakan alamat yang ada pada pointer, 
    namun Linked List tidak bisa digunakan untuk mengakses data secara acak."

    hide screen strukdat_2_1

    show screen strukdat_2_2 with fade

    bn "Kemudian ada Struktut Data Tree, Tree merupakan struktur data hierarkis. 
    Binary tree adalah jenis struktur tree di mana setiap node memiliki paling banyak dua child, yang disebut sebagai left child dan right child. Binary tree seringkali diimplementasikan menggunakan link."

    bn "Struktur Data Tree memiliki beberapa istilah seperti, Root atau Node paling awal(atas), Child merupakan node turunan dari node yang ada di atasnya, 
    Leaf merupakan Child node yang tidak memiliki Child lagi, dan Edge merupakan garis penghubung tiap Node."

    bn "Struktur Data Tree memiliki kemampuan untuk menggambarkan data secara struktural karena memiliki bentuk hirarki dari atas ke bawah."

    bn "Struktur Data Selanjutnya adalah Graph, merupakan salah satu struktur data non-linier yang yang memiliki kumpulan simpul terhingga dan terhubung karena memiliki sebuah keterkaitan antar simpul."

    bn "Graph biasanya memiliki sebuah Node(simpul) yang disebut dengan Verteks dan terhubung dengan Node lain menggunakan Edge(garis). 
    Semisal Edge X,Y berarti Node X terhubung dengan Node Y."

    bn "Penggunaan Graph membuat kita mudah untuk menemukan jalur-jalur yang terhubung kepada suatu Node 
    sehingga dapat membantu kita untuk memahami mengenai suatu permasalahan tertentu. Namun kompleksitas memory yang digunakan lebih besar."

    hide screen strukdat_2_2

    show screen strukdat_2_3 with fade
    
    bn "Sekiranya untuk jenis struktur data itu dulu, kita akan membahas lebih lanjut mengenai manfaat penggunaan Struktur Data."

    bn "Struktur data digunakan karena memiliki banyak manfaat, contohnya adalah:"

    bn "Mampu membuat pemrograman menjadi lebih mudah."

    bn "Penyimpanan dan penganturan data lebih efisien, rapi, dan terorganisir."

    bn "Dapat digunakan untuk mengelola sumber daya dan layanan semisal pada sistem operasi."

    bn "Bisa digunakan untuk pengindeksan objek yang tersimpan pada suatu basis data."

    bn "Searching atau pencarian lebih cepat dapat dilakukan menggunakan struktur data melalui indeks yang ada."

    bn "Dan masih banyak lagi manfaat penggunaan data yang dapat kita terima."

    bn "Namun karena sudah jam segini, mungkin saya tutup dahulu sekarang kita pindah ke sesi tanya jawab. "

    hide screen strukdat_2_3

    "Penjelasan melalui presentasi sudah usai, tanya jawab dilakukan untuk mengisi hingga waktu akhir dari pertemuan."

    bn normal "Sudah? Karena tidak ada pertanyaan lagi Ibu tutup untuk hari ini pada mata kuliah Struktur Data."

    bn "Sampai ketemu dipertemuan selanjutnya, dan terimakasih sudah berpartisipasi dalam kelas."

    t normal "Terimakasih bu…"

    t "Terimakasihh"

    "[bn] meninggalkan kelas, kelas pertama pada hari inipun berakhir."

    "Masih terdapat 2 kelas lain, kini mahasiswa sudah mulai keluar dari ruang kelas dan berpindah pada kelas selanjutnya."

    call attend_strukdat
    call attend_class

    jump basdat_2

label uts_strukdat:

    scene bg campus class with dissolve

    "Sama seperti hari sebelumnya, sesampainya di depan ruang kelas yang akan digunakan untuk UTS, kamu mengecek posisi tempat dudukmu terlebih dahulu."

    "Setelah memastikan dimana posisi tempat dudukmu, kamu memasuki ruang kelas."

    "Mungkin karena ini merupakan hari kedua UTS dijalankan, kamu merasakan beban dan rasa grogi yang lebih sedikit daripada kemarin."

    "Memasuki ruang kelas, kini pikiranmu lebih tenang dan siap untuk mengerjakan UTS yang ada."

    "Dosen pengawas juga sudah menunggu di dalam kelas dan menyuarakan instruksi-instruksi yang ada."

    scene bg campus class with fade

    "Sesuai yang diperintahkan dosen penjaga UTS, tas-tas mahasiswa diletakkan di depan kelas secara rapi."

    "Mahasiswa hanya perlu membawa peralatan tulis dan kartu ujian di bangku masing-masing."

    "Sama seperti sebelumnya, setelah kamu duduk kertas ujian tidak langsung dibagikan namun menunggu waktu yang telah ditentukan terlebih dahulu."

    "Ketika waktu sudah menunjukan jam mulai yang tertera pada soal ujian, dosen pengawas mulai berputar mengelilingi kelas sembari membacakan peraturan ujian kali ini."

    pa normal "Selamat pagi teman-teman pada pagi hari ini kita akan melanjutkan ujian tengah semester untuk mata kuliah Struktur Data."

    pa "Bapak harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    pa "Soal akan bapak bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    pa "Bapak harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Setelah menerima lembar soal dan lembar jawaban untuk UTS mata kuliah Struktur Data ini, kamu memejamkan matamu sebentar berdoa dan mempersiapkan diri untuk mengerjakan."

    "Merasa cukup dengan persiapanmu, kamu mulai mengisi biodata pada lembar jawab sebelum mulai menelaah soal-soal UTS yang ada."

    "(Pada {b}game ini{/b} UTS hanya akan memiliki 5 soal pilihan ganda!)"

    "(Setiap pertanyaan akan ditampilkan dan bisa dijawab dalam waktu 90 detik)"

    "(Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya)"

    "(Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal)"

    "(Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.)"

    "(Perlu diketahui UTS pada kampus dapat dilaksankan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.)"

    "(Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.)"

    menu: 
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UTS."
    "1. FIFO atau First In First Out merupakan sebuah konsep yang digunakan pada struktur data?"
    menu:
        "A. Tree.":
            "A. Tree."
        "B. Stack.":
            "B. Stack."
        "C. Queue.":
            "C. Queue."
            $a_strukdatTS +=20
        "D. Linked List.":
            "D. Linked List."
        "E. Graph.":
            "E. Graph."
    "2. Pada struktur data manakah yang menggunakan konsep dimana data yang terlebih dahulu keluar adalah data yang terakhir masuk?"
    menu:
        "A. Tree.":
            "A. Tree."
        "B. Stack.":
            "B. Stack."
            $a_strukdatTS +=20
        "C. Queue.":
            "C. Queue."
        "D. Linked List.":
            "D. Linked List."
        "E. Graph.":
            "E. Graph."
    "3. Apa yang dimaksud node Leaf pada struktur data Tree?"
    menu:
        "A. Node yang berada pada paling atas pada tree.":
            "A. Node yang berada pada paling atas pada tree."
        "B. Node yang berada pada posisi paling bawah pada tree.":
            "B. Node yang berada pada posisi paling bawah pada tree."
        "C. Node turunan dari node yang ada diatasnya.":
            "C. Node turunan dari node yang ada diatasnya."
        "D. Merupakan child node yang tidak memiliki child lagi.":
            "D. Merupakan child node yang tidak memiliki child lagi."
            $a_strukdatTS +=20
        "E. Garis penghubung tiap node.":
            "E. Garis penghubung tiap node."
    "4. (...) Merupakan istilah untuk garis yang menghubungkan suatu node ke node yang lain pada struktur data Graph?"
    menu:    
        "A. Verteks.":
            "A. Verteks."
        "B. Edge.":
            "B. Edge."
            $a_strukdatTS +=20
        "C. Simpul.":
            "C. Simpul."
        "D. List.":
            "D. List."
        "E. Graph List.":
            "E. Graph List."
    "5. Manakah dibawah ini yang bukan merupakan keuntungan penggunaan struktur data?"
    menu:      
        "A. Membuat penyimpanan dan pengaturan data lebih rapi, efisien, dan terorganisir.":
            "A. Membuat penyimpanan dan pengaturan data lebih rapi, efisien, dan terorganisir."
        "B. Pencarian dapat dilakukan secara lebih cepat ketika mengaplikasikan struktur data.":
            "B. Pencarian dapat dilakukan secara lebih cepat ketika mengaplikasikan struktur data.."
        "C. Bisa digunakan untuk menghindari pengindeksan yang akan memperlambat pencarian.":
            "C. Bisa digunakan untuk menghindari pengindeksan yang akan memperlambat pencarian."
            $a_strukdatTS +=20
        "D. Dapat digunakan untuk mengelola sumber daya dan layanan semisal pada sistem operasi.":
            "D. Dapat digunakan untuk mengelola sumber daya dan layanan semisal pada sistem operasi."
        "E. Mampu membuat pemrograman lebih mudah.":
            "E. Mampu membuat pemrograman lebih mudah."

    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengumpulkan kertas ujianmu, kamu memasukan barang-barangmu pada tas yang sebelumnya dikelompokan dengan rapi di depan kelas."

    "Kemudian kamu segera keluar dari dalam kelas. Di luar sebelumnya sudah ada beberapa mahasiswa yang keluar lebih dahulu sebelum dirimu."

    "Kamu menghabiskan waktu dengan mengobrol dengan temanmu sembari membaca materi mata kuliah yang akan diujikan setelahnya."

    jump uts_basdat

            
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