import hashlib

# Proses Enkripsi MD5 (Hashing)
def enkripsi_md5(teks):
    hasil = hashlib.md5(teks.encode("utf-8")).hexdigest()
    return hasil


# Proses Verifikasi MD5
def verifikasi_md5(teks, hash_input):
    hash_asli = enkripsi_md5(teks)

    if hash_asli == hash_input.strip().lower():
        return "Hash cocok! Verifikasi berhasil."
    else:
        return "Hash tidak cocok!"
