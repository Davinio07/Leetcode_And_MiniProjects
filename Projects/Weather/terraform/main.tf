resource "azurerm_resource_group" "daviresourcegroup" {
    name = var.Resource_Group_Name
    location = var.location
}

resource "azurerm_storage_account" "davistoragesccount" {
    name = var.Storage_Account_Name 
    location = var.location
    resource_group_name = azurerm_resource_group.daviresourcegroup.name
    account_tier = var.account_Tier
    account_replication_type = var.account_replication_type
}

resource "azurerm_application_insights" "applicationinsights" {
    name = var.application_type_name
    resource_group_name = azurerm_resource_group.daviresourcegroup.name
    location = var.location
    application_type = var.application_type
    }

resource "azurerm_service_plan" "serviceplan" {
  name = var.azurerm_service_plan_name
  resource_group_name = azurerm_resource_group.daviresourcegroup.name
  location = var.location
  os_type = var.os_type
  sku_name = var.sku_name
}

resource "azurerm_linux_function_app" "linuxfunctionapp" {
    name = var.linux_function_app_name
    resource_group_name = azurerm_resource_group.daviresourcegroup.name
    location = var.location
    storage_account_name = azurerm_storage_account.davistoragesccount.name
    storage_account_access_key = azurerm_storage_account.davistoragesccount.primary_access_key
    service_plan_id = azurerm_service_plan.serviceplan.id
    site_config {
        application_stack {
          python_version = "3.11"
        }
    }
    
    app_settings = {
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.applicationinsights.connection_string
  }
}