from user import User_big
from user import Post
user_one=User_big("Đặng Lê Huy","huydl@gmail.com",123456,"Chăn lợn")
user_two=User_big("Mai Anh Sỹ","syma@gmail.com",32332,"Bán trà đá")
#user_one.Show_infor()
user_two.Show_infor()

new_job_user_one=user_one.Change_job_title("Nói phét")
user_one.Show_infor()

new_post=Post("Làm chủ python trong 4 tuần",user_one.name)
new_post.Show_post_infor()