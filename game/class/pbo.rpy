
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
    "2. Behaviour yang mungkin terdapat dalam Kelas Burung yang benar dibawah ini adalah?"
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
            "D. Abstract"
        "E. Class and Object":
            "E. Class and Object"
            $a_pboTS += 20
    "4. Prinsip yang mampu menyembunyikan hal-hal yang rumit dan memperlihatkan hanya hal-hal yang penting saja merupakan prinsip PBO yaitu?"
    menu:
        "A. Abstraction":
            "A. Abstraction"
            $a_pboTS += 20
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
        "A. Kelas yang diwarisi dapat memiliki atribut yang sama dengan yang mewarisi.":
            "A. Kelas yang diwarisi dapat memiliki atribut yang sama dengan yang mewarisi."
        "B. Kelas yang mewarisi menurunkan atribut yang kepada kelas yang diwarisi.":
            "B. Kelas yang mewarisi menurunkan atribut yang kepada kelas yang diwarisi."
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

    scene bg campus class with dissolve

    "Kamu memasuki ruang kelas untuk pertemuan mata kuliah PBO pagi hari ini."

    "Di dalam kelas, sudah terdapat banyak temanmu yang telah datang dan bersenda gurau satu sama lain."

    "Kamu meletakan tas pada salah satu bangku yang terdapat dalam kelas, seperti biasanya kamu duduk pada tempat favoritmu."

    "Tak lama kemudian, salah satu temanmu datang dan duduk di sampingmu. Kemudian kalian berdua mulai berbincang untuk menghabiskan waktu sebelum kelas dimulai."

    "Kurang lebih 10 menit setelah kamu mulai berbincang dengan teman di sebelahmu, salah satu teman memasuki ruang kelas sambil berkata jika [pa] sedang berjalan menuju kelas."

    "Setelah mengetahui hal itu, teman-teman sekelasmu mulai kembali ke tempat duduk dan bersiap untuk perkuliahan. Tidak lama kemudian, [pa] memasuki ruang kelas, pertanda kelas pertama pada pagi hari ini akan segera dimulai."

    "Seperti biasa, setelah [pa] masuk, [pa] langsung menyambungkan laptopnya dengan proyektor sebelum memulai perkuliahan."

    pa normal "Selamat pagi teman-teman, hari ini kita bertemu lagi dengan saya dalam mata kuliah PBO."

    pa "Pada pertemuan ke-3 ini, kita akan mempelajari lebih lanjut mengenai prinsip Enkapsulasi dan Abstraksi."

    pa "Kita akan membahas ulang prinsip-prinsip tersebut, serta memberikan contoh dan penjelasannya."

    show screen pbo_3_1 with fade

    pa class "Pertama, kita akan membahas mengenai prinsip Enkapsulasi. Prinsip ini merupakan prinsip yang mencakup pembungkusan suatu atribut atau metode dalam sebuah objek. "

    pa "Hal ini menyebabkan adanya pembatasan akses pada atribut atau metode yang ada, sehingga atribut atau metode yang ada tersebut tidak dapat diakses dari luar objek dan mampu menyembunyikan detail implementasi suatu objek."

    pa "Enkapsulasi memungkinkan kita menjaga data dari akses yang tidak diinginkan, sementara data tetap bisa diakses melalui metode yang telah ditentukan."

    pa "Dalam pembatasan akses dalam enkapsulasi terdapat 3 kata kunci yaitu, public, protected, dan private."

    pa "Ketiga kata kunci tersebut dapat digunakan untuk menyatakan sebuah atribut atau metode dalam suatu kelas."

    hide screen pbo_3_1

    show screen pbo_3_2 with fade

    pa "Penulisannya diletakkan sebelum nama variabel, semisal variabel nama yang bersifat public ditulis dengan public $nama."

    pa "Kemudian untuk pengertian dari masing-masing hak akses sendiri adalah sebagai berikut."

    pa "Pengertian dari hak akses public adalah dimana jika sebuah atribut atau metode dinyatakan sebagai public maka atribut atau metode tersebut bisa diakses dari mana saja. Baik dari kelas tersebut, kelas turunan, maupun kode yang berada di luar kelas."

    pa "Pengertian dari hak akses protected adalah dimana jika sebuah atribut atau metode yang dinyatakan sebagai protected hanya akan bisa diakses dari dalam kelas itu sendiri atau dari turunan kelas tersebut. Apabila kita mencobanya dari luar kelas atau turunan kelasnya makan akan muncul sebuah error, karena tidak memiliki hak akses."

    pa "Lalu, pengertian dari hak akses private adalah dimana jika sebuah atribut atau metode yang dinyatakan sebagai private maka atribut atau method tersebut hanya bisa diakses melalui kelas itu sendiri saja, kelas lainnya tidak bisa mengakses atribut atau method private tersebut."

    pa "Mungkin untuk memberikan gambaran yang lebih jelas, bapak akan bapak akan memberikan contoh kasus enkapsulasi dalam kehidupan sehari-hari."

    hide screen pbo_3_2

    show screen pbo_3_3 with fade

    pa "Semisal dalam kehidupan berkeluarga dalam suatu rumah tangga."

    pa "Dalam sebuah rumah biasanya terdapat hal-hal yang bisa diakses oleh umum, keluarga itu sendiri, dan masing-masing individu dalam sebuah rumah tersebut."

    pa "Hak akses public dalam sebuah rumah mungkin bisa mencakup ruang-ruangan yang bisa digunakan secara bersama, semisal ruang tamu, ruang keluarga, dan dapur."

    pa "Ruangan-ruangan tersebut bisa digunakan oleh seisi rumah, bahkan terkadang tamu juga bisa menggunakan ruangan tersebut."

    pa "Lalu, untuk hak akses protected dalam sebuah rumah mencakup ruangan-ruangan yang bisa dibilang terbatas untuk beberapa orang saja. "

    pa "Semisal kamar orang tua dan ruang kerja, dimana biasanya yang menggunakan ruangan tersebut hanya orang tua saja, namun tidak menutup kemungkinan anggota keluarga lain dapat mengakses ruangan yang dianggap protected tersebut. "

    pa "Meskipun begitu tamu atau orang yang bukan merupakan anggota keluarga tidak boleh masuk atau mengakses ke ruangan tersebut."

    pa "Kemudian yang terakhir adalah contoh hak akses private, permisalan yang dapat kita ambil dalam kehidupan sebuah rumah tangga adalah semisal gadget dari masing-masing anggota keluarga."

    pa "Smartphone milik masing-masing anggota keluarga bisa kita anggap memiliki hak akses yang private, dimana pemiliknya saja yang bisa mengakses atau menggunakannya."

    pa "Mungkin itu permisalan yang dapat kita gunakan sebagai contoh kasus pengaplikasian prinsip enkapsulasi, dimana pemberian hak akses agar apa yang terdapat didalamnya bisa menjadi lebih terjaga merupakan hal yang penting."

    pa "Dalam contoh di atas, dengan adanya pembatasan hak akses kepada apa yang ada di dalam rumah, maka rumah tangga dapat tertata dengan baik, privasi juga keamanan menjadi lebih terjaga."

    pa "Mungkin itu untuk pembahasan prinsip enkapsulasi ya teman-teman, kita akan berlanjut ke prinsip yang berikutnya."

    hide screen pbo_3_3

    show screen pbo_3_4 with fade

    pa "Prinsip yang berikutnya akan kita pelajari secara lebih mendetail adalah prinsip abstraksi."

    pa "Seperti yang sudah diajarkan sebelumnya, prinsip abstraksi dapat digunakan untuk menyimpan detail internal yang kompleks dari suatu objek atau sistem, dan hanya menampilkan informasi yang relevan atau yang perlu diketahui saja."

    pa "Selain itu dengan menggunakan prinsip abstraksi juga dapat mengurangi kompleksitas dari kode yang kita kembangkan dengan menyembunyikan hal-hal rumit sehingga akan mempermudah penggunaan dari sistem dan kode yang dikembangkan."

    pa "Lalu prinsip abstraksi juga memungkinkan pengguna pengembang atau pengguna menjadi lebih berfokus pada fitur atau fungsi yang ada, dengan tidak terlihatnya rincian alur teknis dari fitur atau fungsi tersebut."

    pa "Kode yang dikembangkan menggunakan abstraksi yang baik, akan membuat kode tersebut menjadi lebih mudah dimengerti atau dibaca. Dengan mudahnya kode untuk dibaca atau dimengerti, maka perawatan terhadap kode juga akan menjadi lebih mudah."

    pa "Kemudian, setelah menjelaskan keuntungan atau manfaat yang bisa didapatkan dari penggunaan abstraksi bapak akan memberi suatu contoh kasus dalam kehidupan sehari-hari mengenai penerapan abstraksi."

    hide screen pbo_3_4

    show screen pbo_3_5 with fade

    pa "Contoh dari penerapan prinsip abstraksi pada kehidupan sehari-hari semisal pada sistem reservasi perjalanan."

    pa "Pada sistem tersebut, pengguna atau pemakai aplikasi tidak perlu memikirkan detail teknis dari proses reservasi untuk perjalanan mereka. 
    Pengguna hanya perlu memberikan data tanggal, tujuan, dan kota asal pada interface atau antarmuka yang dibuat."

    pa "Semisal kita membuat sebuah kelas abstrak dengan nama Transportasi, di dalam kelas abstrak tersebut terdapat sebuah metode abstrak dengan nama reservasi()."

    pa "Kelas Transportasi akan mewarisi kepada kelas-kelas yang mewakili jenis-jenis transportasi seperti 
    Pesawat, Bus, Kapal, dan KeretaApi. Lalu masing-masing dari kelas jenis transportasi tersebut akan mengimplementasikan metode reservasi()."

    pa "Kurang lebih seperti jika kita mengambil contoh implementasi pada kehidupan sehari-hari ya."

    pa "Dan mungkin itu saja kelas kita untuk hari ini, kita telah mempelajari mengenai prinsip pada PBO yaitu prinsip enkapsulasi dan prinsip abstraksi secara lebih lanjut."

    hide screen pbo_3_5 with dissolve

    pa normal "Besok pada pertemuan selanjutnya kita akan membahas mengenai sisa prinsip yang belum kita bahas pada hari ini ya."

    pa "Karena masih ada waktu, mungkin jika ada pertanyaan bisa ditanyakan sekarang teman-teman."

    "Beberapa mahasiswa mengacungkan jarinya lalu mengajukan pertanyaan kepada [pa] mengenai materi yang diajarkan hari ini."

    "Kemudian sesi tanya jawab masih terus berlangsung hingga jam perkuliahan selesai."

    pa "Saya kira cukup untuk pertemuan kali ini, terima kasih telah berpartisipasi pada pertemuan kali ini dan sampai ketemu minggu depan teman-teman."

    r normal2 "Terimakasih pak…"

    t normal "Terimakasih…"

    "[pa] meninggalkan ruang kelas, dan pertemuan ke-3 mata kuliah PBO pada hari ini selesai."

    "Setelah selesai mengemas barang-barangmu, kamu meninggalkan ruang kelas dan bersiap untuk kelas berikutnya."

    call attend_pbo
    call attend_class
    jump jarkom_3

label pbo_4:

    scene bg campus class with dissolve

    pa normal "Selamat pagi teman-teman, hari ini kita bertemu lagi dengan saya dalam pertemuan terakhir mata kuliah PBO."

    pa "Seperti yang sudah bapak katakan minggu kemarin, kalau kalian masih ingat tentunya. 
    Kita akan mempelajari lebih detail mengenai prinsip-prinsip yang ada dalam PBO."

    pa "Setelah pada minggu kemarin kita telah mempelajari tentang prinsip enkapsulasi dan abstraksi, 
    maka pada hari ini kita akan mempelajari mengenai prinsip inheritance atau pewarisan dan prinsip polymorphism."

    pa "Oh iya untuk materi ujian akhir semester nanti, menggunakan materi dari materi pertemuan ke-3 dan minggu ini ya."

    r normal2 "Berarti materi setelah UTS ya kan pak?"

    pa "Iya, benar, dari materi yang diajarkan setelah UTS."

    pa "Jadi belajar yang sungguh-sungguh biar dapat hasil yang memuaskan."

    "Setelah menginformasikan materi untuk ujian akhir, [pa] lalu menghubungkan laptopnya dengan proyektor, 
    tidak lama kemudian setelah layar laptop [pa] telah terproyeksikan di depan kelas, pembelajaran pun dimulai."

    show screen pbo_4_1 with fade

    pa class "Pertama, kita akan membahas mengenai prinsip inheritance dalam PBO."

    pa "Sesuai yang kalian sudah pelajari sebelumnya, prinsip inheritance atau pewarisan ini memiliki pengertian dimana sebuah kelas dalam PBO 
    dapat menurunkan atau mewariskan atribut dan method yang dimiliki pada kelas lainnya."

    pa "Dengan menggunakan pewarisan tersebut, dalam pemrograman memungkinkan kita untuk melakukan code reuse atau penggunaan ulang kode. "

    pa "Hal tersebut dapat mempercepat proses pengkodean dengan mengurangi pengkodean ulang, selain itu code reuse juga dapat menghindari duplikasi kode yang ada di program."

    pa "Telah dijelaskan sebelumnya, sebuah kelas dapat menurunkan atau mewariskan atribut atau metodenya ke kelas lain. 
    Hal itu membuat sebuah hirarki yang ada dalam kode program."

    hide screen pbo_4_1

    show screen pbo_4_2 with fade

    pa "Kelas yang menurunkan atau mewariskan atribut atau metode disebut dengan parent, super, atau base class."

    pa "Sementara kelas yang menggunakan atau mewarisi atribut atau metode dari kelas parentnya disebut dengan child, sub, atau derived class."

    pa "Dalam praktik pemrogramannya, untuk mendeklarasikan sebuah kelas mewarisi kelas lainnya digunakan kata kunci extends."

    pa "Extends digunakan setelah, penulisan nama kelas, setelah itu diikuti dengan nama dari parent classnya."

    pa "Contoh deklarasinya semisal, public class S extends Z. Dimana S adalah nama dari subclass dan Z adalah nama dari parent class nya."

    pa "Kemudian bapak akan memberikan contoh penerapan prinsip Inheritance dalam kehidupan sehari-hari."

    hide screen pbo_4_2

    show screen pbo_4_3 with fade

    pa "Dalam kehidupan sehari-hari mungkin kita bisa mengambil contoh dari sebuah keluarga."

    pa "Pada sebuah keluarga memiliki orang tua, bisa dianggap orang tua yang ada di keluarga tersebut merupakan sebuah parent class yang memiliki atribut dan metodenya masing-masing."

    pa "Lalu, dalam keluarga tersebut memiliki keturunan atau anak, anak tersebut bisa kita anggap sebagai sub atau child classnya."

    pa "Pada contoh tersebut, dapat digambarkan properti atau harta yang dimiliki oleh orang tua akan diberikan atau diwariskan kepada keturunannya. Tidak hanya properti atau harta saja yang diwariskan kepada keturunan, 
    namun juga dapat seperti pengetahuan, penampilan, dan pengalaman dapat diwariskan dari orang tua kepada keturunannya."

    pa "Dengan begitu maka keturunan atau anak dalam suatu keluarga akan mewarisi apa yang diwariskan oleh orang tuanya. Dimana warisan yang didapatkan, dapat dimanfaatkan, diperluas, atau digunakan sesuai kebutuhan yang ada."

    pa "Mungkin itu dulu untuk pembahasan mengenai prinsip Inheritance atau pewarisan."

    pa "Kita akan berpindah pada pembahasan yang selanjutnya yaitu, prinsip Polymorphism."

    hide screen pbo_4_3

    show screen pbo_4_4 with fade

    pa "Polymorphism merupakan salah satu prinsip yang terdapat pada PBO, yaitu konsep dimana objek, variabel, atau metode yang dapat memiliki berbagai bentuk. 
    Polimorfisme memungkinkan penggunaan metode dengan nama yang sama pada berbagai objek dan memungkinkan objek untuk mengambil bentuk yang berbeda, tergantung pada kelas mereka."

    pa "Dengan kata lain, objek dapat berperilaku secara berbeda tergantung pada kelasnya, tetapi pengguna tidak perlu mengetahui kelas spesifik dari objek tersebut."

    pa "Hal tersebut dapat terjadi ketika parent class direferensikan oleh child class."

    hide screen pbo_4_4

    show screen pbo_4_5 with fade

    pa "Polymorphism terbagi menjadi dua jenis, yaitu Polymorphism compile-time dan Polymorphism runtime."

    pa "Polymorphism compile-time merupakan polimorfisme dimana method atau sebuah fungsi dipanggil ketika compile terjadi."

    pa "Polymorphism runtime merupakan polimorfisme dimana method atau sebuah fungsi dipanggil ketika kode dieksekusi atau pada saat runtime."

    pa "Kemudian kita akan membahas mengenai penerapan pada kehidupan sehari-hari untuk fungsi polymorphism."

    hide screen pbo_4_5

    show screen pbo_4_6 with fade

    pa "Semisal pada remote TV yang kita miliki, contoh untuk masing-masing jenis polymorphism adalah sebagai berikut."

    pa "Polymorphism compile-time, semisal pada tombol power pada remote memiliki fungsi yang berbeda ketika tv menyala dan tv mati akan memiliki fungsi yang berbeda. 
    Tombol tersebut memiliki fungsi yang berbeda, dan sudah ditentukan ketika awal pembuatannya."

    pa "Sementara polymorphisme runtime, semisal tombol volume up dan down, ketika tv dalam kondisi mati, maka tombol tersebut tidak memiliki fungsi atau tidak berfungsi. 
    Perilaku tombol bergantung pada situasi saat tombol ditekan (waktu runtime)."

    pa "Mungkin itu dulu ya untuk pembahasan mengenai prinsip-prinsip yang ada dalam PBO."

    hide screen pbo_4_6

    scene bg campus class with dissolve

    pa normal "Jadi nanti untuk ujian akhir semester, materinya adalah materi yang telah bapak berikan setelah UTS ya. Jadi selamat belajar ya teman-teman."

    t normal "Jangan susah-susah ya pak soalnya."

    t "Hmmm berarti materi-materi minggu kemarin dan sekarang ya…"

    r normal2 "Berarti aku harus ringkasin materi dua minggu ini yaa hmm…."

    pa "Kalau begitu bapak tutup ya, pertemuan hari ini. Selamat belajar dan semoga mendapatkan hasil yang diinginkan pada ujian nanti."

    pa "Terimakasih sudah mengikuti kelas sampai pertemuan kali ini, sampai jumpa pada pertemuan selanjutnya teman-teman."

    t "Terimakasih pak."

    t "Terimakasihhh"

    r "Terimakasih juga pak."

    "Dengan begitu kelas ditutup dan pembelajaran untuk hari ini telah usai. Kamu keluar dari ruangan kelas dan melanjutkan aktivitasmu berikutnya."

    call attend_pbo
    call attend_class
    jump jarkom_4

label attend_pbo:

    $ a_pboA +=1
    $ a_pboN +=8

    return