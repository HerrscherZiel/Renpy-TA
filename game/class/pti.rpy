
default a_ptiA = 0
default a_ptiT = 0
default a_ptiC = 0
default a_ptiTS = 0
default a_ptiAS = 0
default a_ptiN = 0

label pti_1:

    scene bg campus class with fade

    pa normal "Kalau begitu bapak mulai perkuliahannya, hari ini kita akan memperlajari mengenai Pengantar Teknologi Informasi."

    pa "Karena ini baru pertemuan pertama, bapak akan menjelaskan dasarnya terlebih dahulu."

    "Kemudian Pak Andy yang semula berdiri di depan kelas, menempati tempat duduk dosen dan mengambil laptop yang ada di dalam tasnya. 
    Pak Andy memulai pengajaran sembari menghubungkan laptopnya dengan proyektor."

    "Setelah kabel terhubung, dan proyektor mulai menampilkan apa yang ada pada layar laptop Pak Andy."

    "Terlihat proyektor memperlihatkan slide suatu file powerpoint."

    show screen pti_1

    pa "Pada mata kuliah Pengantar Tekonologi Informasi ini kita akan mempelajari tentang pengetahuan mengenai teknologi dasar dan komunikasi."

    pa "Disini nanti kita akan mempelajari semua tentang teknologi, mulai dari pengertian, sejarah perkembangan, contoh, manfaat, dan implementasi."

    pa "Teknologi Informasi adalah semua teknologi yang dapat digunakan untuk dapat digunakan oleh manusia untuk dapat membuat, mengubah, menyimpan, memproses, dan menyebarkan serta menerima informasi."

    pa "Teknologi Informasi sudah ada sejak zaman pra sejarah, mulai dari coretan-coretan manusia prasejarah pada dinding goa yang menggambar kejadian atau aktivitas mereka."

    "Slide presentasi yang sedang dipresentasikan menunjukkan gambar perkembangan teknologi dari yang terdahulu."

    pa "Kemudian ketika zaman sudah berkembang namun teknologi modern belum ditemukan, manusia mulai melakukan penulisan menggunakan symbol-symbol dalam kulit kayu."

    pa "Lalu pada saat ini setelah teknologi informasi modern ditemukan contoh teknologi yang digunakan adalah seperti personal komputer, laptop, handphone, radio, alat elektronik lainnya, media cetak, pustaka yang ada pada internet, dan lain sebagainnya."

    "Kemudian gambar-gambar contoh teknologi informasi terkini ditampilkan pada slide presentasi."

    hide screen pti_1

    show screen pti_1_2 with fade

    pa "Contoh teknologi informasi modern adalah seperti personal komputer, laptop, handphone, radio, alat elektronik lainnya, media cetak, pustaka yang ada pada internet, dan lain sebagainnya."

    pa "Teknologi Informasi modern sudah biasa kita gunakan dalam kehidupan sehari-hari. Selain itu teknologi informasi juga kita gunakan dalam berbagai sektor seperti pekerjaan, pendidikan, perekonomian, sosial, maupun kesehatan."

    pa "Era globalisasi yang ada juga mendorong perkembangan teknologi dengan cepat. Sudah sebaiknya agar kita tidak tertinggal dengan kemajuan zaman, kita juga ikut menggunakan teknologi yang ada untuk membantu kegiatan kita."

    pa "Meskipun begitu, sebagai manusia yang berpendidikan kita harus cermat dalam menggunakan teknologi yang ada, jangan menggunakannya untuk hal yang tidak baik."

    pa "Ohh jam pertemuannya ternyata sudah mau habis, sebelum bapak tutup pertemuan kalini mungkin ada pertanyaan dari kalian?"

    hide screen pti_1_2 with fade

    "Beberapa dari temanmu mengajukan pertanyaan, dan Pak Andypun menjawab pertanyaan mereka."

    r normal2 "Pak untuk materi presentasi pertemuan ini apakah kami boleh memintanya pak?"

    pa "Ohh boleh-boleh, nanti kamu atau perwakilan kelas chat saya saja, akan saya share materi hari ini."

    r "Baik pak, terimakasih."

    pa "Sebelum bapak tutup, bapak ada tugas untuk kalian, tugasnya gampang kok."

    pa "Carilah masing-masing 2 teknologi informasi modern dan implementasinya dalam bidang Kesehatan dan Pendidikan."

    "{i}Tutorial tugas!{i}"

    "Tugas terkadang akan diberikan oleh dosen pada suatu mata kuliah."

    "Menyelesaikan tugas akan memberikan point tambahan pada stat akademik kalian!"

    "Informasi mengenai Tugas dapat diakses menggunakan menu tugas, dan dapat dikerjakan ketika kalian memilih ikon mengerjakan tugas pada menu {b}MAP{/b}."

    "Mengerjakan tugas akan menghabiskan satu fase waktu, jadi pilihlah waktu yang tepat!!"

    "Pada satu waktu pengerjaan tugas kalian dapat mengerjakan 2 tugas."

    "Tugas akan habis waktu pengerjaannya ketika sudah melakukan pertemuan mata kuliah tersebut pada minggu setelahnya."

    $ my_task.addTask(task_pti_1)

    call screen tutorial_task1 with dissolve

    pa "Nanti hasilnya dijadikan satu dan diupload di drive, lalu bapak tolong dikirimi linknya ya."

    r "Baik pak."

    pa "Kalau begitu kelas hari ini bapak tutup, terimakasih telah mengikuti kelas hari ini, sampai jumpa pada pertemuan selanjutnya."

    t normal "Terimakasihhh…."

    call attend_pti
    call attend_class

    pause 1.5

    jump pre_alpro

label pti_2:

    scene bg campus class with fade

    pa normal "Selamat siang kini kita bertemu kembali pada pertemuan ke 2 dari mata kuliah Pengantar Teknologi Informasi."

    pa "Pada pertemuan kali ini kita akan membahas mengenai perbedaan data, informasi, dan pengetahuan. 
    Selain itu kalau masih sempat saya akan menjelaskan sedikit mengenai sistem informasi."

    "Kemudian [pa] menghubungkan latopnya dengan proyektor."

    "Setelah proyektor telah jelas menayangkan apa yang disajikan di laptop, kelaspun dimulai."

    show screen pti_2

    pa "Pertama, apa itu data, informasi, dan pengentahuan."

    pa "Data merupakan sebuah fakta atau keterangan pasti yang dapat direpresentasikan sebagai symbol, gambar, teks, suara, atau sinyal."

    pa "Sementara Informasi merupakan hasil dari pemrosesan atau pengolahan data sehingga mampu memberikan gambaran yang lebih jelas mengenai suatu hal."

    pa "Pengetahuan merupakan informasi yang telah ditelaah sedemikian rupa sehingga mampu membuat seseorang untuk memahami suatu hal."

    pa "Untuk lebih mudahnya semisal, kita memiliki data bahwa suhu saat ini adalah 13 derajat celcius."

    pa "Informasi yang kita dapat adalah suhu saat ini sedang dingin."

    pa "Lalu dengan informasi yang didapatkan kita memiliki pengetahuan karena suhu dingin, lebih baik kita memakai pakaian yang hangat agar tidak kedinginan."

    pa "Ya kurang lebih seperti itu untuk Data, Informasi, dan Pengetahuan."

    hide screen pti_2

    show screen pti_2_2 with fade

    pa "Kita lanjut ke pembahasan yang selanjutnya yaitu Sistem Operasi(SO)."

    pa "Apasih Sistem Operasi itu ? Sistem Operasi atau yang biasa disingkat dengan SO merupakan sebuah sistem perangkat lunak yang berfungsi 
    untuk mengelola sumber daya dan mengoperasikan perangkat lunak maupun perangkat keras pada suatu perangkat komputasi seperti komputer, tablet, ataupun smartphone."

    pa "Beberapa fungsi dari sistem operasi adalah sebagai berikut:"

    pa "Sistem operasi menjadi dasar bagi perangkat lunak lain untuk menjalankan operasi, karena fungsinya yang menjalankan operasi dasar."

    pa "Kemudian sistem operasi juga berfungsi sebagai pengatur kinerja perangkat keras pada komputer."

    pa "Lalu sistem operasi juga mampu berfungsi sebagai tempat penyimpanan perangkat lunak lainnya."

    pa "Visualisasi atau tampilan pada komputer maupun smarthphone juga merupakan hasil olahan dari sistem operasi."

    pa "Tidak kalah pentingnya dengan fungsi yang lain, sistem operasi juga memiliki fungsi sebagai sistem pengaman, yang mampu membantu keamanan data-data yang ada."

    hide screen pti_2_2

    show screen pti_2_3 with fade

    pa "Untuk contohnya sendiri mungkin kalian juga sudah pada tahu, bapak akan berikan beberapa contoh disini."

    pa "Windows, merupakan salah satu sistem operasi yang sangat sering digunakan, kebanyakan perangkat lunak kompatibel dengan Windows. 
    Namun karena memiliki banyak pemakai, sistem operasi ini rentan akan serangan virus."

    pa "Linux, merupakan salah satu sistem operasi yang mudah untuk diubah atau dimodifikasi sesuai kebutuhan. 
    Tentu saja untuk melakukannya diperlukan keahlian, hal tersebut juga menjadi kelemahan dari sistem operasi ini karena proses instalasi dan penggunaannya relatif lebih sulit."

    pa "MAC OS, merupakan sistem operasi khusus buatan Apple Computer yang hanya dapat digunakan pada mesin macintosh. 
    Memiliki sistem keamanan yang kuat namun memiliki harga yang relatif mahal."

    "Mendengarkan penjelasan [pa], kamu mencatat poin-poin penting yang dijelaskan."

    "[pa] menjelaskan slide-slide yang ada secara runtut."

    "Pertemuan kali ini menambah pengetahuanmu mengenai Sistem Operasi."

    "[pa] menjelaskan hingga akhirnya waktu pertemuan berakhir."

    hide screen pti_2_3

    pa normal "Cukup sekian dari saya, sampai ketemu lagi pada pertemuan berikutnya teman-teman."

    t normal "Terimakasih…"

    r normal2 "Terimakasih…"

    "[pa] meninggalkan ruangan, dan kelas pertama pada hari ini berakhir."

    call attend_pti
    call attend_class

    pause 1.5
    jump alpro_2

label pti_3:

    "PTI 3"

    jump alpro_3

label pti_4:

    "PTI 4"

    jump alpro_4

label attend_pti:

    $ a_ptiA +=1
    $ a_ptiN +=8

    return


