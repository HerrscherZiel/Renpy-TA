
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

    jump pre_libur

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