from dask.distributed import Client, LocalCluster

import processing.config as config
from utils.logging import log

cluster = None
client = None


def start_local_cluster() -> Client:
    global cluster
    global client
    if cluster is None:
        cluster = LocalCluster(n_workers=config.dask_workers)
        client = Client(cluster)
    log.info('Cluster info: {}'.format(str(cluster)))
    return client


def stop_local_cluster():
    global cluster
    global client
    client.close()
    cluster.close()
    cluster = None
    client = None
