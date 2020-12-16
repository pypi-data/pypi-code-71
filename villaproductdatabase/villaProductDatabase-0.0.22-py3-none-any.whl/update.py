# AUTOGENERATED! DO NOT EDIT! File to edit: update.ipynb (unless otherwise specified).

__all__ = ['Updater']

# Cell
import pandas as pd
from datetime import datetime
import pickle, json , boto3, zlib, os, logging

# Cell
try:
#   INVENTORY_BUCKET_NAME = os.environ['INVENTORY_BUCKET_NAME']
  INPUT_BUCKET_NAME = os.environ['INPUT_BUCKET_NAME']
except Exception as e:
  print(f'missing environment variable {e} in update NB')
#   INVENTORY_BUCKET_NAME = None
  INPUT_BUCKET_NAME = None

# Cell
class Updater:
  @classmethod
  def updateWithDict(cls, originalObject, inputDict:dict ):
    data = originalObject.data
    data.update(inputDict)
    return cls.fromDict(data)

  @classmethod
  def valueUpdate(cls, inputs):
    '''
      check for difference and batch update the changes in product data
    '''
    itemsUpdated = {'success':0, 'failure': 0, 'skipped': 0 ,'failureMessage':[], 'timetaken': 0}
    t0 = datetime.now()

    logging.info(f'there are {len(inputs)} products to update')

    with cls.batch_write() as batch:
      # loop through each product
      for input_ in inputs:
        iprcode = input_['iprcode']
        cprcode = input_['cprcode']

        # check if product is in the database, if not, create an empty class with the product code
        incumbentBr = next(cls.query(iprcode , cls.cprcode == cprcode), cls(iprcode = iprcode, cprcode = cprcode, data = {}))
        # save original data to a variable
        originalData = incumbentBr.data.copy()
        # update data
        updatedData = cls.updateWithDict(incumbentBr, input_)

        logging.info(f'incumbentBr is {incumbentBr.iprcode}\n, prcode is {iprcode}')

        # check for difference
        if updatedData.data != originalData:
          logging.info(f'product {iprcode} has changed from \n{originalData} \n{updatedData.data}')
          batch.save(updatedData)
          itemsUpdated['success'] += 1
        else:
          logging.info(f'no change for {iprcode}')
          itemsUpdated['skipped'] += 1

        # log time taken
        itemsUpdated['timetaken'] = (datetime.now()- t0).total_seconds()*1000
    return itemsUpdated



  @classmethod
  def updateLambdaInput(cls, inputs):
    '''
    update products in the database by first grouping the data from lambda
    input
    - iprcode: String
      ibrcode: String
    '''
#     groupedInput = cls.Helper.groupByProduct(input)
    return cls.valueUpdate(inputs)

  @classmethod
  def updateS3Input(cls, inputBucketName = INPUT_BUCKET_NAME, key = '', **kwargs):
    s3Result = cls.loadFromS3(bucketName= inputBucketName, key = key, **kwargs)
    updateResult = cls.valueUpdate(s3Result)
#     transformedS3Result = [{
#         'ib_prcode': item.get('ib_prcode') or item.get('prcode'),
#         'ib_brcode': item.get('ib_brcode') or item.get('brcode'),
#         'ib_cf_qty': item.get('ib_cf_qty'),
#         'new_ib_vs_stock_cv': item.get('new_ib_vs_stock_cv')
#         } for item in s3Result]

#     logging.info(f' s3 result is {transformedS3Result}')
#     groupedInput = cls.Helper.groupByProduct(transformedS3Result)
#     updateResult = cls.bulkUpdate(groupedInput, **kwargs)
    return updateResult
