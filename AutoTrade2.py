import easytrader
from easytrader import helpers

user = easytrader.use('ht_client')
user.prepare(user='666628069726', password='518518',commpasswd='516518', exe_path='D:\\软件安装\\htwt\\xiadan.exe')



# user = easytrader.use('xq',initial_assets=50000)
# user.prepare('xq_18521312371.json')
 
# xq_follower = easytrader.follower('xq')
# xq_follower.login(user='18521312371', password='19891121lC')
# xq_follower.follow(user, 'ZH010389', total_assets=50000)

xq_follower = easytrader.follower('xq')
xq_follower.login(user='18521312371', password='19891121lC')
xq_follower.follow(user, 'ZH1110261', total_assets=76675, cmd_cache=False)