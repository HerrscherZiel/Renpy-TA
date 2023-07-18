
default a_pboA = 0
default a_pboT = 0
default a_pboC = 0
default a_pboTS = 0
default a_pboAS = 0
default a_pboN = 0


label pbo_1:

    scene bg campus class with dissolve    

    call awal_kelas

    pa normal "Selamat pagi teman-teman, hari ini kita bertemu lagi dengan saya dalam mata kuliah yang berbeda."

    pa "Hari ini kita akan mempelajari mengenai Pemrograman Berorietasi Objek(PBO), dimana kita akan membahas tentang pengertian juga kelas dan objek pada PBO."

    "[pa] mengeluarkan laptop dan menyambungkannya dengan proyektor. Setelah layar laptop terproyeksikan pada papan tulis, [pa] mulai menerangkan materi."

    show screen pbo_1_1 with fade
    
    pa "Langsung saja, apa sih pengertian PBO itu? Jadi PBO itu adalah suatu cara memandang atau suatu konsep pemrograman yang berorientasi pada objek-objek nyata untuk mengatur sebuah desan program"

    pa "Pada PBO juga terdapat konsep Kelas dan Objek."

    pa "Dapat kita contohkan, semisal pada mahluk hidup terdapat beberapa kelas, semisal Kelas Burung dan Kelas Ikan."

    pa "Pada Kelas Burung memiliki objek seperti Elang, Gagak, Nuri dan lain sebagainya, sementara pada Kelas Ikan di dalamnya terdapat objek seperti Nila, Cupang, Hiu dan lain sebagainya."

    pa "Kelas dalam PBO memiliki fungsi sebagai suatu template untuk suatu objek. Sebuah kelas dapat menentukan struktur dan perilaku untuk objek dengan kelas tersebut."

    pa "yang dimaksud menentukan struktur dan perilaku adalah semisal pada Kelas Burung, memiliki kesamaan yaitu burung memiliki paruh dan dapat berkicau. 
    Sementara pada Kelas Ikan, memiliki kesamaan yaitu ikan memiliki insang dan memiliki kemampuan untuk berenang."

    hide screen pbo_1_1

    show screen pbo_1_2 with fade

    pa "Kemudian, apa itu objek pada PBO? Objek adalah dasar dari pemrograman berorientasi objek, 
    yang merupakan sebuah instance atau bentukan dari suatu kelas dan memiliki dua karakteristik, yaitu state dan behaviour."

    pa "State merupakan atribut-atribut yang dimiliki oleh suatu objek."

    pa "Behaviour merupakan fungsi yang dimiliki dan dapat dijalankan oleh suatu objek."

    pa "Semisal, pada objek mahasiswa, mahasiswa memiliki atribut nama, NIM, alamat, Prodi, dan lain sebagainya. 
    Sedangkan mahasiswa tersebut memiliki behaviour dapat melakukan pengisian KRS, mendatangi perkuliahan, melakukan UTS dan UAS, dan lain sebagainya."

    "Setelah penjelasan mengenai materi pa melanjutkan perkuliahan dengan tanya jawab."

    hide screen pbo_1_2 with fade
    pause 0.5

    pa normal "Coba [r] sebutkan kelas-kelas yang bisa terdapat pada suatu sistem Perpustakaan."

    r normal2 "Umm… Kelas Buku dan Kelas Peminjam pak?"

    pa "Ya baik boleh, kalau begitu kamu coba [name] sebutkan atribut-atribut yang ada pada Kelas Buku"

    menu: 
        "Ummm…. Buku pengetahuan, buku anak-anak pak?":

            pa "Wah tadi pasti enggak memerhatikan ya?"

            mc normal jacket "hehe maaf pak…."

            pa "Lain kali diperhatikan, biar enggak ketinggalan sama yang lain ya."

            mc "Baik pak."

        "Judul, Kategori, Penulis, Penerbit, Tahun terbit":

            mc normal jacket "Atribut Kelas Buku….. Judul, kategori, penulis, penerbit, tahun terbit pak?"

            pa "Ya ya boleh boleh… buku memang selalu ada judul, kategorinya, penulis, penerbit, dan tahun terbitnya."

            pa "Jawaban yang bagus."

            $a_pboC+=2

    "Kemudian tanya jawab masih terus berlangsung pada mahasiswa lain hingga jam perkuliahan selesai."

    "Satu-persatu mahasiswa diberi pertanyaan yang masih berhubungan dengan pertanyaan sebelumnya."

    "Hingga hampir semua mahasiswa diberi pertanyaan oleh [pa], tidak sedikit dari mereka yang tidak bisa menjawab."

    "Entah karena tidak memerhatikan ataupun belum paham dengan materi yang diajarkan."

    scene bg campus class with fade

    pa normal "Saya kira cukup untuk pertemuan kali ini, sampai ketemu minggu depan teman-teman."

    r normal2 "Terimakasih pak…"

    t normal "Terimakasih…"

    "[pa] meninggalkan ruang kelas, dan pertemuan PBO pada hari ini selesai."

    "Setelah selesai mengemas barang-barangmu, kamu meninggalkan ruang kelas dan bersiap untuk kelas berikutnya."

    call attend_pbo
    call attend_class
    jump jarkom_1

label pbo_2:

    "PBO 2"

    scene bg campus class with dissolve

    call awal_kelas

    scene bg campus class with fade

    "[pa] Memasuki ruang kelas, kelas pertama pada pagi hari ini akan segera dimulai."

    "Seperti biasa, setelah [pa] masuk, [pa] langsung menyambungkan laptopnya dengan proyektor sebelum memulai perkuliahan."

    pa normal "Selamat pagi teman-teman, hari ini kita bertemu lagi dengan saya dalam mata kuliah yang berbeda."

    pa "Pada pertemuan pertama kita sudah membahas mengenai pengertian Pemrograman Berorietasi Objek(PBO), pengertian dan contoh pembahasan mengenai kelas dan objek pada PBO."

    show screen pbo_2_1 with fade

    pa "Hari ini pada pertemuan kedua dari mata kuliah Pemrograman Berorietasi Objek(PBO), dimana kita akan membahas mengenai prinsip-prinsip khusus yang ada pada PBO."

    pa "Fitur-fitur itu adalah Encapsulation, Abstraction, Inheritance, dan Polymorphism."

    pa "Fitur PBO yang pertama adalah Enskapsulasi adalah suatu cara pada PBO untuk menyembunyikan suatu data dengan membungkus suatu class. 
    Enskapsulasi akan menambah keamanan data dan method dari suatu kelas. Enkapsulasi juga memberikan suatu hak akses pada atribut dan method yang ada pada suatu kelas. "

    pa "Hal ini perlu dilakukan karena ketika adanya sharing data antar metode yang ada pada suatu class, 
    tidak diinginkannya terjadi perubahan yang tidak diingankan dan merugikan yang terjadi pada kelas tersebut. "

    pa "Kemudian yang kedua yaitu Abstraksi, Abstraksi pada PBO memungkinkan untuk pengembang memerintahkan suatu fungsi tanpa perlu untuk mengetahui seluk beluk bagaimana fungsi itu bekerja."

    pa "Abtraksi menyembunyikan hal-hal rumit dan hanya menunjukkan hal yang perlu diketahui saja atau bisa juga dibilang dapat menyederhanakan. 
    Abstraksi juga mampu membedakan suatu objek dengan objek lainnya."

    hide screen pbo_2_1

    show screen pbo_2_2 with fade

    pa "Prinsip yang selanjutnya adalah Inheritance atau pewarisan, merupakan salah satu hal yang paling penting pada PBO karena 
    menggunakan inheritance atau pewarisan kita dapat menggunakan kelas yang pernah kita gunakan untuk membentuk suatu kelas baru."

    pa "Prinsip ini menggunakan sistem hirarki oleh karena itu kelas yang mewarisi kelas sebelumnya memiliki kemiripan dengan kelas yang diwarisi. 
    Namun karena itu juga semakin jauh atau turun kelas yang maka akan semakin sedikit kesamaan dengan kelas yang paling atas."

    pa "Lalu terdapat prinsip Polymorphism atau polimorfisasi, dari namanya sendiri dari bahasa latin Poly yang berarti banyak dan morph yang artinya bentuk. 
    Maksut dari banyak dan bentuk tersebut adalah dimana suatu objek yang berbeda-berda dapat diakses melalui interface yang sama."

    pa "Semisal pada kelas Hewan, hewan memiliki method mengeluarkan suara, namun suara yang dikeluarkan tidaklah sama antara satu hewan dengan yang lainnya. 
    Meskipun begitu untuk mengetahui apa suara yang dikeluarkan oleh seekor hewan kita bisa hanya memanggil method suara tersebut."

    hide screen pbo_2_2

    show screen pbo_2_3 with fade

    pa "Dan pembahasan terakhir pada pagi hari ini adalah manfaat penggunaan PBO."

    pa "Manfaat-manfaat penggunaan PBO antara lain menurut Sukamto dan Salahudin(2016) adalah:"

    pa "PBO mampu meningkatkan produktivitas, "

    pa "PBO juga mampu mempercepat pengembangan suatu perangkat lunak."

    pa "Selain itu PBO juga mudah dalam pemeliharaannya."

    pa "Penggunaan PBO juga memungkinkan kode yang digunakan menjadi lebih konsisten."

    pa "Semua hal diatas mampu meningkatkan kualitas perangkat lunak."

    hide screen pbo_2_3

    "Setelah menjelaskan manfaat-manfaat pengaplikasian PBO, [pa] mulai sesi tanya jawab untuk materi hari ini."

    pa "Ya kalau ada pertanyaan bisa ditanyakan sekarang, sebelum kelas berakhir ya."

    "Sesi pertanyaan berlangsung hingga jam perkuliahan berakhir."

    "Setelah jam perkuliahan berakhir [pa] menutup perkuliahan."

    scene bg campus class with fade

    pa normal "Sekiranya cukup untuk pagi hari ini, terimakasih sudah mengikuti perkuliahan dan sampai jumpa minggu depan."

    r normal2 "Terimakasih pak…"

    t normal "Terimakasih…"

    "[pa] meninggalkan ruang kelas, dan pertemuan PBO pada hari ini selesai."

    "Setelah selesai mengemas barang-barangmu, kamu meninggalkan ruang kelas dan bersiap untuk kelas berikutnya."

    call attend_pbo
    call attend_class

    jump jarkom_2

label uts_pbo:

    scene bg campus class with dissolve

    "Hari ini merupakan hari terakhir ujian tengah semester dilaksanakan."

    "Kamu merasa senang karena hari-hari ujian segera akan berakhir."

    "Setelah memastikan dimana posisi tempat dudukmu , kamu memasuki ruang kelas tersebut."

    "Dosen pengawas juga sudah menunggu di dalam kelas dan menyuarakan instruksi kepada semua mahasiswa yang ada."

    scene bg campus class with fade

    "Sesuai intruksi dari dosen pengawas ujian, tas mahasiswa diletakkan di depan kelas secara rapi."

    "Mahasiswa hanya perlu membawa peralatan tulis dan kartu ujian di bangku masing-masing."

    "Sama seperti sebelumnya, setelah kamu duduk kertas ujian tidak langsung dibagikan namun menunggu waktu yang telah ditentukan terlebih dahulu."

    "Ketika waktu sudah menunjukan jam mulai yang tertera pada soal ujian, dosen pengawas mulai berputar mengelilingi kelas sembari membacakan peraturan ujian kali ini."

    bn normal "Selamat pagi teman-teman pada siang hari ini kita akan melanjutkan ujian tengah semester untuk mata kuliah Pemrograman Berorientasi Objek."

    bn "Ibu harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    bn "Soal akan saya bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    bn "Saya harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Setelah menerima lembar soal dan lembar jawaban untuk UTS mata kuliah Pemrograman Berorientasi Objek ini, kamu memejamkan matamu sebentar berdoa dan mempersiapkan diri untuk mengerjakan."

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
    "1. Dalam PBO terdapat konsep yang dinamakan dengan Kelas, manakah dibawah ini yang benar mengenai Kelas?"
    menu:
        "A. Kelas merupakan sebuah template untuk suatu objek, yang akan menuntukan struktur dan perilakunya.":
            "A. Kelas merupakan sebuah template untuk suatu objek, yang akan menuntukan struktur dan perilakunya."
            $a_pboTS +=20
        "B. Kelas merupakan dasar dari pemrograman berbasis objek, yang merupakan sebuah instance atau bentukan dari suatu objek.":
            "B. Kelas merupakan dasar dari pemrograman berbasis objek, yang merupakan sebuah instance atau bentukan dari suatu objek."
        "C. Kelas merupakan fungsi-fungsi yang dapat dilakukan oleh suatu objek.":
            "C. Kelas merupakan fungsi-fungsi yang dapat dilakukan oleh suatu objek."
        "D. Kelas merupakan atribut-atribut dasar yang ada pada suatu objek.":
            "D. Kelas merupakan atribut-atribut dasar yang ada pada suatu objek."
        "E. Kelas dan Objek pada PBO merupakan suatu konsep yang sama, tidak ada perbedaan diantara keduanya.":
            "E. Kelas dan Objek pada PBO merupakan suatu konsep yang sama, tidak ada perbedaan diantara keduanya."
    "2. Behaviour yang mungkin terdapat dalam Kelas Burung yang benar dibawah ini kecuali?"
    menu:
        "A. Bertelur, Berkicau, Terbang.":
            "A. Bertelur, Berkicau, Terbang."
            $a_pboTS += 20
        "B. Bergerak, Bersuara, Berklorofil.":
            "B. Bergerak, Bersuara, Berklorofil."
        "C. Bergerak, Berkembang biak, Beroda.":
            "C. Bergerak, Berkembang biak, Beroda."
        "D. Bermesin, Beroda, Berjalan":
            "D. Bermesin, Beroda, Berjalan"
        "E. Beranak, Berkicau, Menyusui":
            "E. Beranak, Berkicau, Menyusui"

    "3. Dibawah ini yang bukan merupakan prinsip-prinsip yang ada pada PBO kecuali?"
    menu:
        "A. Polymorphism":
            "A. Polymorphism"
        "B. Encapsulation":
            "B. Encapsulation"
        "C. Inheritance":
            "C. Inheritance"
        "D. Abstract":
            "D. Abstract":
        "E. Class and Object":
            "E. Class and Object"
            $a_pboTS += 20
    "4. Prinsip yang mampu menyembunyikan hal-hal yang rumit dan memperlihatkan hanya hal-hal yang penting saja merupakan prinsip PBO yaitu?"
    menu:
        "A. Abstraction":
            "A. Abstraction"
        "B. Polymorphism":
            "B. Polymorphism"
        "C. Inheritance":
            "C. Inheritance"
        "D. Encapsulation":
            "D. Encapsulation"
        "E. Class and Object":
            "E. Class and Object"
    "5. Berikut beberapa pernyataan dari prinsip Pewarisan pada PBO, pernyataan yang benar kecuali?"
    menu:
        "A. Kelas yang diwarisi dapat memiliki atribut yang sama dengan yang mewarisi":
            "A. Kelas yang diwarisi dapat memiliki atribut yang sama dengan yang mewarisi"
        "B. Kelas yang diwarisi dapat memiliki atribut yang sama dengan yang mewarisi":
            "B. Kelas yang diwarisi dapat memiliki atribut yang sama dengan yang mewarisi"
        "C. Prinsip pewarisan merupakan prinsip yang berbentuk hirarki.":
            "C. Prinsip pewarisan merupakan prinsip yang berbentuk hirarki."
        "D. Semakin lama pewarisan dilakukan, kelas yang berada di paling bawah memiliki kesamaan yang paling sedikit dari kelas awal pewarisan.":
            "D. Semakin lama pewarisan dilakukan, kelas yang berada di paling bawah memiliki kesamaan yang paling sedikit dari kelas awal pewarisan."
        "E. Pewarisan mampu melindungi kelas dari perubahan-perubahan yang tidak diinginkan.":
            "E. Pewarisan mampu melindungi kelas dari perubahan-perubahan yang tidak diinginkan."
            $a_pboTS += 20

    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengkoreksi dan meneliti kertas jawaban dan biodatamu selama beberapa kali akhirnya kamu beranjak dari tempat dudukmu."

    "Mengumpulkan kertas ujian, kemudian memasukan barang-barangmu pada tas yang sebelumnya sudah dikelompokan dengan rapi di depan kelas."

    "Kemudian kamu segera keluar dari dalam kelas. Di luar sebelumnya sudah ada beberapa mahasiswa yang keluar lebih dahulu sebelum dirimu."

    "Kamu menghabiskan waktu dengan mengobrol dengan temanmu sembari membaca materi mata kuliah terakhir yang akan diujikan."

    jump uts_jarkom


label pbo_3:

    "PBO 3"

    jump jarkom_3

label pbo_4:

    "PBO 4"

    jump jarkom_4

label attend_pbo:

    $ a_pboA +=1
    $ a_pboN +=8

    return