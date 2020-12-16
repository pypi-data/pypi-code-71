import requests, json, datetime
from .models.product import VtexProduct
from .models.product import VtexSku
from .models.product import VtexPrice
from .models.product import VtexInventory

class VtexController:
    @classmethod
    def get_product_by_refId(self, base_url='', app_key='', app_token='', refId=''):
        # create headers
        headers = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        headers['X-VTEX-API-AppKey'] = app_key
        headers['X-VTEX-API-AppToken'] = app_token
        
        # do request to get product by refId
        r = requests.get(f'{base_url}/catalog_system/pvt/products/productgetbyrefid/{refId}', headers=headers)

        # parse response if product exists
        product = None
        if r.status_code == 200:
            response = json.dumps(r.content.decode('utf-8'))
            if 'null' not in response:
                product = response
                
        # return
        return product

    @classmethod
    def get_sku_by_refId(self, base_url='', app_key='', app_token='', refId=''):
       # create headers
        headers = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        headers['X-VTEX-API-AppKey'] = app_key
        headers['X-VTEX-API-AppToken'] = app_token
        
        # do request to get product by refId
        r = requests.get(f'{base_url}/catalog/pvt/stockkeepingunit?refId={refId}', headers=headers)
        
        # parse response if sku exists
        sku = None
        if r.status_code == 200:
            sku = json.dumps(r.content.decode('utf-8'))
        
        # return
        return sku

    @classmethod
    def create_products(self, base_url='', base_url_price='', app_key='', app_token='', products=[]):
        # create headers
        headers = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        headers['X-VTEX-API-AppKey'] = app_key
        headers['X-VTEX-API-AppToken'] = app_token

        # loop in all products to create
        for product in products:
            # create skus array
            skus = product.skus

            # clear skus to not send in json
            product.skus = None
            
            # create product payload
            payload_product = json.dumps(product.__dict__, ensure_ascii=False).encode('utf-8')

            # do request to create a product
            r = requests.post(f'{base_url}/catalog/pvt/product', headers=headers, data=payload_product)
            
            # # log
            print(f'Vtex create product <{product.RefId}> {r.status_code}:{r.text}')
            
            # if product are created with success, we need to create sku
            if r.status_code == 200:
                # get vtex internal ID
                product.Id = json.loads(r.content.decode('utf-8'))['Id']

                # loop in all product skus
                for sku in skus:
                    # set vtex product ID based on created product
                    sku.ProductID = product.Id
 
                    # call create sku
                    self.create_sku(
                        base_url=base_url, 
                        base_url_price=base_url_price, 
                        app_key=app_key, 
                        app_token=app_token, 
                        sku=sku)

    @classmethod
    def create_sku(self, base_url='', base_url_price='', app_key='', app_token='', sku=''):
        # create headers
        headers = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json; charset=utf-8'
        headers['X-VTEX-API-AppKey'] = app_key
        headers['X-VTEX-API-AppToken'] = app_token

        # create sku payload
        payload_sku = json.dumps(sku.__dict__, ensure_ascii=False).encode('utf-8')

        # do request
        r = requests.post(f'{base_url}/catalog/pvt/stockkeepingunit', headers=headers, data=payload_sku)
        
        # if sku are created with success we need to create price and inventory
        if r.status_code == 200:
            # log
            print(f'Vtex create sku <{sku.RefId}> {r.status_code}')
            
            # get vtex sku internal ID
            Id = json.loads(r.content.decode('utf-8'))['Id']
            sku.Id = Id
            
            # create price, inventory and image for this sku
            self.create_price(base_url=base_url_price, app_key=app_key, app_token=app_token, sku=sku)
            self.create_inventory(base_url=base_url, app_key=app_key, app_token=app_token, sku=sku)
            self.create_image(base_url=base_url, app_key=app_key, app_token=app_token, sku=sku)

    @classmethod
    def create_price(self, base_url='', app_key='', app_token='', sku=''):
        # create headers
        headers = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        headers['X-VTEX-API-AppKey'] = app_key
        headers['X-VTEX-API-AppToken'] = app_token

        # check if price exists
        if sku.price:
            # create price payload
            payload_price = json.dumps(sku.price, ensure_ascii=False)

            # do request
            r = requests.put(f'{base_url}/prices/{sku.Id}', headers=headers, data=payload_price)
            
            # log
            print(f'Vtex create price for SKU <{sku.RefId}>. {r.status_code}:{r.content.decode("utf-8")}')

    @classmethod
    def create_inventory(self, base_url='', app_key='', app_token='', sku=''):
        # create inventory url
        url = f'{base_url}/logistics/pvt/inventory/skus/{sku.Id}/warehouses/1_1'
        
        # create headers
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "X-VTEX-API-AppKey": app_key,
            "X-VTEX-API-AppToken": app_token
        }
        
        # check if inventory exists
        if sku.inventory:
            # create payload
            payload_inventory = json.dumps(sku.inventory)

            # do request
            r = requests.request("PUT", url, data=payload_inventory, headers=headers)
            
            # log
            print(f'Vtex create inventory for SKU <{sku.RefId}> {r.status_code}:{r.content.decode("utf-8")}')

    @classmethod
    def create_image(self, base_url='', app_key='', app_token='', sku=''):
        # create headers
        headers = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        headers['X-VTEX-API-AppKey'] = app_key
        headers['X-VTEX-API-AppToken'] = app_token

        if sku.images:
            # loop in all images
            for image in sku.images:
                # create image payload
                payload_image = json.dumps(image, ensure_ascii=False)

                # do request
                r = requests.post(f'{base_url}/catalog/pvt/stockkeepingunit/{sku.Id}/file', headers=headers, data=payload_image)
                
                # log
                print(f'Vtex create image for SKU <{sku.RefId}>. {r.status_code}:{r.content.decode("utf-8")}')