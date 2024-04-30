
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

    call attend_strukdat from _call_attend_strukdat
    call attend_class from _call_attend_class_24
    
    jump basdat_1

label strukdat_2:

    scene bg campus class with dissolve

    call awal_kelas from _call_awal_kelas_5

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

    call attend_strukdat from _call_attend_strukdat_1
    call attend_class from _call_attend_class_25

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

    scene bg campus class with dissolve

    "[bn] memasuki ruang kelas beberapa menit setelah dirimu menyandarkan tubuh pada bangkumu."

    "Ruang kelas masih belum terisi penuh oleh mahasiswa, hanya sekitar setengah dari temanmu yang sudah berada dalam ruang kelas."

    "[bn] duduk di bangku dosen, dan mempersiapkan laptop dan materi yang akan disampaikan pada pagi hari ini."

    "Kelas pagi hari ini akan dimulai ketika mahasiswa yang hadir dirasa sudah cukup banyak."

    "Masih ada beberapa menit lagi untuk menunggu temanmu yang lain memasuki ruang kelas."

    "Satu persatu mahasiswa memasuki ruang kelas, sebelum pada akhirnya [bn] memulai perkuliahan pagi hari ini."

    scene bg campus class with fade

    bn normal "Selamat pagi teman-teman kita bertemu lagi setelah minggu kemarin melakukan ujian tengah semester."

    bn "Pagi ini kita bertemu lagi pada mata kuliah Struktur data pertemuan ke-3, pada pertemuan hari ini kita akan membahas mengenai tipe data."

    bn "Sebenarnya pembahasan mengenai tipe data ini seharusnya kita bahas pada awal pertemuan, tapi ya mungkin sudah dipelajari juga pada mata kuliah lain."

    bn "Pagi hari ini juga saya tidak sampai selesai ya, mohon maaf karena ada urusan mendadak jadi harus pergi."

    t normal "Baik buuu."

    bn "Kita mulai saja ya, karena tadi juga sudah lumayan lama menunggu teman-teman, supaya tidak tambah molor juga."

    "[bn] menyalakan proyektor, dan materi yang akan dibahas pada pagi hari ini terlihat di depan kelas."

    bn "Sebelumnya, apa itu tipe data?"

    show screen strukdat_3_1 with fade

    bn class "Tipe data dalam pemrograman merupakan sebuah konsep pengklasifikasian sebuah data dimana klasifikasi tersebut mampu menggambarkan jenis nilai yang dapat disimpan atau dioperasikan dalam sebuah program."

    bn "Ada banyak macam tipe data yang terdapat dalam pemrograman, dibawah ini merupakan sedikit contoh dan pembahasan mengenai tipe data."

    bn "Pada pagi hari ini ibu akan sedikit membahas mengenai tipe data Bilangan bulat, pecahan yang digunakan untuk bilangan."

    bn "Kemudian ada tipe data teks, yang digunakan menyimpan data teks."

    bn "Boolean merupakan tipe data yang dapat digunakan untuk menentukan 'True' dan 'False'"

    bn "Kemudian masih ada tipe data lain seperti 'Date and Time' dan 'Strktur'"

    hide screen strukdat_3_1

    show screen strukdat_3_2 with fade

    bn  "1. Tipe data bilangan bulat, terdapat beberapa tipe data yang termasuk tipe data bilangan bulat seperti tipe data byte, short, integer, dan long."

    bn "Tipe data byte merupakan tipe data bilangan bulat dengan rentang paling kecil (8-bit) diantara tipe data bilangan bulat lainnya, data type ini akan berguna ketika digunakan untuk menyimpan memori dalam array yang besar."

    bn "Tipe data short, merupakan tipe data bilangan bulat yang memiliki kapasitas 16-bit, yang berarti tipe data short memiliki rentang yang lebih besar dari tipe data byte namun lebih kecil dari integer dan long."

    bn "Tipe data integer, Integer atau singkatnya int merupakan tipe data yang paling umum digunakan dalam pemrograman dan merepresentasikan bilangan bulat dalam pemrograman. "

    bn "Tipe data long, tipe data ini merupakan tipe data bilangan bulat yang digunakan untuk menyimpan bilangan bulat yang lebih besar daripada range yang dapat digunakan pada tipe data integer."

    bn "Itu penjelasan singkat untuk tipe data bilangan bulat, lalu kita akan berlanjut pada tipe data yang selanjutnya."

    hide screen strukdat_3_2

    show screen strukdat_3_3 with fade

    bn "Kemudian 2. Tipe data pecahan, sesuai namanya jenis tipe data yang satu ini mampu digunakan untuk menampung data yang bernilai pecahan atau desimal."

    bn "Tipe data float, tipe data ini merupakan tipe data yang mampu menyimpan bilangan pecahan. Floats memiliki presisi terbatas, yang berarti dalam beberapa kasus, ada pembulatan dan potensi kehilangan presisi saat melakukan operasi matematika yang kompleks."

    bn "Tipe data double, merupakan tipe data yang mampu menyimpan bilangan pecahan dengan tingkat presisi lebih tinggi daripada tipe data float, namun juga menggunakan memori lebih banyak."

    bn "Lalu jenis tipe data yang selanjutnya adalah,"

    hide screen strukdat_3_3

    show screen strukdat_3_4 with fade

    bn "3. Tipe data teks, tipe data dengan jenis ini biasa digunakan untuk menyimpan data teks ataupun karakter, disini saya akan menjelaskan mengenai tipe data char dan string."

    bn "Tipe data Char, tipe data ini merupakan tipe data yang digunakan untuk menyimpan karakter tunggal, seperti karakter ‘A’,‘@’, dan semacamnya."

    bn "Tipe data String, tipe data string umumnya digunakan untuk menyimpan data yang bertipe teks, baik dari satu karakter maupun sampai banyak kata."

    bn "Sebenarnya masih ada beberapa tipe data lain yang dapat digunakan untuk menyimpan data tipe teks, namun untuk hari ini cukup dua itu saja dulu."

    hide screen strukdat_3_4

    show screen strukdat_3_5 with fade

    bn "4. Jenis tipe data yang berikutnya adalah tipe data logika yaitu Boolean, tipe data ini hanya memiliki nilai ‘True’ dan ‘False’. "

    bn "Tipe data boolean sangat berguna ketika kita akan mengambilkan sebuah keputusan, dengan menentukan apakah itu ‘True’ atau ‘False’."

    bn "Tipe data boolean menjadi tipe data pilihan ketika kita ingin memutuskan suatu hal yang hanya memiliki dua kemungkinan."

    bn "Kemudian tipe data yang selanjutnya adalah 'Date and Time'."

    hide screen strukdat_3_5

    show screen strukdat_3_6 with fade

    bn "5. Tipe data Date and Time, merupakan jenis tipe data khusus yang digunakan untuk menyimpan sebuah data tanggal dan waktu."

    bn "Tipe data Date and Time dapat mencakup informasi seperti tahun, bulan, hari, jam, menit, detik, dan bahkan milidetik."

    bn "Date and Time sering digunakan dalam aplikasi yang melibatkan jadwal, penanggalan, pemantauan waktu, dan banyak aplikasi lainnya. Contohnya adalah pemakaiannya dalam sistem penyewaan dalam pariwisata dan lain sebagainya."

    hide screen strukdat_3_6

    show screen strukdat_3_7 with fade

    bn "6. Tipe data yang selanjutnya adalah tipe data struktur, ya tipe data yang dimaksud adalah apa yang sebelumnya kita pelajari dalam mata kuliah ini."

    bn "Dalam pemrograman, merujuk pada pengorganisasian data menjadi unit yang lebih besar dan kompleks yang terdiri dari beberapa elemen atau atribut. "

    bn "Tipe data terstruktur digunakan untuk merepresentasikan entitas yang lebih kompleks dan memiliki banyak properti atau atribut yang berbeda."

    bn "Tipe data seperti array merupakan salah satu contoh tipe data struktur. Tipe data ini dapat kita gunakan untuk menyimpan sekumpulan nilai atau elemen yang serupa dalam satu variabel.."

    bn  "Hmmm mungkin hari ini sampai disini saja ya."

    bn "Sebelum saya tutup akan saya sedikit perlihatkan contoh dari tipe data yang ada."

    hide screen strukdat_3_7
    
    "[bn] kemudian mengganti slide ke slide berikutnya yang berisi contoh-contoh dari tipe data yang baru saja diterangkan."

    "Teman-temanmu mengamati sambil sesekali melemparkan pertanyaan kepada [bn]."

    "Tanya jawab terjadi selama beberapa menit sebelum [bn] mengumumkan sebuah informasi untuk pertemuan minggu depan."

    scene bg campus class with fade

    bn normal "Oh iya, sebelum ibu tutup ada yang perlu ibu sampaikan."

    bn "Untuk pertemuan minggu depan, kita isi dengan quiz ya teman-teman."

    t normal "Nooooo"

    t "Quiz lagi huhuuu…"

    t "Yahh anggap aja latihan ujian akhir nanti."

    bn "Hahaha… iya anggap saja buat latihan ujian akhir semester nanti."

    bn "Untuk materi, dimulai dari pertemuan yang pertama ya teman-teman."

    bn "Mungkin masih ada yang ingat apa saja?"

    r normal2 "Umm… Pengertian struktur data.., struktur data, array, stack, queue, terus…"

    bn "Ya itu benar, apa lagi ada yang bisa bantu menjawab?"

    menu:

        "Struktur data Tree, Linked List, dan Graph":
            mc normal jacket "Struktur data Tree, Linked List, dan Graph bu?"

            bn "Iya benar, itu semua yang akan menjadi materi quiz dan ujian akhir semester nanti ya."

            $ a_strukdatC += 5

        "………":

            t "Struktur data Tree, Graph terus yang satu lagi apa ya?"

            bn "Hayo apalagi kemarin yang sudah dibahas?"

            t "Linked list bu?"

            bn "Iya benar, itu semua yang akan menjadi materi quiz dan ujian akhir semester nanti ya."

    bn "Ingat ya itu semua materi yang digunakan, untuk hari ini cukup sampai sini saja."

    bn "Karena Ibu ada keperluan mendesak lain, ibu akhiri pertemuan siang hari ini."

    bn "Terimakasih atas partisipasinya, dan sampai jumpa pada pertemuan selanjutnya teman-teman."

    t "Terimakasih bu…"

    t "Terimakasihhh"

    "[bn] meninggalkan kelas, tanda kelas pertama pada hari ini telah berakhir."

    "Masih terdapat 2 kelas lain pada hari ini, mahasiswa mulai keluar dari ruang kelas dan berpindah ke kelas selanjutnya."

    call attend_strukdat from _call_attend_strukdat_2
    call attend_class from _call_attend_class_26

    jump basdat_3

label strukdat_4:

    scene bg campus class with dissolve

    "Memasuki ruang kelas, kamu teringat pertemuan pertama pada hari ini adalah mata kuliah struktur data yang akan diisi dengan quiz."

    "Di dalam ruang kelas sudah terdapat banyak teman-temanmu yang sedang membuka buku catatan mereka, atau sedang menatap layar HP mereka dengan serius."

    "Setelah menempati tempat dudukmu, kamu langsung mempersiapkan dirimu untuk quiz yang sebentar lagi akan kamu kerjakan."

    "Selama beberapa menit kamu membaca materi yang terdapat pada internet, akhirnya [bn] memasuki ruang kelas."

    bn normal "Selamat siang teman-teman, kita bertemu lagi pada pagi hari ini."

    bn "Sesuai apa yang telah saya informasikan sebelumnya, hari ini pertemuan akan diisi dengan quiz. "

    t normal "Tidak susah kan bu quiznya?"

    bn "Ya kalau kalian memperhatikan sewaktu pertemuan harusnya enggak ya."

    bn "Kalau kalian engga belajar ya beda lagi dong."

    t "Semoga mudah ya bu hahahaha"

    r normal2 "Berapa soal bu quiznya?"

    bn "Cukup 5 soal saja, itu untuk menguji apakah kalian memahami apa yang diajarkan atau tidak."

    t "Yeyyy cuma lima aja."

    bn "Mungkin langsung saja ya untuk menyingkat waktu, ibu sudah mempersiapkan soal quiznya di laman ini."

    "[bn] menulis alamat sebuah laman pada whiteboard yang berisi soal-soal untuk quiz pada siang hari ini."

    bn "Kalian kerjakan saja pada kertas, tulis nama dan NIM kalian lalu kumpulkan ketika jam telah usai ya."

    "Kamu membuka alamat laman yang diberikan menggunakan HPmu, setelah membuka laman tersebut kamu mulai menyiapkan secarik kertas dan bolpoinmu."

    "Kamu mulai mengerjakan soal yang terdapat pada layar HPmu."

    show screen strukdat_4_0 with fade

    "Seperti yang dikatakan oleh [bn] terdapat 5 soal yang ada pada lembar soal."

    "Soal pertama yang terdapat lembar soal adalah:"

    "1. Apakah yang dimaksud dengan Struktur Data dalam pemrograman?"

    show screen strukdat_4_1 with dissolve

    menu:
        "a. Sebuah metode atau cara dalam menyusun, mengatur, dan menyimpan data pada komputer agar menjadi lebih efektif dan efisien":

            "a. Sebuah metode dalam menyusun, mengatur, dan menyimpan data pada komputer agar menjadi lebih efektif dan efisien."
            $a_strukdatC += 2

            mc normal jacket "Yupps ini jawabannya."

        "b. Salah satu bahasa pemrograman yang saat ini digunakan pada semua bidang kehidupan.":

            "b. Salah satu bahasa pemrograman yang saat ini digunakan pada semua bidang kehidupan."

            mc "Kayaknya bukan yang ini deh, tapi apa ya…"

        "c. Sebuah program yang terstruktur dan berisi kumpulan data-data komputer":

            "c. Sebuah program yang terstruktur dan berisi kumpulan data-data komputer"

            mc "Fix ini sih jawabannya."

        "d. Sebuah metode yang dapat digunakan untuk menampilkan grafik data secara menarik":
            
            "d. Sebuah metode yang dapat digunakan untuk menampilkan grafik data secara menarik"

            mc "Jawabannya yang ini nihh"

    "Selesai menjawab pertanyaan pertama, kamu kemudian melanjutkan ke pertanyaan kedua."

    hide screen strukdat_4_1 with dissolve

    "2. 	Struktur data yang memiliki bentuk hierarkis adalah struktur data?"

    mc "Hmmm yang dimaksud hierarkis itu apa ya?"

    show screen strukdat_4_2 with dissolve

    menu:

        "Array":

            "a. Array"

            mc "Array itu yang indexnya dimulai dari 0 kan, itu ya yang berarti ."

        "Linked List":

            "b. Linked list"

            mc "Feeling ku yang ini sihh…"

        "Tree":

            "c. Tree"
            $a_strukdatC += 2

            mc "Tree kan kalau gak salah dari node paling atas terus ke node yang bawah atau node anaknya. "

        "Queue":

            "d. Queue"

            mc "Hierarkis berarti harus urut gitu kan."

    "Menjawab pertanyaan nomor 2, kamu berlanjut ke pertanyaan berikutnya."

    hide screen strukdat_4_2 with dissolve

    "3. Untuk menyimpan data bilangan bernilai -3.4 , 4.4 , dan 5.0 kita bisa menggunakan tipe data?"

    show screen strukdat_4_3 with dissolve

    menu:
    
        "Float, Int, Double":

            "a. Float, Int, Double"

            mc "Hmmm kayaknya yang ini sih."

        "Float dan Int":

            "b. Float dan Int"

            mc "Setahuku float bisa desimal, int bisa gak ya?"

        "Int dan Double":

            "c. Int dan Double"

            mc "Cuma tahu doublenya aja, int bisa desimal gak ya?."

        "Float dan Double":

            "d. Float dan Double"
            $a_strukdatC += 2

            mc "Float dan double sih yang buat desimal, int bilangan bulat."

    "Setelah menjawab pertanyaan nomor 3, tinggal 2 pertanyaan lagi yang tersisa."

    "Merasa ingin segera menyelesaikan quiz, kamu meneruskan menjawab pertanyaan no 4."

    hide screen strukdat_4_3 with dissolve

    "4. 	Manakah dibawah ini tipe data yang baik digunakan untuk mengambil keputusan dan hanya memiliki nilai ‘True’ dan ‘False’?"

    show screen strukdat_4_4 with dissolve

    menu:

        "Boolean":

            "a. Boolean"
            $a_strukdatC += 2

            mc "Iya, aku ingat boolean cuma bisa bernilai ‘True’ dan ‘False’"

        "Date and Time":

            "b. Date and Time"

            mc "Kayaknya bukan yang ini deh…."

        "Char":

            "c. Char"

            mc "Apa yang ini ya? Kalau gak salah char kan hanya bisa diisi satu karakter."

        "String":

            "d. String"

            mc "String bisa buat nyimpen banyak kata kan… berarti baik buat mengambil keputusan nih."

    "Selesai menjawab, kini ada satu pertanyaan lagi yang tersisa sebelum kamu menyelesaikan quiz pada siang hari ini."

    hide screen strukdat_4_4 with dissolve

    "5. Mengapa kita sebaiknya menggunakan tipe data yang tepat dalam sistem kita, kecuali?"

    show screen strukdat_4_5 with dissolve

    menu:

        "Tipe data yang tepat dapat mempermudah dalam pemrograman.":

            "a. Tipe data yang tepat dapat mempermudah dalam pemrograman."

            mc "Kayaknya bukan yang ini deh, tipe data ga mempermudah pemrograman."

        "Efisiensi penggunaan memori.":

            "b. Efisiensi penggunaan memori."

            mc "Setahuku tipe data pemakaian memorinya sama semua…	"

        "Kompatibilitas pada kode yang sedang dikembangkan.":

            "c. Kompatibilitas pada kode yang sedang dikembangkan."

            mc "Emang kalo tipe datanya salah jadi gabisa gitu kah?"

        "Meningkatkan estetika program yang dikembangkan.":

            "d. Meningkatkan estetika program yang dikembangkan."
            $a_strukdatC += 2

            mc "Estetika? Kan cuma dikodenya, bukan programnnya."

    "Dengan menjawab pertanyaan terakhir, kini semua soal yang ada pada lembar soal telah kamu jawab."

    "Kamu telah menyelesaikan quiz mata kuliah struktur data pada pagi hari ini."

    hide screen strukdat_4_5 with dissolve

    hide screen strukdat_4_0 with dissolve

    "Kamu berdiri dan beranjak dari bangkumu kemudian berjalan untuk mengumpulkan lembar jawabanmu."

    "Tidak lupa, sebelum mengumpulkan lembar jawabanmu kamu tuliskan nama dan NIMmu pada lembar jawaban."

    "Kamu mengamati teman-temanmu sebagian besar telah menyelesaikan quiz mereka, hanya tinggal beberapa temanmu saja yang masih sibuk menulis jawaban pada lembar jawab."

    "Setelah mengumpulkan lembar jawaban, kamu kembali menuju bangkumu dan menunggu hingga semua temanmu telah menyelesaikan quiz yang diberikan."

    scene bg campus class with fade

    "Kurang lebih 15 menit, semua mahasiswa telah menyelesaikan quiz yang diberikan. Kini [bn] sedang menjelaskan mengenai materi yang akan digunakan sebagai bahan soal untuk ujian akhir semester."

    bn normal "Teman-teman, mungkin seperti yang telah kalian ketahui, materi yang akan digunakan sebagai materi ujian akhir semester adalah semua materi yang telah diajarkan ya."

    bn "Soal ujian tengah semester kemarin dan soal quiz pada pagi hari ini bisa ibu jadikan soal untuk ujian nanti."

    bn "Jadi selamat belajarnya ya teman-teman."

    t normal "Wahhh lumayan banyak dong."

    t "Hmmm berarti ketambahan materi tipe data itu…"

    t "Kalau soal yang tadi sih aku lumayan bisa, semoga aja mirip-mirip."

    r normal2 "Berarti tinggal ringkasan yang dulu ditambah ringkasan pertemuan 3 aja ya"

    bn "Kalau begitu ibu tutup ya, pertemuan hari ini. Selamat belajar dan semoga mendapatkan hasil yang diinginkan pada ujian nanti."

    bn "Terimakasih sudah mengikuti kelas sampai pertemuan kali ini, sampai jumpa pada pertemuan selanjutnya teman-teman."

    t "Terimakasih bu."

    t "Terimakasihhh"

    r "Terimakasih juga buu."

    "Dengan begitu kelas ditutup dan pembelajaran untuk hari ini telah usai. Kamu keluar dari ruangan kelas dan bersiap untuk kelas berikutnya."

    call attend_strukdat from _call_attend_strukdat_3
    call attend_class from _call_attend_class_27

    jump basdat_4

label uas_strukdat:

    scene bg campus upper hall with fade

    "Hari ini merupakan hari keduamu dalam minggu ujian akhir, suasana setelah memasuki gedung kampus tidak jauh berbeda dengan hari sebelumnya."

    "Terlihat banyak mahasiswa-mahasiswa lain baik dari program studimu maupun program studi lainnya telah hadir dan duduk berjajar di area dalam kampus."

    "Kebanyakan dari mereka sedang memegang kertas-kertas maupun handphone masing-masing dan tampak sedang fokus membaca materi perkuliahan."

    "Meskipun ada juga yang hanya duduk dan mengobrol dengan orang disebelah mereka."

    "Kamu berjalan menuju kelas dimana ujian akhir mata kuliah Strukdat akan dilaksanakan sambil melihat-lihat kondisi di sekitaran ruang kelas ujian."

    "Setelah sampai di area ruangan kelas yang akan digunakan untuk ujian akhir Strukdat, teman-teman sekelasmu telah ramai duduk mengelompok dan membaca catatan mereka masing-masing."

    r normal2 "Pagi [name]!"

    mc normal jacket "Pagi [r], gimana belajarnya??"

    r "Sudah siap lah ya, gimana kamu? Udah siap belum?"

    mc "Ya siap-siap engga juga sihhh…."

    r "Seperti biasanya berarti hahahaha"

    t normal 'Pagi [r], pagi [name]!'

    mc "Halooo, pagiii"

    r "Pagiiii"

    "Salah satu teman sekelasmu baru saja datang dan menyapa kalian berdua."

    t "[r] mau tanya dongg, soal materi ujian nanti…."

    r "Tanya apa? Sini cobaa…"

    t "Ini nihh… materi ini…."

    "Teman sekelasmu itu langsung duduk disebelah [r] dan mengeluarkan kertas catatan dari dalam ranselnya."

    r "[name] sini sekalian kalo mau ikut bahas materi?"

    t "Iyaa sinii ajaa…"

    mc "Engga lah, aku baca-baca sendiri ajaa…."

    r "Okeyyyy"

    "Kamu yang masih berdiri kemudian duduk dan bersandar pada tembok ruang kelas, kemudian melihat jam digital yang ada pada HPmu."

    "Waktu telah menunjukkan pukul 7.25, masih tersisa lima menit sebelum pintu ruang kelas ujian akhir dibuka. "

    "Merasa sudah cukup siap untuk melakukan ujian akhir, kamu hanya duduk diam sambil mengingat-ingat materi yang akan diujikan."

    scene bg black

    "Lima menit berlalu dengan cepat, kini dosen pengawas ujian telah membuka pintu ruang ujian. [bn] yang akan menjadi dosen pengawas ujian pada ujian Strukdat kali ini."

    "Seperti ujian tengah semester lalu, posisi tempat duduk untuk ujian telah ditentukan dan terlihat pada kertas yang ditempelkan pada pintu ruang kelas."

    "Setelah melihat dimana kamu akan duduk, kamu memasuki ruang kelas untuk melaksanakan ujian akhir pertamamu di hari kedua."

    scene bg campus class with dissolve

    pause 1.5

    "Memasuki ruang kelas ujian, [bn] memberi instruksi kepada mahasiswa untuk meletakkan tas atau ransel di depan kelas secara rapi. Lalu hanya membawa peralatan tulis dan kartu mahasiswa ke bangku ujian."

    "Setelah meletakan tasmu di depan ruangan, kamu mengambil peralatan tulismu sebelum berjalan menuju bangku ujian."

    "Terlihat lembar jawab ujian sudah diletakan pada masing-masing bangku ujian."

    "Kemudian ketika semua bangku ujian telah terisi oleh peserta ujian, [bn] lalu menjelaskan peraturan ujian."

    "Tidak ada yang berbeda seperti peraturan-peraturan ujian pada umumnya."

    "Selesai menjelaskan, beberapa menit kemudian soal ujian disebarkan kepada seluruh peserta yang ada."

    "Kamu menerima beberapa soal ujian dari bangku yang ada di depanmu, setelah mengambil salah satu soal ujian, kamu meneruskan pembagian soal-soal ujian lainnya ke bangku yang ada di belakangmu."

    bn normal "Sekarang sudah memasuki waktu ujian, kalian bisa mulai mengerjakan soal yang ada pada lembar jawaban."

    bn "Jangan lupa untuk mengisi biodata kalian terlebih dahulu, dan pastikan sudah terisi sesuai."

    bn "Selamat mengerjakan, dan semoga mendapatkan hasil yang memuaskan."

    "Setelah [bn] memberi instruksi jika ujian sudah dimulai, dan mahasiswa bisa mulai mengerjakan soal ujian."

    "Kamu berdiam dan berdoa terlebih dahulu sebelum mulai mengisi lembar jawaban dengan identitas dirimu."

    "Membuka lembar soal ujian, terdapat beberapa panduan pengerjaan soal pada bagian atas lembar. Kamu menyempatkan diri untuk membaca beberapa panduan pengerjaan tersebut."

    "({i}Ketika {b}UAS{/b} terdapat 5 soal pilihan ganda yang harus dikerjakan untuk menyelesaikan ujian)"

    "({i}Setiap pertanyaan akan ditampilkan dan akan muncul dalam waktu 45 detik{/i})"

    "({i}Ketika waktu 45 detik habis, soal akan hilang dari layar{/i})"

    "({i}Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya{/i})"

    "({i}Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal{/i})"

    "({i}Setelah pemain menjawab nomor terakhir, maka UAS akan berakhir.{/i})"

    "({i}Perlu diketahui UAS pada kampus dapat dilaksanakan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.{/i})"

    "({i}Soal UAS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.{/i})"

    "Selesai membaca panduan pengerjaan pada lembar soal, kamu lalu bersiap menjawab soal-soal ujian yang ada."

    "Mulai mengerjakan UAS?"

    menu: 
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UAS"

    "Soal pertama yang terdapat lembar soal adalah:"

    label soalstrukdat1:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_strukdat1'

        show screen strukdatas_1 with dissolve
        "1. Root dan child merupakan istilah yang digunakan pada struktur data?"
        mc normal jacket "Hmmm root dan child ya?"
        show screen countdown
        menu:

            "A. Array":
                "a. Array"
                mc "Array itu yang indexnya dimulai dari 0 kan, itu ya yang berarti ."

            "B. Linked List":
                "b. Linked list"
                mc "Feeling ku yang ini sihh…"

            "C. Tree":
                "c. Tree"
                mc "Tree kan kalau gak salah dari node paling atas terus ke node yang bawah atau node anaknya. "
                $ a_strukdatAS += 5

            "D. Queue":
                "d. Queue"
                mc "Hierarkis berarti harus urut gitu kan."
        hide screen countdown
        "Kamu menjawab pertanyaan pertama dengan lancar, setelah beberapa kali memeriksa jawaban kamu yakin akan jawaban pertamamu."
        hide screen strukdatas_1 with dissolve
        jump soalstrukdat2

    label telat_strukdat1:
        "Kamu terlambat menjawab pertanyaan, soal no 1 dilewati"
    
    hide screen strukdatas_1 with dissolve

    label soalstrukdat2:
        "Kemudian kamu lanjut menuju pertanyaan selanjutnya."

        "2. 	Head dan tail merupakan istilah yang digunakan pada struktur data?"
        mc "Head dan tail, head dan tail…..?"
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_strukdat2'

        show screen strukdatas_2 with dissolve
        show screen countdown
        menu:

            "A. Array":
                "a. Array"
                mc "mc Array…..."

            "B. Linked List":
                "b. Linked list"
                mc "Kayaknya linked list deh, nanti head atau tailnya terus ada hubungannya sama pointer-pointer itu.."
                $ a_strukdatAS += 5

            "C. Tree":
                "c. Tree"
                mc "Tree kan kalau gak salah dari node paling atas terus ke node yang bawah atau node anaknya. "

            "D. Queue":
                "d. Queue"
                mc "Queue bukannya yang pakai First In First Out itu ya?."
        hide screen countdown
        "Berhasil menjawab pertanyaan nomor 2, kamu berlanjut ke pertanyaan berikutnya."
        hide screen strukdatas_2 with dissolve
        jump soalstrukdat3

    label telat_strukdat2:
        "Kamu terlambat menjawab pertanyaan, soal no 2 dilewati"
    
    hide screen strukdatas_2 with dissolve

    label soalstrukdat3:
        "3. Manakah dibawah ini yang merupakan tipe data yang cocok untuk data nama dan umur?"
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_strukdat3'

        show screen strukdatas_3 with dissolve
        show screen countdown
        menu:

            "A. Boolean dan Array":
                "a. Boolean dan Array"
                mc "Yakin nih aku jawab ini??"

            "B. String dan Date":
                "b. String dan Date"
                mc "Date? Bukanlahh…."

            "C. String dan Integer":
                "c. String dan Integer"
                mc "Yuppss… string untuk nama, dan integer buat umurnya."
                $ a_strukdatAS += 5

            "D. Float dan Text":
                "d. Float dan Text"
                mc "Masa float sama text sih…."
        hide screen countdown
        "Setelah menjawab pertanyaan nomor 3, kamu bergegas menuju pertanyaan selanjutnya."

        "Tersisa dua soal ujian lagi, merasa cepat ingin menyelesaikan ujian ini, kamu langsung membaca pertanyaan nomor 4."
        hide screen strukdatas_3 with dissolve
        jump soalstrukdat4

    label telat_strukdat3:
        "Kamu terlambat menjawab pertanyaan, soal no 3 dilewati"
    
    hide screen strukdatas_3 with dissolve
    
    label soalstrukdat4:
        "4. Mengapa kita sebaiknya menggunakan tipe data yang tepat dalam sistem kita, kecuali?"
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_strukdat4'

        show screen strukdatas_4 with dissolve
        show screen countdown
        menu:

            "A. Tipe data yang tepat dapat mempermudah dalam pemrograman.":
                "a. Tipe data yang tepat dapat mempermudah dalam pemrograman."
                mc "Kayaknya bukan yang ini deh, tipe data ga mempermudah pemrograman."

            "B. Efisiensi penggunaan memori.":
                "b. Efisiensi penggunaan memori."
                mc "Setahuku tipe data pemakaian memorinya sama semua…	"

            "C. Kompatibilitas pada kode yang sedang dikembangkan.":
                "c. Kompatibilitas pada kode yang sedang dikembangkan."
                mc "Emang kalo tipe datanya salah jadi gabisa gitu kah?"

            "D. Meningkatkan estetika program yang dikembangkan.":
                "d. Meningkatkan estetika program yang dikembangkan."
                mc "Estetika? Kan cuma dikodenya, bukan programnnya."
                $ a_strukdatAS += 5
        hide screen countdown
        "Selesai menjawab pertanyaan ke 4, kini hanya tinggal satu pertanyaan lagi yang tersisa sebelum kamu menyelesaikan ujian akhir Strukdat pada pagi hari ini."

        "Setelah mengecek jawaban no 4, kamu langsung membaca soal terakhir yang terdapat pada lembar soal ujian."
        hide screen strukdatas_4 with dissolve
        jump soalstrukdat5

    label telat_strukdat4:
        "Kamu terlambat menjawab pertanyaan, soal no 4 dilewati"
    
    hide screen strukdatas_4 with dissolve

    label soalstrukdat5:
        "5. Yang bukan merupakan tipe data pemrograman yang berada dalam satu kelompok adalah?"
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_strukdat5'

        show screen strukdatas_5 with dissolve
        show screen countdown
        menu:

            "A. String, text, char":
                "a. String, text, char"
                "mc Hmm… bukannya satu kelompok ya?"

            "B. Float, double, int":
                "b. Float, double, int"
                mc "Hmmm sama-sama angka tapi int kan bilangan bulat ya.."
                $ a_strukdatAS += 5

            "C. Int dan short":
                "c. Int dan double"
                mc "Jelas yang ini bener sih……."

            "D. Short, Int, Long":
                "d. Short, Int, Long"
                mc "Harusnya ini dalam satu kelompok sih…."
        hide screen countdown
        "Setelah memilih jawaban untuk pertanyaan terakhir, semua soal yang terdapat pada lembar soal ujian sudah kamu selesaikan."
        hide screen strukdatas_5 with dissolve
        jump end_strukdat

    label telat_strukdat5:
        "Kamu terlambat menjawab pertanyaan, soal no 5 dilewati"
    
    hide screen strukdatas_5 with dissolve

    label end_strukdat:
            
        "Kamu melihat sekelilingmu, masih ada temanmu yang masih mengerjakan ujian, namun ada juga yang sudah beranjak dari bangku ujian."

        "Sebelum mengumpulkan jawaban, tidak lupa kamu mengecek apakah biodata dan jawaban yang kamu isi semuanya sudah benar."

        "Selesai mengecek, kamu berdiri dari bangkumu dan berjalan menuju meja dosen untuk mengumpulkan lembar jawaban ujianmu."

        "Lalu tidak lupa untuk mengambil tas ransel milikmu yang ketika ujian berlangsung diletakkan di depan kelas secara rapi."

        "Ujian pertamamu dalam hari yang kedua telah selesai, kamu berjalan keluar dari ruang kelas ujian"

        "Keluar dari ruang kelas ujian, menandakan kamu telah menyelesaikan ujian akhir mata kuliah Strukdat, kamu merasa senang namun kamu belum bisa merasa lega karena pada hari ini masih tersisa 2 ujian akhir mata kuliah lainnya."

        jump uas_basdat

label attend_strukdat:

    $ a_strukdatA +=1
    $ a_strukdatN +=8

    return