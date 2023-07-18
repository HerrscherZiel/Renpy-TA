
default a_basdatA = 0
default a_basdatT = 0
default a_basdatC = 0
default a_basdatTS = 0
default a_basdatAS = 0
default a_basdatN = 0

label basdat_1:

    scene bg black with fade
    pause 2.0
    scene bg campus class with dissolve

    "Menempati posisi tempat duduk yang kurang lebih sama dengan ruang kelas sebelumnya."

    "Kamu mengamati kondisi ruang kelas yang ada saat ini."

    "Setelah berada pada kurang lebih 3 ruang kelas yang berbeda, kamu mendapati beberapa hal yang sama pada ruang kelas yang kamu tempati."

    "Tiap ruang kelas memiliki paling tidak 2 buah AC atau pendingin ruangan, memiliki proyektor, dan pada meja untuk pengajar terdapat sebuah komputer yang dapat digunakan."

    "Ketika mengamati ruang kelas saat ini, tiba-tiba [pa] memasuki ruang kelas."

    pa normal "Selamat pagi teman-teman!!"

    t normal "Selamat pagi [pa]!"

    pa "Kita bertemu pada pagi hari ini pada pertemuan pertama mata kuliah Basis Data."

    pa "Pertemuan kali ini saya menjelaskan mengenai pengertian basis data dan mengapa basis data penting untuk kita gunakan."

    "[pa] menyambungkan laptop dengan proyektor dan memperlihatkan apa yang ada pada layar laptopnya."

    show screen basdat_1_1 with fade

    pa "Langsung saja, apa itu basis data ? Basis data merupakan sebuah koleksi atau kumpulan data-data yang memiliki relasi yang disimpan secara sistematis dan dalam bentuk elektronik."

    pa "Basis data kita gunakan dalam berbagai bidang kehidupan. Semisal dalam sekolah, kita gunakan untuk menyimpan data administrasi yang ada di sekolah. 
    Pada perusahaan basis data digunakan untuk menyimpan semua data yang ada, dan masih banyak contoh lain."

    pa "Basis data tidak jauh dari penggunaan perangkat lunak Sistem Manajemen Basis Data, dengan perangkat lunak tersebut kita dapat lebih mudah dalam mengolah data-data yang ada."

    pa "Proses pengolahan data tersebut meliputi penambahan, pengurangan, perubahan, penyimpanan, dan pemanggilan data-data."

    hide screen basdat_1_1

    show screen basdat_1_2 with fade

    pa "Mengapa basis data itu penting dan apa manfaatnya?"

    pa "Basis data itu penting, seperti yang diterangkan sebelumnya penggunaan basis data dapat membantu kita dalam berbagai hal seperti."

    pa "Integritas Data, menggunakan manajemen basis data dapat membantu kita dalam menjaga konsistensi dari data-data dengan menerapkan aturan-aturan pada data yang ada."

    pa "Keamanan Data, menggunakan sistem manajemen basis data juga dapat meningkatkan keamanan data-data yang kita miliki. 
    Semisal dengan penggunaan hak ases untuk masing-masing tipe atau jabatan pengguna."

    pa "Lalu dengan menggunakan sistem manajemen basis data, kita dapat menganalisis data-data yang ada dengan mengelompokan sesuai keinginan kita. 
    Sehingga akan lebih mudah mendapatkan informasi dari data yang ada."

    pa "Dan tentu saja, ketika kita memiliki banyak data jutaan hingga miliaran data tidak mungkin atau akan sangat sulit ketika mengelolanya tanpa menggunakan basis data."
    
    pa "Sehingga dengan menggunakan perangkat lunak untuk basis data memungkinkan kita untuk mengelola data dalam jumlah yang banyak tersebut."

    "Pertama kali mendengarkan pengertian dan manfaat basis data kamu dan teman-temanmu dengan tanggap mencatat apa yang sekiranya perlu untuk dicatat."

    "[pa] menerangkan mata kuliah ini hingga slide terakhir yang ada pada presentasinya."

    "Kemudian kelas dilakukan dengan tanya jawab mengenai dasar basis data."

    hide screen basdat_1_2    

    scene bg campus class with fade

    pa normal "Saya rasa cukup untuk hari ini, kita bertemu lagi minggu depan untuk mata kuliah ini."

    pa "dan kalau tidak salah nanti kelas siang juga dengan saya ya?"

    "Teman-temanmu langsung mengecek jadwal untuk kelas selanjutnya."

    "Ketika temanmu yang lain sedang mengecek jadwal, Rissa mengeluarkanya suaranya."

    r normal2 "Iya pak, nanti pukul 12 ada kelas bapak untuk mata kuliah Web 1."

    pa "Oh yaa…. Kalau begitu sampai ketemu nanti siang, terimakasih…."

    r "Terimakasih pak…."

    t normal "Terimakasih….."

    "Dengan selesai pertemuan kali ini, kini saatnya mahasiswa untuk beristirahat"

    "Tanpa pikir panjang kamu mengemas barang-barangmu dan keluar dari kelas."

    call attend_basdat
    call attend_class

    call istirahat

    jump web_1

label basdat_2:

    scene bg campus class with dissolve

    call awal_kelas

    scene bg campus class with fade

    pa normal "Selamat pagi teman-teman hari ini kita bertemu lagi pada mata kuliah Basis Data."

    pa "Pertemuan sebelumnya kita telah membahas mengenai basis data dan beberapa fungsinya."

    pa "Pada hari ini kita akan lebih berfokus mengenai Sistem Manajemen Basis Data."

    show screen basdat_2_1 with fade

    pa "Apa itu Sistem Manajemen Basis Data? Sistem Manajemen Basis Data merupakan suatu perangkat lunak yang digunakan untuk membuat, 
    memelihara, mengontrol, dan mengakses basis data secara lebih praktis, aman, mudah dipahami, dan efisien."

    pa "Untuk fiturnya kurang lebih sama seperti yang dijelaskan pada pertemuan minggu lalu."

    pa "Namun untuk kelebihan dan kekurangannya kurang lebih seperti ini."

    pa "Kelebihan, Mampu mengurangi duplikasi data."

    pa "Menjaga konsistensi data."

    pa "Meningkatkan keamanan data."

    pa "Meningkatkan efektifitas dan efisiensi penggunaan data."

    pa "Memiliki layanan untuk membackup dan recovery data."

    pa "Adapun kekurangan dalam menggunakan Sistem Manajemen Basis Data adalah."

    pa "Membutuhkan kemampuan tertentu untuk dapat mengoperasikan dan memanajemen atau menjadi administrator sistem."

    pa "Diperlukannya storage sebagai penyimpanan baik internal maupun eksternal untuk memaksimalkan kinerja."

    pa "Harga sistem manajemen basis data yang terbilang mahal."

    pa "Membutuhkan banyak sumber daya dalam pengoperasiannya."

    hide screen basdat_2_1

    show screen basdat_2_2 with fade

    pa "Kalau mungkin kalian belum mengetahui contoh Sistem Manajemen Basis Data, ini merupakan beberapa contohnya."

    pa "Oracle, Microsoft Access, MySQL, Microsoft SQL Server, SQLite, PostgreSQL, dan lain sebagainya."

    pa "Kemudian kita berlanjut pada Komponen-komponen yang ada Sistem Manajemen Basis Data."

    pa "Yaitu yang pertama, Perangkat Keras, perangkat keras diperlukan sebagai perangkat fisik komputer yang dapat digunakan untuk sistem kerja."

    pa "Kedua, Data, data merupakan komponen yang nantinya akan disimpan dan dimanajemen oleh Sistem Manajemen basis Data."

    pa "Ketiga, Perangkat Lunak, Sistem Manajemen Basis Data juga merupakan perangkat lunak. 
    Selain itu program yang datanya akan dimanajemen pada sistem juga merupakan perangkat lunak."

    pa "Kemudian, Pengguna atau User, yang menjadi user dapat berupa Administrator, Programmer, maupun pengguna sistem."

    hide screen basdat_2_2

    show screen basdat_2_3 with fade

    pa "Lalu sebelum waktu habis bapak akan menjelaskan singkat mengenai DDL, dan DML yang ada pada Sistem Manajemen Basis Data."

    pa "Apa itu DDL? DDL atau Data Definition Language merupakan sebuah bahasa dari Sistem Manajemen Basis Data yang berfungsi sebagai pendefinisi dan pengelola struktur atau skema dari suatu basis data. "

    pa "Sementara DML atau Data Manipulation Language merupakan sebuah bahasa dari Sistem Manajemen Basis Data yang berfungsi untuk mengakses, mengambil data, merubah suatu data pada basis data."

    pa "Mungkin untuk lebih lengkapnya bapak akan bahas pada pertemuan selanjutnya ya."

    hide screen basdat_2_3

    pa "Sekarang kalau ada pertanyaan boleh bertanya?"
    
    "Beberapa mahasiswa mengajukan pertanyaan mengenai materi basis data yang baru saja dibahas."

    "Hingga akhir waktu pertemuan [pa] masih menjelaskan dan menjawab pertanyaan yang diajukan oleh mahasiswa."

    "Setelah semua pertanyaan terjawab [pa] menutup pertemuan pagi hari ini."

    pa normal "Terimakasih teman-teman sudah aktif dalam pertemuan kali ini."

    pa "Saya tutup kelas ini dan sampai jumpa di pertemuan selanjutnya."

    t normal "Terimakasih pak."

    r normal2 "Terimakasih…"

    mc normal jacket "Terimakasih…"

    "Kelas selesai dan kini memasuki waktu istirahat sebelum kelas selanjutnya dimulai."

    call attend_basdat
    call attend_class

    call istirahat

    jump web_2

label uts_basdat:

    scene bg campus class with dissolve

    "Setelah menunggu untuk beberapa waktu, akhirnya kelas untuk ujian selanjutnya sudah dibuka."

    "Setelah memastikan dimana posisi tempat dudukmu, kamu memasuki ruang kelas."

    "Memasuki ruang kelas, kini pikiranmu lebih tenang dan siap untuk mengerjakan UTS yang ada."

    "Dosen pengawas juga sudah menunggu di dalam kelas dan menyuarakan instruksi-instruksi yang ada."

    scene bg campus class with fade

    "Sesuai yang diperintahkan dosen penjaga UTS, tas-tas mahasiswa diletakkan di depan kelas secara rapi."

    "Mahasiswa hanya perlu membawa peralatan tulis dan kartu ujian di bangku masing-masing."

    "Sama seperti sebelumnya, setelah kamu duduk kertas ujian tidak langsung dibagikan namun menunggu waktu yang telah ditentukan terlebih dahulu."

    "Ketika waktu sudah menunjukan jam mulai yang tertera pada soal ujian, dosen pengawas mulai berputar mengelilingi kelas sembari membacakan peraturan ujian kali ini."

    pa normal "Selamat pagi teman-teman pada pagi hari ini kita akan melanjutkan ujian tengah semester untuk mata kuliah Basis Data."

    pa "Bapak harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    pa "Soal akan bapak bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    pa "Bapak harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Setelah menerima lembar soal dan lembar jawaban untuk UTS mata kuliah Basis Data ini, kamu memejamkan matamu sebentar berdoa dan mempersiapkan diri untuk mengerjakan."

    "Merasa cukup dengan persiapanmu, kamu mulai mengisi biodata pada lembar jawab sebelum mulai menelaah soal-soal UTS yang ada."

    "(Pada {b}game ini{/b} UTS hanya akan memiliki 5 soal pilihan ganda!)"

    "(Setiap pertanyaan akan ditampilkan dan bisa dijawab dalam waktu 90 detik)"

    ("Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya)"

    "(Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal)"

    "(Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.)"

    '(Perlu diketahui UTS pada kampus dapat dilaksankan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.)'

    "(Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.)"

    menu:
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UTS."
    "1. Apakah yang dimaksud dengan Basis Data?"
    menu:
        "A. Basis data merupakan data-data yang tersebar dalam suatu ruang penyimpanan.":
            "A. Basis data merupakan data-data yang tersebar dalam suatu ruang penyimpanan."
        "B. Basis data merupakan fakta-fakta mengenai suatu penelitian.":
            "B. Basis data merupakan fakta-fakta mengenai suatu penelitian."
        "C. Basis data merupakan sekumpulan data-data yang memiliki relasi yang disimpan secara sistematis.":
            "C. Basis data merupakan sekumpulan data-data yang memiliki relasi yang disimpan secara sistematis."
            $a_basdatTS +=20
        "D. Basis data merupakan tempat penyimpanan data-data yang dikumpulkan.":
            "D. Basis data merupakan tempat penyimpanan data-data yang dikumpulkan."
        "E. Basis data teridiri dari data-data yang tidak memiliki relasi.":
            "E. Basis data teridiri dari data-data yang tidak memiliki relasi."
    "2. Dari beberapa pernyataan dibawah, manakah pernyataan yang benar mengenai manfaat penggunaan Basis Data?"
    menu:
        "A. Basis data memperbesar atau menambah ruang penyimpanan data.":
            "A. Basis data memperbesar atau menambah ruang penyimpanan data."
        "B. Basis data hanya memiliki manfaat terhadap bidang pembiayaan saja.":
            "B. Basis data hanya memiliki manfaat terhadap bidang pembiayaan saja."
        "C. Basis data sangat berguna ketika digunakan pada jumlah data yang sangat kecil.":
            "C. Basis data sangat berguna ketika digunakan pada jumlah data yang sangat kecil."
        "D. Basis data mampu menjaga konsistensi dari data-data yang ada di dalamnya":
            "D. Basis data mampu menjaga konsistensi dari data-data yang ada di dalamnya"
            $a_basdatTS +=20
        "E. Basis data merupakan suatu cara untuk menyimpan data dengan cara yang masih manual.": 
            "E. Basis data merupakan suatu cara untuk menyimpan data dengan cara yang masih manual."
    "3. Berikut merupakan contoh sistem atau aplikasi Sistem Manajemen Basis Data, kecuali?" 
    menu:
        "A. MySQL.":
            "A. MySQL."
        "B. PostgreSQL.":
            "B. PostgreSQL."
        "C. Oracle.":
            "C. Oracle."
        "D. MongoDB.":
            "D. MongoDB."
        "E. DataSQL.":
            "E. DataSQL."
            $a_basdatTS +=20
    "4. Manakah dibawah ini yang merupakan penjelasan dari Database Manipulation Language(DML) yang benar?"
    menu:
        "A. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk menciptakan table.":
            "A. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk menciptakan table."
        "B. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk menghapus table.":
            "B. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk menghapus table."
        "C. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk menambah basis data.":
            "C. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk menambah basis data."
        "D. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk mengubah nama table.":
            "D. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk mengubah nama table."
        "E. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk mengubah nilai suatu data.":
            "E. DML merupakan sebuah bahasa pada sistem manajemen basis data yang digunakan untuk mengubah nilai suatu data."
            $a_basdatTS +=20
    "5. Manakah dibawah ini merupakan pernyataan yang benar mengenai sistem manajemen basis data(SMBD)?"
    menu:
        "A. SMBD mampu menjaga integritas data namun tidak bisa mengurangi redudansi data.":
            "A. SMBD mampu menjaga integritas data namun tidak bisa mengurangi redudansi data."
        "B. SMBD mampu mengurangi redudansi data namun tidak bisa menjaga integritas data.":
            "B. SMBD mampu mengurangi redudansi data namun tidak bisa menjaga integritas data."
        "C. Tidak perlu keahlian dalam pengoperasian atau manajemen SMBD.":
            "C. Tidak perlu keahlian dalam pengoperasian atau manajemen SMBD."
        "D. SMBD tidak dapat digunakan untuk membackup atau merecover basis data.":
            "D. SMBD tidak dapat digunakan untuk membackup atau merecover basis data."
        "E. Memerlukan keahlian dalam pengoperasian atau manajemen SMBD.":
            "E. Memerlukan keahlian dalam pengoperasian atau manajemen SMBD."
            $a_basdatTS +=20

    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengkoreksi dan meneliti kertas jawaban dan biodatamu selama beberapa kali akhirnya kamu beranjak dari tempat dudukmu."

    "Mengumpulkan kertas ujian, kemudian memasukan barang-barangmu pada tas yang sebelumnya sudah dikelompokan dengan rapi di depan kelas."

    "Kemudian kamu segera keluar dari dalam kelas. Di luar sebelumnya sudah ada beberapa mahasiswa yang keluar lebih dahulu sebelum dirimu."

    "Kamu menghabiskan waktu dengan mengobrol dengan temanmu sembari menunggu temanmu yang lain selesai menyelesaikan ujian mereka."

    call istirahat
    jump uts_web


label basdat_3:

    "Basdat 3"

    call istirahat

    jump web_3

label basdat_4:

    "Basdat 4"

    call istirahat

    jump web_4

label attend_basdat:

    $ a_basdatA +=1
    $ a_basdatN +=8

    return