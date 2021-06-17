# NuToKvm
此程式可以將Nutanix的VM轉為Proxmox的qcow2，並運行  
事先步驟:  
    1.先在Proxmox放置qcow2 image上的nfs server上掛載nitanix storeage container  
    2.Proxmox建立一個VM其磁碟大小與Nutanix上的VM磁碟大小一樣  
    3.之後執行此程式依照提示輸入Proxmox的VM編號及Nutanix上的VM名稱即可進行轉換  
 
