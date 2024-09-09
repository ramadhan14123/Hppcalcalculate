$(document).ready(function() {
    // Fungsi untuk menambahkan label biaya baru
    $('#add-biaya').click(function() {
        let newBiayaItem = `
            <div class="biaya-item">
                <input type="text" placeholder="Nama Biaya" class="nama-biaya">
                <input type="number" placeholder="Jumlah Biaya (Rp)" class="jumlah-biaya">
            </div>`;
        $('#biaya-container').append(newBiayaItem);
    });

    // Fungsi untuk menghitung total HPP dan menampilkan biaya
    $('#hitung-hpp').click(function() {
        let biayaItems = [];
        let biayaListHTML = '';

        // Ambil semua input biaya
        $('.biaya-item').each(function() {
            let namaBiaya = $(this).find('.nama-biaya').val();
            let jumlahBiaya = $(this).find('.jumlah-biaya').val();
            if (namaBiaya && jumlahBiaya) {
                biayaItems.push({ nama: namaBiaya, biaya: jumlahBiaya });
                biayaListHTML += `<li>${namaBiaya}: Rp ${jumlahBiaya}</li>`;
            }
        });

        // Kirim data ke server Flask untuk dihitung
        $.ajax({
            url: '/hitungHpp',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ biaya_items: biayaItems }),
            success: function(response) {
                $('#total-hpp').text(response.total_biaya);
                $('#biaya-list').html(biayaListHTML); // Update the list with biaya items
                $('#result').show();
            }
        });
    });
});
