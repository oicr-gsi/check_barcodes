import time

from filters.barcode import get_collisions
from loaders.file_provenance import load_file_provenance
from tasks.check_barcodes import config
from utils.logging import log

## load fpr
start_time = time.time()
log.info('Loading file provenance report from: {}'.format(config.fpr_path))
fpr = load_file_provenance(config.fpr_path)
log.info('Completed loading file provenance report in {:.1f}s'.format(time.time() - start_time))

## select only CASAVA lane_name + sample_name + workflow_run + barcode

lanes = fpr.loc[(fpr['Workflow Name'] == "CASAVA") & (fpr['Sample Name'].notnull()),
                ['Lane Name', 'Sample Name', 'Workflow Run SWID', 'IUS Tag']].drop_duplicates()
lanes.reset_index()

start_time = time.time()
collisions_df = get_collisions(lanes, config.collision_threshold, config.collision_operator)
log.info('get_collisions completed in {:.1f}s'.format(time.time() - start_time))
log.info('Collisions (threshold = {}, operator = {}) = {}'
         .format(config.collision_threshold, str(config.collision_operator.__name__), len(collisions_df)))

for index, row in collisions_df.iterrows():
    print('{}-{}-{} (Workflow run SWID = {}) collides with: {}'.format(
        str(lanes.loc[index]['Lane Name']),
        str(lanes.loc[index]['Sample Name']),
        lanes.loc[index]['IUS Tag'],
        str(lanes.loc[index]['Workflow Run SWID'].astype(int)),
        ','.join(lanes.loc[row['collisions']]['Sample Name'] + '-' + lanes.loc[row['collisions']]['IUS Tag'])))
