# MEMBUAT KELAS DENGAN NAMA "KAMUS" DAN DENGAN METODE TAMBAH DAN AMBILSINONIM
class Kamus:
    # INPUT DIIBARATKAN SEBGAI SEBUAH GRAPH, UNTUK IMPLEMENTASI GRAPH MENGGUNAKAN DICTIONARY
    def __init__(self) -> None:
        self.dict = {}

    # INPUT AKAN DIMASUKKAN KE DICTIONARY SEMUA KATA DIJADIKAN SEBUAH KEY, 
    # APABILA SUDAH TERDAPAT KEY TERKAIT MAKA KATA YANG BERHUBUNGAN DI ASSIGN SEBAGAI ARRAY PADA VALUE DICTIONARY
    def tambah(self, fromNode, toNode):
        if not fromNode in self.dict.keys():
            self.dict[fromNode] = []
        
        for node in toNode:
            self.dict[fromNode].append(node)
            if not node in self.dict.keys():
                self.dict[node] = []
            self.dict[node].append(fromNode)

    # UNTUK MENGAMBIL SINONIM, KARENA SUDAH DIBENTUK SEPERTI GRAPH MAKA YANG DIAMBIL SEMBAGAI SINONIM MERUPAKAN NEIGHBOR DARI KATA/NODE TERSEBUT
    def ambilSinonim(self, node):
        if node in self.dict.keys():
            print(self.dict[node])

kamus = Kamus()
kamus.tambah("big", ["large", "great"])
kamus.tambah("big", ["huge", "fat"])
kamus.tambah("huge", ["enormous", "gigantic"]);
kamus.ambilSinonim("big")
kamus.ambilSinonim("huge")
kamus.ambilSinonim("collosal")