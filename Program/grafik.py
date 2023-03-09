def dfs(grafik, mulai, kunjungan=None):
    if kunjungan is None:
        kunjungan = set()
    kunjungan.add(mulai)
    print(mulai)
    for anggota in grafik[mulai]:
        if anggota not in kunjungan:
            dfs(grafik, anggota, kunjungan)

# Contoh pemanggilan fungsi untuk memulai DFS
grafik = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs(grafik, 'A')