# git

### Cách xóa 1 branch ở local hoặc remote 
#### Local  
- Liệt kê các branch: git branch:
- Tạo mới 1 branch : git checkout -b level1 
- Xóa nhánh level1 vừa tạo: 
    + Đầu tiên phải checkout ra branch khác, chẳng han: git checkout master  
    + Xóa branch level1: git branch -d level1 
    
#### Remote 
- Trên repo git. Tạo 1 nhành là remote
-  Để xóa nhánh remote: git push -d  origin remote
  
### Caì đặt git
#### Linux
- apt update 
- apt install git 
- git version
#### Mac 
- brew install git 
- git version 


### Cấu hình git
- git config --global user.email "dev.vn@gmail.com"
- git config --global user.name "dev png"
- Xem thông tin vừa cấu hình 
    + username: git config user.name 
    + email : git config user.email 
    
### Git gồm có 3 phần
- Thư mục working directory: Là nơi mà dev lập trình và thay đổi mã nguồn
    + Câu lệnh dùng là: git add 
    
- Staging Area: Quản lý các file đã thay đổi hoặc thêm mới để commit .
    + Câu lệnh: git commit -> dữ liệu được đẩy vào local repository ( new commit)
    + Quay lại commit trước: git checkout HEAD
    
- Local repository:
    + Đẩy những thay đổi lên remote repo : git push  
    + Lấy thay đổi trên remote repo  : git fetch  (Local repository)
    + Lấy các file trên remote rep đến workign dicrectory: git pull 
    
### Tạo git repo trên local 
#### Linux:
- mkdir demogit; cd demogit;
- git init // Khởi tạo
- git status // Xem trạng thái hiện tại của repo 
- git add .
- git commit -m "init demogit" 
- git log // xem log hoặc git log --oneline  
- git show 
- git diff 

- Liệt kê remote repo 
    + git remote -v 
        + origin	https://github.com/png-dev/demogit.git (fetch)
        + origin	https://github.com/png-dev/demogit.git (push)
- Thêm remote repo 
    + git remote add origin link_repo
- Đẩy code từ local repo lên remote repo 
    + git push -u origin name_branch_push 
- Đẩy code từ local repo lên remote repo nhánh mới 
    + git push --set-upstream origin branch_new_repo
- Xóa remote remove origin
    + git remote remove origin  
 
### Lưu thông tin đăng nhập trên git 
- git config credential.helper store 
- Để xóa thông tin đăng nhập 
    + git config credential.helper clean  
    
### git fetch 
- Lấy  các commits, file từ remote repo về local repo, không ảnh hướng dến working directory
- Muốn xem nôi dung cac commit, file
    + git checkout 
- Lấy các nội dung mới nhất từ all branch ở remote repo 
    + git fetch <remote> 
- Branch cụ thể: git fetch <remote> <branch> 

### git pull 
- git pull = git fetch + git merge 
- Khi pull mà bị conflict vì pull origin branch khác ..  Hủy bỏ lệnh git merge 
    + git merge --abort 
    
### git branch 
- Tạo 1 branch 
    + git branch development 
- Liệt kê các branch hiện tại 
    + git branch 
- Chuyển sang 1 branch mới 
    + git switch master 
- Tạo 1 branch mới và chuyển qua branch mới luôn:
    + git checkout -b new_branch 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
    





















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

