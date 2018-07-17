from gmail import GMail, Message
from random import choice

gmail = GMail('nhung11296@gmail.com','nambatcohoi')

html_content = """
<p style="text-align: center;">&nbsp; &nbsp; Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<h1 style="text-align: center;">ĐƠN XIN NGHỈ HỌC</h1>
<p>K&iacute;nh gửi : Huỳnh Tuấn Anh</p>
<p>T&ecirc;n em l&agrave;: Đỗ Thị Hồng Nhung - Lớp C4E19</p>
<p>Em viết đơn n&agrave;y xin nghỉ 1 buổi với l&iacute; do {{sickness}}</p>
<p>Em hứa sẽ l&agrave;m b&agrave;i đ&acirc;y đủ</p>
<p>Em xin cảm ơn!</p>
<p>&nbsp;</p>
<h1>&nbsp;</h1>
"""
reasons = ["reason 1", "reason 2", "reason3", "reason 4", "reason 5"]
# random trong list
choice(reasons)

html_to_send = html_content.replace("{{sickness}}",choice(reasons))

msg = Message('123', to = '20130075@student.hust.edu.vn', html=html_to_send)
gmail.send(msg)