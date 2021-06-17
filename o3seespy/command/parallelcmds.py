
def get_pid(osi):
    """
    Get the processor ID of the calling processor.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    """
    _parameters = []
    return osi.to_process("getPID", _parameters)


def get_np(osi):
    """
    Get total number of processors.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    """
    _parameters = []
    return osi.to_process("getNP", _parameters)


def barrier(osi):
    """
    Set a barrier for all processors, i.e.,faster processors will pause here to wait for all processorsto reach to this
    point.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    """
    _parameters = []
    return osi.to_process("barrier", _parameters)


def send(osi, pid, data):
    """
    Send information to another processor.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    pid: int
            Id of processor where data is sent to
    data: str
            Can be a string
    """
    pid = int(pid)
    _parameters = [pid, *data]
    return osi.to_process("send", _parameters)


def recv(osi, pid):
    """
    Receive information from another processor.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    pid: str
            If ``pid`` is ``'any'``, the processor can receive data from any processor.
    """
    _parameters = [pid]
    return osi.to_process("recv", _parameters)


def bcast(osi, params=None):
    """
    Broadcast information from processor 0 to all processors.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    """
    if params is None:
        params = []
    return osi.to_process("Bcast", params)


def set_start_node_tag(osi):
    """
    Set the starting node tag for the :doc:`mesh`.The purpose of this command is to controlthe node tags generated by
    the :doc:`mesh`. Somenodes are shared by processors, which musthave same tags. Nodes which are unique toa processor
    must have uniques tags acrossall processors.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    """
    _parameters = []
    return osi.to_process("setStartNodeTag", _parameters)


def domain_change(osi):
    """
    Mark the domain has changed manually.This is used to notify processors whose domain is not changed,but the domain in
    other processors have changed.

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    """
    _parameters = []
    return osi.to_process("domainChange", _parameters)


def partition(osi, ncuts, niters: int=None, ufactor: int=None, info=False):
    """
    In a parallel environment, this command partitions the model. It requires that all processorshave the exact same
    model to be partitioned. 

    Parameters
    ----------
    osi: o3seespy.OpenSeesInstance
    ncuts: int
            Specifies the number of different partitionings that it will compute.  the final partitioning is the one
            that achieves the best edge cut or communication volume.  (optional default is 1).
    niters: int, optional
            Specifies the number of iterations for the refinement algorithms  at each sobjecte of the uncoarsening
            process.  (optional default is 10).
    ufactor: int, optional
            Specifies the maximum allowed load imbalance among the partitions.  (optional default is 30, indicating a
            load imbalance of 1.03).
    info: bool
            Print information. 
    """
    ncuts = int(ncuts)
    if niters is not None:
        niters = int(niters)
    if ufactor is not None:
        ufactor = int(ufactor)
    _parameters = [ncuts]
    if niters is not None:
        _parameters += ['-niter', niters]
    if ufactor is not None:
        _parameters += ['-ufactor', ufactor]
    if info:
        _parameters += ['-info']
    return osi.to_process("partition", _parameters)
