# debug 10.201.21.146
1.

![alt text](scan.png)
2.

theod@kali:~$ sudo gobuster dir -u http://10.201.21.146/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

![alt text](backup.png)


![alt text](backupweb.png)


![alt text](grid.png)

PHP хэсэг нь формоор ирсэн мэдээллийг сервер дээр message.txt файлын төгсгөлд бичиж хадгалах (лог/сэтгэгдэл хадгалах) зориулалттай: FormSubmit класс, SaveMessage() нь $_GET-ээс утгуудыг авдаг, __destruct() нь file_put_contents()-оор бичдэг.

message > bytes > store

store.evil > unserialize()> message
![alt text](index.png)


![alt text](indph.png)


![alt text](reverse.png)

php code oo ajiluulad awsan formsubmit
![alt text](s.png)


![alt text](url.png)


![alt text](success.png)


![alt text](a.png)


![alt text](passwd.png)

crackdaad jamaica geh password olson
![alt text](ha.png)


![alt text](userf.png)

дээрх мөрийг 00-header файлын төгсгөлд нэмбэл, хэрвээ 00-header файлыг хэн нэгэн дараа гүйцэтгэвэл (эсвэл системийн эхлүүлэх/нийлүүлэх процесс тухайн 00-header-ийг унших байвал) тэр үед /home/james/bash гэж root-ээс үүсгэсэн setuid bash үүсч болох тул james хэрэглэгч түүнээр root эрхээр shell авах боломжтой болно. Энэ нь маш ноцтой privilege escalation (root болно) аюултай.
![alt text](froot.png)


![alt text](lf.png)

