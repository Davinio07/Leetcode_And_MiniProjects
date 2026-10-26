variable "location" {
  type    = string
  default = "northeurope"
}

variable "Resource_Group_name" {
  type = string
  default = "Resource_Group_davi"
}

variable "Storage_Account_name" {
    type = string
    default = "storageaccountdavi"
}

variable "Account_Tier" {
    type = string
    default = "Standard"
}

variable "account_replication_type" {
    type = string
    default = "LRS"
}

variable "storage_Container_name" {
  type = string
  default = "storagecontainerdavi"
}