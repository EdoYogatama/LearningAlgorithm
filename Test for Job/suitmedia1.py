def tekaTekiTeko(batas):
    # FUNGSI YANG MENGOLAH ANGKA INPUT SESUAI DENGAN KRITERIA SOAL
    for i in range(batas):
        num = i+1
        a = num%2
        b = num%3
        c = num%5
        # MENGGUNAKAN IF ELSE STATEMENT DALAM PERINTAH PRINT 
        # ANGKA YANG DI MOD DAN MENGHASILKAN NILAI 0 MAKA HABIS DIBAGI
        print("Teka" if(a==0 and b>0 and c>0) # HANYA 2
                else "Teki" if(a>0 and b==0 and c>0) # HANYA 3
                else "Teko" if(a>0 and b>0 and c==0) # HANYA %
                else "TekaTeki" if(a==0 and b==0 and c>0) # 2 DAN 3
                else "TekaTeko" if(a==0 and b>0 and c==0) # 2 DAN 5
                else "TekiTeko" if(a>0 and b==0 and c==0) # 3 DAN 5
                else "TekaTekiTeko" if(a==0 and b==0 and c==0) # SEMUA
                else num) # TIDAK HABIS DIBAGI ANGKA 2,3,5   

# MENGGUNAKAN WHILE UNTUK ERROR EXCEPTION SEHINGGA JIKA ANGKA YANG DI INPUT KURANG DARI 20 PROGRAM AKAN MEMINTA INPUT KEMBALI
batas = int(input())
while(batas < 20):
    print("Nilai input harus lebih besar dari 20")
    batas = int(input())
tekaTekiTeko(batas)