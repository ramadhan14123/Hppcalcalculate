from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def hitung_harga_jual(hpp, persentase_keuntungan):
    harga_jual = hpp * (1 + persentase_keuntungan / 100)
    return harga_jual

def hitung_keuntungan(harga_jual, hpp):
    return harga_jual - hpp

def hitung_rugi(hpp, harga_jual):
    if harga_jual < hpp:
        return hpp - harga_jual
    return 0

def hitung_hpp(total_biaya, jumlah_unit):
    return total_biaya / jumlah_unit

def hitung_harga_jual(hpp, persentase_keuntungan):
    harga_jual = hpp * (1 + persentase_keuntungan / 100)
    return harga_jual

@app.route('/')
def halaman():
    return render_template('halaman.html')

@app.route('/profit')
def profit():
    return render_template('profit.html')

@app.route('/hitung', methods=['POST'])
def hitung():
    harga_jual = float(request.form['hargaJual'])
    harga_hpp = float(request.form['hargaHPP'])

    # Hitung selisih
    selisih = harga_jual - harga_hpp
    persentase = (abs(selisih) / harga_hpp) * 100

    if selisih > 0:
        hasil = f"Untung: Rp {selisih:.2f} ({persentase:.2f}%)"
    elif selisih < 0:
        hasil = f"Rugi: Rp {abs(selisih):.2f} ({persentase:.2f}%)"
    else:
        hasil = "Tidak ada untung atau rugi."

    return render_template('profit.html', hasil=hasil)

@app.route('/hpp', methods=['GET', 'POST'])
def hpp():
    if request.method == 'POST':
        total_biaya = float(request.form['total_biaya'])
        jumlah_unit = int(request.form['jumlah_unit'])
        persentase_keuntungan = float(request.form['persentase_keuntungan'])

        hpp = hitung_hpp(total_biaya, jumlah_unit)
        harga_jual = hitung_harga_jual(hpp, persentase_keuntungan)
        rugi_per_unit = hitung_rugi(hpp, harga_jual)

        return render_template('hpp.html', 
                               hpp=hpp, 
                               harga_jual=harga_jual,  rugi_per_unit=rugi_per_unit)

    return render_template('hpp.html')

@app.route('/total')
def tot_biaya():
    return render_template('total_biaya.html')

@app.route('/hitungHpp', methods=['POST'])
def hitung_totalhpp():
    data = request.json  
    total_biaya = 0
    for item in data['biaya_items']:
        total_biaya += float(item['biaya']) 

    response = {
        'total_biaya': total_biaya
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
