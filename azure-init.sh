# Create Container Registry

# Set the following
project_name="telegrab"
rg=$project_name
loc="westeurope"
plan=$project_name
stor=$project_name
fun=$project_name
acr_id="<< your container repository name >>.azurecr.io"

# Create resource group, storage account and app service plan
az group create -n $rg -l $loc
az storage account create -n $stor -g $rg --sku Standard_LRS
az appservice plan create --name $plan --resource-group $rg --sku P1v2 --is-linux

# Create Azure Function using docker image
az functionapp create --resource-group $rg --os-type Linux --plan  $plan --deployment-container-image-name $acr_id/selenium:latest --name  $fun --storage-account $stor

# To update the function container
az functionapp config container set -n $fun -g $rg --docker-custom-image-name $acr_id/selenium:latest


# Build, push container and set function
docker build --tag telegrab.azurecr.io/selenium . && docker push $acr_id/selenium:latest && az functionapp config container set -n $fun -g $rg --docker-custom-image-name $acr_id/selenium:latest
