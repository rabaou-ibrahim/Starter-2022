CSV_file.csv = $1
sudo adduser $2
sudo u+rwx $1
if [ $2 == ./groups ] then
useradd -g admin $2
sudo mkhomedir_helpler $2
chmod $2 ./home