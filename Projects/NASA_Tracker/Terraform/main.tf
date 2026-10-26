resource "azurerm_resource_group" "resource_Group" {
  name = var.Resource_Group_name
  location = var.location
}

resource "azurerm_storage_account" "storage_Account" {
  name = var.Storage_Account_name
  resource_group_name = azurerm_resource_group.resource_Group.name
  location = var.location
  account_tier = var.Account_Tier
  account_replication_type = var.account_replication_type

}

resource "azurerm_storage_container" "storage_Container" {
  name = var.storage_Container_name
  storage_account_id = azurerm_storage_account.storage_Account.id
  container_access_type = "private"
}