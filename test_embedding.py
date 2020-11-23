from alpaca_server.alpaca_model.pytorchAPI.utils import get_glove_embeddings
vocab={"hello":1, "nhanh":2,"chào_mừng":0}
# vocab={'<pad>': 0, 'của': 1, 'ông': 2, 'là': 3, '.': 4, 'đã': 5, 'người': 6, '...': 7, 'nước_mắm': 8, 'nhưng': 9, 'tôi': 10, 'có': 11, 'cái': 12, 'ba_phước': 13, 'cả': 14, 'đó': 15, 'sản_xuất': 16, 'tui': 17, 'mấy': 18, 'đang': 19, 'cơ_nghiệp': 20, 'chuyên_môn_hoá': 21, 'tốt': 22, 'nhiều': 23, 'về': 24, 'mới': 25, 'để': 26, 'và': 27, 'cho': 28, 'còn': 29, 'bạc': 30, 'hiện': 31, 'một': 32, 'nói': 33, 'phước_hương': 34, 'chục': 35, 'hầm': 36, 'nuôi': 37, 'trên': 38, 'con': 39, 'cá_tra': 40, 'sẽ': 41, 'theo': 42, 'chỉ': 43, 'từ': 44, 'tạo_lập': 45, 'nên': 46, 'xu_hướng': 47, 'phát_triển': 48, 'việc': 49, 'cũng': 50, 'thì': 51, 'quả': 52, 'quá': 53, 'nghe': 55, 'đến': 56, 'hôm_nay': 57, 'dịp': 58, 'ấp': 59, 'long_châu': 60, '1': 61, 'xã': 62, 'thạnh_mỹ_tây': 63, 'châu_phú_an_giang': 64, 'gặp': 65, 'người_ta': 66, 'thường': 67, 'gọi': 68, 'ba': 69, 'phước': 70, 'trần': 71, 'văn_minh': 72, 'bỏ': 73, 'công': 74, 'ngày_tháng': 75, 'lo': 76, 'chỗ': 77, 'an_nghỉ': 78, 'cuối': 79, 'đời': 80, 'những': 81, 'dân_nghèo': 82, 'vùng': 83, 'lũ': 84, 'mất': 85, 'vóc': 86, 'nhỏ_nhắn': 87, 'tóc': 88, 'da': 89, 'ngăm_ngăm': 90, 'mặt': 91, 'rõ': 92, 'nét': 93, 'từng_trải': 94, 'ông_già': 95, '70': 96, 'tuổi': 97, 'cuộc_đời': 98, 'cần_cù': 99, 'lao_động': 100, 'miệt_mài': 101, 'đứng': 102, 'bên': 103, 'với': 104, 'giọng': 105, 'tự_hào': 106, 'chú': 107, 'xem': 108, 'cơ_sở': 109, 'năm': 110, 'làm': 111, 'ra': 112, 'gần': 113, '2000': 114, 'tấn': 115, 'cá': 116, '600000': 117, 'tất_cả': 118, 'tài_sản': 119, 'giờ_đây': 120, '3': 121, 'tỉ': 122, 'rồi': 123, 'chẳng': 124, 'nữa': 125, 'nghĩa_địa': 126, 'nhìn': 127, 'hướng': 128, 'cánh_tay': 129, 'căn': 130, 'nhà': 131, 'đúc': 132, 'nằm': 133, 'ven': 134, 'kênh_xáng': 135, 'vịnh_tre': 136, 'vòng': 137, 'qua': 138, 'dãy': 139, 'nhà_kho': 140, 'ủ': 141, 'lố_nhố': 142, 'công_nhân': 143, 'làm_việc': 144, 'mà': 145, 'thầm': 146, 'khâm_phục': 147, 'nông_dân': 148, 'tốt_nghiệp': 149, 'tiểu_học': 150, 'trường': 151, 'làng': 152, 'bàn_tay': 153, 'trắng': 154, 'chủ_tịch': 155, 'hội_đồng_quản_trị': 156, 'doanh_nghiệp': 157, 'tư_nhân': 158, 'lại': 159, 'bảo': 160, 'chẳng_là': 161, 'mình': 162, 'bởi': 163, 'cách': 164, 'được': 165, 'chia': 166, 'con_cháu': 167, 'chúng': 168, 'trực_tiếp': 169, 'tổ_chức': 170, 'kinh_doanh': 171, '<unk>': 172}#{"hello":1, "sorry":0,"chào_mừng":2, ".":3}#[0,1,2]
sen=[['Chuyên_môn_hoá', 'là', 'xu_hướng', 'của', 'phát_triển', 'việc', 'tốt', 'cũng', 'chuyên_môn_hoá', 'thì', 'quả', 'là', 'tốt', 'quá', '.'], [ 'Nghe', 'nhiều', 'về', 'ông', 'nhưng', 'đến', 'hôm_nay', 'tôi', 'mới', 'có', 'dịp', 'về', 'ấp', 'Long_Châu', '1', 'xã', 'Thạnh_Mỹ_Tây', 'Châu_Phú_An_Giang', 'để', 'gặp', 'ông', '.'], ['Người_ta', 'thường', 'gọi', 'ông', 'là', 'ông', 'Ba', 'Phước', 'Trần', 'Văn_Minh', 'người', 'đã', 'bỏ', 'nhiều', 'công', 'của', 'và', 'ngày_tháng', 'để', 'lo', 'chỗ', 'an_nghỉ', 'cuối', 'đời', 'cho', 'những', 'người', 'dân_nghèo', 'vùng', 'lũ', '...'], ['Cái', 'mất', 'cái', 'còn', '.'], ['Ông', 'Ba_Phước', 'vóc', 'người', 'nhỏ_nhắn', 'tóc', 'bạc', 'da', 'ngăm_ngăm', 'mặt', 'hiện', 'rõ', 'nét', 'từng_trải', 'của', 'một', 'ông_già', '70', 'tuổi', 'đã', 'có', 'cả', 'cuộc_đời', 'cần_cù', 'lao_động', 'miệt_mài', '.'], ['Ông', 'đứng', 'bên', 'tôi', 'nói', 'với', 'giọng', 'tự_hào', '.'], ['Chú', 'xem', 'đó', 'cả', 'cơ_sở', 'sản_xuất', 'nước_mắm', 'Phước_Hương', 'một', 'năm', 'làm', 'ra', 'gần', '2000', 'tấn', 'nước_mắm', 'cả', 'chục', 'hầm', 'nuôi', 'cá', 'hiện', 'có', 'trên', '600000', 'con', 'cá_tra', '...'], ['Tất_cả', 'tài_sản', 'của', 'tui', 'giờ_đây', 'trên', '3', 'tỉ', 'bạc', 'rồi', 'sẽ', 'chẳng', 'còn', 'là', 'của', 'tui', 'nữa', 'nhưng', 'cái', 'nghĩa_địa', 'đó', 'mới', 'là', 'của', 'tui', '...'], ['Tôi', 'nhìn', 'theo', 'hướng', 'cánh_tay', 'của', 'ông', 'Ba_Phước', 'chỉ', 'từ', 'căn', 'nhà', 'đúc', 'nằm', 'ven', 'con', 'kênh_xáng', 'Vịnh_Tre', 'vòng', 'qua', 'mấy', 'dãy', 'nhà_kho', 'ủ', 'nước_mắm', 'mấy', 'hầm', 'nuôi', 'cá_tra', 'đang', 'lố_nhố', 'mấy', 'chục', 'công_nhân', 'làm_việc', 'mà', 'thầm', 'khâm_phục', 'người', 'nông_dân', 'chỉ', 'tốt_nghiệp', 'tiểu_học', 'trường', 'làng', 'từ', 'bàn_tay', 'trắng', 'đã', 'tạo_lập', 'nên', 'cơ_nghiệp', '...'], ['Ba_Phước', 'đang', 'là', 'chủ_tịch', 'hội_đồng_quản_trị', 'doanh_nghiệp', 'tư_nhân', 'sản_xuất', 'nước_mắm', 'Phước_Hương', 'nhưng', 'lại', 'bảo', 'cơ_nghiệp', 'đó', 'sẽ', 'chẳng_là', 'của', 'mình', 'bởi', 'theo', 'cách', 'nói', 'của', 'ông', 'cơ_nghiệp', 'ông', 'tạo_lập', 'nên', 'đã', 'được', 'chia', 'cho', 'con_cháu', 'chúng', 'đã', 'và', 'đang', 'trực_tiếp', 'tổ_chức', 'sản_xuất', 'kinh_doanh', '.']]#[["hello", "sorry", "chào_mừng", "."]]
embeddings = get_glove_embeddings(vocab, 100)#, sen)
print(embeddings)