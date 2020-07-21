#### welcome page with animal tree ###
my_browser = "chrome"
tree_url = "http://localhost:3000/"

tree_list_css = ".tree li"
whole_tree_css = '#root > div > div > div:nth-child(2) > div:nth-child(2) > div > ol'

delete_node_btn_css = ".deleteNode"

frog_label_xpth = '//*[@id="root"]/div/div/div[2]/div[2]/div/ol/ol[3]/li[1]/text()'

ant_label_xpth = '//*[@id="root"]/div/div/div[2]/div[2]/div/ol/ol[1]/li[1]/text()'
ant_text_box_css = "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > ol > ol:nth-child(2) > li:nth-child(2) > input[type=text]"

ant_delete_node_xpth = '//*[@id="root"]/div/div/div[2]/div[2]/div/ol/ol[1]/li[1]/span'

rat_label_xpth = '//*[@id="root"]/div/div/div[2]/div[2]/div/ol/ol[1]/ol/li[1]/text()'
rat_delete_node_xpth = '//*[@id="root"]/div/div/div[2]/div[2]/div/ol/ol[1]/ol/li[1]/span'

ant_txt_xpth = '//*[@id="root"]/div/div/div[2]/div[2]/div/ol/ol[1]/li[2]/input'
frog_text_input_xss = '#root > div > div > div:nth-child(2) > div:nth-child(2) > div > ol > ol:nth-child(4) > li:nth-child(2) > input[type=text]'