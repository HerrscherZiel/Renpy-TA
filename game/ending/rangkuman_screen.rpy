
default edkutu = False
default ednolife = False
default edantikupu = False
default edbagaikuda = False
default edsehatno = False
default ednormies = False
default edbadend = False
default edidaman = False

screen rangkuman_screen1:

    frame:
        xsize 1920
        ysize 1080

        background "rangkuman/rangkuman_health.png"

        vbox:
            xpos 400
            ypos 355
            spacing 450
            $ health = round((hunger+energy+vit) / 3)
            text "[health]" size 76 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        
        hbox:
            xpos 130
            ypos 555
            xsize 750
            spacing 100
            if health <= 30:
                text "Kesehatan Rendah - Kamu memiliki tingkat kesehatan yang rendah pada akhir permainanmu.\n \nIngat!!! Badan yang tidak sehat akan selalu menjadi hambatan untuk melakukan aktivitas secara maksimal. Tingkatkan kesehatanmu dengan mulai mengatur pola hidupmu menjadi  lebih baik!! Kamu dapat memulai pola hidup sehat dengan mengatur pola makan, olahraga yang terjadwal, dan cukup istirahat !!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            elif health > 30 and health <= 60:
                text "Kesehatan Menengah - Kamu memiliki tingkat kesehatan yang cukup baik pada akhir permainanmu.\n \nIngat!!! Kesehatan merupakan langkah pertama untuk dapat menjalani kehidupan perkuliahan dengan baik. Dengan menjaga kesehatan kamu dapat beraktivitas secara lebih leluasa dan maksimal. Jangan lupa untuk mengatur pola makan, olahraga yang terjadwal, dan cukup istirahat !!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            else:
                text "Kesehatan Tinggi - Kamu memiliki tingkat kesehatan yang tinggi pada akhir permainanmu.\n \nIngat!!! Selalu jaga kesehatanmu untuk mendapatkan hasil yang maksimal. Pertahankan pola hidup sehat, atur pola makan, olahraga yang terjadwal, dan cukup istirahat !!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            

        vbox:
            xpos 1250
            ypos 350
            spacing 55
            text ": [thinCount] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [fitCount] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [healthyCount] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        vbox:
            xpos 1760
            ypos 350
            spacing 55
            text ": [obesseCount] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [weakCount] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [sickCount] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1250
            ypos 740
            spacing 350
            text ": [sicks] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [weaks] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1490
            ypos 823
            spacing 350
            text ": [thins] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        

        #slide left
    imagebutton:
        xpos 800
        ypos 950
        idle "tutorial/left_idle.png"
        hover "tutorial/left_idle.png"

    #slide right
    imagebutton:
        xpos 1000
        ypos 950
        auto "tutorial/right_%s.png"
        action  [Hide("rangkuman_screen1"), Show("rangkuman_screen2")]

screen rangkuman_screen2:

    frame:
        xsize 1920
        ysize 1080

        background "rangkuman/rangkuman_akademik.png"

        vbox:
            xpos 400
            ypos 355
            spacing 450
            $ academic = round((knowledge+practice+application) / 3)
            text "[academic]" size 76 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        
        hbox:
            xpos 130
            ypos 555
            xsize 750
            spacing 100
            if academic < 50:
                text "Akademik Rendah - Kamu memiliki nilai akademik yang rendah pada akhir permainanmu.\n \nIngat!!! Meskipun kehidupan perkuliahan memanglah lebih bebas, namun jangan sampai lupa tujuan kita berkuliah untuk masa depan yang lebih baik. Tingkatkan nilai akademikmu dengan cara giat belajar, jangan takut bertanya, dan ikuti semua perkuliahan dengan sungguh-sungguh!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            elif academic >= 50 and academic <= 70:
                text "Akademik Menengah - Kamu memiliki nilai akademik yang cukup baik pada akhir permainanmu.\n \nIngat!!! Untuk mendapatkan hasil akademik yang lebih maksimal kamu perlu lebih tekun dalam belajar. Jangan menyerah dan cepat putus asa ketika menghadapi masalah yang sulit. Belajarlah dengan sungguh-sungguh dan jangan sungkan untuk bertanya !!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            else:
                text "Akademik Tinggi - Kamu memiliki nilai akademik yang tinggi pada akhir permainanmu.\n \nIngat!!! Pertahankan nilai akademikmu saat ini, jangan mudah untuk cepat puas dengan hasil yang telah didapatkan. Terus belajar dan raih hasil yang lebih memuaskan !!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            

        hbox:
            xpos 1100
            ypos 400
            spacing 320
            $ masuk = a_alproA + a_basdatA + a_deA + a_jarkomA + a_pboA + a_ptiA + a_webA + a_strukdatA 
            $ masuks = masuk/32*100
            $ boloss = 32 - masuk
            text ": [masuk]/32 \n= [masuks] %" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [boloss] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1100
            ypos 560
            spacing 355
            $ quiz = a_alproC + a_basdatC + a_deC + a_jarkomC + a_pboC + a_ptiC + a_webC + a_strukdatC 
            $ quizz = quiz/40*100
            $ tugas = a_alproT + a_basdatT + a_ptiT + a_webT
            $ tugass = tugas/50*100
            text ": [quiz]/40 \n [quizz] %" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [tugas]/50 \n [tugass] %" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1100
            ypos 730
            spacing 290
            $ uts = a_alproTS + a_basdatTS + a_deTS + a_jarkomTS + a_pboTS + a_ptiTS + a_webTS + a_strukdatTS 
            $ utss = uts/8
            $ uas = a_alproAS + a_basdatAS + a_deAS + a_jarkomAS + a_pboAS + a_ptiAS + a_webAS + a_strukdatAS 
            $ uass = uas/8*5
            text ": [uts]/800 \n [utss] %" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [uas]/160 \n [uass] %" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        

    #slide left
    imagebutton:
        xpos 800
        ypos 950
        auto "tutorial/left_%s.png"
        action  [Hide("rangkuman_screen2"), Show("rangkuman_screen1")]    

    #slide right
    imagebutton:
        xpos 1000
        ypos 950
        auto "tutorial/right_%s.png"
        action  [Hide("rangkuman_screen2"), Show("rangkuman_screen3")]    

screen rangkuman_screen3:

    frame:
        xsize 1920
        ysize 1080

        background "rangkuman/rangkuman_social.png"

        vbox:
            xpos 400
            ypos 355
            spacing 450
            $ social = round((friend+community+public) / 3)
            text "[social]" size 76 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        
        hbox:
            xpos 130
            ypos 555
            xsize 750
            spacing 100
            if social < 40:
                text "Sosial Rendah - Kamu memiliki nilai sosial yang rendah pada akhir permainanmu.\n \nIngat!!! Meskipun dalam kehidupan perkuliahan kamu tetap memerlukan kehidupan sosialmu! Dengan terus berinteraksi dengan orang lain kamu akan mendapatkan pengalaman dan relasi yang sebelumnya tidak kamu punyai. Jangan malu untuk mengenal orang baru dalam kehidupanmu!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            elif social >= 40 and social <= 70:
                text "Sosial Menengah - Kamu memiliki nilai sosial yang cukup baik pada akhir permainanmu.\n \nIngat!!! Tingkatkan interaksimu dengan orang lain untuk mendapatkan berbagai macam pengalaman dan hal yang baru dalam hidupmu !!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            else:
                text "Sosial Tinggi - Kamu memiliki nilai sosial yang tinggi pada akhir permainanmu.\n \nIngat!!! Pertahankan kehidupan sosialmu saat ini. Mungkin terlalu banyak kamu menghabiskan waktumu untuk berinteraksi dengan orang lain memiliki sisi yang negatif, oleh karena itu jangan lupa untuk membagi waktu sebaik mungkin !!!" size 25 font "fonts/Montserrat-SemiBoldItalic.ttf"
            

        hbox:
            xpos 1100
            ypos 400
            spacing 450
            text ": [friendc]" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text ": [kenalan]" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1100
            ypos 560
            spacing 355
            text ": [communityc] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1100
            ypos 730
            spacing 290
            $ uts = a_alproTS + a_basdatTS + a_deTS + a_jarkomTS + a_pboTS + a_ptiTS + a_webTS + a_strukdatTS 
            text ": [publicc] x" size 42 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        

    #slide left
    imagebutton:
        xpos 800
        ypos 950
        auto "tutorial/left_%s.png"
        action  [Hide("rangkuman_screen3"), Show("rangkuman_screen2")]    

    #slide right
    imagebutton:
        xpos 1000
        ypos 950
        auto "tutorial/right_%s.png"
        action  [Hide("rangkuman_screen3"), Show("rangkuman_screen4")]

screen rangkuman_screen4:

    frame:
        xsize 1920
        ysize 1080

        background "rangkuman/rangkuman_lokasi.png"

        #mininmart
        vbox:
            xpos 380
            ypos 360
            spacing 55
            text "-" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[locmins] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[locminm] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 380
            ypos 735
            text "[locmin] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        #kos
        vbox:
            xpos 590
            ypos 360
            spacing 55
            text "[lockosp] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[lockoss] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[lockosm] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 590
            ypos 735
            text "[lockos] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        #kampung
        vbox:
            xpos 800
            ypos 360
            spacing 55
            text "[lockampp] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[lockamps] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[lockampm] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 800
            ypos 735
            text "[lockamp] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        #perpus
        vbox:
            xpos 1090
            ypos 360
            spacing 55
            text "-" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[loclibs] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "-" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1090
            ypos 735
            text "[loclib] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        #kota
        vbox:
            xpos 1310
            ypos 360
            spacing 55
            text "[lockotap] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[lockotas] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[lockotam] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1310
            ypos 735
            text "[lockota] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            
        #kampus
        vbox:
            xpos 1510
            ypos 360
            spacing 55
            text "-" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[loccamps] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "-" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        hbox:
            xpos 1510
            ypos 735
            text "[loccamp] x" size 46 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

    #slide left
    imagebutton:
        xpos 800
        ypos 950
        auto "tutorial/left_%s.png"
        action  [Hide("rangkuman_screen4"), Show("rangkuman_screen3")]    

    #slide right
    imagebutton:
        xpos 1000
        ypos 950
        auto "tutorial/right_%s.png"
        action  [Hide("rangkuman_screen4"), Show("rangkuman_screen5")]

screen rangkuman_screen5:

    frame:
        xsize 1920
        ysize 1080

        background "rangkuman/rangkuman_aktivitas.png"

        vbox:
            xpos 380
            ypos 310
            spacing 165
            text "[makanc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[jalanc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[olahragac]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        vbox:
            xpos 940
            ypos 310
            spacing 165
            text "[jajanc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[malasc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[sosialc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

        vbox:
            xpos 1510
            ypos 310
            spacing 165
            text "[mainc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[tidurc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[bersihc]" size 43 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"      

    #slide left
    imagebutton:
        xpos 800
        ypos 950
        auto "tutorial/left_%s.png"
        action  [Hide("rangkuman_screen5"), Show("rangkuman_screen4")]    

    #slide right
    imagebutton:
        xpos 1000
        ypos 950
        auto "tutorial/right_%s.png"
        action  [Hide("rangkuman_screen5"), Show("ending_page")]

screen ending_page:

    frame:
        xsize 1920
        ysize 1080

        background "rangkuman/ending_page.png"

        hbox:
            xpos 380
            ypos 355
            spacing 410
            $ health = round((hunger+energy+vit) / 3)
            text "[health]" size 76 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            $ academic = round((knowledge+practice+application) / 3)
            text "[academic]" size 76 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            $ social = round((friend+community+public) / 3)
            text "[social]" size 76 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
  
        hbox:
            # xpos 300
            xalign 0.5
            ypos 355
            #ed1
            if social >= 70 and health >= 70 and academic >= 70:
                $ edidaman = True
                imagebutton:
                    ypos 120
                    idle "rangkuman/idaman.png"
                    action NullAction()
            elif social >= 40 and health >= 40 and academic >= 40 and social < 70 and health < 70 and academic < 70:
                $ ednormies = True 
                imagebutton:
                    ypos 120
                    idle "rangkuman/normies.png"
                    action NullAction()
            elif social < 40 and health < 40 and academic < 40:
                $ edbadend = True 
                imagebutton:
                    ypos 120
                    idle "rangkuman/bad_end.png"
                    action NullAction()

            #aca
            elif academic > health and academic > social:
                #hi mid mid
                if academic >= 70 and social <70 and social >= 40 and health <70 and health >= 40: 
                    $ edkutu = True
                    imagebutton:
                        ypos 120
                        idle "rangkuman/kutu.png"
                        action NullAction()
                #hi low low
                elif academic >= 70 and social < 40 and health < 40: 
                    $ ednolife = True
                    imagebutton:
                        ypos 120
                        idle "rangkuman/no_life.png"
                        action NullAction()
                #mid low low
                elif academic <70 and academic >= 50 and social < 40 and health < 40:
                    $ ednormies = True 
                    imagebutton:
                        ypos 120
                        idle "rangkuman/normies.png"
                        action NullAction()
                #else
                else:
                    $ edkutu = True 
                    imagebutton:
                        ypos 120
                        idle "rangkuman/kutu.png"
                        action NullAction()

            #soc
            elif social > health and social > academic:
                #hi mid mid
                if social >= 70 and academic <70 and academic >= 40 and health <70 and health >= 40: 
                    $ edantikupu = True
                    imagebutton:
                        ypos 120
                        idle "rangkuman/anti_kupu.png"
                        action NullAction()
                #hi low low
                elif social >= 70 and academic < 40 and health < 40: 
                    $ edbagaikuda = True
                    imagebutton:
                        ypos 120
                        idle "rangkuman/bagai_kuda.png"
                        action NullAction()
                #mid low low
                elif social <70 and social >= 40 and academic < 40 and health < 40: 
                    $ ednormies = True
                    imagebutton:
                        ypos 120
                        idle "rangkuman/normies.png"
                        action NullAction()
                #else
                else:
                    $ edantikupu = True 
                    imagebutton:
                        ypos 120
                        idle "rangkuman/anti_kupu.png"
                        action NullAction()

            #health
            elif health > academic and health > social: 
                #hi mid mid
                if health >= 70 and academic <70 and academic >= 40 and social <70 and social >= 40: 
                    $ edsehatno = True
                    imagebutton:
                        ypos 120
                        idle "rangkuman/sehat_no.png"
                        action NullAction()
                #hi low low
                elif health >= 70 and academic < 40 and social < 40: 
                    $ edsehatno = True
                    imagebutton:
                        ypos 120
                        idle "rangkuman/sehat_no.png"
                        action NullAction()
                #mid low low
                elif health <70 and health >= 40 and academic < 40 and social < 40:
                    $ ednormies = True 
                    imagebutton:
                        ypos 120
                        idle "rangkuman/normies.png"
                        action NullAction()
                #else
                else:
                    $ edsehatno = True 
                    imagebutton:
                        ypos 120
                        idle "rangkuman/sehat_no.png"
                        action NullAction()


    #slide left
    imagebutton:
        xpos 800
        ypos 950
        auto "tutorial/left_%s.png"
        action  [Hide("ending_page"), Show("rangkuman_screen5")]    

    #slide right
    imagebutton:
        xpos 1000
        ypos 950
        auto "tutorial/right_%s.png"
        action  [Hide("ending_page"), Return()]

screen ending_screen1:

    frame:
        xsize 1920
        ysize 1080

        background "rangkuman/rangkuman_lokasi.png"


