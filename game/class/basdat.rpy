
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

    "Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya)"

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

    scene bg campus hall with dissolve

    "Setelah beristirahat selama beberapa menit di luar ruangan, kelas berikutnya sudah akan dimulai."

    "Kamu dan teman-temanmu mulai memasuki ruang kelas berikutnya."

    "Setelah memasuki ruang kelas, seperti biasanya kamu memiliki untuk menempati duduk yang berada di dekat jendela."

    scene bg campus class with fade

    "Selagi menunggu dosen yang belum kunjung datang, kamu mengobrol dengan teman yang duduk di sebelahmu untuk menghabiskan waktu ."

    "10 menit berlalu setelah kamu dan teman sekelasmu memasuki ruangan, terlihat [pa] berjalan mendekati ruang kelas  pertanda kelas akan segera dimulai."

    pa normal "Selamat pagi teman-teman kita berjumpa lagi pada hari ini pada pertemuan ke-3  mata kuliah Basis Data."

    pa "Pada pertemuan ke-3 ini kita akan membahas lebih lanjut mengenai materi yang sudah pernah kita bahas sebelumnya, yaitu Data Definition Language."

    "Setelah menyambungkan laptopnya dengan proyektor dan materi untuk hari ini sudah terlihat di depan kelas, perkuliahan pun dimulai."

    scene bg campus class with fade

    pa normal "Data Definition Language, seperti yang kalian tahu merupakan sebuah bahasa dari sistem manajemen basis data yang berfungsi sebagai pendefinisi dan pengelola struktur skema suatu basis data."

    show screen basdat_3_1 with fade

    pa class "Data definition language pada basis data sendiri memiliki berbagai macam kegunaan, seperti dapat digunakan untuk menambah, mengubah, menghapus, mengelola indeks, mendefinisikan fungsi, dan lain sebagainya."

    pa "Pada pertemuan hari ini kita akan mengenal lebih lanjut, syntax atau perintah dan kegunaannya. Kali ini kita akan mempelajari data definition language menggunakan basis data MySQL."

    pa "MySQL merupakan sebuah sistem manajemen basis data yang bisa kita gunakan secara gratis."

    pa "Mungkin jika kalian ingin mencoba secara langsung pada MySQL kalian dapat mencari tahu sendiri bagaimana cara menginstallnya di internet."

    pa "Agar tidak terlalu banyak, materi hari ini kita fokuskan untuk mempelajari perintah yang dapat digunakan untuk membuat basis data, membuat table, menghapus table, mengganti nama table, mendefinisikan primary key, dan menambah kolom dalam suatu tabel."

    pa "Sebelumnya agar gambaran kalian mengenai basis data tidak terlalu kosong, akan bapak jelaskan secara singkat ya."

    pa "Basis data seperti yang sudah kalian tahu memiliki fungsi utama untuk menyimpan data secara terorganisir dan terstruktur."

    pa "Bapak akan menjelaskan basis data pada MySQL ya, karena ada beberapa perbedaan juga kalau menggunakan basis data lain."

    hide screen basdat_3_1

    show screen basdat_3_2 with fade

    pa "Basis data dapat dibuat atau ditambahkan dengan cara menuliskan syntax create database nama_db pada command line."

    pa "Syntax tersebut dapat dijelaskan sebagai berikut, create berarti kita menuliskan perintah untuk membuat, lalu database yang berarti kita akan membuat sebuah database atau basis data baru, dan yang terakhir nama_db bebas kita isikan sesuai nama basis data yang ingin kita gunakan."

    pa "Jangan lupa setelah menulis syntax kita harus menutupnya dengan delimiter, atau pemisah pernyataan dalam SQL. Delimiter pada SQL secara default adalah tanda ‘ ; ‘."

    pa "Jadi pagi hari ini, kita akan menulis syntax untuk membuat basis data dengan nama latihan. Maka penulisannya adalah sebagai berikut:"

    "pa create database latihan;"

    pa "Setelah menekan enter, dan jika syntax berhasil dijalankan maka akan terlihat tulisan Query OK, maka basis data berhasil dibuat."

    pa "Kemudian untuk mengecek apakah basis data baru sudah berhasil ditambahkan, kita bisa melihat ke list basis data, 
    dengan menuliskan syntax show databases; maka akan terlihat tampilan seperti gambar ini."

    pa "Terlihat basis data latihan sudah terdapat pada list basis data, yang berarti basis data latihan berhasil ditambahkan."

    pa "Kemudian, setiap basis data memiliki tabel-tabel yang mewakili entitas-entitas didalamnya."

    pa "Semisal untuk basis data pada sebuah kampus, bernama kampus merdeka memiliki tabel mahasiswa, dosen, dan mata kuliah."

    pa "Tabel-tabel tersebut mewakili entitas mahasiswa, dosen, dan mata kuliah, dimana data-data setiap entitas akan disimpan pada tabel tersebut."

    pa "Setiap tabel juga memiliki kolom dan barisnya, kolom mewakili atribut dari entitas tersebut dan baris mewakili entri individual dalam tabel."

    pa "Semisal pada tabel Mahasiswa terdapat kolom atau atribut nama, NIM, dan program studi."

    pa "Kemudian barisnya terisi dengan data, Budi, 14011, dan TRPL."

    pa "Kurang lebih seperti penjelasan mengenai tabel, kolom, dan baris dalam basis data."

    pa "Berikutnya bapak akan memberi contoh syntax untuk membuat sebuah tabel."

    hide screen basdat_3_2

    show screen basdat_3_3 with fade

    pa "Oh iya, sebelum menulis syntax itu, kita harus memilih basis data mana yang kita akan tambahkan tabelnya. 
    Karena sebelumnya kita sudah membuat basis data latihan, 
    kita akan menggunakan basis data tersebut dengan syntax use latihan;"

    pa "Syntax untuk menambah tabel Mahasiswa, dengan kolom nama, NIM, dan program studi adalah sebagai berikut:"

    pa "create table mahasiswa(nama varchar(255), nim varchar(15), prodi varchar(50));"

    pa "Query atau syntax tersebut bisa dijelaskan sebagai berikut, create digunakan untuk membuat, 
    lalu table berarti kita akan membuat sebuah table. Kemudian mahasiswa merupakan nama table yang ingin kita buat."

    pa "Setelah nama table, kita lanjutkan dengan tanda kurung buka ‘(‘ dan ditutup dengan kurung tutup ‘)’ 
    lalu kita isi dengan atribut yang ada di dalamnya, atribut pertama adalah nama dengan tipe data varchar dengan batas karakter yang kita inginkan semisal 255. 
    Atribut berikutnya ditambahkan setelah menambahkan tanda ‘,’ setelah atribut pertama."

    pa "Maka kita akan menuliskannya sebagai berikut (nama varchar(255), nim varchar(15), prodi varchar(50))"

    pa "Secara penuh kita menuliskannya sebagai berikut create table mahasiswa(nama varchar(255), nim varchar(15), prodi varchar(50));"

    pa "Untuk mengecek apakah tabel tersebut telah ditambahkan pada basis data, kita bisa mengeceknya dengan menuliskan syntax show tables;"

    hide screen basdat_3_3

    show screen basdat_3_4 with fade

    pa "Terlihat tabel mahasiswa sudah ditambahkan pada basis data latihan."

    pa "Kemudian untuk melihat struktur atau skema pada tabel mahasiswa kita bisa menuliskan syntax desc mahasiswa;"

    pa "Tabel yang sudah kita buat bisa kita ubah strukturnya, semisal ingin menambahkan sebuah kolom tambahan didalamnya."

    pa "Syntax yang dapat digunakan untuk melakukan hal tersebut adalah sebagai berikut."

    hide screen basdat_3_4

    show screen basdat_3_5 with fade

    pa "alter table mahasiswa add column alamat varchar(255);"

    pa "Syntax tersebut dapat dijelaskan sebagai berikut, mengubah struktur tabel mahasiswa dengan menambah kolom alamat bertipe varchar dengan 255 maksimal karakter."

    pa "Alter disini berfungsi untuk merubah suatu struktur dalam basis data, table berarti kita akan merubah sebuah struktur tabel, add column berarti kita akan menambah kolom pada tabel tersebut, 
    dan alamat varchar(255) adalah nama kolom beserta tipe datanya."

    pa "Setelah menuliskan syntax tersebut, untuk melihat perbedaannya kita tuliskan kembali desc mahasiswa;"

    pa "Dapat dilihat, kolom alamat sudah berhasil ditambahkan pada tabel mahasiswa."

    pa "Kemudian yang terakhir untuk hari ini, kita akan mempelajari mengenai syntax untuk menghapus sebuah tabel."

    hide screen basdat_3_5

    show screen basdat_3_6 with fade

    pa "Sebelumnya, kita tambahkan dulu tabel matkul pada basis data;"

    pa "Gambar disamping kiri memperlihatkan tabel matkul sudah ada pada basis data latihan."

    pa "Untuk menghapus tabel matkul, kita bisa menuliskan syntax drop table matkul;"

    pa "Penjelasan untuk syntax tersebut adalah, drop berarti kita akan menghilangkan atau menghapus sesuatu dalam basis data, 
    table matkul berarti apa yang akan kita drop adalah sebuah table bernama matkul;"

    pa "Setelah memasukkan syntax drop table matkul; lalu kita cek dengan syntax show tables; 
    dapat dilihat tabel matkul sudah tidak ada pada basis data latihan yang berarti kita berhasil menghapus tabel mahasiswa;"

    pa "Hari ini kita mempelajari mengenai membuat basis data, membuat table, menambahkan kolom, dan menghapus tabel."

    hide screen basdat_3_6 with fade

    pa "Mungkin itu dulu dari saya, kalian bisa mempelajari kegunaan lebih lanjut dari syntax create, alter, dan drop sendiri ya."

    scene bg campus class with dissolve

    pa normal "Pertemuan selanjutnya kita akan mempelajari mengenai DML atau data manipulative language."

    pa "Sekarang karena masih ada sedikit waktu kalau ada pertanyaan boleh bisa ditanyakan teman-teman."

    "Beberapa mahasiswa mengajukan pertanyaan mengenai materi basis data yang baru saja dibahas."

    "Hingga akhir waktu pertemuan [pa] masih menjelaskan dan menjawab pertanyaan yang diajukan oleh mahasiswa."

    "Setelah semua pertanyaan terjawab [pa] menutup pertemuan pagi hari ini."

    "[pa] meninggalkan sebuah tugas untuk dikerjakan sampai minggu depan."

    $taskbasdat = True

    call n_task

    pa normal "Terimakasih teman-teman sudah aktif dalam pertemuan kali ini."

    pa "Saya tutup pertemuan kali ini sampai jumpa di pertemuan selanjutnya."

    t normal "Terimakasih pak."

    r normal2 "Terimakasih…"

    mc normal jacket "Terimakasih…"

    "Kelas selesai dan kini memasuki waktu istirahat sebelum kelas selanjutnya dimulai."

    call attend_basdat
    call attend_class

    call istirahat

    jump web_3

label basdat_4:

    scene bg campus hall with dissolve

    "Setelah menunggu selama beberapa menit di luar ruangan, waktu untuk kelas berikutnya telah dimulai."

    "Kamu dan teman-temanmu mulai memasuki ruang kelas berikutnya."

    "Setelah memasuki ruang kelas, seperti biasanya kamu memilih untuk menempati duduk yang berada di dekat jendela."

    "Selagi menunggu dosen yang belum kunjung datang, kamu mengobrol dengan teman yang duduk di sebelahmu untuk menghabiskan waktu ."

    "10 menit berlalu setelah kamu dan teman sekelasmu memasuki ruangan, terlihat [pa] berjalan mendekati ruang kelas  pertanda kelas akan segera dimulai."

    pa normal "Selamat pagi teman-teman kita berjumpa lagi pada hari ini pada pertemuan ke-4  mata kuliah Basis Data yang juga akan menjadi pertemuan terakhir pada mata kuliah ini."

    pa "Pada pertemuan terakhir ini kita akan membahas lebih lanjut mengenai materi yang sudah bapak beritahu sebelumnya, yaitu Data Manipulation Language."

    "Setelah menyambungkan laptopnya dengan proyektor dan materi untuk hari ini sudah terlihat di depan kelas, perkuliahan pun dimulai."

    scene bg campus class with fade

    pa normal "Data Manipulation Language, seperti yang kalian tahu merupakan sebuah bahasa dari sistem manajemen basis data yang digunakan untuk mengelola dan memanipulasi data dalam suatu basis data."

    show screen basdat_4_1 with fade

    pa class "Data manipulation language pada basis data sendiri memiliki berbagai macam kegunaan, seperti dapat digunakan untuk 
    menyisipkan data(Insert), memperbarui data(update), menghapus data(delete), dan untuk memilih data(select) ."

    pa "Pada pertemuan hari ini kita akan mengenal lebih lanjut, syntax atau perintah dan kegunaannya. 
    Kali ini kita akan mempelajari data manipulation language menggunakan basis data MySQL."

    pa "Melanjutkan dari basis data latihan yang kita buat pada pertemuan sebelumnya, kita telah membuat sebuah tabel bernama mahasiswa dengan atribut nama, nim, dan prodi."

    pa "Hari ini kita akan mencoba DML dalam tabel mahasiswa, dimana kita akan mencoba menyisipkan, mengubah, menghapus, dan memilih data pada tabel tersebut."

    pa "Oh iya, setelah berhasil masuk pada MySQL untuk memilih basis data latihan tuliskan syntax use latihan;"

    hide screen basdat_4_1

    show screen basdat_4_2 with fade

    pa "Setelah basis data latihan berhasil dipilih, kita akan mencoba memasukan syntax untuk menyisipkan(Insert) data pada tabel mahasiswa, dengan data sebagai berikut."

    pa "nama: Budi, 14011, TRPL."

    pa "Untuk memasukan data tersebut kita bisa menuliskan syntax, INSERT INTO mahasiswa (nama, nim, prodi) VALUES (‘Budi’, ‘14011’, ‘TRPL’);"

    pa "Syntax diatas dapat diterangkan sebagai berikut, INSERT INTO merupakan perintah untuk menyisipkan data pada sebuah tabel, 
    mahasiswa merupakan target dimana data akan disisipkan pada tabel tersebut, lalu (nama, nim, prodi) merupakan target kolom dimana data-data akan dimasukkan."

    pa "Kemudian, VALUES () berisikan data yang akan dimasukan pada masing-masing kolom yang sudah dituliskan sebelumnya."

    pa "Setelah selesai memasukkan syntax untuk menyisipkan data, kita dapat mengecek apakah data sudah berhasil dimasukkan dengan memasukan syntax untuk memilih data."

    hide screen basdat_4_2

    show screen basdat_4_3 with fade

    pa "Syntax untuk memilih atau melihat data yang ada pada tabel mahasiswa adalah sebagai berikut:"

    pa "SELECT * FROM mahasiswa;"

    pa "Penjelasan untuk syntax diatas adalah, SELECT merupakan perintah untuk memilih atau mengambil data, lalu tanda ‘*’ memiliki arti ALL atau semua, 
    yang berarti SELECT * FROM mahasiswa memiliki artian pilih semua data yang ada pada (tabel) mahasiswa."

    pa "Dapat kita lihat, data dengan nama Budi telah berhasil kita masukkan."

    pa "Syntax DML berikutnya yang akan kita pelajari adalah cara menghapus data pada tabel mahasiswa."

    hide screen basdat_4_3

    show screen basdat_4_4 with fade

    pa "Namun sebelum itu, bapak akan menambahkan satu data lagi pada tabel mahasiswa yaitu Fandi, 14012, TRPL."
    
    pa "Nah, setelah menambahkan data kedua yang dapat dilihat pada gambar bagian kiri, kita akan menghapus data dengan nama Fandi."

    pa "Syntax untuk menghapus data dengan nama Fandi adalah, DELETE FROM mahasiswa WHERE nama=’Fandi’;"

    pa "Penjelasan untuk syntax tersebut adalah, DELETE FROM merupakan perintah untuk menghapus data dari sebuah tabel, 
    bernama mahasiswa, kemudian setelah menentukan dari tabel apa sebuah data akan dihapus, 
    kita juga harus menentukan kriteria dari data yang akan dihapus."

    pa "Kriteria yang akan dipilih diawali dengan syntax, WHERE, lalu masukan kriteria yang akan dihapus. 
    Karena kita akan menghapus data dengan nama Fandi, maka kita masukan nama=’Fandi’;"

    pa "Sehingga syntax untuk menghapus data dengan nama Fandi adalah, DELETE FROM mahasiswa WHERE nama=’Fandi’;"

    pa "Terlihat data dengan nama Fandi telah berhasil dihapus."

    pa "Kemudian yang terakhir pada hari ini, kita akan mempelajari tentang cara mengubah data pada suatu tabel."

    hide screen basdat_4_4

    show screen basdat_4_5 with fade

    pa "Semisal pada tabel mahasiswa, data nama dengan nama Budi akan dirubah menjadi Budiyono, maka kita harus memasukkan syntax;"

    pa "UPDATE mahasiswa SET nama=’Budiyono’ WHERE nama=’Budi’;"

    pa "Penjelasan syntax tersebut adalah, UPDATE merupakan perintah untuk mengubah, mahasiswa merupakan target tabel yang datanya ingin dirubah."

    pa "SET merupakan perintah untuk merubah suatu data menjadi data baru, 
    nama=’Budiyono’ berarti data nama akan berubah menjadi bernilai ‘Budiyono’."

    pa "WHERE seperti sebelumnya merupakan sebuah perintah untuk menunjukan kriteria, nama=’Budi’ berarti data dengan nama ‘Budi’ yang akan dirubah."
    
    pa "Terlihat data dengan nama Budi telah berubah menjadi Budiyono."

    hide screen basdat_4_5 with dissolve

    pa normal "Hari ini kita telah mempelajari mengenai menambahkan data, melihat data, menghapus data, dan merubah data."

    pa "Mungkin itu dulu dari saya, kalian bisa mempelajari kegunaan lebih lanjut dari sendiri ya."

    scene bg campus class with dissolve

    pa normal "Ini merupakan pertemuan terakhir, jadi bapak akan memberi tahu materi yang akan digunakan untuk ujian akhir semester nanti."

    pa "Materi untuk ujian nanti adalah materi dari pertemuan ke-3 dan ke-4 ya teman-teman."

    t normal "Baik pakkk"

    pa "Sekarang karena masih ada sedikit waktu kalau ada pertanyaan boleh bisa ditanyakan teman-teman."

    "Beberapa mahasiswa mengajukan pertanyaan mengenai materi basis data yang baru saja dibahas."

    "Hingga akhir waktu pertemuan [pa] masih menjelaskan dan menjawab pertanyaan yang diajukan oleh mahasiswa."

    "Setelah semua pertanyaan terjawab [pa] menutup pertemuan pagi hari ini."

    scene bg black with Dissolve(1.0)

    scene bg campus class with fade

    pa normal "Terimakasih teman-teman sudah aktif dalam pertemuan pada mata kuliah ini."

    pa "Saya tutup pertemuan terakhir pada mata kuliah ini, selamat belajar dan semoga mendapatkan hasil yang diinginkan pada ujian nanti."

    t normal "Terimakasih pak."

    r normal2 "Terimakasih…"

    mc normal jacket "Terimakasih…"

    "Kelas selesai dan kini memasuki waktu istirahat sebelum kelas selanjutnya dimulai."

    call attend_basdat
    call attend_class

    call istirahat

    jump web_4

label uas_basdat:

    scene bg campus upper hall with dissolve

    pause 1.5

    "Keluar dari ruang ujian, kamu langsung mencari tempat duduk di depan ruang kelas ujian berikutnya yang terletak di sebelah ruang kelas yang baru digunakan untuk ujian."

    "Kamu duduk di sebelah teman-temanmu yang langsung mengeluarkan buku catatan masing-masing untuk mempersiapkan ujian berikutnya."

    "Terlihat [r] yang baru saja keluar dari ruang ujian berjalan menghampirimu. Setelah berada di depanmu ia duduk dan mendekat kepadamu."

    r normal2 "[name] Gimana barusan? Lancar engga ngerjainnya?"

    mc normal jacket "Hmmm… ngerjainnya sih lancar, tapi gatau hasilnya gimana…"

    mc "Kamu gimana? Tumben baru aja keluar, biasanya awal-awal udah keluar duluan."

    r "Huhh… aku bingung pertanyaan yang akhir-akhir itu…. Mikir lamaaaaa…. Terus gatau bener apa engga jawabanku huhu…"

    mc "Yaudah… kata temen SMA ku dulu, yang sudah ya sudah ahahaha"

    r "Dasarrrr huu…."

    "Kamu mengisi sela waktu sebelum ujian selanjutnya dengan mengobrol bersama [r] yang juga tidak mempersiapkan untuk ujian selanjutnya."

    "Setelah mengobrol bersama [r] selama beberapa waktu kini dirimu menjadi lebih tenang untuk mengikuti ujian berikutnya."

    "Sekarang sudah memasuki waktu ujian akhir yang kedua, setelah pintu ujian dibuka kamu dan [r]  berdiri dan bergegas masuk ke ruang ujian."

    scene bg campus upper hall with fade

    pause 1.0

    scene bg campus class with fade

    "Memasuki ruang kelas ujian, dosen pengawas ujian memberi instruksi kepada mahasiswa untuk meletakkan tas atau ransel di depan kelas secara rapi. Lalu hanya membawa peralatan tulis dan kartu mahasiswa ke bangku ujian."

    "Setelah meletakan tasmu di depan ruangan, kamu mengambil peralatan tulismu sebelum berjalan menuju bangku ujian."

    "Terlihat lembar jawab ujian sudah diletakan pada masing-masing bangku ujian."

    "Kemudian ketika semua bangku ujian telah terisi oleh peserta ujian, dosen pengawas ujian lalu menjelaskan peraturan ujian."

    "Tidak ada yang berbeda seperti peraturan-peraturan ujian pada umumnya."

    "Selesai menjelaskan, beberapa menit kemudian soal ujian disebarkan kepada seluruh peserta yang ada."

    "Kamu menerima beberapa soal ujian dari bangku yang ada di depanmu, setelah mengambil salah satu soal ujian, kamu meneruskan pembagian soal-soal ujian lainnya ke bangku yang ada di belakangmu."

    "Setelah dosen pengawas ujian memberi instruksi jika ujian sudah dimulai, dan mahasiswa bisa mulai mengerjakan soal ujian."

    "Kamu berdiam dan berdoa terlebih dahulu sebelum mulai mengisi lembar jawaban dengan identitas dirimu."

    "Membuka lembar soal ujian, terdapat beberapa panduan pengerjaan soal pada bagian atas lembar. Kamu menyempatkan diri untuk membaca beberapa panduan pengerjaan tersebut."

    "({i}Ketika {b}UAS{/b} terdapat 5 soal pilihan ganda yang harus dikerjakan untuk menyelesaikan ujian{/i})"

    "({i}Setiap pertanyaan akan ditampilkan dan akan ditampilkan selama 90 detik{/i})"

    "({i}Ketika waktu 90 detik habis, soal akan hilang dari layar{/i})"

    "({i}Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya.{/i})"

    "({i}Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal.{/i})"

    "({i}Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.{/i})"

    "({i}Perlu diketahui UTS pada kampus dapat dilaksanakan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.{/i})"

    "({i}Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.{/i})"

    "Selesai membaca panduan pengerjaan pada lembar soal, kamu lalu bersiap menjawab soal-soal ujian yang ada."

    "Mulai mengerjakan UAS?"

    menu: 
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UAS"

    "Soal pertama yang terdapat lembar soal adalah:"

    label soalbasdat1:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_basdat1'

        show screen basdatas_1 with dissolve
        "1. Manakah dibawah ini yang merupakan kode perintah dari DDL dan DML?"
        mc normal jacket "DDL dan DML yaa…..?"
        show screen countdown
        menu:

            "A. Create dan Delete":
                "a. Create dan Delete"
                mc "Create itu DDL terus Delete itu DML."
                $ a_basdatAS +=5

            "B. Create dan Drop":
                "b. Create dan Drop"
                mc "Create itu DDL kalo Drop itu…"

            "C. Update dan Insert":
                "c. Update dan Insert"
                mc "Keduanya DML gak sih? "

            "D. Alter dan Drop":
                "d. Alter dan Drop"
                mc "Bukannya keduanya DLL."
        hide screen countdown
        "Kamu menjawab pertanyaan pertama dengan lancar, setelah beberapa kali memeriksa jawaban kamu yakin akan jawaban pertamamu."
        hide screen basdatas_1 with dissolve
        jump soalbasdat2

    label telat_basdat1:
        "Kamu terlambat menjawab pertanyaan, soal no 1 dilewati"

    hide screen basdatas_1 with dissolve

    label soalbasdat2:

        "Kemudian kamu lanjut menuju pertanyaan selanjutnya."
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_basdat2'

        show screen basdatas_2 with dissolve
        "2. 	Pernyataan yang benar mengenai DDL dan DML adalah?"

        mc "Perbedaan… DDL dan DML…..?"
        show screen countdown
        menu:

            "A. DDL digunakan untuk mendefinisikan dan memanipulasi basis data":
                "a. DDL untuk mendefinisikan dan memanipulasi basis data"
                mc "DLL itu cuma untuk mendefinisikan kalau gak salah…."

            "B. DML digunakan untuk mendefinisikan dan memanipulasi basis data":
                "b. DML digunakan untuk mendefinisikan dan memanipulasi basis data"
                mc "DML cuma buat manipulasi data dalam basis data enggak sih?"

            "C. DML digunakan untuk mengelola data dalam suatu basis data":
                "c. DML digunakan ketika kita ingin mengelola data dalam suatu basis data"
                mc "Yuppp… yang ini bener…"
                $ a_basdatAS +=5

            "D. DDL digunakan untuk mengelola data dalam suatu basis data":
                "d. DDL digunakan untuk mengelola data dalam suatu basis data"
                mc "Bukannya harusnya DML ya?"
        hide screen countdown
        "Berhasil menjawab pertanyaan nomor 2, kamu berlanjut ke pertanyaan berikutnya."
        hide screen basdatas_2 with dissolve
        jump soalbasdat3

    label telat_basdat2:
        "Kamu terlambat menjawab pertanyaan, soal no 2 dilewati"

    hide screen basdatas_2 with dissolve

    label soalbasdat3:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_basdat3'

        show screen basdatas_3 with dissolve
        "3. Perintah yang digunakan untuk melakukan pencarian suatu data dalam basis data adalah?"
        show screen countdown
        menu:

            "A. Select":
                "a. Select"
                mc "Select digunakan untuk memilih data, berarti bener yang ini."
                $ a_basdatAS +=5

            "B. Drop":
                "b. Drop"
                mc "Drop itu digunakan untuk menghapus skema gak sih…"

            "C. Insert":
                "c. Insert"
                mc "Insert itu buat masukin data kan?"

            "D. Alter":
                "d. Alter"
                mc "Alter bukannya buat ngerubah struktur data ya?"
        hide screen countdown
        "Setelah menjawab pertanyaan nomor 3, kamu bergegas menuju pertanyaan selanjutnya."

        "Tersisa dua soal ujian lagi, merasa cepat ingin menyelesaikan quiz ini, kamu langsung membaca pertanyaan nomor 4."
        hide screen basdatas_3 with dissolve
        jump soalbasdat4

    label telat_basdat3:
        "Kamu terlambat menjawab pertanyaan, soal no 3 dilewati"

    hide screen basdatas_3 with dissolve

    label soalbasdat4:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_basdat4'

        show screen basdatas_4 with dissolve
        "4. 	Manakah dibawah ini yang merupakan perintah yang digunakan untuk menghapus suatu entitas pada suatu basis data?"
        show screen countdown
        menu:

            "A. Delete":
                "a. Delete"
                mc "Delete bukan yaa??"

            "B. Drop":
                "b. Drop"
                mc "Drop ya bener drop!"
                $ a_basdatAS +=5

            "C. Alter":
                "c. Alter"
                mc "Alter itu untuk mengubah skema basis data…"

            "D. Update":
                "d. Update"
                mc "Update? "
        hide screen countdown
        "Selesai menjawab pertanyaan ke 4, kini hanya tinggal satu pertanyaan lagi yang tersisa sebelum kamu menyelesaikan ujian akhir Strukdat pada pagi hari ini."

        "Setelah mengecek jawaban no 4, kamu langsung membaca soal terakhir yang terdapat pada lembar soal ujian."
        hide screen basdatas_4 with dissolve
        jump soalbasdat5

    label telat_basdat4:
        "Kamu terlambat menjawab pertanyaan, soal no 4 dilewati"
    
    hide screen basdatas_4 with dissolve

    label soalbasdat5:
        $ time = 45
        $ timer_range = 45
        $ timer_jump = 'telat_basdat5'

        show screen basdatas_5 with dissolve
        "5. Manakah dibawah ini yang merupakan perintah untuk memasukan data mahasiswa dengan nama ‘Yono’ pada tabel ‘Mahasiswa’?"
        show screen countdown
        menu:

            "A. INSERT INTO mahasiswa (nama) VALUES (‘Yono’)":
                "a. INSERT INTO mahasiswa (nama) VALUES (‘Yono’)"
                mc "Kayaknya bener…."

            "B. INSERT INTO nama_mahasiswa (‘Yono)":
                "b. INSERT INTO nama_mahasiswa (‘Yono)"
                mc "Hmmm….."

            "C. INSERT INTO Mahasiswa (nama) VALUES (‘Yono’)":
                "c. INSERT INTO Mahasiswa (nama) VALUES (‘Yono’)"
                "mc Harusnya yang ini bener sih……."
                $ a_basdatAS +=5

            "D. INSERT INTO Mahasiswa_name (‘Yono’)":
                "d. INSERT INTO Mahasiswa_name (‘Yono’)"
                mc "Kaya ada yang salah…."
        hide screen countdown
        "Setelah memilih jawaban untuk pertanyaan terakhir, semua soal yang terdapat pada lembar soal ujian sudah kamu selesaikan."
        hide screen basdatas_5 with dissolve
        jump end_basdat

    label telat_basdat5:
        "Kamu terlambat menjawab pertanyaan, soal no 5 dilewati"

    hide screen basdatas_5 with dissolve

    label end_basdat:

        "Kamu melihat sekelilingmu, masih ada temanmu yang masih mengerjakan ujian, namun ada juga yang sudah beranjak dari bangku ujian."

        "Sebelum mengumpulkan jawaban, tidak lupa kamu mengecek apakah biodata dan jawaban yang kamu isi semuanya sudah benar."

        "Selesai mengecek, kamu berdiri dari bangkumu dan berjalan menuju meja dosen untuk mengumpulkan lembar jawaban ujianmu."

        "Lalu tidak lupa untuk mengambil tas ransel milikmu yang ketika ujian berlangsung diletakkan di depan kelas secara rapi."

        "Ujian pertamamu dalam hari yang kedua telah selesai, kamu berjalan keluar dari ruang kelas ujian"

        "Keluar dari ruang kelas ujian, menandakan kamu telah menyelesaikan ujian akhir mata kuliah Basdat, kamu merasa senang namun kamu belum bisa merasa lega karena pada hari ini masih tersisa satu ujian akhir mata kuliah lainnya."

        scene bg campus upper hall with fade

        pause 1.5

        call istirahat_uas

        jump uas_web

label attend_basdat:

    $ a_basdatA +=1
    $ a_basdatN +=8

    return