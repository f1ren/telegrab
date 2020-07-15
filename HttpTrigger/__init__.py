import logging

import azure.functions as func

from HttpTrigger.telegram_wrap import web_handler


def main(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()
    logging.info(req.get_body().decode('utf-8')[:1000])
    try:
        web_handler(body)
    except Exception as e:
        logging.exception('Error in web_handler ' + str(e))
        raise

    # create blob service client and container client
    # credential = DefaultAzureCredential()
    # storage_account_url = "https://" + os.environ["par_storage_account_name"] + ".blob.core.windows.net"
    # client = BlobServiceClient(account_url=storage_account_url, credential=credential)
    # blob_name = "test" + str(datetime.now()) + ".txt"
    # blob_client = client.get_blob_client(container=os.environ["par_storage_container_name"], blob=blob_name)
    # blob_client.upload_blob(link_list)

    return func.HttpResponse(
             'OK',
             status_code=200
    )
