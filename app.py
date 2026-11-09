
from flask import Flask, render_template, request
from crypto import enkripsi_md5, verifikasi_md5

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    hasil = ""
    pesan = ""
    teks = ""

    if request.method == "POST":

        teks = request.form.get("teks", "")
        aksi = request.form.get("aksi")
        hash_input = request.form.get("hash_input", "")

        if aksi == "generate":

            if teks:
                hasil = enkripsi_md5(teks)
            else:
                pesan = "Masukkan teks terlebih dahulu!"

        elif aksi == "verify":

            if teks and hash_input:
                pesan = verifikasi_md5(teks, hash_input)
            else:
                pesan = "Lengkapi teks dan hash MD5!"

    return render_template(
        "index.html",
        hasil=hasil,
        pesan=pesan,
        teks=teks
    )

if __name__ == "__main__":
    app.run(debug=True)
