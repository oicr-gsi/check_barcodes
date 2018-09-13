import defopt
import tasks.check_barcodes.config as check_barcodes_config


def check_barcodes(fpr_path = check_barcodes_config.fpr_path,
                   collision_threshold=check_barcodes_config.collision_threshold,
                   collision_operator=check_barcodes_config.collision_operator):
    """
    Calculate barcode collisions from file provenance report

    :param str fpr_path: file provenance path
    :param int collision_threshold:  collision threshold
    :param str collision_operator: the operator to use when comparing edit distance to the collision threshold
    """

    check_barcodes_config.fpr_path=fpr_path
    check_barcodes_config.collision_threshold=collision_threshold
    check_barcodes_config.collision_operator=collision_operator

    import tasks.check_barcodes.check_barcodes


if __name__ == '__main__':
    defopt.run([check_barcodes], short={}, strict_kwonly=False)
