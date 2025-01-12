# server test with MinIO
this repository is about create a web static with server MinIO
1. download file from [minio.com](https://min.io/open-source/download?platform=kubernetes), in this project im choose windows.
2. then run minio server in cmd:
   C:\Users\User cd C:\minio #where yours file minio downloading in this case i move from Downloads to Local Disk C
   C:\minio server C:\server_test #create folder first to connect with minio or minio create the folder for you
3. open 127.0.0.1:9000 in your browser to dashboard MinIO with username and password is "minioadmin" if you haven't change the password before
4. and the last, you can manage your server in dashboard minio like create a bucket from dashboard or with SDK whatever you choose it's okay
5. if you want to create, uploud, or delete file from SDK you should see Documentation in [MinIO web](https://min.io/docs/minio/kubernetes/upstream/operations/installation.html)
