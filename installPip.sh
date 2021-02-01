  #!/bin/sh
echo "正在安装相关依赖包"
sudo python3 -m pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r requirements.txt
