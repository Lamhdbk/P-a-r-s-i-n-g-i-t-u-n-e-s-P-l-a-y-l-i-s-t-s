# P-a-r-s-i-n-g-i-t-u-n-e-s-P-l-a-y-l-i-s-t-s
 tìm nhạc trùng lặp các bản nhạc trong các tệp danh sách phát iTunes và lập các thống kê khác nhau như độ dài bản nhạc và xếp hạng. Bạn sẽ bắt đầu bằng cách xem định dạng danh sách phát iTunes và sau đó tìm hiểu cách trích xuất thông tin từ các tệp này bằng Python. Để vẽ dữ liệu này, bạn sẽ sử dụng thư viện matplotlib

Trong nội dung project này bạn sẽ được học:
1.  xml and property list (p-list) files
2. python list and dictionaries
3. Using python set objects
4. Using numpy array
5. Histogram and scatter plots
6. Making Simple plot with the matplotlib library
7. Creating and saving data file

Trong dự án này, chúng tôi sẽ sử dụng plistlib mô-đun tích hợp để đọc danh sách phát các tập tin. Chúng tôi cũng sẽ sử dụng thư viện matplotlib để vẽ biểu đồ và các mảng numpy để lưu trữ dữ liệu.
Mục tiêu trong dự án này là tìm các bản sao trong bộ sưu tập nhạc của bạn, xác định các bản nhạc được chia sẻ giữa các danh sách phát, vẽ biểu đồ phân phối thời lượng bản nhạc và vẽ biểu đồ mối quan hệ giữa xếp hạng và độ dài bài hát.
Khi bộ sưu tập nhạc của bạn phát triển, bạn luôn có những bài hát trùng lặp. Để xác định các bản sao, hãy tìm kiếm các tên trong từ điển được liên kết với phím Bản nhạc (đã thảo luận trước đó) để tìm các bản sao và sử dụng bản nhạc độ dài như một tiêu chí bổ sung để phát hiện các bản sao, vì một bản nhạc có
tên giống nhau nhưng độ dài khác có thể là duy nhất. Để tìm các bản nhạc được chia sẻ giữa hai hoặc nhiều danh sách phát, bạn sẽ xuất bộ sưu tập dưới dạng tệp danh sách phát, thu thập tên bản nhạc cho từng danh sách phát và so sánh chúng dưới dạng tập hợp để khám phá các tuyến đường chung bằng cách tìm giao điểm
giữa các bộ. Trong khi thu thập dữ liệu từ bộ sưu tập nhạc của mình, bạn sẽ tạo một cặp của các âm mưu với gói âm mưu matplotlib (http://matplotlib.org/) mạnh mẽ được phát triển bởi John Hunter quá cố. Bạn sẽ vẽ một biểu đồ để hiển thị phân phối thời lượng bản nhạc và biểu đồ phân tán để so sánh xếp hạng bài hát với độ dài bài hát.
