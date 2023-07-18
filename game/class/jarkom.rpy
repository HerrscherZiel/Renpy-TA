
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

    "Jarkom 3"

    jump pre_libur

label jarkom_4:

    "Jarkom 4"

    jump pre_libur

label attend_jarkom:

    $ a_jarkomA +=1
    $ a_jarkomN +=8

    return