# NuToKvm
此程式可以將Nutanix的VM轉為Proxmox的qcow2，並運行  

事先步驟:

    1. 先在Proxmox放置qcow2 image上的nfs server上掛載nitanix storeage container。
    
    2. Proxmox建立一個VM，其磁碟大小與Nutanix上的VM磁碟大小一樣。
    
    3. 之後執行此程式依照提示輸入Proxmox的VM編號及Nutanix上的VM名稱即可進行轉換。  
    
運作流程：  

    1. 尋找nutanix上其vm名稱的disk uuid，並抓出其數量(註1)。  
    2. 將uuid disk copy至Proxmox上的暫存目錄，並將其轉換為qcow2。 
　　3. 轉換後會直接轉至Proxmox上的qcow2檔並取代。 
　　4. 轉換後會刪除在暫存目錄的uuid disk。
    
 
