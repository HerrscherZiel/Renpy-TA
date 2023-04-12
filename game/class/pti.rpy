
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

    pa "Pada mata kuliah Pengantar Tekonologi Informasi ini kita akan mempelajari tentang pengetahuan mengenai teknologi dasar dan komunikasi."

    pa "Disini nanti kita akan mempelajari semua tentang teknologi, mulai dari pengertian, sejarah perkembangan, contoh, manfaat, dan implementasi."

    pa "Teknologi Informasi adalah semua teknologi yang dapat digunakan untuk dapat digunakan oleh manusia untuk dapat membuat, mengubah, menyimpan, memproses, dan menyebarkan serta menerima informasi."

    pa "Teknologi Informasi sudah ada sejak zaman pra sejarah, mulai dari coretan-coretan manusia prasejarah pada dinding goa yang menggambar kejadian atau aktivitas mereka."

    "Slide presentasi yang sedang dipresentasikan menunjukkan gambar perkembangan teknologi dari yang terdahulu."

    pa "Kemudian ketika zaman sudah berkembang namun teknologi modern belum ditemukan, manusia mulai melakukan penulisan menggunakan symbol-symbol dalam kulit kayu."

    pa "Lalu pada saat ini setelah teknologi informasi modern ditemukan contoh teknologi yang digunakan adalah seperti personal komputer, laptop, handphone, radio, alat elektronik lainnya, media cetak, pustaka yang ada pada internet, dan lain sebagainnya."

    "Kemudian gambar-gambar contoh teknologi informasi terkini ditampilkan pada slide presentasi."

    pa "Contoh teknologi informasi modern adalah seperti personal komputer, laptop, handphone, radio, alat elektronik lainnya, media cetak, pustaka yang ada pada internet, dan lain sebagainnya."

    pa "Teknologi Informasi modern sudah biasa kita gunakan dalam kehidupan sehari-hari. Selain itu teknologi informasi juga kita gunakan dalam berbagai sektor seperti pekerjaan, pendidikan, perekonomian, sosial, maupun kesehatan."

    pa "Era globalisasi yang ada juga mendorong perkembangan teknologi dengan cepat. Sudah sebaiknya agar kita tidak tertinggal dengan kemajuan zaman, kita juga ikut menggunakan teknologi yang ada untuk membantu kegiatan kita."

    pa "Meskipun begitu, sebagai manusia yang berpendidikan kita harus cermat dalam menggunakan teknologi yang ada, jangan menggunakannya untuk hal yang tidak baik."

    pa "Ohh jam pertemuannya ternyata sudah mau habis, sebelum bapak tutup pertemuan kalini mungkin ada pertanyaan dari kalian?"

    "Beberapa dari temanmu mengajukan pertanyaan, dan Pak Andypun menjawab pertanyaan mereka."

    r normal2 "Pak untuk materi presentasi pertemuan ini apakah kami boleh memintanya pak?"

    pa "Ohh boleh-boleh, nanti kamu atau perwakilan kelas chat saya saja, akan saya share materi hari ini."

    r "Baik pak, terimakasih."

    pa "Sebelum bapak tutup, bapak ada tugas untuk kalian, tugasnya gampang kok."

    pa "Carilah masing-masing 2 teknologi informasi modern dan implementasinya dalam bidang Kesehatan dan Pendidikan."

    "{i}Tutorial tugas!{i}"

    "Tugas terkadang akan diberikan oleh dosen pada suatu mata kuliah."

    "Menyelesaikan tugas akan memberikan point tambahan pada stat akademik kalian!"

    "Tugas dapat diakses menggunakan menu tugas, dan dapat dikerjakan ketika kalian memilih ikon mengerjakan tugas."

    "Mengerjakan tugas akan menghabiskan satu fase waktu, jadi pilihlah waktu yang tepat!!"

    "Pada satu waktu pengerjaan tugas kalian dapat mengerjakan 2 tugas."

    "Tugas akan habis waktu pengerjaannya ketika sudah melakukan pertemuan mata kuliah tersebut pada minggu setelahnya."

    pa "Nanti hasilnya dijadikan satu dan diupload di drive, lalu bapak tolong dikirimi linknya ya."

    r "Baik pak."

    pa "Kalau begitu kelas hari ini bapak tutup, terimakasih telah mengikuti kelas hari ini, sampai jumpa pada pertemuan selanjutnya."

    t "Terimakasihhh…."

    call attend_pti
    call attend_class

    jump pre_alpro

label attend_pti:

    $ a_ptiA +=1
    $ a_ptiN +=8

    return


