from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim
import ssl
import atexit

ESXi_host = "" # target IP address
ESXi_user = "root"
ESXi_pass = "" # password

target_vm_name = "VM01"

guest_user = "administrator" # the user name of guest OS
guest_pass = "" # the password

guest_cmd_path = "C:\\Windows\\System32\\cmd.exe" # absolute path
guest_cmd_args = "powershell get-host"

si = SmartConnectNoSSL(host=ESXi_host, user=ESXi_user, pwd=ESXi_pass)
atexit.register(Disconnect, si)
content = si.content

vm_objects = conetnt.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
vm = ""

for vm_obj in vm_objects.view:
	if vm_obj.name == target_vm_name:
		vm = vm_obj
		break

creds = vim.vm.guest.NamePasswordAuthentication(username=guest_user, password=guest_pass)
spec = vim.vm.guest.ProcessManager.ProgramSpec(programPath=guest_cmd_path, arguments=guest_cmd_args)
print(content.guestOperationsManager.processManager.StartProgramInGuest(vm, creds, spec))