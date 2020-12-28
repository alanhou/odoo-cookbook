# Install from command line

## 执行如下命令安装Odoo

### 获取更新
```
sudo apt-get update
```

### 运行如下命令安装主要依赖：
```
sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools
```

### 下载安装wkhtmltopdf：
```
wget  https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb
```

如果以上命令执行中出现错误，使用下面的命令强制安装依赖：
```
sudo apt-get install -f
```

### 配置PostgreSQL数据库

```
sudo apt install postgresql
sudo -u postgres createuser --superuser $(whoami)
```

### 配置git(请自行修改以下信息)
```
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
```

### 克隆 Odoo 代码
```
mkdir ~/odoo-dev
cd ~/odoo-dev
git clone -b 14.0 --single-branch --depth 1 https://github.com/odoo/odoo.git
```

### 创建激活虚拟环境
```
python3 -m venv ~/venv-odoo-14.0
source ~/venv-odoo-14.0/bin/activate
```

### 安装Python依赖
```
cd ~/odoo-dev/odoo/
pip3 install wheel
pip3 install -r requirements.txt
```

### 启动Odoo实例

```
createdb odoo-test
python3 odoo-bin -d odoo-test –i base --addons-path=addons --db-filter=odoo-test$
```





# Install with shell script

## Odoo 14.0安装脚本

##### 1. Download the script（Make sure you have root access）:
```
wget https://raw.githubusercontent.com/alanhou/odoo14-cookbook/master/Chapter01/odoo-install.sh
```

#### 2. Make the script executable
```
sudo chmod +x odoo-install.sh
```
##### 3. Execute the script:
```
sudo ./odoo-install.sh
```

##### 4. Stop all Odoo proccesses: 
```
ps -ef | grep odoo | awk '{ print $2}' | xargs kill -9
```

##### 5. To restart Odoo with logs enabled:  
```
~/odoo-12.0/bin/python3 ~/odoo-dev/odoo/odoo-bin -d odoo-test
```