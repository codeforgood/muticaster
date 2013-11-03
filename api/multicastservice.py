__author__ = 'sravi'

# Relays dict as represented in the problem description
relays_dict = {
    "S": {"name": "Small", "throughput": 1, "cost": 0.01, "subnet": "10.0.1.0/24"},
    "M": {"name": "Medium", "throughput": 5, "cost": 0.05, "subnet": "10.0.2.0/24"},
    "L": {"name": "Large", "throughput": 10, "cost": 0.10, "subnet": "10.0.3.0/24"},
    "X": {"name": "Super", "throughput": 25, "cost": 0.25, "subnet": "10.0.4.0/24"}
}

# having this in desc sorted form instead of sorting it by hand
relay_types = ["X", "L", "M", "S"]


def get_host_ip_of_type(relay_type, instance):
    """
    Return a host ip address for a given relay type and instance value
    @param: relay_type: String
    @param: instance: int
    @return: host_ip: String
    returns 10.0.1.2 when relay_type is "S" and instance=2
    """
    return relays_dict[relay_type]["subnet"].rpartition('.')[0] + "." + str(instance)


def get_routing(recipients):
    """
    Build the routing meta info to determine the number of hosts needed per subnet category
    for the given recipients
    @param: recipients: List of recipient phone numbers
    @return: rt: Routing info table of the form {"X":1, "L":0, "M":1, "S":1}
    """
    recipients_count = len(recipients)
    rt = {}
    for i in range(len(relay_types)):
        if recipients_count == 0:
            break
        relay_hosts_needed = recipients_count / relays_dict[relay_types[i]]["throughput"]
        recipients_count = recipients_count % relays_dict[relay_types[i]]["throughput"]
        rt[relay_types[i]] = relay_hosts_needed
    return rt


def get_recipients_assigned_for_routing(routing_table, recipients):
    """
    Build the actual routes using the routing table generated before and the recipients list
    @param routing_table: Python dict of form {"X":1, "L":0, "M":1, "S":1}
    @param recipients: Python List  ["123-456-5678", "345-245-2552", ...]
    @return routes: Nested dictionary of routes with hosts and recipients assigned to each hosts
    """
    routes = []
    start = 0
    for i in range(len(relay_types)):
        if relay_types[i] in routing_table:
            hosts_needed = routing_table[relay_types[i]]
            if hosts_needed > 0:
                for j in range(hosts_needed):
                    host_ip = get_host_ip_of_type(relay_types[i], j+1)
                    end = start + relays_dict[relay_types[i]]["throughput"]
                    route = {'ip': host_ip, 'recipients': recipients[start: end]}
                    start = end
                    routes.append(route)
    return routes
