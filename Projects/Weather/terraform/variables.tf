variable "Resource_Group_Name" {
  type = string
  default = "daviresourcegroup"
}

variable "location" {
  type = string
  default = "westeurope"
}

variable "Storage_Account_Name" {
  type = string
  default = "davistoragesccount123"
}

variable "account_Tier" {
    type = string
    default = "Standard"
}

variable "account_replication_type" {
    type = string
    default = "LRS"
}

variable "application_type_name" {
  type = string
  default = "applicationinsights"
}

variable "application_type" {
    type = string
    default = "web"
}

variable "azurerm_service_plan_name" {
    type = string
    default = "serviceplanname"
}

variable "os_type" {
    type = string
    default = "Linux"
}

variable "sku_name" {
  type = string
  default = "Y1"
}

variable "linux_function_app_name" {
    type = string
    default = "linuxfunctionappname"
}