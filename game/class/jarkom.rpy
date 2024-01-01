
default a_jarkomA = 0
default a_jarkomT = 0
default a_jarkomC = 0
default a_jarkomTS = 0
default a_jarkomAS = 0
default a_jarkomN = 0

label jarkom_1:

    scene bg black with dissolve
    pause 2.0
    
    scene bg campus class with dissolve

    call awal_kelas

    scene bg campus class with fade

    bn normal "Selamat pagi teman-teman…"

    r normal2 "Pagi buu…"

    bn "Hari ini kita berjumpa lagi pada pertemuan pertama untuk mata kuliah Jaringan Komputer."

    bn "Pertemuan pertama ini kita akan membahas mengenai pengertian, tujuan, dan jenis."

    # hide screen strukdat_1_1

    show screen jarkom_1_1 with fade

    bn "Pertama, pengertian jaringan komputer adalah, jaringan komunikasi yang memungkinkan antara suatu komputer dengan komputer lainnya saling berkomunikasi dan dapat bertukar data."

    bn "Terdapat berbagai tujuan penggunaan jaringan komputer, semisal untuk membagi sumber daya seperti tukar menukar data, penggunaan perangkat keras bersama seperti hardisk, printer, dll."

    bn "Jaringan komputer juga dapat digunakan untuk komunikasi, dengan menggunakan e-mail, sosial media, chatting, dan lain sebagainya. 
    Kini kita dapat mengetahui informasi secara langsung meskipun berada pada belahan dunia yang berbeda."

    bn "Tentu saja, jaringan komputer memudahkan kita untuk mencari informasi yang telah diunggah pada suatu website."

    bn "Kemudian kita lanjut pada jenis-jenis jaringan komputer."

    bn "Jenis jaringan komputer berdasarkan geografisnya adalah sebagai berikut."

    bn "Pertama, LAN atau Local Area Network, merupakan suatu jaringan komputer yang hanya mencakup area lokal saja, biasa digunakan untuk area seperti rumah, sekolah atau kantoran."

    bn "Penggunaan LAN hanya memerlukan biaya yang relatif kecil, namun juga dengan wilayah atau jangkauan penggunaan yang kecil juga."

    hide screen jarkom_1_1

    show screen jarkom_1_2 with fade

    bn "Kedua, MAN atau Metropolitan Area Network merupakan sebuah jaringan komputer yang memiliki area jangkauan lebih luas daripada penggunaan LAN. 
    Biasanya MAN digunakan untuk menghubungkan jaringan luas namun masih terletak pada satu daerah."

    bn "Dengan area jangkauan yang lebih luas dari LAN dan biasanya dapat lebih dari 10km, WAN memiliki keefektivitasan lebih baik daripada LAN. 
    Namun tentu saja biaya yang diperlukan untuk perawatan jika terjadi kerusakan akan lebih mahal dan memakan waktu lebih lama."

    bn "Kemudian, WAN atau Wide Area Network merupakan jaringan komputer dengan cakupan area yang sangat luas. WAN dapat mencakup satu negara, antar negara, bahkan benua."

    bn "Dengan menggunakan WAN kita dapat berbagi informasi ataupun sumber daya pada area yang lebih luas. Namun dengan luasnya area cakupan tentu saja biaya operasionalnya tidaklah sedikit. 
    Penyetingan untuk membuat jaringan WAN juga lebih sulit dan rumit."

    "Kamu mencatat apa yang kamu rasa perlu, dan memerhatikan apa yang diterangkan oleh [bn]"

    "[bn] menjelaskan materi perkuliahan hingga waktu pertemuan berakhir."

    hide screen jarkom_1_2

    bn normal "Selesai untuk pertemuan kita hari ini, sampai jumpa minggu depan teman-teman…"

    r normal2 "Sampai jumpa bu…"

    t normal "Terimakasih…"

    bn "Selamat menikmati akhir pekan…."

    "Dengan ditutupnya pembelajaran mata kuliah ini, berakhir sudah kuliah pada hari ini."

    "Namun sebelum ada satupun mahasiswa yang meninggalkan ruangan, tiba-tiba [r] berdiri dan membicarakan suatu hal."

    call attend_jarkom
    call attend_class

    jump first_hima

label jarkom_2:

    "Jarkom 2"

    scene bg campus class with dissolve

    call awal_kelas

    scene bg campus class with fade

    "[bn] memasuki ruang kelas, pertemuan kedua untuk hari ini akan segera dimulai"

    bn normal "Selamat pagi teman-teman…"

    r normal2 "Pagi buu…"

    bn "Hari ini kita berjumpa lagi pada pertemuan kedua untuk mata kuliah Jaringan Komputer."

    bn "Pada pertemuan pertama kita sudah membahas mengenai pengertian, tujuan, dan jenis jaringan komputer."

    bn "Pertemuan kedua ini kita masih akan membahas mengenai jenis-jenis jaringan komputer namun berdasarkan hal lain yang membedakan."

    bn "Kalau kalian masih inget minggu kemarin yang dijelaskan adalah jenis-jenis jaringan komputer berdasarkan geografinya."

    bn "Coba sebelum pertemuan ini dimulai saya mau tanya siapa yang masih inget, coba mas-mas yang duduk di deket jendela yang pakai jaket itu!"

    mc normal jacket "Saya bu?"

    bn "Iya kamu mas coba, masih inget engga, berdasarkan geografisnya dari yang lingkup paling kecil dulu apa hayo?"

    menu:

        "MAN, LAN, WAN":

            mc "MAN, LAN, WAN bu urutannya?"

            bn "Salah… udah lupa ya mas?"

        "WAN, MAN, LAN":

            mc "WAN, MAN, LAN bu urutannya?"

            bn "Salah… udah lupa ya mas?"

        "LAN, MAN, WAN":

            $ a_jarkomC+=5

            mc "LAN, MAN, WAN bu urutannya?"

            bn "Ya benar urutan berdasarkan ruang lingkupnya seperti itu mas."

        "Saya lupa bu hehe":

            mc "Saya lupa bu hehe…"

            bn "Waduh… dipelajari kembali ya mas?"

    bn "Jenis-jenis jaringan komputer berdasarkan geografisnya dan diurutkan dari ruang lingkup dari kecil ke besar adalah 
    Local Area Network, kemudian Metropolitan Area Network, dan Wide Area Network."

    show screen jarkom_2_1 with fade

    bn "Itu kalau berdasarkan geografisnya, kita sekarang akan membahas mengenai jenis jaringan komputer berdasarkan fungsinya."

    bn "Berdasarkan fungsinya ada Client-Server dan Peer-to-Peer."

    bn "Apa itu jaringan komputer Client-Server? Jaringan ini menggunakan satu komputer sebagai pusat atau server yang menyediakan sumber daya bagi komputer-komputer lainnya yang menjadi klient."

    bn "Komputer klien mengirimkan request untuk sumber daya kepada komputer server, lalu komputer server akan mengatur atau menerima request tersebut. 
    Apabila terlalu banyak request dalam waktu bersamaan jumlah komputer server dapat ditambah."

    bn "Karena bekerja sebagai pusat pada jaringan, komputer server tentu saja memiliki spesifikasi dan konfigurasi yang lebih dari komputer kliennya."

    hide screen jarkom_2_1

    show screen jarkom_2_2 with fade

    bn "Kemudian yang kedua Peer-to-Peer, berbeda dengan jaringan dengan model Client-Server, jaringan dengan model ini saling berbagi sumber daya 
    atau dengan kata lain dalam semua komputer pada jaringan ini menjadi server dan klien untuk komputer lain."

    bn "Satu komputer pada jaringan Peer-to-Peer harus dapat melayani request dari komputer lain yang ada di jaringan, 
    namun ketika membutuhkan sumber daya lain komputer tersebut juga bisa mengirim request pada komputer lain."

    bn "Pada jaringan dengan model Peer-to-Peer tidak bisa atau akan terlalu susah jika digunakan pada komputer yang berjumlah banyak 
    sehingga biasanya dilakukan pada komputer dengan jumlah yang tidak terlalu banyak."

    bn "Kurang lebih begitu untuk yang jenis jaringan komputer bedasarkan fungsi sebuah komputer, kita lanjut berdasarkan distribusi sumbernya. 
    Terdapat dua tipe yaitu model Terpusat, dan model Terdistribusi."

    hide screen jarkom_2_2

    show screen jarkom_2_3 with fade

    bn "Sebenarnya ini lebih seperti penjelasan lebih lanjut mengenai Jaringan Komputer Server-Client ya."

    bn "Pada jaringan dengan model Terpusat, yaitu jaringan yang hanya memiliki satu induk komputer yang berfungsi menjadi komputer Server. 
    Jadi semua kompter Klien meminta sumber daya hanya pada satu komputer Server"

    bn "Pada jaringan dengan model Terdistribusi, 
    jaringan ini memiliki beberapa beberapa komputer Server yang terhubung dan bisa melayani semua komputer Klien yang ada."

    bn "Itu merupakan jaringan Komputer berdasar cara Distribusi Sumber Dayanya ya. 
    Kemudian masih ada jaringan komputer berdasar media transmisinya."

    hide screen jarkom_2_3

    show screen jarkom_2_4 with fade

    bn "Berdasarkan media transmisinya terdapat 2 jenis model jaringan yaitu Jaringan Berkabel(Wired), dan Nirkabel(Wireless)."

    bn "Jaringan Berkabel sesuai namanya jaringan ini menggunakan kabel sebagai media penghubung atau penyalur informasi antara satu komputer dan komputer lainnya. 
    Jaringan berkabel biasanya memiliki kecepatan lebih tinggi, namun kurang fleksibel dalam pemakaiannya."

    bn "Jaringan Nirkabel atau Wireless tidak menggunakan kabel sebagai penyalur informasi atau datanya namun memanfaatkan gelombang elektromagnetik. 
    Jaringan nirkabel biasanya memiliki kecepatan yang tidak terlalu tinggi namun lebih praktis dalam penggunaannya."

    bn "Kurang lebih untuk hari ini materinya seperti itu dulu ya."

    hide screen jarkom_2_4

    bn "Jika ada pertanyaan bisa ditanyakan sebelum jam pertemuan berakhir."

    "Kemudian kelas dilanjutkan dengan sesi tanya jawab hingga waktu pertemuan berakhir."

    scene bg campus class with fade

    bn normal "Selesai untuk pertemuan kita hari ini, sampai jumpa minggu depan teman-teman…"

    r normal2 "Sampai jumpa bu…"

    t normal "Terimakasih…"

    bn "Selamat menikmati akhir pekan…."

    "Dengan ditutupnya pembelajaran mata kuliah ini, berakhir sudah kuliah pada hari ini."

    call attend_jarkom
    call attend_class

    if hima == True:
        jump penerimaan_hima
    else:
        scene bg black with fade
        pause 1.5

        "Sebelum pulang ke kos kamu sempat mampir pada suatu warung makan untuk mengisi perutmu."

        call eat

        "Setelah perutmu terisi, kamar kos merupakan tujuan selanjutnya pada siang hari ini."

        "Menyegarkan tubuhmu adalah salah satu hal yang ingin kamu lakukan ketika matahari bersinar terik."

        "Kamu melanjutkan perjalanan dan pulang ke kos."

    call change_timephase
    call screen mapUI with dissolve

label uts_jarkom:

    scene bg campus class with dissolve

    "Setelah menunggu untuk beberapa waktu, akhirnya kelas untuk ujian selanjutnya sudah dibuka."

    "Kamu merasa senang karena ujian tengah semester akan segera berakhir."

    "Setelah memastikan dimana posisi tempat dudukmu , kamu memasuki ruang kelas tersebut."

    "Dosen pengawas juga sudah menunggu di dalam kelas dan menyuarakan instruksi kepada semua mahasiswa yang ada."

    scene bg campus class with fade

    "Sesuai intruksi dari dosen pengawas ujian, tas mahasiswa diletakkan di depan kelas secara rapi."

    "Mahasiswa hanya perlu membawa peralatan tulis dan kartu ujian di bangku masing-masing."

    "Sama seperti sebelumnya, setelah kamu duduk kertas ujian tidak langsung dibagikan namun menunggu waktu yang telah ditentukan terlebih dahulu."

    "Ketika waktu sudah menunjukan jam mulai yang tertera pada soal ujian, dosen pengawas mulai berputar mengelilingi kelas sembari membacakan peraturan ujian kali ini."

    bn normal "Selamat pagi teman-teman pada siang hari ini kita akan melanjutkan ujian tengah semester untuk mata kuliah Jaringan Komputer."

    bn "Bapak harap kalian sudah mempersiapkan diri untuk ujian hari ini."

    bn "Soal akan saya bagikan, tolong kartu ujiannya ditaruh di meja dan nanti kalau ada pertanyaan bisa langsung ditanyakan."

    bn "Saya harap kejujuran dari kalian dan semangat dan selamat mengerjakan."

    "Setelah menerima lembar soal dan lembar jawaban untuk UTS mata kuliah Jaringan Komputer ini, kamu memejamkan matamu sebentar berdoa dan mempersiapkan diri untuk mengerjakan."

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
    "1. Jenis jaringan komputer WAN merupakan jaringan komputer yang ....?"
    menu:
        "A. Jenis jaringan komputer yang memiliki jangkauan geografis paling luas.":
            "A. Jenis jaringan komputer yang memiliki jangkauan geografis paling luas."
            $a_jarkomTS +=20
        "B. Jenis jaringan komputer yang memiliki jangkauan dalam satu kota.":
            "B. Jenis jaringan komputer yang memiliki jangkauan geografis yang memiliki jangkauan dalam satu kota."
        "C. Jenis jaringan komputer yang memiliki jangkauan dalam satu bangunan.":
            "C. Jenis jaringan komputer yang memiliki jangkauan dalam satu bangunan."
        "D. Jenis jaringan komputer yang memiliki jangkauan geografis paling kecil.":
            "D. Jenis jaringan komputer yang memiliki jangkauan geografis paling kecil."
        "E. Jenis jangkauan yang tidak mencakup jangkauan antar kota.":
            "E. Jenis jangkauan yang tidak mencakup jangkauan antar kota."
    "2. Jenis jaringan komputer LAN merupakan jaringan komputer yang ...?"
    menu:
        "A. Jenis jaringan komputer yang memiliki jangkauan geografis paling luas.":
            "A. Jenis jaringan komputer yang memiliki jangkauan geografis paling luas."
        "B. Jenis jaringan komputer yang memiliki jangkauan dalam satu kota.":
            "B. Jenis jaringan komputer yang memiliki jangkauan geografis yang memiliki jangkauan dalam satu kota."
        "C. Jenis jaringan komputer yang memiliki jangkauan antar kota dan daerah.":
            "C. Jenis jaringan komputer yang memiliki jangkauan antar kota dan daerah."
        "D. Jenis jaringan komputer yang memiliki jangkauan geografis paling kecil.":
            "D. Jenis jaringan komputer yang memiliki jangkauan geografis paling kecil."
            $a_jarkomTS +=20
        "E. Jenis jangkauan yang tidak mencakup jangkauan antar kota.":
            "E. Jenis jangkauan yang tidak mencakup jangkauan antar kota."
    "3. Model jaringan komputer menurut fungsinya dimana sisi client hanya dapat meminta atau request layanan kepada sisi penyedia layanan saja disebut model jaringan?"
    menu:
        "A. Jaringan Peer-to-Peer":
            "A. Jaringan Peer-to-Peer"
        "B. Jaringan LAN.":
            "B. Jaringan LAN."
        "C. Jaringan MAN.":
            "C. Jaringan MAN."
        "D. Jaringan Client-to Server.":
            "D. Jaringan Client-to Server."
            $a_jarkomTS += 20
        "E. Jaringan Wireless.":
            "E. Jaringan Wireless."
    "4. Apakah yang dimaksud dengan model jaringan komputer Terdistribusi?"
    menu:
        "A. Jaringan komputer dimana hanya terdapat satu induk komputer yang mendistribusikan layanan":
            "A. Jaringan komputer dimana hanya terdapat satu induk komputer yang mendistribusikan layanan"
        "B. Jaringan komputer dimana terdapat banyak induk komputer yang mampu menyediakan layanan untuk berbagai komputer":
            "B. Jaringan komputer dimana terdapat banyak induk komputer yang mampu menyediakan layanan untuk berbagai komputer"
            $a_jarkomTS += 20
        "C. Jaringan komputer dimana komputer-komputer menggunakan komputer induk yang sama yang ada dalam satu bangunan.":
            "C. Jaringan komputer dimana komputer-komputer menggunakan komputer induk yang sama yang ada dalam satu bangunan."
        "D. Jaringan komputer yang menggunakan teknologi nirkabel.":
            "D. Jaringan komputer yang menggunakan teknologi nirkabel."
        "E. Jaringan komputer yang tidak memiliki komputer induk, dan memerlukan penyedia layanan eksternal.":
            "E. Jaringan komputer yang tidak memiliki komputer induk, dan memerlukan penyedia layanan eksternal."
    "5. Menurut media transmisinya, manakah jenis jaringan yang memiliki kecepatan paling cepat?"
    menu:
        "A. Terdisitribusi":
            "A. Terdisitribusi"
        "B. Terpusat.":
            "B. Terpusat."
        "C. Wired.":
            "C. Wired."
            $a_jarkomTS += 20
        "D. Wireless.":
            "D. Wireless."
        "E. LAN.":
            "E. LAN."    
    
    "Setelah menjawab semua pertanyaan yang ada, kamu merasa lega karena ujian tengah semester telah berakhir."

    "Mengkoreksi dan meneliti kertas jawaban dan biodatamu selama beberapa kali akhirnya kamu beranjak dari tempat dudukmu."

    "Terdapat rasa cemas mengenai hasil semua ujian yang telah kamu selesaikan, namun kamu sudah berpasrah karena ujian sudah berakhir."

    "Mengumpulkan kertas ujian, kemudian memasukan barang-barangmu pada tas yang sebelumnya sudah dikelompokan dengan rapi di depan kelas."

    "Kemudian kamu segera keluar dari dalam kelas. Di luar sebelumnya sudah ada beberapa mahasiswa yang keluar lebih dahulu sebelum dirimu."

    "Kamu menghabiskan waktu dengan mengobrol dengan temanmu sembari menunggu temanmu yang lain menyelesaikan ujian mereka."

    jump uts_akhir

label jarkom_3:

    scene bg campus class with dissolve

    "Setelah beberapa menit menunggu, sekarang sudah memasuki waktu untuk kelas berikutnya. "

    "Kamu dan teman-temanmu mulai memasuki kelas yang akan digunakan untuk pembelajaran terakhir pada hari ini."

    "Ketika memasuki ruang kelas, [bn] yang akan mengajar kelas berikutnya telah duduk dan menunggu di dalam ruangan."

    bn normal "Selamat siang teman-teman, silahkan masuk sembari menunggu teman-teman yang lain masuk kelas."

    "Tidak memakan waktu yang lama, satu persatu teman kelasmu memasuki ruangan, setelah dirasa banyak mahasiswa yang telah memasuki ruangan, [bn] membuka pertemuan pada siang hari ini."

    bn "Selamat siang, sepertinya sudah pada hadir ya… Kalau begitu ibu mulai kelas pada siang hari ini."

    bn "Bertemu lagi kita pada mata kuliah Jaringan Komputer pertemuan ke 3. Pada pertemuan siang hari ini, kita akan membahas mengenai OSI Layer, apa itu OSI Layer, Fungsi, dan penjelasannya."

    bn "Mungkin langsung ibu jelaskan saja untuk menghemat waktu ya, jadi apa itu OSI Layer?"

    show screen jarkom_3_1 with fade

    bn class "Dalam jaringan, setiap komputer memiliki cara untuk berkomunikasi masing-masing. Namun dengan banyaknya jenis atau cara berkomunikasi 
    tersebut, maka dibutuhkan sebuah standar yang mampu membuat semua jenis sistem komputer dapat berkomunikasi satu sama lain."

    bn "Maka dibentuklah model OSI (Open Systems Interconnection) yang merupakan sebuah konsep kerja yang memungkinkan agar komputer-komputer 
    yang terdapat pada jaringan tersebut mampu berinteraksi dan berkomunikasi satu sama lain menggunakan protokol yang sudah distandarisasi."

    bn "Model OSI terdiri dari 7 lapisan yang memiliki fungsi dan tanggung jawab yang berbeda-beda dalam komunikasi jaringan."

    bn "Pengertian dan penjelasan dari ke-7 lapisan abstrak tersebut adalah sebagai berikut:"

    hide screen jarkom_3_1

    show screen jarkom_3_2 with fade

    bn "Lapisan 1, Physical Layer, Lapisan fisik ini merupakan lapisan paling bawah atau lapisan pertama yang terdapat pada OSI model."

    bn "Lapisan ini mengatur semua perangkat fisik yang digunakan dalam transmisi data semisal kabel, konektor, dan perangkat fisik lainnya."

    bn "Menggunakan perangkat fisik tersebut, lapisan ini memiliki tugas untuk mentransmisikan data ke dalam bentuk bit data melalui media transmisi yang ada."

    bn "Kemudian, setelah Lapisan fisik, kita lanjut ke lapisan yang berikutnya."

    bn "Lapisan 2, Data Link Layer, Lapisan data link ini merupakan lapisan yang mengatur jalur komunikasi dalam jaringan yang sama."

    bn  "Lapisan ini mengatur bagaimana data dikemas, lalu bagaimana data dikirimkan masih dalam jaringan lokal, 
    serta memiliki tugas untuk deteksi dan koreksi kesalahan yang mungkin terjadi ketika transmisi data terjadi."

    bn "Lalu pada lapisan ke-3 terdapat Network Layer."

    hide screen jarkom_3_2

    show screen jarkom_3_3 with fade

    bn "Network Layer atau lapisan jaringan ini merupakan lapisan yang berfokus pada routing data, pengalamatan, dan pengiriman data melalui jaringan-jaringan yang ada."

    bn "Lapisan ini menentukan cara data dikirimkan dari satu titik ke titik yang lain yang berada pada jaringan. "

    bn "Kemudian pada lapisan ke-4, terdapat Transport Layer."

    bn "Transport Layer mengatur komunikasi end-to-end, pengendalian aliran data agar data dapat disampaikan dengan baik, dan pengelolaan koneksi agar lebih optimal."

    bn "Seperti yang disebutkan sebelumnya, lapisan ini memastikan data dapat ditransmisikan dan diterima pada tujuan dengan baik. 
    Hal tersebut dilakukan dengan segmentasi data dan penyusunan ulang data pada penerima atau user."

    bn "Lanjut pada lapisan ke-5, Session Layer."

    hide screen jarkom_3_3

    show screen jarkom_3_4 with fade

    bn "Session Layer atau lapisan sesi ini mengatur pembukaan dan penutupan sesi serta melakukan pengelolaan sesi komunikasi antar perangkat yang berbeda."

    bn "Lapisan ini memungkinkan dua perangkat mampu berkomunikasi dan berkoordinasi dengan baik satu sama lain. 
    Dengan kata lain lapisan ini mendefinisikan bagaimana dua perangkat tersebut dapat mengelola koneksi satu sama lain."

    bn "Lapisan ke-6 adalah, Presentation Layer."

    bn "Presentation Layer atau layer presentasi ini mengatur enkripsi, dekripsi, kompresi, dan juga penyandian data."

    bn "Layer ini dapat dikatakan berfungsi sebagai penerjemah atau translator sehingga data yang ditransmisikan dapat ditranslasikan menjadi format yang mampu dibaca oleh penerima."

    bn "Lalu lapisan OSI paling atas atau no 7 adalah, Application Layer."

    hide screen jarkom_3_4

    show screen jarkom_3_5 with fade

    bn "Application Layer atau Lapisan Aplikasi ini merupakan tempat aplikasi berinteraksi dengan jaringan."

    bn "Lapisan ini berfungsi sebagai antarmuka dengan aplikasi dengan fungsionalitas jaringan, mengatur bagaimana aplikasi dapat mengakses jaringan, dan kemudian membuat pesan-pesan kesalahan."

    bn "Itu merupakan penjelasan mengenai 7 lapisan Model OSI."

    bn "Dengan model OSI ini membuat kita menjadi lebih mudah dalam memahami bagaimana komunikasi berjalan, selain itu dengan model OSI ini membaginya menjadi 7 lapisan dengan fungsi-fungsi yang telah terdefinisi dengan baik."
    
    bn  "Oleh karena hal tersebut, mampu membuat pengembangan, pemahaman, dan troubleshooting jaringan yang efisien menjadi lebih mudah."

    hide screen jarkom_3_5

    bn "Kurang lebih begitu untuk materi OSI model yang ibu terangkan hari ini."

    bn "Jadi hari ini kita telah membahas pengertian OSI model, dan masing-masing penjelasan dari 7 lapisan OSI model yang ada."

    bn "Mungkin untuk hari ini cukup sampai sini dulu ya, kita lanjutkan lagi untuk besok pembahasan mengenai topologi jaringan. Besok kita akan mempelajari mengenai pengertian dan contoh dari topologi jaringan."

    bn "Untuk perkuliahan hari ini, kita lanjutkan dengan sesi tanya jawab ya, kalau kalian ada pertanyaan untuk materi pada hari ini, bisa kalian tanyakan sekarang."

    "Pembelajaran berlanjut pada sesi tanya jawab. Sesi tanya jawab masih terus berlangsung pada mahasiswa lain hingga jam perkuliahan selesai."

    scene bg campus class with dissolve

    bn normal "Saya kira cukup untuk pertemuan kali ini, terimakasih atas partisipasinya pada perkuliahan hari ini dan sampai ketemu minggu depan teman-teman."

    r normal2 "Terimakasih bu…"

    t normal "Terimakasih…"

    "[bn] meninggalkan ruang kelas, dan pertemuan ke-3 mata kuliah Jaringan Komputer pada hari ini selesai."

    "Setelah selesai mengemas barang-barangmu, kamu meninggalkan ruang kelas dan bersiap untuk pulang."

    call attend_jarkom
    call attend_class

    if hima == True:
        call hima_1
    else:
        scene bg black with fade
        pause 1.5
    call change_timephase
    call screen mapUI with dissolve

label jarkom_4:

    scene bg campus hall with dissolve

    scene bg campus upper hall with fade

    scene bg campus class with fade

    bn normal "Selamat siang teman-teman, bagaimana kabarnya? Semoga baik-baik saja ya."

    "[bn] memasuki ruang kelas, pertanda perkuliahan terakhir pada semester ini akan segera dimulai."

    bn "Seperti yang kalian ketahui, hari ini merupakan pertemuan terakhir untuk mata kuliah Jaringan Komputer, dan juga merupakan pertemuan terakhir sebelum ujian akhir dilaksanakan."

    bn "Untuk menghemat waktu mungkin kita mulai saja kelasnya. Minggu lalu kita sudah mempelajari mengenai OSI Model dan 7 layer yang terdapat di dalamnya."

    bn "Minggu ini kita akan mempelajari mengenai Topografi dalam jaringan beserta contoh dan penjelasannya."

    "[bn] menyiapkan materi yang akan dipaparkan pada perkuliahan. Setelah materi telah terlihat di depan kelas, perkuliahan pun dimulai."

    scene bg campus class with dissolve

    bn normal "Jadi karena kita akan mempelajari mengenai topografi jaringan, maka kita harus memahami dulu apa itu topografi jaringan?"

    show screen jarkom_4_1 with fade

    bn class "Topografi jaringan merujuk kepada cara-cara bagaimana perangkat-perangkat yang berada dalam sebuah jaringan dihubungkan satu sama lain."

    bn "Cara bagaimana jaringan dihubungkan satu sama lain tersebut membentuk pola fisik maupun geometris yang masing-masing dari pola tersebut memiliki karakteristik dan pola yang berbeda-beda."

    bn "Ibu akan menjelaskan beberapa contoh dari topologi jaringan yang ada."

    bn "Topologi jaringan yang pertama adalah, topologi bintang."

    hide screen jarkom_4_1

    show screen jarkom_4_2 with fade

    bn "Topologi bintang atau stars ini merupakan topologi jaringan dimana perangkat-perangkat yang terdapat dalam jaringan tersebut terhubung pada suatu pusat atau switch yang terdapat pada pusat."

    bn "Beberapa karakteristik yang terdapat pada topologi ini adalah,"

    bn "Pada topologi bintang hanya terdapat satu pusat kontrol."

    bn "Perangkat-perangkat langsung terhubung pada pusat kontrol yang mampu membuat komunikasi yang lebih efisien."

    bn "Kerusakan atau masalah pada salah satu perangkat user tidak mempengaruhi kinerja jaringan."

    bn "Lalu apa saja keuntungan dari topologi ini?"

    hide screen jarkom_4_2

    show screen jarkom_4_3 with fade

    bn "Topologi bintang relatif mudah untuk dikembangkan ketika diperlukan."

    bn "Dengan hanya adanya satu pusat kontrol, maka akan memudahkan pengelolaan dari jaringan yang ada."

    bn "Selain itu, karena hanya ada satu pusat kontrol dan tiap perangkat terhubung pada pusat kontrol tersebut maka apabila terjadi kegagalan pada suatu perangkat, 
    perangkat yang lain tidak akan terpengaruh, hal ini juga membuat identifikasi dan perbaikan menjadi lebih mudah."

    bn "Kemudian ibu akan berlanjut pada kerugian penggunaan topologi bintang?"

    bn "Selain menjadi keuntungan, memiliki satu pusat kontrol juga dapat menjadi kekurangan karena apabila pusat kontrol tersebut 
    mengalami masalah maka semua perangkat pada jaringan tersebut juga akan terkena imbasnya."

    bn "Kemudian kerugian berikutnya adalah biaya yang relatif mahal, karena topologi bintang terbilang boros dalam pemakaian kabel."

    bn "Topologi yang berikutnya adalah topologi bus."

    hide screen jarkom_4_3

    show screen jarkom_4_4 with fade

    bn "Topologi bus merupakan topologi jaringan dimana semua perangkat yang ada pada jaringan terhubung pada satu kabel sentral yang berfungsi sebagai media komunikasi antar jaringan."

    bn "Karakteristik dari topologi bus adalah sebagai berikut."

    bn "Pertama, proses instalasi jaringan terbilang relatif mudah dan sederhana sehingga biaya menjadi lebih ekonomis."

    bn "Lalu topologi bus memiliki satu kabel sentral yang menghubungkan semua perangkat dalam jaringan."

    bn "Tiap-tiap node dihubungkan secara serial dengan kabel dan ditutup dengan terminator."

    bn "Kemudian untuk keuntungan penggunaan topologi bus sendiri adalah,"

    hide screen jarkom_4_4

    show screen jarkom_4_5 with fade

    bn "Topologi bus merupakan topologi dengan desain dan instalasi yang sederhana."

    bn "Topologi bus juga memiliki biaya yang rendah."

    bn "Selain itu, topologi ini juga mudah untuk dikembangkan."

    bn "Lalu kita berlanjut pada kekurangan pada topologi bus."

    bn "Apabila kabel sentral mengalami kegagalan, maka seluruh jaringan juga akan terpengaruh."

    bn "Kinerja topologi ini akan berkurang ketika semakin banyak perangkat yang terhubung dalam jaringan."

    bn "Pada topologi ini tidak mudah untuk menemukan atau mendeteksi kesalahan."

    bn "Kemudian kita akan berlanjut pada topologi yang berikutnya yaitu topologi ring atau cincin."

    hide screen jarkom_4_5

    show screen jarkom_4_6 with fade

    bn "Topologi cincin merupakan topologi dimana perangkat-perangkat yang terdapat dalam jaringan saling terhubung ke dua perangkat yang ada di sebelahnya. "

    bn "Karena perangkat yang terdapat pada jaringan terhubung dengan perangkat yang ada di sebelahnya, 
    maka bentuk jaringan akan melingkar dan terlihat seperti cincin."

    bn "Karakteristik dari topologi cincin sendiri adalah sebagai berikut."

    bn "Memiliki jalur cincin, dimana data akan mengalir searah sepanjang jalur cincin."

    bn "Lalu karena data mengalir dalam satu arah, maka menghindarkan dari tabrakan atau collision dapat dihindari."

    bn "Kemudian keuntungan yang dapat kita dapatkan dengan menggunakan topologi cincin adalah"

    hide screen jarkom_4_6

    show screen jarkom_4_7 with fade

    bn "Memiliki kinerja yang lebih baik dan optimal dalam mengakses data."

    bn "Kualitas aliran data yang lebih cepat karena data bergerak secara lebih fleksibel."

    bn "Mengurangi resiko terjadinya tabrakan data dengan data yang hanya berputar satu arah."

    bn 'Meskipun begitu, ada beberapa kelemahan pada penggunaan topologi cincin semisal,'

    bn "Susahnya konfigurasi ulang ketika melakukan perubahan dalam jaringan."

    bn "Menambah atau mengurangi perangkat akan menjadi lebih sulit dan membutuhkan biaya lebih."

    bn "Dan apabila terdapat salah satu perangkat yang mengalami masalah, maka seluruh jaringan dapat terkena dampaknya."

    bn "Kemudian kita lanjut pada topologi yang selanjutnya, yaitu topologi mesh."

    hide screen jarkom_4_7

    show screen jarkom_4_8 with fade

    bn "Topologi mesh merupakan sebuah topologi campuran antara topologi star dan topologi ring."

    bn "Pada topologi ini setiap perangkat yang ada akan terhubung dengan semua perangkat yang terdapat dalam jaringan."

    bn "Karakteristik dari topologi mesh adalah sebagai berikut,"

    bn "Memiliki koneksi langsung karena setiap perangkat terhubung dengan satu sama lainnya."

    bn "Redudansi, karena setiap perangkat terhubung satu sama lain maka akan ada banyak redundansi di dalamnya."

    bn "Sementara kelebihan penggunaan topologi ini adalah"

    hide screen jarkom_4_8

    show screen jarkom_4_9 with fade

    bn "Memiliki keandalan yang tinggi, karena apabila ada jalur yang tidak bisa digunakan masih terdapat jalur alternatif lainnya."

    bn "Masalah yang terjadi pada suatu perangkat tidak memengaruhi perangkat lainnya."

    bn "Memiliki kecepatan pengiriman data yang tinggi."

    bn "Sementara itu topologi mesh juga memiliki kelemahan seperti,"

    bn "Membutuhkan biaya yang relatif mahal."

    bn "Instalasi jaringan rumit."

    bn "Serta pengelolaan yang sulit."

    bn "Setelah ini terdapat satu topologi lagi yang ingin ibu jelaskan."

    bn "Topologi terakhir yang akan ibu jelaskan hari ini adalah, Topologi Tree"

    hide screen jarkom_4_9

    show screen jarkom_4_10 with fade

    bn "Topologi tree atau pohon ini merupakan topologi campuran antara topologi star dengan topologi bus."

    bn "Terdapat beberapa perangkat yang terhubung pada switch utama dan beberapa perangkat lainnya terhubung pada switch penghubung."

    bn "Karakteristik dari topologi tree sendiri adalah sebagai berikut,"

    bn "Membentuk sebuah hirarki jaringan, dengan adanya perangkat yang berada di atas perangkat lainnya."

    bn "Memiliki pusat kontrol yang seringkali berupa switch."

    bn "Sementara itu kelebihan dari penggunaan topologi tree sendiri adalah,"

    hide screen jarkom_4_10

    show screen jarkom_4_11 with fade

    bn "Mampu digunakan dalam jaringan yang berskala besar."

    bn "Dengan adanya hirarki dalam jaringan, membuat jaringan menjadi lebih terstruktur dan terorganisasi."

    bn "Penambahan klien pada tingkatan bawah dapat dilakukan secara lebih mudah."

    bn "Namun penggunaan topologi tree juga memiliki kekurangan, seperti…"

    bn "Perawatan pada jaringan akan menjadi lebih sulit dengan adanya banyak perangkat dalam jaringan tersebut."

    bn "Memerlukan biaya yang relatif mahal, apalagi untuk memiliki pusat kontrol yang reliable sehingga jaringan tidak mudah terjadi masalah."

    bn "Kerusakan pada kabel utama dapat memengaruhi seluruh jaringan, begitu pula dengan perangkat yang terdapat pada bagian atas, jika mengalami kerusakan maka bagian bawahnya juga akan terkena dampaknya."

    bn "Mungkin sampai disini dulu pembahasan mengenai topologi jaringan pada hari ini."

    bn "Hari ini kita sudah sedikit membahas mengenai topologi jaringan bintang, jaringan cincin, jaringan bus, jaringan mesh, dan jaringan tree."

    hide screen jarkom_4_11 with dissolve

    bn normal "Apakah ada pertanyaan untuk materi kita hari ini teman-teman?"

    bn "Apabila ada silahkan bertanya selagi waktu masih ada."

    "Kemudian satu persatu teman kelasmu mengacungkan jarinya dan bertanya mengenai materi."

    "Salah satu temanmu yang mengacungkan jarinya adalah rissa."

    r normal2 "Bu, berarti untuk ujian akhirnya sampai ke materi ini ya bu?"

    bn "Iya, nanti ujian akhirnya menggunakan materi dari pertemuan minggu ke-3 dan minggu ke-4."

    r "Oh ya bu terimakasih."

    "Setelah itu masih terdapat beberapa pertanyaan sebelum kelas akhirnya ditutup."

    scene bg campus class with dissolve

    bn normal"Sekian dari saya untuk pertemuan hari ini. Terimakasih atas partisipasinya sampai pertemuan terakhir ini ya teman-teman."

    bn "Saya tutup pertemuan hari ini, selamat belajar untuk ujian akhir nanti dan semoga mendapatkan hasil yang terbaik."

    scene bg campus class with fade

    "Kelas ditutup, [bn] meninggalkan ruang kelas tidak lama kemudian mahasiswa-mahasiswa juga ikut meninggalkan ruang kelas"

    "Pertemuan kuliah terakhir pada tahun ini telah selesai, hanya tersisa ujian akhir yang menunggumu minggu depan."

    "Bagaimanapun hasil yang akan kamu terima, kamu harus melalui ujian akhir tersebut."

    "Setelah terdiam untuk beberapa waktu di bangkumu memikirkan ujian akhir nanti, akhirnya kamu berdiri dan bergegas untuk pulang."

    call attend_jarkom
    call attend_class

    if hima == True:
        call hima_2
    else:
        scene bg black with fade
        pause 1.5
    call change_timephase
    call screen mapUI with dissolve

label attend_jarkom:

    $ a_jarkomA +=1
    $ a_jarkomN +=8

    return