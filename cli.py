import defopt

import processing.config as processing_config
import processing.dask_cluster as processing
import tasks.check_barcodes.config as check_barcodes_config


def check_barcodes(fpr_path=check_barcodes_config.fpr_path,
                   collision_threshold=check_barcodes_config.collision_threshold,
                   collision_operator=check_barcodes_config.collision_operator,
                   num_workers=processing_config.dask_workers):
    """
    Calculate barcode collisions from file provenance report

    :param str fpr_path: file provenance path
    :param int collision_threshold:  collision threshold
    :param str collision_operator: the operator to use when comparing edit distance to the collision threshold
    :param int num_workers: the number of worker processes to spawn
    """

    check_barcodes_config.fpr_path = fpr_path
    check_barcodes_config.collision_threshold = collision_threshold
    check_barcodes_config.collision_operator = collision_operator
    processing_config.dask_workers = num_workers

    # get dask client + local cluster
    processing.start_local_cluster()

    # execute check_barcodes task/script
    # noinspection PyUnresolvedReferences
    import tasks.check_barcodes.check_barcodes

    # close the dask client
    processing.stop_local_cluster()


if __name__ == '__main__':
    defopt.run([check_barcodes], short={}, strict_kwonly=False)
