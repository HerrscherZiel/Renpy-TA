
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

    jump jarkom_2

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