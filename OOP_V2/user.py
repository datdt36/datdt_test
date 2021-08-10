class User_big:
    #Thuộc tính
    def __init__(self,name,email,password,job_title):
        self.name=name
        self.email=email
        self.password=password
        self.job_title=job_title

    #Hành vi.
    def Change_job_title(self,new_job_title):
        self.job_title=new_job_title

    #Show infor.
    def Show_infor(self):
        print("User "+self.name+" hiện đang làm "+self.job_title+". Liên hệ qua email "+self.email)


class Post:
    def __init__(self,post_name,author):
        self.post_name=post_name
        self.author=author


    def Show_post_infor(self):
        print("Bài viết: "+self.post_name+" là của tác giả: "+self.author)

