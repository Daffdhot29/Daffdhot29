import cv2 as cv
from numpy import pi 

# settings camera
Camera = cv.VideoCapture(0)
Camera.set(cv.CAP_PROP_FRAME_WIDTH,1280)
Camera.set(cv.CAP_PROP_FRAME_HEIGHT,1280)

while True:
    _, frame = Camera.read()
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)
    cv.circle(frame,(cx,cy),5,(25,25,25),2)

    # mengambil nilai dari warna pixel 
    pixel_center = hsv_frame[cy,cx]
    hue = pixel_center[0]
    saturation = pixel_center[1] #intensitas warna
    value = pixel_center[2]

    color = "Null"

    if color == 0 | saturation == 0 :
         color = "WHITE"
    elif value < 50 :
        color = "BLACK"
    elif saturation < 50 :
        color = "GRAY"
    elif hue < 5 :
         color = "RED"
    elif hue < 15 :
        color = "ORANGE" 
    elif hue < 31 :
        color = "BROWN"
    elif hue < 35 :
        color = "YELLOW"
    elif hue < 75 :
        color = "GREEN"
    elif hue < 120 :
        color = "BLUE"
    elif hue < 170 :
        color = "PINK"
    else :
        color = "RED"
    pixel_center_bgr = frame[cy,cx]

    b = int(pixel_center_bgr[0])
    g = int(pixel_center_bgr[1])
    r = int(pixel_center_bgr[2])
    
    print(pixel_center)

    cv.putText(frame,color,(cy-100, cx-100),0, 2,(b,g,r),9)
    cv.imshow("Color Detector",frame)
    key = cv.waitKey(1)

    if key == 27:
        break

Camera.release()
cv.destroyAllWindows()

# Noted

# import cv2 as cv: Mengimpor pustaka OpenCV untuk pemrosesan citra. Pustaka ini sering digunakan dalam pemrosesan gambar, deteksi objek, dan visi komputer.
# from numpy import pi: Mengimpor nilai pi dari pustaka NumPy. Pada kode ini, pi tidak digunakan, sehingga bisa dihapus.
# Camera = cv.VideoCapture(0): Membuka kamera (kamera default dengan ID 0). Fungsi ini digunakan untuk menangkap video dari perangkat kamera.
# Camera.set(cv.CAP_PROP_FRAME_WIDTH, 1280): Mengatur lebar resolusi frame menjadi 1280 piksel.
# Camera.set(cv.CAP_PROP_FRAME_HEIGHT, 1280): Mengatur tinggi resolusi frame menjadi 1280 piksel.
# while True:: Membuat loop yang terus berjalan untuk menangkap gambar dari kamera secara terus-menerus.
# _, frame = Camera.read(): Menangkap frame gambar dari kamera. _ di sini digunakan untuk mengabaikan nilai kembalian pertama (boolean yang menunjukkan apakah frame berhasil dibaca atau tidak), 
# sementara frame menyimpan data gambar.
# hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV): Mengubah gambar yang awalnya dalam format BGR (Blue, Green, Red) menjadi format HSV (Hue, Saturation, Value). 
# Format HSV lebih mudah digunakan untuk deteksi warna.
# height, width, _ = frame.shape: Mengambil dimensi gambar (tinggi dan lebar). _ digunakan untuk mengabaikan saluran warna (BGR) yang ketiga.
# cx = int(width / 2): Menghitung koordinat horizontal (x) dari tengah gambar.
# cy = int(height / 2): Menghitung koordinat vertikal (y) dari tengah gambar.
# cv.circle(frame, (cx, cy), 5, (25, 25, 25), 2): Menggambar lingkaran kecil di tengah gambar untuk menunjukkan titik pusat. 5 adalah radius, (25, 25, 25) 
# adalah warna (hijau dalam BGR), dan 2 adalah ketebalan garis.
# pixel_center = hsv_frame[cy, cx]: Mengambil nilai HSV dari pixel yang terletak di tengah gambar.
# hue = pixel_center[0]: Mengambil nilai Hue (warna) dari pixel tersebut.
# saturation = pixel_center[1]: Mengambil nilai Saturation (intensitas warna) dari pixel tersebut.
# value = pixel_center[2]: Mengambil nilai Value (kecerahan) dari pixel tersebut.
# color = "Null": Menetapkan nilai awal untuk variabel color, yang akan berfungsi untuk menyimpan hasil deteksi warna.
# if color == 0 | saturation == 0:: Pemeriksaan kondisi jika color bernilai 0 atau jika saturation bernilai 0. Namun, sintaks ini salah karena operator bitwise | digunakan, yang seharusnya adalah operator logika or. Seharusnya:
# Tujuan dari bagian ini adalah mendeteksi warna putih (dengan nilai saturation 0).
# elif value < 50:: Jika nilai kecerahan (value) lebih rendah dari 50, maka warna dianggap hitam.
# elif saturation < 50:: Jika intensitas warna (saturation) lebih rendah dari 50, maka warna dianggap abu-abu (gray).
# elif hue < 5:: Jika nilai hue kurang dari 5, maka warna dianggap merah.
# elif hue < 15:: Jika nilai hue kurang dari 15, maka warna dianggap oranye.
# elif hue < 31:: Jika nilai hue kurang dari 31, maka warna dianggap coklat.
# elif hue < 35:: Jika nilai hue kurang dari 35, maka warna dianggap kuning.
# elif hue < 75:: Jika nilai hue kurang dari 75, maka warna dianggap hijau.
# elif hue < 120:: Jika nilai hue kurang dari 120, maka warna dianggap biru.
# elif hue < 170:: Jika nilai hue kurang dari 170, maka warna dianggap merah muda (pink).
# else:: Jika tidak ada kondisi sebelumnya yang terpenuhi, maka warna dianggap merah.
# pixel_center_bgr = frame[cy, cx]: Mengambil nilai warna pixel di titik tengah gambar dalam format BGR (Blue, Green, Red).
# b = int(pixel_center_bgr[0]): Menyimpan nilai biru dari pixel.
# g = int(pixel_center_bgr[1]): Menyimpan nilai hijau dari pixel.
# r = int(pixel_center_bgr[2]): Menyimpan nilai merah dari pixel.
# print(pixel_center): Menampilkan nilai pixel yang diambil di tengah gambar dalam format HSV.
# cv.putText(frame, color, (cy-100, cx-100), 0, 2, (b, g, r), 9): Menambahkan teks (warna terdeteksi) ke gambar pada posisi yang disesuaikan dengan titik tengah, dengan ukuran font 2 dan ketebalan 9.   
# cv.imshow("Color Detector", frame): Menampilkan gambar dengan teks warna yang terdeteksi dalam jendela bernama "Color Detector".
# key = cv.waitKey(1): Menunggu input dari pengguna. Jika pengguna menekan tombol tertentu (misalnya, ESC), loop akan berhenti.
# if key == 27:: Jika tombol ESC (dengan kode ASCII 27) ditekan, keluar dari loop dan menghentikan aplikasi.
# Camera.release(): Melepaskan sumber daya kamera setelah selesai digunakan.
# cv.destroyAllWindows(): Menutup semua jendela yang dibuka oleh OpenCV.
