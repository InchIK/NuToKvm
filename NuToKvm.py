import paramiko
from shutil import copyfile
import subprocess
import os
import sys

#nutanix cvm ip address
ip = "192.168.1.2"
#nutanix cvm login username
username = "username"
#nutanix cvm login password
password = "password"
#Proxmox mount nutanix storeage container patch
srcPath = "/mnt/nutanix/.acropolis/vmdisk/"
#Proxmox cpoy nutanix vmdisk file temp patch
tmpPath = "/nfs/tmp/"
#Proxmox qcow2 image file patch
dstPath = "/nfs/images/"

def nuVmDiskUUID(vmname):
   try:
       client = paramiko.SSHClient()
       client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       client.connect(ip, port=22, username=username, password=password, timeout=20)
       #get NUTANIX VMDISK_UUID
       command = "/usr/local/nutanix/bin/acli vm.disk_get " + vmname + " include_vmdisk_paths=1 | grep -Ew \'vmdisk_uuid\'"
       stdin, stdout, stderr = client.exec_command(command)
       result = stdout.readlines()
       if client is not None:
          client.close()
          del client, stdin, stdout, stderr
   except:
      print("SSH Connect Error!!")
   return result

try:
   proxmoxNumber = input("key in Proxmox Number:")
   vmname = input("key in vmname:")
   print("Input Proxmox Number:",proxmoxNumber)
   print("Input Nutanix VM Name:",vmname)
   if len(vmname) > 0:
      #get VMDISK_UUID Amount
      resultLen = len(nuVmDiskUUID(vmname))
      result = nuVmDiskUUID(vmname)
      #List VMDISK_UUID
      for i in range(resultLen):
         sourceVmdisk = result[i][16:-2]
         print("VMDisk" + "[" + str(i) + "]:",sourceVmdisk)
         print("VMDisk Amount: " + str(resultLen))
         #vmfile vmsrc to vmtmp
         vmsrc = srcPath + sourceVmdisk
         vmtmp = tmpPath + sourceVmdisk
         fsize = int(os.path.getsize(vmsrc))
         print("vmdisk-size:" + str(fsize/1024**3) +"GB")
         print("copying....")
         copyfile(vmsrc,vmtmp)
         print("copy done!")
         print("Start Conver ",sourceVmdisk," -> vm-" + proxmoxNumber + "-disk-" + str(i) +".qcow2",)
         cmdScript = "qemu-img convert -c " + tmpPath  + sourceVmdisk + " -O qcow2 " + dstPath + proxmoxNumber + "/vm-" + proxmoxNumber + "-disk-" + str(i) + ".qcow2"
         print("Convering.....")
         os.system(cmdScript)
         print("Conver done!")
         #del tmp vmfile
         os.remove(vmtmp)
   else:
      print("Input Vm Name!")
except KeyboardInterrupt:
   print("\nConnect close!")
