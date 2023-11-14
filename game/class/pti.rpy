
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

    show screen pti_1 with fade

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

    "{i}Tutorial tugas!{/i}"

    "Tugas terkadang akan diberikan oleh dosen pada suatu mata kuliah."

    "Menyelesaikan tugas akan memberikan point tambahan pada stat akademik kalian!"

    "Informasi mengenai Tugas dapat diakses menggunakan menu tugas, dan dapat dikerjakan ketika kalian memilih ikon mengerjakan tugas pada menu {b}MAP{/b}."

    pa "Mengerjakan tugas akan menghabiskan satu fase waktu, jadi pilihlah waktu yang tepat!!"

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

label uts_pti:

    scene bg campus class with dissolve

    show screen trans_screen with dissolve
    pause 2.0

    pa normal "Selamat pagi teman-teman pada pagi hari ini kita akan melakukan ujian tengah semester untuk mata kuliah pengantar teknologi informasi."

    pa "Bapak harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    pa "Soal saya bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    pa "Bapak harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Kamu memandang soal ujian, terdapat keterangan seperti nama mata kuliah, tanggal ujian, jam ujian, dan waktu ujian."

    "(Pada {b}game ini{/b} UTS hanya akan memiliki 5 soal pilihan ganda!)"

    "(Setiap pertanyaan akan ditampilkan dan bisa dijawab dalam waktu 90 detik)"

    "(Setelah menjawab pertanyaan, akan langsung menuju pertanyaan berikutnya)"

    "(Jawaban tidak bisa diubah dan Soal akan ditampilkan secara urut berdasarkan nomor soal)"

    "(Setelah pemain menjawab nomor terakhir, maka uts akan berakhir.)"

    "(Perlu diketahui UTS pada kampus dapat dilaksankan dengan berbagai macam cara, dengan cara ujian umumnya mahasiswa akan menjawab soal yang diberikan dalam batas waktu tertentu.)"

    "(Soal UTS seringkali berbentuk uraian dan penilaiannya tergantung dari masing-masing dosen pengajar.)"

    "Setelah paham dengan peraturan ujian kali ini, kamu mulai menulis biodatamu pada lembar jawaban yang telah diterima."

    "Kemudian kamu bersiap menjawab pertanyaan yang ada."

    "Mulai UTS?"

    menu: 
        "Mulai":
            "Setelah mempersiapkan diri, kamu siap mengerjakan soal UTS"
    
    "1. Manakah dari pernyataan dibawah yang benar dan sebaiknya kita lakukan mengenai teknologi informasi?"
    menu:
        "A. Teknologi Informasi merupakan teknologi-teknologi yang bisa dan hanya bisa membantu dalam bidang kesehatan.":
            "A. Teknologi Informasi merupakan teknologi-teknologi yang bisa dan hanya bisa membantu dalam bidang kesehatan."
        "B. Teknologi Informasi baiknya kita jauhi karena hanya dapat memberi dampak-dampak yang buruk.":
            "B. Teknologi Informasi baiknya kita jauhi karena hanya dapat memberi dampak-dampak yang buruk."
        "C. Teknologi Informasi sudah layaknya tidak kita gunakan, lebih baik menggunakan cara yang lebih tradisional.":
            "C. Teknologi Informasi sudah layaknya tidak kita gunakan, lebih baik menggunakan cara yang lebih tradisional."
        "D. Teknologi Informasi adalah semua teknologi yang dapat digunakan untuk dapat digunakan oleh manusia untuk dapat membuat, mengubah, menyimpan, memproses, dan menyebarkan serta menerima informasi.":
            "D. Teknologi Informasi adalah semua teknologi yang dapat digunakan untuk dapat digunakan oleh manusia untuk dapat membuat, mengubah, menyimpan, memproses, dan menyebarkan serta menerima informasi."
            $a_ptiTS +=20
        "E. Teknologi Informasi baiknya hanya kita gunakan hanya dalam bidang pendidikan.":
            "E. Teknologi Informasi baiknya hanya kita gunakan hanya dalam bidang pendidikan."
    "2. Manakah dari teknologi informasi dibawah yang dapat kita gunakan untuk membantu kita dalam berkomunikasi jarak jauh dengan teman kita yang berada pada pulau yang berbeda?"
    menu:
        "A. Handphone.":
            "A. Handphone."
            $a_ptiTS +=20
        "B. Mobil.":
            "B. Mobil."
        "C. Kereta.":
            "C. Kereta."
        "D. Kamera":
            "D. Kamera."
        "E. Teropong.":
            "E. Teropong."
    "3. Apakah yang dimaksud dengan Informasi?"
    menu:
        "A. Informasi merupakan sebuah fakta-fakta yang kita dapatkan melalui penelitian.":
            "A. Informasi merupakan sebuah fakta-fakta yang kita dapatkan melalui penelitian."
        "B. Informasi merupakan data lapangan dari suatu kegiatan praktik.":
            "B. Informasi merupakan data lapangan dari suatu kegiatan praktik."
        "C. Informasi merupakan pengetahuan mengenai fakta-fakta yang ada untuk memecahkan suatu permasalahan.":
            "C. Informasi merupakan pengetahuan mengenai fakta-fakta yang ada untuk memecahkan suatu permasalahan."
        "D. Informasi merupakan hasil pemrosesan dari fakta-fakta yang mampu memberikan gambaran lebih jelas mengenai sesuatu.":
            "D. Informasi merupakan hasil pemrosesan dari fakta-fakta yang mampu memberikan gambaran lebih jelas mengenai sesuatu."
            $a_ptiTS +=20
        "E. Informasi merupakan sebuah pengetahuan yang didapatkan dari sebuah hal fiksi.":
            "E. Informasi merupakan sebuah pengetahuan yang didapatkan dari sebuah hal fiksi."
    "4. Dari beberapa opsi dibawah ini apakah yang termasuk data yang diambil dari lingkungan sekolah?"
    menu:
        "A. Jumlah murid.":
            "A. Jumlah kendaraan."
        "B. Jumlah guru.":
            "B. Jumlah guru."
        "C. Jumlah ruang kelas.":
            "C. Jumlah ruang kelas."
        "D. Jumlah mata pelajaran.":
            "D. Jumlah mata pelajaran."
        "E. Jumlah kendaraan.":
            "E. Jumlah kendaraan."
            $a_ptiTS +=20
    "5. Manakah dari pernyataan dibawah ini yang merupakan fungsi sebuah Sistem Operasi?"
    menu:
        "A. Sistem operasi tidak dapat berfungsi sebagai tempat penyimpanan perangkat lunak lainnya.":
            "A. Sistem operasi tidak dapat berfungsi sebagai tempat penyimpanan perangkat lunak lainnya."
        "B. Visualisasi bukanlah merupakan salah satu hasil dari olahan dari sistem operasi.":
            "B. Visualisasi bukanlah merupakan salah satu hasil dari olahan dari sistem operasi."
        "C. Sistem Operasi bukan hanya mampu memberikan keamanan data namun juga mampu mengatur kinerja dari komputer.":
            "C. Sistem Operasi bukan hanya mampu memberikan keamanan data namun juga mampu mengatur kinerja dari komputer."
            $a_ptiTS +=20
        "D. Sistem operasi tidak menjadi merupakan dasar untuk perangkat lunak lain untuk melakukan operasi.":
            "D. Sistem operasi tidak menjadi merupakan dasar untuk perangkat lunak lain untuk melakukan operasi."
        "E. Tidak adanya sistem operasi tidak akan memengaruhi kinerja perangkat keras.":
            "E. Tidak adanya sistem operasi tidak akan memengaruhi kinerja perangkat keras."

    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega sekaligus cemas akan hasil yang didapat nanti."

    "Mengumpulkan kertas ujianmu, kamu memasukan barang-barangmu pada tas yang sebelumnya dikelompokan dengan rapi di depan kelas."

    "Kemudian kamu segera keluar dari dalam kelas. Di luar sebelumnya sudah ada beberapa mahasiswa yang keluar lebih dahulu sebelum dirimu."

    "Di luar ruangan, kamu dan temanmu yang telah selesai mengerjakan UTS Pengantar Teknologi Informasi sempat membahas mengenai jawaban dari masing-masing soal yang ada."

    "Lalu sembari menunggu mahasiswa lain selesai mengerjakan dan UTS mata kuliah berikutnya dilakukan kamu mengobrol santai dan membaca materi dari mata kuliah yang akan di UTSkan berikutnya."

    jump uts_alpro

label pti_3:

    scene bg campus class with fade

    # Keamanan, contoh kejahatan, contoh malware


    "Kamu masuk ke dalam ruang kelas, di dalam kelas belum terlihat banyak mahasiswa yang telah menempati tempat duduknya."

    "Mungkin karena hari ini merupakan hari pertama perkuliahan dimulai kembali setelah dilaksanakannya ujian tengah semester pada minggu lalu."

    "Seperti sebelum-sebelumnya, kamu memilih untuk duduk pada bangku yang terletak dekat dengan jendela dan berada pada barisan tengah kelas."

    "Sembari menunggu kamu mengeluarkan HPmu dan memainkan beberapa aplikasi yang terdapat di dalam HPmu."

    "Kemudian selagi kamu sibuk dengan HPmu, satu persatu mahasiswa mulai memasuki ruang kelas, sebelum pada akhirnya [pa] juga memasuki ruangan."

    "Hari ini merupakan pertemuan ke-3 mata kuliah PTI" 
    
    "Kelas dimulai setelah [pa] selesai mengatur peralatannya."

    scene bg campus class with dissolve

    pa normal "Selamat pagi teman-teman kita bertemu lagi setelah minggu kemarin kalian telah melaksanakan ujian tengah semester."

    pa "Pagi ini kita bertemu lagi pada mata kuliah PTI pertemuan ke-3, dimana kita akan membahas mengenai keamanan teknologi informasi,
    meningkatkan keamanan data, contoh kejahatan cybercrime, dan contoh malware."

    pa "Sebelumnya, sebenarnya mengapa keamanan teknologi informasi itu penting? Ada yang mau jawab?"

    menu:
        "Acungkan Jari":

            mc normal jacket "Karena dengan memiliki keamanan yang memadai, kita bisa terhindar dari kemungkinan tindakan-tindakan yang berhubungan dengan teknologi informasi yang dapat merugikan kita?"

            pa "Ya apa yang kamu katakan itu ada benarnya, karena sesuai namanya keamanan akan terhubung dengan tindakan atau kegiatan yang dapat merugikan."

            pa "Dengan keamanan teknologi informasi tersebut kita dapat mencegah maupun menanggulangi kejahatan cyber yang mungkin terjadi."

            $a_ptiC += 5

        "Menunggu mahasiswa lain mengacungkan jari":

            t normal"Untuk menjauhkan data kita dari tindakan atau kejahatan cyber yang dapat merugikan kita pak."

            pa "Ya apa yang kamu katakan itu ada benarnya, karena sesuai namanya keamanan akan terhubung dengan tindakan atau kegiatan yang dapat merugikan."

            pa "Dengan keamanan teknologi informasi tersebut kita dapat mencegah maupun menanggulangi kejahatan cyber yang mungkin terjadi."

            pa "Untuk lebih lengkapnya bapak mulai saja perkuliahannya, perhatikan slide-slide berikut teman-teman."

    "[pa] membuka slide yang berisikan materi pengajaran PTI untuk hari ini."

    show screen pti_3_1

    pa class "Menurut G.J. Simmons, keamanan sistem informasi merupakan langkah-langkah pencegahan yang dilakukan pada suatu sistem berbasis 
    informasi yang berbentuk non-fisik dengan tujuan untuk mencegah tindakan-tindakan penipuan."

    pa "Dapat kita simpulkan juga keamanan sistem informasi merupakan sebuah prosedur yang dapat digunakan dalam mencegah kegiatan-kegiatan yang mampu merugikan 
    sistem-sistem informasi seperti tindakan pencurian data, akses tidak sah, merusak bagian sistem, dan lain sebagainya."

    pa "Sistem keamanan yang dapat kita gunakan dalam melindungi sistem informasi kita meliputi perangkat keras, perangkat lunak, jaringan komunikasi, dan data yang kita miliki."

    pa "Itu sedikit pengertian mengenai keamanan sistem informasi, sekarang kita akan membahas mengenai hal-hal 
    yang dapat dilakukan untuk meningkatkan keamanan sistem informasi."

    hide screen pti_3_1

    show screen pti_3_2 with fade

    pa "Untuk meningkatkan keamanan pada sistem informasi yang kita miliki kita dapat melakukan beberapa hal."

    pa "Hal yang dapat kita lakukan untuk mencegah atau meminimalisir terjadinya hal-hal yang tidak kita inginkan adalah."

    pa "1. Memiliki sistem keamanan untuk memisahkan klasifikasi data, sehingga data-data dapat dipisahkan mana yang dapat diakses oleh banyak orang dan mana data yang bersifat rahasia dimana hanya beberapa orang saja yang dapat mengakses."

    pa "2. Pastikan data terenkripsi ketika melakukan transfer data. Hal ini penting karena jika data tidak terenkripsi ketika melakukan transfer data terdapat kemungkinan dimana data tersebut bocor dan dapat dilihat pihak yang tidak diinginkan."

    pa "3. Memiliki autentikasi berlapis, hal ini diperlukan sehingga akun atau proses yang dimiliki tidak mudah untuk dibobol oleh orang lain. Contohnya adalah penggunaan password dan OTP ketika melakukan proses log in."

    pa "4. Ketika melakukan akses terhadap data-data yang sangat rahasia, baiknya kita menggunakan perangkat keras pribadi, untuk menghindari kebocoran data atau akses dari pihak yang tidak diinginkan."

    pa "5. Menggunakan perangkat lunak anti malware. Hal ini dapat membantu kita dalam mencegah perangkat lunak lain yang dapat berakibat negatif masuk dalam sistem informasi kita."

    pa "Kurang lebih seperti itu hal-hal yang dapat kita lakukan untuk memperkuat keamanan sistem kita, sebenarnya masih banyak lagi jika kita cari tahu lebih dalam."

    pa "Selanjutnya kita akan membahas mengenai contoh-contoh dari kejahatan digital atau cybercrime."

    hide screen pti_3_2

    show screen pti_3_3 with fade

    pa "Cybercrime merupakan bentuk kejahatan yang terjadi di dunia maya. Contoh atau bentuk tindakan kejahatan yang dapat terjadi adalah sebagai berikut:"

    pa "1. {b}Serangan Malware{/b}, atau Malicious Ware yang merupakan sebuah perangkat lunak yang berisikan kode berbahaya ketika masuk ke dalam sistem, jaringan, maupun server yang kita miliki. "

    pa "Malware dapat masuk melalui berbagai macam cara, seperti email, data yang kita unduh, aplikasi palsu, maupun web-web tidak aman yang kita kunjungi."

    pa "2. {b}Phising{/b}, phising merupakan sebuah cybercrime yang biasanya menargetkan data pribadi seseorang seperti password, kartu kredit, maupun data pribadi lainnya. Phising dapat dilakukan dengan menyamar atau mengirimkan sebuah pesan palsu yang mirip dengan yang asli sehingga korban tertipu dan menuliskan data pribadinya."

    pa "3. {b}Hacking{/b}, hacking merupakan tindak cybercrime dimana pelaku masuk kedalam sistem melalui celah keamanan kemudian mencuri data, merusak sistem, atau mengekspos data yang ditemukan."

    hide screen pti_3_3

    show screen pti_3_4 with fade

    pa "4. {b}DDoS atau Distributed Denial-of-Service{/b}, merupakan sebuah cybercrime yang menargetkan sebuah jaringan, web, atau server dengan cara meningkatkan trafik target menjadi sangat tinggi yang akan menyebabkan overload atau kelebihan kapasitas sehingga target tidak dapat dikunjungi atau diakses."

    pa "5. {b}Pembajakan{/b}, banyak sekali ditemui penyebaran seperti film bajakan yang dengan mudah bisa di download oleh khalayak umum. Tentu saja pembajakan seperti akan menyebabkan kerugian material bagi produsen itu sendiri."

    pa "Itu merupakan beberapa contoh kejahatan digital atau cyber. Baiknya setelah kita mengetahui hal-hal tersebut kita dapat menjadi lebih berhati-hati sehingga terhindar dari segala bentuk kejahatan cyber."

    pa "Karena tadi juga sempat dijelaskan mengenai malware, kita juga akan membahas mengenai beberapa malware."

    hide screen pti_3_4

    show screen pti_3_5 with fade

    pa "1. Virus, virus merupakan sebuah malware yang mampu menduplikasi dirinya sendiri. Ketika masuk ke dalam sebuah folder dalam komputer serangkaian kode virus akan bekerja dan mampu memodifikasi dan menginfeksi file-file yang terdapat di dalamnya. "

    pa "Virus dapat disebarkan melalui berbagai macam cara seperti, e-mail, file unduhan, jaringan yang kita sambungkan, bahkan melalui port usb yang kita gunakan."

    pa "2. Keylogger, sesuai namanya malware yang satu ini mampu menyimpan aktivitas pengetikan yang kita lakukan, sehingga pelaku mengetahui data-data sensitif seperti password yang kita ketikan."

    pa "3. Worm, worm merupakan sebuah malware yang mirip dengan virus. Worm mampu menduplikasi dirinya sendiri bahkan tanpa memerlukan bantuan kita. Worm biasanya digunakan untuk menyerang server sebuah website dan database."

    hide screen pti_3_5

    show screen pti_3_6 with fade

    pa "4. Trojan, Trojan merupakan salah satu malware yang mampu mencuri data dan mengakses komputer kita dengan cara menyamar menjadi salah satu perangkat lunak untuk mengelabui kita. Malware ini sering kita temui dari aktivitas phising yang terjadi pada kita."

    pa "5. Ransomware, malware ini mampu membuat kita tidak bisa mengakses file yang kita miliki dalam sistem. Untuk dapat mengakses file kita kembali, biasanya pelaku meminta kita untuk menebus dengan uang tebusan."

    pa "6. Adware, adware sendiri bukanlah sebuah malware yang bisa langsung membahayakan sistem kita. Namun dengan adanya adware, malware-malware bisa memasuki sistem yang kita miliki. Sesuai namanya adware merupakan sebuah malware yang menampilkan banyak iklan-iklan yang terus bermunculan pada layar kita."

    "Kelas dilanjutkan dengan [pa] yang menampilkan contoh-contoh dari malware yang diterangkan."

    hide screen pti_3_6 with dissolve

    "[pa] memberi contoh dengan langsung mencari contoh malware yang bisa ditemukan di internet, kemudian dilanjutkan dengan sesi tanya jawab hingga jam pelajaran usai."

    scene bg campus class with fade

    pa normal "Mungkin sampai disini dulu pertemuan kita hari ini." 
    
    pa "Terimakasih sudah mengikuti kelas pada pagi hari ini."

    pa "Oh iya sebelum saya tutup, saya mau memberi tahu kalau nilai ujian kemarin sudah keluar ya."

    "Mendengar informasi mengenai hasil ujian tengah semester kemarin, terdapat beberapa reaksi dari teman sekelasmu. Beberapa dari mereka terlihat gembira dan tidak sabar untuk melihat hasil pekerjaan mereka."

    pa "Untuk mengeceknya kalian bisa membuka simaster, kemudian menu akademik kemahasiswaan, lalu pada sub menu akademik pilih hasil studi."

    pa "Silahkan dilihat sendiri-sendiri ya."

    t normal "Baik pak terimakasih."

    pa "Kalau begitu bapak tutup, cukup sekian dan terimakasih sampai bertemu di pertemuan berikutnya."

    t "Terimakasih."

    r normal2 "Terimakasih pak."

    "Kelas berakhir, mahasiswa satu persatu meninggalkan ruangan. Menunggu untuk beberapa menit sebelum memasuki ruang kelas selanjutnya."

    call attend_pti
    call attend_class

    pause 1.5
    jump alpro_3

label pti_4:

    scene bg campus class with dissolve

    "Kamu memasuki ruang kelas pertama untuk perkuliahan hari ini, belum terlihat banyak mahasiswa yang sudah berada di dalam kelas."

    "Hari ini merupakan pertemuan terakhir untuk mata kuliah pengantar teknologi informasi."

    "Seperti kelas-kelas biasanya, kamu memilih bangku yang terletak dengan jendela dan berada pada barisan tengah kelas."

    "Sembari menunggu untuk kelas dimulai, kamu mengeluarkan HPmu dan membuka beberapa aplikasi untuk menghabiskan waktu."

    "Satu persatu mahasiswa mulai memasuki ruang kelas, sebelum pada akhirnya [pa] juga memasuki ruang kelas."

    "Hari ini merupakan pertemuan ke-4 mata kuliah PTI, [pa] mengatur peralatan mengajarnya sebelum membuka pertemuan pada pagi hari ini."

    scene bg campus class with fade

    pa normal "Selamat pagi teman-teman, pada pagi hari ini kita bertemu lagi pada pertemuan terakhir mata kuliah pengantar teknologi informasi."

    pa "Pada pagi hari ini bapak akan sedikit menerangkan mengenai komponen-komponen sistem informasi."

    show screen pti_4_1 with dissolve

    pa class "Komponen yang pertama adalah perangkat keras atau hardware. Sesuai namanya hardware merupakan perangkat fisik yang ada pada sistem."

    pa "Perangkat fisik yang digunakan dapat dikelompokan menjadi beberapa kelompok seperti:"

    pa "Input device, merupakan perangkat keras yang dapat digunakan untuk memasukan data contohnya seperti keyboard, mouse, microphone, dan lain sebagainya."

    pa "Processing device, yang bekerja sebagai pusat atau otak komputer, terdiri atas CPU, graphics card, memory RAM, dan lain sebagainya."

    pa "Output device, merupakan kelompok perangkat keras yang mampu menyajikan atau menampilkan data yang ada, contohnya seperti monitor, speaker, proyektor, dan lain sebagainya."

    pa "Storage, merupakan perangkat keras yang memiliki fungsi sebagai tempat penyimpanan data, contoh dari storage adalah Harddisk, flashdisk, CD, dan lain sebagainya. "

    pa "Itu merupakan penjelasan mengenai salah satu komponen sistem informasi yaitu perangkat keras atau hardware."

    pa "Kita akan melanjutkan pembahasan mengenai komponen selanjutnya."
    
    pa "Komponen dari sistem informasi yang kedua adalah perangkat lunak atau sering kita sebut dengan software. "

    hide screen pti_4_1

    show screen pti_4_2 with fade

    pa "Software dapat kita artikan sebagai program yang terdapat dalam komputer yang memiliki fungsi atau tugas tertentu."

    pa "Perangkat lunak juga dapat kita bagi ke beberapa pengelompokkan seperti:"

    pa "Sistem Operasi, perangkat lunak sistem operasi memiliki fungsi sebagai pengatur sistem kerja perangkat keras dan perangkat lunak yang ada di komputer."

    pa "Aplikasi, merupakan sebuah perangkat lunak yang sering kita gunakan untuk menyelesaikan tugas atau kebutuhan tertentu."

    pa "Bahasa pemrograman, perangkat lunak bahasa pemrograman merupakan perangkat lunak yang memiliki fungsi sebagai penerjemah instruksi-instruksi dari bahasa program ke kode bahasa mesin tertentu 
    melalui sebuah prosedur agar mampu dibaca dan diterima oleh komputer."

    pa "Kurang lebih seperti itu untuk pembahasan komponen perangkat lunak"

    pa "Lalu komponen sistem informasi yang berikutnya adalah Jaringan Telekomunikasi."

    hide screen pti_4_2

    show screen pti_4_3 with fade

    pa "Jaringan telekomunikasi disini memungkinkan komunikasi dan menghubungkan perangkat satu sama lain, baik untuk mendapatkan informasi baru atau saling bertukar informasi."

    pa "Jaringan komunikasi mungkin kalian sudah mendengar dari mata kuliah lain dapat dilakukan menggunakan wired ataupun wireless."

    pa "Jaringan Kabel, merupakan jaringan telekomunikasi yang menggunakan kabel fisik untuk mentransmisikan data."

    pa "Jaringan kabel memiliki kecepatan transfer yang lebih cepat namun lebih rumit dalam pengelolaan dan pemeliharaannya."

    pa "Jaringan Nirkabel(wireless), merupakan jaringan telekomunikasi yang menggunakan gelombang radio atau sinyal mikro dalam mentransmisikan datanya."

    pa "Jaringan Nirkabel memiliki keunggulan dalam mobilitasnya, namun memiliki kecepatan yang lebih rendah daripada jaringan kabel serta rentan terkena gangguan sinyal."

    pa "Masih terdapat dua komponen yang ada setelah komponen jaringan."

    pa "Komponen sistem informasi berikutnya adalah basis data."

    hide screen pti_4_3

    show screen pti_4_4 with fade

    pa "Basis data seperti yang mungkin sudah kalian ketahui dapat digunakan untuk menyimpan semua data-data yang terdapat pada sistem. "

    pa "Dengan penggunaan basis data, akan mempermudah kita dalam berbagai macam hal seperti, penyimpanan data, pengelompokan data, keamanan, analisa, dan lain sebagainya."

    pa "Kemudian komponen sistem informasi yang berikutnya adalah sumber daya manusia."

    pa "Tentu saja manusia sebagai pelaku atau penggerak utama semua komponen-komponen lainnya diperlukan dalam pengoperasian sebuah sistem informasi."

    pa "Komponen-komponen sistem informasi yang disebutkan sebelumnya juga dapat membantu manusia dalam pengoperasian sistem informasi."

    pa "Jadi itu kurang lebih seperti komponen-komponen yang terdapat pada sistem informasi."

    pa "Mulai dari perangkat keras, perangkat lunak, jaringan komunikasi, basis data dan manusia."

    pa "Semua komponen merupakan komponen-komponen yang ada dan membentuk sebuah sistem informasi."

    hide screen pti_4_4 with fade

    pa normal "Mungkin materi pagi hari ini sampai disini dulu ya, mungkin ada yang ingin ditanyakan?"

    "Kelas dilanjutkan dengan sesi tanya jawab hingga kelas waktu pertemuan telah habis."

    scene bg campus class with Dissolve(2.0)

    pa normal "Karena ini pertemuan terakhir mata kuliah ini jadi bapak ucapkan terimakasih sudah mengikuti mata kuliah ini."

    pa "Untuk materi yang digunakan untuk ujian akhir semester nanti adalah materi yang bapak ajarkan setelah ujian tengah semester kemarin ya?"

    t normal "Berarti materi pertemuan 3 dan hari ini ya pak?"

    pa "Iya benar, materi pertemuan 3 dan 4 ya teman-teman."

    t "Baik pakk."

    pa "Nanti kalau ada pertanyaan tinggal tanya langsung saja ya."

    r normal2 "Baik pak."

    pa "Ya sudah, pertemuan kali ini bapak tutup, sekian dan terimakasih teman-teman."

    t "Terimakasih pak."

    t "Terimakasihhh"

    r "Terimakasih [pa]"

    "Kelas ditutup, [pa] meninggalkan ruang kelas disusul dengan teman-temanmu keluar dari ruang kelas satu persatu."

    "Masih terdapat beberapa menit sebelum kelas selanjutnya dimulai."

    call attend_pti
    call attend_class

    pause 1.5
    jump alpro_4

label attend_pti:

    $ a_ptiA +=1
    $ a_ptiN +=8

    return


