import json as json
from pprint import pprint

with open('sample.json','r') as data_file:    
    data = json.load(data_file)
    data["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["protocal"] = "udp"
    data["vnics"]["vnics"][2]["portgroupName"] = "EXT_VLAN_201b"
    data["featureConfigs"]["features"][5]["ospf"]["enabled"] = "true"

    data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["holdDownTimer"] =  data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["holdDownTimer"] +  data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["keepAliveTimer"]

    data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["holdDownTimer"] =  data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["holdDownTimer"] +  data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["keepAliveTimer"]

    data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["holdDownTimer"] =  data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["holdDownTimer"] +  data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["keepAliveTimer"]
    pprint(data)
    


